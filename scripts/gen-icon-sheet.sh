#!/bin/sh
# Renders docs/action-icons.png from the packaged action symbols.
# Uses macOS qlmanage, which only writes square images, so the sheet is laid out square.
set -e
cd "$(dirname "$0")/.."
rm -f docs/action-icons.png
qlmanage -t -s 2200 -o docs docs/action-icons.svg >/dev/null 2>&1
mv docs/action-icons.svg.png docs/action-icons.png
echo "wrote docs/action-icons.png"
