#!/usr/bin/env python3
"""
Packs the built plugin into a ZIP .lplug4 for the Logi Marketplace UPLOAD.

The local plugin service wants the package as an uncompressed tar (see
pack-lplug4.py); a zip is silently rejected on install. The Marketplace upload
validator is the opposite: it unzips the file, so a tar fails there with
"error while unzipping". The developer uploads this zip; the Marketplace then
re-serves a tar to end users. So both artifacts are needed:

  pack-lplug4.py      -> SubtitleEdit_<v>.lplug4             (tar, direct install)
  pack-lplug4-zip.py  -> SubtitleEdit_<v>_marketplace.lplug4 (zip, upload only)

Usage:  python3 scripts/pack-lplug4-zip.py [Release|Debug]
"""
import pathlib
import re
import sys
import zipfile

CONFIG = sys.argv[1] if len(sys.argv) > 1 else "Release"
ROOT = pathlib.Path(__file__).resolve().parent.parent
SOURCE = ROOT / "SubtitleEditPlugin" / CONFIG


def version():
    y = (ROOT / "SubtitleEditPlugin" / "package" / "metadata" / "LoupedeckPackage.yaml").read_text()
    m = re.search(r"^version:\s*(\S+)", y, re.M)
    return (m.group(1) if m else "1_0").replace(".", "_")


def main():
    if not (SOURCE / "bin").is_dir():
        sys.exit(f"No build found at {SOURCE}. Run: dotnet build -c {CONFIG}")

    # localization.generated is the service's scratch output, not part of the package.
    folders = [d.name for d in sorted(SOURCE.iterdir())
               if d.is_dir() and d.name != "localization.generated"]
    if "bin" not in folders or "metadata" not in folders:
        sys.exit(f"Expected bin/ and metadata/ under {SOURCE}, found {folders}")

    out = ROOT / "dist" / f"SubtitleEdit_{version()}_marketplace.lplug4"
    out.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for folder in folders:
            for path in sorted((SOURCE / folder).rglob("*")):
                if path.is_file():
                    z.write(path, path.relative_to(SOURCE).as_posix())

    with zipfile.ZipFile(out) as z:
        if z.testzip() is not None:
            sys.exit("zip integrity check failed")
        names = z.namelist()
    for required in ("metadata/LoupedeckPackage.yaml", "metadata/Icon256x256.png",
                     "bin/SubtitleEditPlugin.dll"):
        if required not in names:
            sys.exit(f"Package is missing {required}")

    print(f"wrote {out} ({out.stat().st_size / 1048576:.1f} MB, {len(names)} files)")


if __name__ == "__main__":
    main()
