---
title: FamilySearch GEDZip
permalink: /gedzip/
sidebar:
  nav: "gedzip"
---

## FamilySearch GEDZip

It is often useful to transmit a GEDCOM document together with a set of external
files. The FamilySearch GEDZip file format is provided for this purpose.
A FamilySearch GEDZip file is a Zip archive, as defined by [http://www.pkware.com/appnote](http://www.pkware.com/appnote)
and standardized by ISO/IEC 21320-1:2015.

*Note — A few details about the zip archive format are useful to fully understand GEDCOM Package :*
- An archive can contain one or more files.
- Files within an archive can be added, removed, or updated
individually without needing to re-process the rest of the archive.
- Libraries such as libzip allow applications to operate directly on the
- zip archive as if it were a normal directory tree.
- What the zip specification calls a “file name” is actually a local path
and may contain directories.
- Directory separators are / internally and are converted to the
appropriate form by the zip processing tool during zipping and
unzipping. Because of this, unzipping a GEDZip file in any local directory
results in all GEDZip FILE (p.58) references working as-is for the
resulting gedcom.ged without the need for any additional
processing.

More instructions and recommendations can be found in the actual specification.
