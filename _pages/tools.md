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
| Web tool | — | <https://magikeygedcomconverter.azurewebsites.net/> | under development |

## v7.0 parsers

| Language | License | Site | Notes |
|----------|---------|------|-------|
| Javascript | public domain | <https://github.com/gedcom7code/js-parser> | DOM-style, no validation, with SCHMA handling |

## Validators

| Language | License | Site | Notes |
|----------|---------|------|-------|
| Web tool | — | <http://ged-inline.elasticbeanstalk.com/> | in beta |


## Example FamilySearch GEDCOM 7.0 Files

The following files are provided for testing.

| File     | Notes                  |
|----------|------------------------|
| [escapes.ged](/testfiles/gedcom70/escapes.ged) | This file contains @ characters that are doubled only when they appear at the start of a line string. |
| [extension-record.ged](/testfiles/gedcom70/extension-record.ged) | This file contains a _LOC record, which is referenced from an individual with a _LOC tag. |
| [long-url.ged](/testfiles/gedcom70/long-url.ged) | This file contains a URL of a submitter that is very long, to test the ability to parse very long lines. |
| [minimal70.ged](/testfiles/gedcom70/minimal70.ged) | This file is the smallest legal FamilySearch GEDCOM 7.0 file. |
| [remarriage.ged](/testfiles/gedcom70/remarriage.ged) | This file contains a couple who married, divorced, and then later remarried. |
| [same-sex-marriage.ged](/testfiles/gedcom70/same-sex-marriage.ged) | This file contains a same sex marriage. |
| [voidptr.ged](/testfiles/gedcom70/voidptr.ged) | This file contains several @VOID@ references. |

## Other Development Tools

Other development, conversions tools and sample files will be posted here as they become available.
If you have a FamilySearch GEDCOM 7 tool that we should list, post an announcement of the tool on the [GEDCOM General Google Group](https://groups.google.com/g/gedcomgeneral).
