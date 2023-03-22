---
title: Tools for FamilySearch GEDCOM
permalink: /tools/
sidebar:
  nav: "tools"
---
***Code and sample files for developers***

*This page contains links to code and tools that may be of use to software developers. These tools are authored and maintained by third parties and may vary in license, quality, and correctness.*

## v5.5.1 to v7.0 Conversion Code

| Language | License | Site | Notes |
|----------|---------|------|-------|
| C | public domain | <https://github.com/gedcom7code/c-converter> | Command-line |
| Java | public domain | <https://github.com/gedcom7code/java-converter> | Command-line |
| Web tool | — | <https://magikeygedcomconverter.azurewebsites.net/> | Website |

## v7.0 parsers

| Language | License | Site | Notes |
|----------|---------|------|-------|
| Javascript | public domain | <https://github.com/gedcom7code/js-parser> | DOM-style, no validation, with SCHMA handling |
| Python | MIT license | <https://github.com/DavidMStraub/python-gedcom7> | based on regular expressions generated directly from the ABNF grammar via abnf-to-regexp |
| Go | GPL3 | <https://github.com/funwithbots/go-gedcom> | Golang package using ABNF grammar for validation |
| C | public domain | <https://github.com/gedcom7code/c-parser> | Parses tree and resolves points with syntatic validation |

## Development Aids

| Language | License | Site | Notes |
|----------|---------|------|-------|
| Web tool | — | <http://ged-inline.elasticbeanstalk.com/> | GEDCOM file validator website |
| C | MIT | <https://github.com/ArmidaleSoftware/gedcom7> | Compatibility checker command-line tool |
| Web tool | — | <https://magikeygedcomconverter.azurewebsites.net/Compatibility> | Compatibillity checker website |

## Example FamilySearch GEDCOM 7.0 Files

The following files are provided for testing.

| File     | Notes                  |
|----------|------------------------|
| [escapes.ged](/testfiles/gedcom70/escapes.ged) | This file contains @ characters that are doubled only when they appear at the start of a line string. |
| [extension-record.ged](/testfiles/gedcom70/extension-record.ged) | This file contains a _LOC record, which is referenced from an individual with a _LOC tag. |
| [long-url.ged](/testfiles/gedcom70/long-url.ged) | This file contains a URL of a submitter that is very long, to test the ability to parse very long lines. |
| [maximal70.ged](/testfiles/gedcom70/maximal70.ged) | This file attempts to exercise all standard tags in various locations, and all standard enumeration values. |
| [minimal70.ged](/testfiles/gedcom70/minimal70.ged) | This file is the smallest legal FamilySearch GEDCOM 7.0 file. |
| [remarriage1.ged](/testfiles/gedcom70/remarriage1.ged) | This file contains a couple who married, divorced, and then later remarried, stored as one family. |
| [remarriage2.ged](/testfiles/gedcom70/remarriage2.ged) | This file contains a couple who married, divorced, and then later remarried, stored as two separate families. |
| [same-sex-marriage.ged](/testfiles/gedcom70/same-sex-marriage.ged) | This file contains a same sex marriage. |
| [spaces.ged](/testfiles/gedcom70/spaces.ged) | This file contains empty DATE and EVEN payloads, with and without spaces. |
| [voidptr.ged](/testfiles/gedcom70/voidptr.ged) | This file contains several @VOID@ references. |

## Other Development Tools

Other development, conversions tools and sample files will be posted here as they become available.
If you have a FamilySearch GEDCOM 7 tool that we should list, post an announcement of the tool on the [GEDCOM Discussions](https://github.com/FamilySearch/GEDCOM/discussions).
