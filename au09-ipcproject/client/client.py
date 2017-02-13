import socket

import sys

'''
FieldType.GRASS     => 'G'
FieldType.LAKE      => 'L'
FieldType.FOREST    => 'F'
FieldType.MOUNTAIN  => 'M'
FieldType.CASTLE1   => 'C'
FieldType.CASTLE2   => 'C'
self.bomb[0]        => 'B'
self.bomb[1]        => 'B'
undefined           => ' '
'''


def receive(client):
    """
    Used to receive visible fields from a client.

    :param client: Socket
    :return: list
    """
    # Updating the clients turn
    Client.TURN += 1
    print("\nTURN >> ", Client.TURN)
    # Getting the user input
    input_bytes = client.recv(1024).decode()
    input_fields = []
    fields = []
    # Colors used to improve logging
    color = {
        "": '',
        "G": '\u001b[32;1m',
        "L": '\u001b[36;1m',
        "F": '\u001b[30;1m',
        "M": '\u001b[37;1m',
        "C": '\u001b[33;1m',
        "B": '\u001b[31;1m',
        "END": '\u001b[0m'
    }

    if not input_bytes:
        print("Connection closed")
        return

    # Handles different sights
    if len(input_bytes) == 18:
        input_fields += [input_bytes[0:6]]
        input_fields += [input_bytes[6:12]]
        input_fields += [input_bytes[12:18]]
    elif len(input_bytes) == 50:
        input_fields += [input_bytes[0:10]]
        input_fields += [input_bytes[10:20]]
        input_fields += [input_bytes[20:30]]
        input_fields += [input_bytes[30:40]]
        input_fields += [input_bytes[40:50]]
    elif len(input_bytes) == 98:
        input_fields += [input_bytes[0:14]]
        input_fields += [input_bytes[14:28]]
        input_fields += [input_bytes[28:42]]
        input_fields += [input_bytes[42:56]]
        input_fields += [input_bytes[56:70]]
        input_fields += [input_bytes[70:84]]
        input_fields += [input_bytes[84:98]]
    else:
        print("Could not read:", input_bytes)
        return
    # Make input code-readable
    for row in input_fields:
        row = row.replace(" ", "")
        for col, c in enumerate(row):
            if c == "B":
                row = row[:col - 1] + c + row[col + 1:]
        fields.append(row)
    # Make input human-readable
    for row in fields:
        line = ""
        for c in row:
            line += color[c] + c + color["END"] + " "
        print(line)

    return fields


class Direction:
    UP = {"cmd": "up", "vec": [-1, 0]}
    RIGHT = {"cmd": "right", "vec": [0, 1]}
    DOWN = {"cmd": "down", "vec": [1, 0]}
    LEFT = {"cmd": "left", "vec": [0, -1]}


