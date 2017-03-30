import argparse
import os

from engines import engines

if __name__ == "__main__":
    # Help strings
    help_h = "-h, --help Shows this help"
    help_d = "-d DESTDIR, --dest-dir=DESTDIR Output destination directory (default=Current Working Directory)"
    help_s = "-s SOURCEDIR, --source-dir=SOURCEDIR Input root directory (default=Current Working Directory)"
    help_a = "-a ARCHIVE, --archive-engine=ARCHIVE use the given archive engine (default=ZIP_STORED)"
    help_n = "-n NAME, --archive-name=NAME name of the archive (default=archive)"
    # Usage string
    usage = "do.py [options]\n" \
            "Note: By default this script will overwrite already created archives!\n\n" \
            + help_h + help_d + help_s + help_a + help_n
    # Argument parser instance
    parser = argparse.ArgumentParser(description='Secure your data!', usage=usage)
    # Available arguments
    parser.add_argument("-d", "--dest-dir", action="store", dest="dest_dir", default=os.curdir, help=help_d)
    parser.add_argument("-s", "--source-dir", action="store", dest="source_dir", default=os.curdir, help=help_s)
    parser.add_argument("-a", "--archive-engine", action="store", dest="archive_engine", default="zip", help=help_a)
    parser.add_argument("-n", "--archive-name", action="store", dest="archive_name", default="archive", help=help_n)
    # Fetch arguments
    args = parser.parse_args()
    # Set default error msg
    error_msg = "Error during archive creation"

    for name in dir(engines):
        obj = getattr(engines, name)

        # Check if object exists and its string matches the archive engine
        if obj and obj.__str__(obj) == args.archive_engine.lower():
            # Instantiate the object
            instance = obj(args.archive_name, args.dest_dir, args.source_dir)
            instance.write()
            # Success log
            print("Created %s in %s from %s using %s"
                  % (args.archive_name, args.dest_dir, args.source_dir, args.archive_engine))
            # Clear error msg if no error occured
            error_msg = None
            break

    if error_msg:
        print(error_msg)
