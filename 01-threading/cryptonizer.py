import threading
import math
import random


class KeyEncrypt(threading.Thread):
    """
    KeyEncrypt lets you encrypt keys by giving a specific message and key using number theory.
    Should be started as a new thread!
    """
    def __init__(self, message, key):
        """
        Used to encrypt messages with a given key
        :param message(``string``):
        :param key(``string``):
        """
        threading.Thread.__init__(self)
        self.message = message
        self.key = key
        self.encrypted = ""

    def run(self):
        """
        Overrides run and uses it to encrypt a message with a key using number theory
        """
        encrypted = []
        for i, char in enumerate(self.message):
            key_char = ord(self.key[i % len(self.key)])
            msg_char = ord(char)
            encrypted.append(chr((msg_char + key_char) % 127))

        self.encrypted = ''.join(encrypted)


class KeyDecrypt(threading.Thread):
    """
    KeyDecrypt lets you decrypt keys by giving a specific message and key using number theory.
    Should be started as a new thread!
    """
    def __init__(self, encrypted, key):
        """
        Used to decrypt messages with a given key
        :param encrypted(``string``):
        :param key(``string``):
        """
        threading.Thread.__init__(self)
        self.encrypted = encrypted
        self.key = key
        self.decrypted = ""

    def run(self):
        """
        Overrides run function and uses it to decrypt a message with a key using number theory
        """
        decrypted = []
        for i, char in enumerate(self.encrypted):
            key_char = ord(self.key[i % len(self.key)])
            enc_char = ord(char)
            decrypted.append(chr((enc_char - key_char) % 127))

        self.decrypted = ''.join(decrypted)


class Cryptonizer:
    """
    Cryptonizer provides a CLI interface to either en- or decrypt message using KeyEncrypt and KeyDecrypt classes.
    """
    def __init__(self):
        """
        Takes user to a guided cli program where he can either encrypt by giving a message and key size,
        or decrypt by giving an encrypted message and key.
        """
        self.keypairs = []

        while True:
            command = input("What to do (e/d) ")
            if command == "e":
                self.encrypt()
            elif command == "d":
                self.decrypt()
            else:
                break

    def genkey(self, size):
        """
        Takes a size, generates an ASCII key with the given length and returns it
        :param size: Length of key
        :return: generated key
        """
        key = []
        for i in range(size):
            key.append(chr(random.randint(33, 127)))

        return ''.join(key)

    def encrypt(self):
        """
        Encrypts an entered message with a generated key of a given size using a specified amount of Threads,
        prints it and adds them to keypairs
        :return:
        """
        encrypted = ""
        threads = []

        try:
            message = input("Message to encrypt: ")
            key = self.genkey(int(input("Key size: ")))
            number_of_threads = int(input("Threads to use: "))
        except ValueError:
            print("Only numbers allowed for key size and number of threads!")
            return False

        for i in range(0, number_of_threads):
            start = i * math.ceil(len(message) / number_of_threads)
            stop = start + math.ceil(len(message) / number_of_threads)
            threads.append(KeyEncrypt(message[start:stop], key))

        for t in threads:
            t.start()

        for t in threads:
            encrypted += t.encrypted

        self.keypairs.append([key, encrypted])
        print("Added to key pairs:")
        print("Key: " + key)
        print("Message: " + encrypted)

    def decrypt(self):
        """
        Decrypts an entered message with a specified key using a specified amount of Threads and prints it
        :return:
        """
        decrypted = ""
        threads = []

        try:
            encrypted = input("Message to decrypt: ")
            key = input("Key to use: ")
            number_of_threads = int(input("Threads to use: "))
        except ValueError:
            print("Only numbers allowed for thread number!")
            return False

        for i in range(0, number_of_threads):
            start = i * math.ceil(len(encrypted) / number_of_threads)
            stop = start + math.ceil(len(encrypted) / number_of_threads)
            threads.append(KeyDecrypt(encrypted[start:stop], key))

        for t in threads:
            t.start()

        for t in threads:
            decrypted += t.decrypted

        print(decrypted)
