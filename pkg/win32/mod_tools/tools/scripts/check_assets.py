import argparse
import os
import sys

buildtools_dir = os.path.normpath(
    os.path.join(os.path.dirname(__file__), "../../buildtools/scripts"))
sys.path.append(buildtools_dir)

# pylint: disable=wrong-import-position
import PackageData

parser = argparse.ArgumentParser()
parser.add_argument('--outputdir', default='data')
args = parser.parse_args()

print

missing_file = False
for filename, arcname in PackageData.CommonFiles(data_dir=args.outputdir):
    if not os.path.exists(filename):
        sys.stderr.write(
            "{} is referenced in prefabs.xml but does not exist!\n".format(
                filename))
        missing_file = True
    else:
        path, fn = os.path.split(filename)
        files = os.listdir(path)
        if fn not in files:
            # pylint: disable=line-too-long
            sys.stderr.write(
                "\n---------------------------------------------------------------------------\n")
            sys.stderr.write("FILENAME MISMATCH - Possibly case?\n")
            sys.stderr.write("{} - specified in prefab\n".format(filename))
            sys.stderr.write(
                "\n---------------------------------------------------------------------------\n")
            # pylint: disable=misplaced-bare-raise
            raise

assert missing_file is False
