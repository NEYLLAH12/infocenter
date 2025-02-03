import os
import argparse
import stat

def change_attributes(file_paths, read_only, hidden, system):
    for file_path in file_paths:
        try:
            current_attributes = os.stat(file_path).st_file_attributes
            new_attributes = current_attributes

            if read_only is not None:
                if read_only:
                    new_attributes |= stat.FILE_ATTRIBUTE_READONLY
                else:
                    new_attributes &= ~stat.FILE_ATTRIBUTE_READONLY

            if hidden is not None:
                if hidden:
                    new_attributes |= stat.FILE_ATTRIBUTE_HIDDEN
                else:
                    new_attributes &= ~stat.FILE_ATTRIBUTE_HIDDEN

            if system is not None:
                if system:
                    new_attributes |= stat.FILE_ATTRIBUTE_SYSTEM
                else:
                    new_attributes &= ~stat.FILE_ATTRIBUTE_SYSTEM

            os.chflags(file_path, new_attributes)
            print(f"Updated attributes for {file_path}")

        except Exception as e:
            print(f"Error updating {file_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description='Change file attributes on Windows.')
    parser.add_argument('files', metavar='F', type=str, nargs='+', help='Files to change attributes for')
    parser.add_argument('--read-only', dest='read_only', action='store_true', help='Set files to read-only')
    parser.add_argument('--not-read-only', dest='read_only', action='store_false', help='Unset read-only attribute')
    parser.add_argument('--hidden', dest='hidden', action='store_true', help='Set files to hidden')
    parser.add_argument('--not-hidden', dest='hidden', action='store_false', help='Unset hidden attribute')
    parser.add_argument('--system', dest='system', action='store_true', help='Set files to system')
    parser.add_argument('--not-system', dest='system', action='store_false', help='Unset system attribute')
    parser.set_defaults(read_only=None, hidden=None, system=None)

    args = parser.parse_args()
    change_attributes(args.files, args.read_only, args.hidden, args.system)

if __name__ == "__main__":
    main()