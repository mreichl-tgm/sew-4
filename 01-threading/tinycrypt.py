import threading


class Crypt(threading.Thread):
    def __init__(self, message, key, encrypt=True):
        """
        Encrypts or Decrypts a message using a given key
        :param message: str
        :param key: str
        :param encrypt: bool
        """
        super().__init__()
        self.message = message
        self.key = key
        self.encrypt = encrypt
        self.crypt = ""

    def run(self):
        """
        Override run to encrypt a message using a new thread
        """
        if type(self.key) == dict:
            self.crypt = self.dict_crypt()

        elif type(self.key) == str:
            self.crypt = self.key_crypt()

    def dict_crypt(self):
        result = ""
        for char in self.message:
            if not self.encrypt:
                new_key = {}
                for v in self.key:
                    new_key[self.key[v]] = [v]

                self.key = new_key

            if char in self.key:
                result += self.key[char]
            else:
                result += char

        return result

    def key_crypt(self):
        """
        Encrypt a message using the given key
        :return:
        """
        result = ""
        # i as index, c as char
        for i, char in enumerate(self.message):
            key_char = ord(self.key[i % len(self.key)])
            # check whether you are in en- or decryption mode
            if self.encrypt:
                result += chr((ord(char) + key_char) % 126)
            else:
                result += chr((ord(char) - key_char) % 126)

        return result


class CryptUI:
    @staticmethod
    def start_ui():
        """
        Starts a new instance of the User Interface
        :return:
        """
        # initial values
        encrypt = True
        threads = []
        crypt = ""
        message = ""
        key = {
            "A": "C",
            "B": "D",
            "C": "E",
            "D": "F",
            "E": "G",
            "F": "H",
            "G": "I",
            "H": "J",
            "I": "K",
            "J": "L",
            "K": "M",
            "L": "N",
            "M": "O",
            "N": "P",
            "O": "Q",
            "P": "R",
            "Q": "S",
            "R": "T",
            "S": "U",
            "T": "V",
            "U": "W",
            "V": "X",
            "W": "Y",
            "X": "Z",
            "Y": "A",
            "Z": "B"
            # etc...
        }
        thread_count = 1
        # catch ValueError
        try:
            # select encrypt or decrypt mode
            mode = input("Encrypt (0), Decrypt (1), End (2):")
            # switch mode
            if mode == "0":
                encrypt = True
            elif mode == "1":
                encrypt = False
            elif mode == "2":
                return
            # select dictionary or key mode
            if mode == "0" or mode == "1":
                mode = input("By built-in Dictionary (0) or Key (1)?")
            # message input
            message = input("Message:")
            # key input
            if mode == "1":
                key = input("Key to use:")
            else:
                message = message.upper()
            # number of threads
            thread_count = int(input("Threads to use:"))
        except ValueError:
            print("Only numbers allowed for modes and threads!")

        # size of one message part
        part_size = int(len(message) / thread_count)
        # appending threads
        for i in range(thread_count):
            start = i * part_size
            stop = start + part_size
            threads.append(Crypt(message[start:stop], key, encrypt))

        # starting threads
        for thread in threads:
            thread.start()
            # combining results
        for thread in threads:
            crypt += thread.crypt

        print(crypt)


c = CryptUI()
c.start_ui()
