#!/usr/bin/env python3
"""Build each GEDZIP test archive from the folder beside it.

Every testfiles/**/NAME.gdz has a folder NAME/ beside it holding the same files, and the
folder is what gets edited. After editing a folder, run this and commit the folder and its
archive together, so the two always match:

  python3 testfiles/build_gdz.py [ARCHIVE.gdz ...]

With no arguments it builds every testfiles/**/*.gdz that has a folder beside it.
It rewrites an archive only when what it holds differs from its folder: an entry missing,
an extra one, a name given twice, or different bytes. A run with nothing changed touches no
archive, and an archive whose contents already match its folder is left as it is, however it
was built. When it writes one, it writes gedcom.ged first and then the other folders and files
in sorted order, each with a fixed timestamp, so the same folder always gives the same bytes.
Prints the path of each archive it rewrote.

Run it from the repository's root. The pull request's checks (validate-gdz.yml) then
confirm that the archive and the folder hold the same files with the same bytes.
"""
import os
import stat
import sys
import tempfile
import zipfile
from pathlib import Path

# ZIP stores times in MS-DOS format, which cannot hold a date before 1980-01-01; that is the earliest fixed time it can write.
STAMP = (1980, 1, 1, 0, 0, 0)
# Fixed permissions, so the archive's bytes do not depend on the permissions of the checkout it was built from.
# The high 16 bits of external_attr hold the Unix mode; 0x10 is the MS-DOS directory attribute.
MSDOS_DIRECTORY = 0x10
DIR_ATTR = ((stat.S_IFDIR | 0o755) << 16) | MSDOS_DIRECTORY
FILE_ATTR = 0o644 << 16  # a file: its permission bits alone, as the archives were first built


def archive_contents(archive):
    with zipfile.ZipFile(archive) as z:
        infos = z.infolist()
        if len({i.filename for i in infos}) != len(infos):
            return None  # a name given twice is never up to date, so the archive is rebuilt
        return {i.filename: (None if i.is_dir() else z.read(i)) for i in infos}


def folder_contents(folder):
    out = {}
    for p in folder.rglob("*"):
        name = p.relative_to(folder).as_posix()
        out[name + "/" if p.is_dir() else name] = None if p.is_dir() else p.read_bytes()
    return out


def build(archive):
    folder = archive.with_suffix("")
    want = folder_contents(folder)
    if "gedcom.ged" not in want:
        raise SystemExit(f"{folder}: no gedcom.ged")
    if archive.exists() and archive_contents(archive) == want:
        return False
    names = ["gedcom.ged"] + sorted(n for n in want if n != "gedcom.ged")
    fd, tmp = tempfile.mkstemp(dir=archive.parent, prefix=archive.name + ".", suffix=".tmp")
    os.close(fd)
    tmp = Path(tmp)
    with zipfile.ZipFile(tmp, "w") as z:
        for name in names:
            info = zipfile.ZipInfo(name, STAMP)
            if want[name] is None:
                info.external_attr = DIR_ATTR
                z.writestr(info, b"", compress_type=zipfile.ZIP_STORED)
            else:
                info.external_attr = FILE_ATTR
                z.writestr(info, want[name], compress_type=zipfile.ZIP_DEFLATED)
    tmp.replace(archive)
    if archive_contents(archive) != want:
        raise SystemExit(f"{archive}: rebuilt archive does not match {folder}")
    return True


def main():
    paths = [Path(a) for a in sys.argv[1:]] or sorted(
        p for p in Path("testfiles").rglob("*.gdz") if p.with_suffix("").is_dir())
    for archive in paths:
        if build(archive):
            print(archive)


if __name__ == "__main__":
    main()
