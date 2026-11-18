#!/usr/bin/env python3
"""Check that every structure in one GEDCOM test file is also in another.

  python3 testfiles/check_subset.py SMALLER.ged LARGER.ged

Each line of SMALLER.ged, together with the chain of lines above it, must also
appear in LARGER.ged. Pointer names are ignored, since a file copied into another
may rename them to avoid collisions (@U1@ in extensions.ged is @XU1@ in
maximal70.ged); @VOID@ is kept. The NOTE directly under SMALLER.ged's HEAD that
describes the file (it begins "This file is intended to provide coverage") is
skipped with its substructures; any other NOTE under HEAD is compared. Prints each line that is missing and exits 1 if
there are any.
"""
import re
import sys

POINTER = re.compile(r"@(?!VOID@)[^@ ]+@")
DESCRIPTION = "1 NOTE This file is intended to provide coverage"


def structures(path, skip_head_note=False):
    """Each line as the tuple of lines from its record down to it, pointer names ignored."""
    chain, out, skipping = [], [], None
    with open(path, encoding="utf-8-sig") as f:
        for number, raw in enumerate(f, 1):
            line = raw.rstrip("\r\n")
            if not line:
                continue
            level = int(line.split(" ", 1)[0])
            if skipping is not None:
                if level > skipping:
                    continue
                skipping = None
            del chain[level:]
            text = POINTER.sub("@@", line)
            if skip_head_note and level == 1 and chain and chain[0] == "0 HEAD" and text.startswith(DESCRIPTION):
                skipping = level
                continue
            chain.append(text)
            out.append((number, tuple(chain)))
    return out


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    smaller, larger = sys.argv[1], sys.argv[2]
    have = {c for _, c in structures(larger)}
    missing = [(n, c) for n, c in structures(smaller, skip_head_note=True) if c not in have]
    for n, c in missing:
        print(f"{smaller}:{n}: not in {larger}: {' / '.join(c)}")
    if missing:
        sys.exit(1)
    print(f"Every structure in {smaller} is in {larger}.")


if __name__ == "__main__":
    main()
