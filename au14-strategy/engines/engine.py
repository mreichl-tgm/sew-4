from abc import abstractmethod, ABCMeta

__author__ = 'uhs374h'


class ArchiveEngine(metaclass=ABCMeta):
    def __init__(self, filename, dest, source=None):
        """ Create a new archive engine

        :param filename: name of the archive
        :param dest: destination directory
        """

        self.filename = filename
        self.dest = dest
        self.source = source

    @abstractmethod
    def __str__(self):
        """ A useful description for the archive engine

        :return: a string representation for the archive engine
        """

    @abstractmethod
    def write(self):
        """ write to a archive file

        :return: None
        """

    @abstractmethod
    def name(self):
        """ Used to set and get the engines name
        
        :return: str
        """