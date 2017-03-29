import bz2
import os
import shutil
from abc import ABCMeta

from engines import engine


class ShutilEngine(engine.ArchiveEngine, metaclass=ABCMeta):
    def write(self):
        shutil.make_archive(base_name=self.filename, format=str(self), base_dir=self.dest, root_dir=self.source)


class ZipEngine(ShutilEngine):
    def name(self):
        return "zip"

    def __str__(self):
        return "zip"


class TarEngine(ShutilEngine):
    def __str__(self):
        return "tar"


class GzTarEngine(ShutilEngine):
    def __str__(self):
        return "gztar"


class XzTarEngine(ShutilEngine):
    def __str__(self):
        return "xztar"


class BzTarEngine(ShutilEngine):
    def __str__(self):
        return "bztar"


class BzTwoEngine(engine.ArchiveEngine):
    def write(self):
        for filename in os.listdir(self.source):
            with open(filename) as file:
                bz_file = bz2.BZ2File(filename + ".bz2", "wb")
                bz_file.write(file.read())

    def __str__(self):
        return "bz2"