class Client:
    # Constants and static variables
    SPAWN = [0, 0]
    TURN = 0

    def __init__(self, host="localhost", port=5050):
        """
        The Client is used to connect and also to play the game.
        """
        self.HOST = host
        self.PORT = port
        # Default values for locations
        self.fields = None
        self.castle = None
        self.bomb = None
        self.has_bomb = False
        # Position relative to the players spawn
        self.rel_pos = [0, 0]
        # Instructions the game should prioritize split into a command and how often it will repeated
        """ 10 x 10 field
        x x x x x x x x x x
        x x x x x x x x x x
        x x o o x x x x x x
        x x o o x x x x x x
        x x x x x x x x x x
        x x x x x x x x x x
        x x x x x x o o x x
        x x x x x x o o x x
        x x x x x x x x x x
        x x x x x x x x x x
        """
        self.steps = [
            [lambda: self.move(Direction.LEFT), 4],
            [lambda: self.move(Direction.DOWN), 4],
            [lambda: self.move(Direction.LEFT), 6],
            [lambda: self.move(Direction.UP), 6],
            [self.fall_back, 1]
        ]
        # Socket initialization
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((self.HOST, self.PORT))

            username = input("Username: ")
            self.client.send(username.encode())
        except IOError:
            print("Connection failed!")
            return
        # First handshake
        data = self.client.recv(1024).decode()
        # Connectivity check
        if not data or not data == "OK":
            self.client.close()
        else:
            # Iterating over instructions
            for step in self.steps:
                for i in range(step[1]):
                    self.fields = receive(self.client)
                    if not self.fields:
                        return

                    self.scan()
                    step[0]()

    def check(self, field, tags="L"):
        """
        Checks if the given field's value is not contained in the given tag.

        :param field: list
        :param tags: str
        :return: bool
        """
        pos = int(len(self.fields) / 2)
        if self.fields[pos + field["vec"][0]][pos + field["vec"][1]] in tags:
            return False
        return True

    def scan(self):
        """
        Scans the environment for bombs and castles.
        If the bomb has been found the player moves towards it.
        If both have been found the player moves to the castle.

        :return:
        """
        pos = int(len(self.fields) / 2)

        for y, row in enumerate(self.fields):
            for x, col in enumerate(row):
                yr = self.rel_pos[0] + y - pos
                xr = self.rel_pos[1] + x - pos
                # Check for bomb
                if not self.bomb and col == "B":
                    self.bomb = [yr, xr]
                    print("Scroll was found!")
                    print("-> Absolute Position:", [y, x])
                    print("-> Relative Position:", self.bomb)
                    self.move_to(self.bomb)
                    self.has_bomb = True
                    print("Scroll was obtained!")
                    return
                # Check for castle different from spawn
                if not self.castle and col == "C" and [yr, xr] != [0, 0]:
                    self.castle = [yr, xr]
                    print("Enemies castle was found!")
                    print("-> Absolute Position:", [y, x])
                    print("-> Relative Position:", self.castle)
                # Check for castle and bomb
                if self.castle and self.has_bomb:
                    print("Both bomb and castle were found!")
                    self.move_to(self.castle)
                    return

    def move_to(self, field):
        """
        Moves to a relative direction

        :param field: list
        """
        while self.rel_pos != field:
            if self.rel_pos[1] < field[1]:
                self.move(Direction.RIGHT)
            elif self.rel_pos[1] > field[1]:
                self.move(Direction.LEFT)
            elif self.rel_pos[0] > field[0]:
                self.move(Direction.UP)
            elif self.rel_pos[0] < field[0]:
                self.move(Direction.DOWN)
            self.fields = receive(self.client)
            if not self.fields:
                return

        print("Target", field, "found!")

    def move(self, direction):
        """
        Moves into a given direction while checking for lakes

        :param direction:
        """
        if not self.fields:
            return

        if self.check(direction, "L"):
            self.client.send(direction["cmd"].encode())
            self.rel_pos[0] += direction["vec"][0]
            self.rel_pos[1] += direction["vec"][1]
            print(direction["cmd"])
        else:
            print("Lake ahead!")
            self.avoid(direction)

    def fall_back(self):
        """
        In case of emergency this function can be used to visit every field on the map
        """
        self.move(Direction.RIGHT)
        for row in range(11):
            for col in range(10):
                self.fields = receive(self.client)
                if not self.fields:
                    return
                self.move(Direction.RIGHT)
            self.fields = receive(self.client)
            if not self.fields:
                return
            self.move(Direction.DOWN)

    def avoid(self, direction):
        """
        Used to avoid a lake by walking around it

        :param direction:
        """
        alt = None
        rev = None

        if direction["vec"][0] == 0:
            if self.check(Direction.UP, "L"):
                alt = Direction.UP
                rev = Direction.DOWN
            if self.check(Direction.DOWN, "L"):
                alt = Direction.DOWN
                rev = Direction.UP
        else:
            if self.check(Direction.LEFT, "L"):
                alt = Direction.LEFT
                rev = Direction.RIGHT
            if self.check(Direction.RIGHT, "L"):
                alt = Direction.RIGHT
                rev = Direction.LEFT

        self.move(alt)
        # Back to the path
        self.fields = receive(self.client)
        self.move(direction)
        # Back to the path
        self.fields = receive(self.client)
        self.move(direction)
        # Back to the path
        self.fields = receive(self.client)
        self.move(rev)


if __name__ == "__main__":
    host = "localhost"
    port = 5050

    if len(sys.argv) > 1:
        host = sys.argv[1]
    else:
        print("Falling back to default host:", host)
    if len(sys.argv) > 2:
        try:
            port = int(sys.argv[2])
        except ValueError:
            print("No valid port!")
            print("Falling back to default port: 5050")

    Client(host=host, port=port)
