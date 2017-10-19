import bz2
import os
import shutil
from abc import ABCMeta

from engines import engine


class ShutilEngine(engine.ArchiveEngine, metaclass=ABCMeta):
    """ Base class for all ArchiveEngine classes using shutil, providing a default write method """

    def write(self):
        shutil.make_archive(base_name=self.filename, format=str(self), base_dir=self.dest, root_dir=self.source)


class ZipEngine(ShutilEngine):
    """ Engine used to create .zip archives """

    def __str__(self):
        return "zip"


class TarEngine(ShutilEngine):
    """ Engine used to create .tar archives """

    def __str__(self):
        return "tar"


class GzTarEngine(ShutilEngine):
    """ Engine used to create .tar.gz archives """

    def __str__(self):
        return "gztar"


class XzTarEngine(ShutilEngine):
    """ Engine used to create .tar.xz archives """

    def __str__(self):
        return "xztar"


class BzTarEngine(ShutilEngine):
    """ Engine used to create .tar.bz archives """

    def __str__(self):
        return "bztar"


class BzTwoEngine(engine.ArchiveEngine):
    """ Engine used to create .bz2 archives """

    def write(self):
        # Iterate over all files
        for filename in os.listdir(self.source):
            try:
                # Create new bz2file
                with bz2.BZ2File(filename + ".bz2", "w"):
                    # Cope file into bz2 archive
                    shutil.copyfile(filename, filename + ".bz2")
            except FileNotFoundError:
                print("File %s was not found, continuing anyway" % filename)
            except IsADirectoryError:
                print("Found directory %s, did not enter" % filename)

    def __str__(self):
        return "bz2"
