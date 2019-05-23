"""Combines all *.eps files in a given folder."""
import pyx
import os
import argparse

OFFSET = 12
IMG_PR_ROW = 4


def combine(source_folder, destination):
    """Combine .eps images."""
    canv = pyx.canvas.canvas()
    tot_files = 0

    for counter, file in enumerate(os.listdir(source_folder)):
        if file.endswith('.eps'):
            path = os.path.join(source_folder, file)
            y, x = divmod(counter, IMG_PR_ROW)
            canv.insert(pyx.epsfile.epsfile(x * OFFSET, y * OFFSET, path))
            tot_files = counter + 1
    canv.writeEPSfile(destination + '.eps')
    return tot_files


def main():
    """Run argparse if invoked directly."""
    parser = argparse.ArgumentParser(description="""Combine all *.eps
                                     in folder into a single image.""")
    parser.add_argument('-s', '--source_folder', help='source folder',
                        required=True)
    parser.add_argument('-d', '--destination',
                        help='destination file (no suffix)',
                        required=True)
    args = parser.parse_args()
    combine(args.source_folder, args.destination)


if __name__ == '__main__':
    main()
