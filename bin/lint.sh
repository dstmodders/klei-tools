#!/usr/bin/env sh

BASE_DIR="$(cd "$(dirname "$0")" && pwd)"

cd "${BASE_DIR}/.." || exit 1

# prettier
find ./pkg/ -type f -name '*.xml' -exec prettier --check {} \;

# clang-format
find . \( -iname '*.cpp' -o -iname '*.hpp' -o -iname '*.c' -o -iname '*.h' \) \
  -exec clang-format --dry-run --Werror {} \;

# pylint
find ./pkg/cmn/ -type f -name '*.py' -exec python2.7 -m pylint {} \;
find ./pkg/unix/ -type f -name '*.py' -exec python2.7 -m pylint {} \;
find ./pkg/win32/Python27/Lib/site-packages/klei/ \
  -type f \
  -name '*.py' \
  -exec python2.7 -m pylint {} \;
