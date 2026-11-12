#!/usr/bin/env python3
"""Build each GEDZIP test archive from the folder beside it.

Every file in testfiles/gedcom71/maximal71.gdz is also in testfiles/gedcom71/maximal71/,
and that folder is what gets edited. After editing it, run this and commit the folder and
the archive together, so the two always match:

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
import sys
import zipfile
from pathlib import Path

STAMP = (1980, 1, 1, 0, 0, 0)


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
    tmp = archive.with_name(archive.name + ".tmp")
    with zipfile.ZipFile(tmp, "w") as z:
        for name in names:
            info = zipfile.ZipInfo(name, STAMP)
            if want[name] is None:
                info.external_attr = (0o40755 << 16) | 0x10
                z.writestr(info, b"", compress_type=zipfile.ZIP_STORED)
            else:
                info.external_attr = 0o644 << 16
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
