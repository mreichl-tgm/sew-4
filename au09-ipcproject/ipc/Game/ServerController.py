import random
import socket
import sys
import threading
import time
from enum import Enum

from PySide import QtCore, QtGui

from ipc.Game import ServerView


class FieldType(Enum):
    GRASS = 0
    CASTLE1 = 1
    CASTLE2 = 2
    FOREST = 3
    MOUNTAIN = 4
    LAKE = 5


class CommandType(Enum):
    UP = "up"
    RIGHT = "right"
    DOWN = "down"
    LEFT = "left"


def show_error(message):
    """
    Zeigt Fehlermeldungen an.
    :param message: Anzuzeigende Nachricht.
    :type message: str
    :return: None
    """
    msg = QtGui.QMessageBox()
    msg.setText(message)
    msg.setWindowTitle("Simple Chat Client")
    msg.setIcon(QtGui.QMessageBox.Critical)
    msg.exec_()


class ServerController(QtGui.QWidget):
    # Default port
    PORT = 5050
    COLS = 20
    ROWS = 10
    # Signals
    err_signal = QtCore.Signal((str,))
    msg_signal = QtCore.Signal()
    pCastle1 = QtGui.QPalette(QtCore.Qt.black)
    pCastle2 = QtGui.QPalette(QtCore.Qt.white)
    pGrass = QtGui.QPalette(QtCore.Qt.green)
    pForest = QtGui.QPalette(QtCore.Qt.darkGreen)
    pLake = QtGui.QPalette(QtCore.Qt.darkBlue)
    pMountain = QtGui.QPalette(QtCore.Qt.darkGray)

    def __init__(self, parent=None):
        """
        Create a new controller with a MyView object
        using the MVC pattern

        :param parent:
        :return: None
        """
        super().__init__(parent)
        # Initial values
        self.fields = []
        self.bomb = []
        self.bomb_label = None
        self.player1 = []
        self.player1_label = None
        self.bomb1 = False
        self.player2 = []
        self.player2_label = None
        self.bomb2 = False
        self.closing = False
        # Setup UI
        self.view = ServerView.Ui_view()
        self.view.setupUi(self)

        self.setup_game()
        self.shuffle = False
        self.listening = False

        self.view.btn_listen.clicked.connect(self.bind_and_listen)
        self.view.btn_shuffle.clicked.connect(self.setup_game)

        self.err_signal.connect(show_error)
        self.msg_signal.connect(self.draw_map)

    def setup_game(self):
        """
        Creates a new game
        """

        # Set all fields to grass
        for i in range(self.ROWS):
            self.fields.append([])
            for j in range(self.COLS):
                self.fields[i].append(FieldType.GRASS)

        # Set player 1's spawn
        x = random.randint(round(self.ROWS * 0.1), round(self.ROWS * 0.3))
        y = random.randint(round(self.COLS * 0.1), round(self.COLS * 0.3))
        self.fields[x][y] = FieldType.CASTLE1
        self.player1 = (x, y)
        self.bomb1 = False
        # Set player 2's spawn
        x = random.randint(round(self.ROWS * 0.7), round(self.ROWS * 0.9))
        y = random.randint(round(self.COLS * 0.7), round(self.COLS * 0.9))
        self.fields[x][y] = FieldType.CASTLE2
        self.player2 = (x, y)
        self.bomb2 = False
        # Set lakes
        if self.COLS > self.ROWS:
            lakes = random.randint(round(self.COLS * 0.2), self.COLS)
        else:
            lakes = random.randint(round(self.ROWS * 0.2), self.ROWS)

        while lakes > 0:
            x = random.randint(0, self.ROWS - 1)
            y = random.randint(0, self.COLS - 1)
            xr = (x + 1) % self.ROWS
            xl = (x - 1) % self.ROWS
            yu = (y + 1) % self.COLS
            yd = (y - 1) % self.COLS
            area = [self.fields[xl][yu],
                    self.fields[x][yu],
                    self.fields[xr][yu],
                    self.fields[xl][y],
                    self.fields[x][y],
                    self.fields[xr][y],
                    self.fields[xl][yd],
                    self.fields[x][yd],
                    self.fields[xr][yd]]
            # Avoid multiple lakes
            if self.fields[x][y] == FieldType.GRASS and FieldType.LAKE not in area:
                self.fields[x][y] = FieldType.LAKE
                lakes -= 1

        # Create forests
        if self.COLS > self.ROWS:
            forests = random.randint(round(self.COLS * 0.2), self.COLS)
        else:
            forests = random.randint(round(self.ROWS * 0.2), self.ROWS)

        while forests > 0:
            x = random.randint(0, self.ROWS - 1)
            y = random.randint(0, self.COLS - 1)
            if self.fields[x][y] == FieldType.GRASS:
                self.fields[x][y] = FieldType.FOREST
                forests -= 1

        # Create mountains
        if self.COLS > self.ROWS:
            mountains = random.randint(round(self.COLS * 0.2), round(self.COLS * 0.5))
        else:
            mountains = random.randint(round(self.ROWS * 0.2), round(self.ROWS * 0.5))

        while mountains > 0:
            x = random.randint(0, self.ROWS - 1)
            y = random.randint(0, self.COLS - 1)
            if self.fields[x][y] == FieldType.GRASS:
                self.fields[x][y] = FieldType.MOUNTAIN
                mountains -= 1

        # Place bomb
        while not self.bomb:
            x = random.randint(0, self.ROWS - 1)
            y = random.randint(0, self.COLS - 1)
            xr = (x + 1) % self.ROWS
            xl = (x - 1) % self.ROWS
            yu = (y + 1) % self.COLS
            yd = (y - 1) % self.COLS
            area = [self.fields[xl][yu],
                    self.fields[x][yu],
                    self.fields[xr][yu],
                    self.fields[xl][y],
                    self.fields[x][y],
                    self.fields[xr][y],
                    self.fields[xl][yd],
                    self.fields[x][yd],
                    self.fields[xr][yd]]
            # Do not set bomb beneath castle
            if self.fields[x][y] != FieldType.LAKE and FieldType.CASTLE1 not in area and FieldType.CASTLE2 not in area:
                self.bomb = [x, y]

        self.shuffle = False
        self.draw_map()

    def draw_map(self):
        """
        Draws the map
        """
        if hasattr(self, 'bomblabel'):
            # Reset labels
            self.bomb_label.deleteLater()
            self.player1_label.deleteLater()
            self.player2_label.deleteLater()
        for x in range(self.ROWS):
            for y in range(self.COLS):
                # Get Widgets
                widget = QtGui.QLabel()
                widget.setAutoFillBackground(True)
                # Adjust color
                if self.fields[x][y] == FieldType.GRASS:
                    widget.setPalette(self.pGrass)
                elif self.fields[x][y] == FieldType.FOREST:
                    widget.setPalette(self.pForest)
                elif self.fields[x][y] == FieldType.LAKE:
                    widget.setPalette(self.pLake)
                elif self.fields[x][y] == FieldType.MOUNTAIN:
                    widget.setPalette(self.pMountain)
                elif self.fields[x][y] == FieldType.CASTLE1:
                    widget.setPalette(self.pCastle1)
                elif self.fields[x][y] == FieldType.CASTLE2:
                    widget.setPalette(self.pCastle2)
                # Draw widgets
                if x == self.bomb[0] and y == self.bomb[1]:
                    self.bomb_label = QtGui.QLabel(widget)
                    self.bomb_label.setText("<span style=\"font-size:18pt; font-weight:600; color:#cc0000;\">XX</span>")
                    self.bomb_label.show()
                if x == self.player1[0] and y == self.player1[1]:
                    self.player1_label = QtGui.QLabel(widget)
                    self.player1_label.setText(
                        "<span style=\"font-size:18pt; font-weight:600; color:#cccc00;\">P1</span>")
                    self.player1_label.show()
                if x == self.player2[0] and y == self.player2[1]:
                    self.player2_label = QtGui.QLabel(widget)
                    self.player2_label.setText(
                        "<span style=\"font-size:18pt; font-weight:600; color:#cccc00;\">P2</span>")
                    self.player2_label.show()
                # Add widget
                self.view.grid.addWidget(widget, x, y)

    def bind_and_listen(self):
        """
        Setup server
        """
        if not self.listening:
            try:
                self.PORT = int(self.view.line_port.text())
                self.listening = True
                self.view.btn_listen.setText("Stop")
                if self.shuffle:
                    self.setup_game()
                self.view.btn_shuffle.setDisabled(True)
                threading.Thread(target=self.__listen_for_clients).start()
            except ValueError:
                show_error("Bitte geben Sie einen gültigen Port ein!")
        else:
            self.serversocket.close()
            if hasattr(self, "client1"):
                self.client1.close()
                self.shuffle = True
            if hasattr(self, "client2"):
                self.client2.close()
                self.shuffle = True
            self.view.list_clients.clear()

    def __listen_for_clients(self):
        """
        Listen for clients
        """
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.serversocket:
                # Binding erstellen und auf localhost am angegebenen Port horchen
                self.serversocket.bind(('localhost', self.PORT))
                # Eingehende Verbindungen ab jetzt annehmen (mit maximal 5 pending connections)
                self.serversocket.listen(5)
                print("Auf client warten...")
                (self.client1, address) = self.serversocket.accept()
                with self.client1:
                    # Name von Spieler 1 eingeben und mit "OK" bestaetigen
                    name = self.client1.recv(1024).decode()
                    self.view.list_clients.addItem(name)
                    self.client1.send("OK".encode())
                    (self.client2, address) = self.serversocket.accept()
                    with self.client2:
                        # Name von Spieler 2 eingeben und mit "OK" bestaetigen
                        name = self.client2.recv(1024).decode()
                        self.view.list_clients.addItem(name)
                        self.client2.send("OK".encode())
                        self.game_loop()
                # Spiel zuende
                self.view.list_clients.clear()
                self.view.btn_listen.setText("Listen")
                self.view.btn_shuffle.setDisabled(False)
                self.listening = False
                self.shuffle = True
        except Exception as e:
            self.view.btn_listen.setText("Listen")
            self.listening = False
            self.view.btn_shuffle.setDisabled(False)
            self.err_signal.emit("Socket error: " + str(e))

    def field_message(self, position):
        """
        Sends all visible fields to the player
        :param position: Player's position
        :return: str
        """
        sight = 1
        if self.fields[position[0]][position[1]] == FieldType.MOUNTAIN:
            sight = 3
        elif self.fields[position[0]][position[1]] == FieldType.GRASS:
            sight = 2

        xu = (position[0] - sight) % self.ROWS
        xd = (position[0] + sight) % self.ROWS
        yl = (position[1] - sight) % self.COLS
        yr = (position[1] + sight) % self.COLS

        x = xu
        y = yl
        msg = ''
        while True:
            f = self.fields[x][y]
            if f == FieldType.GRASS:
                msg += 'G'
            elif f == FieldType.LAKE:
                msg += 'L'
            elif f == FieldType.FOREST:
                msg += 'F'
            elif f == FieldType.MOUNTAIN:
                msg += 'M'
            elif f == FieldType.CASTLE1 or f == FieldType.CASTLE2:
                msg += 'C'

            if x == self.bomb[0] and y == self.bomb[1]:
                msg += 'B'
            else:
                msg += ' '

            if x == xd and y == yr:
                break
            else:
                if y == yr:
                    y = yl
                    x = (x + 1) % self.ROWS
                else:
                    y = (y + 1) % self.COLS
        return msg

    def game_loop(self):
        """
        Bildet die Spielelogik ab und wickelt die Zuege ab.
        :return: None
        """
        msg = self.field_message(self.player1)
        self.client1.send(msg.encode())
        msg = self.field_message(self.player2)
        self.client2.send(msg.encode())
        skip1 = False
        skip2 = False
        while True:
            time.sleep(0.5)
            # ggf. Zug ueberspringen, falls Berg bestiegen wurde
            if not skip1:
                data = self.client1.recv(1024).decode()
                if data == CommandType.UP.value:
                    self.player1 = ((self.player1[0] - 1) % self.ROWS, self.player1[1])
                elif data == CommandType.DOWN.value:
                    self.player1 = ((self.player1[0] + 1) % self.ROWS, self.player1[1])
                elif data == CommandType.RIGHT.value:
                    self.player1 = (self.player1[0], (self.player1[1] + 1) % self.COLS)
                elif data == CommandType.LEFT.value:
                    self.player1 = (self.player1[0], (self.player1[1] - 1) % self.COLS)
                if self.fields[self.player1[0]][self.player1[1]] == FieldType.MOUNTAIN:
                    skip1 = True
            else:
                skip1 = False
            if not skip2:
                data = self.client2.recv(1024).decode()
                if data == CommandType.UP.value:
                    self.player2 = ((self.player2[0] - 1) % self.ROWS, self.player2[1])
                elif data == CommandType.DOWN.value:
                    self.player2 = ((self.player2[0] + 1) % self.ROWS, self.player2[1])
                elif data == CommandType.RIGHT.value:
                    self.player2 = (self.player2[0], (self.player2[1] + 1) % self.COLS)
                elif data == CommandType.LEFT.value:
                    self.player2 = (self.player2[0], (self.player2[1] - 1) % self.COLS)
                if self.fields[self.player2[0]][self.player2[1]] == FieldType.MOUNTAIN:
                    skip2 = True
            else:
                skip2 = False

            # Pruefen, ob Spieler 1 oder Spieler 2 gewonnen bzw. verloren haben
            check1 = self.check_position(self.player1, 1)
            check2 = self.check_position(self.player2, 2)

            if (check1 == 1 and check2 == 1) or (check1 == -1 and check2 == -1):
                # Unentschieden (beide gewonnen oder beide verloren)
                self.client1.send("Draw".encode())
                self.client2.send("Draw".encode())
                self.msg_signal.emit()
                return
            elif check1 == 1 or check2 == -1:
                # Spieler 1 hat gewonnen
                self.client1.send("You win".encode())
                self.client2.send("You lose".encode())
                self.msg_signal.emit()
                return
            elif check2 == 1 or check1 == -1:
                # Spieler 2 hat gewonnen
                self.client1.send("You lose".encode())
                self.client2.send("You win".encode())
                self.msg_signal.emit()
                return
            else:
                # Nachricht sichtbarer Felder schicken
                if not skip1:
                    msg = self.field_message(self.player1)
                    self.client1.send(msg.encode())
                if not skip2:
                    msg = self.field_message(self.player2)
                    self.client2.send(msg.encode())
                self.msg_signal.emit()

    def check_position(self, position, number):
        """
        Prueft die aktuelle Position und ermittelt, ob das
        Spiel gewonnen oder verloren wurde.
        :param position: Position des Spielers
        :type position: (int, int)
        :param number: Spielernummer (1 oder 2)
        :type number: int
        :return: -1 (verloren), 1 (gewonnen), 0 (weder noch)
        :rtype int
        """
        if self.fields[position[0]][position[1]] == FieldType.LAKE:
            # In See gefallen
            return -1
        elif self.fields[position[0]][position[1]] == FieldType.CASTLE2 and number == 1 and self.bomb1:
            # Gegnerische Basis mit Schriftrolle erreicht
            return 1
        elif self.fields[position[0]][position[1]] == FieldType.CASTLE1 and number == 2 and self.bomb2:
            # Gegnerische Basis mit Schriftrolle erreicht
            return 1

        if position[0] == self.bomb[0] and position[1] == self.bomb[1]:
            if number == 1:
                self.bomb1 = True
                print("Player 1 got the scroll")
            else:
                self.bomb2 = True
                print("Player 2 got the scroll")

        return 0

    def closeEvent(self, event):
        """
        Handles the closeEvent for a clean disconnection.
        :param event:
        """
        self.closing = True
        if hasattr(self, 'serversocket'):
            self.serversocket.close()
            if hasattr(self, "client1"):
                self.client1.close()
            if hasattr(self, "client2"):
                self.client2.close()
        event.accept()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    c = ServerController()
    c.show()
    sys.exit(app.exec_())
