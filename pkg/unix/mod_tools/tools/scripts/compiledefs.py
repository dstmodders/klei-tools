import glob
import optparse
import os
import shutil
import sys

from pipelinetools import GetBaseDirectory, VerifyDirectory


def ProcessFile(_file, _):
    # figure out some name stuff
    basename = os.path.splitext(os.path.basename(_file))[0]
    print "Compiling " + basename
    basedir = GetBaseDirectory(_file, "intermediates")
    outdir = VerifyDirectory(basedir, "data/defs")
    outfilename = os.path.join(outdir, basename + ".xml")
    shutil.copyfile(_file, outfilename)
    shutil.copyfile(_file, outfilename)


def main():
    try:
        import psyco
        psyco.full()
    except ImportError:
        pass

    parser = optparse.OptionParser(
        description='compiles defs (currently just copy the xml)')
    parser.add_option('-b', '--bigendian', help="bigendian",
                      action="store_true", dest="bigendian")
    options, arguments = parser.parse_args()

    # generate a list of unique files from the arguments
    files = list(set(sum([glob.glob(x) for x in arguments], [])))

    if len(files) == 0:
        print "No input files specified"
        sys.exit(2)

    for f in files:
        ProcessFile(f, options)


if __name__ == "__main__":
    main()
