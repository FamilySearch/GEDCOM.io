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
| Javascript | dual licensed: unlicense and MIT license | <https://github.com/gedcom7code/js-gedcom> | DOM-style, full validation, with full SCHMA handling and registry parsing; also supports programmatic creation of GEDCOM files |
| C# | MIT | <https://github.com/ArmidaleSoftware/gedcom7> | GEDCOM 7 parsing, validation, and comparison library |

## Development Aids

| Language | License | Site | Notes |
|----------|---------|------|-------|
| Web tool | — | <https://ged-inline.org> | GEDCOM file validator website |
| C# | MIT | <https://github.com/ArmidaleSoftware/gedcom7> | Compatibility checker command-line tool |
| Web tool | — | <https://magikeygedcomconverter.azurewebsites.net/Compatibility> | Compatibillity checker website |
| Web tool | — | <https://gedcom7code.github.io/js-gedcom/> | GEDCOM file validator website |
| Web tool | — | <https://magikeygedcomconverter.azurewebsites.net/Validate> | GEDCOM file validator website |

## Example FamilySearch GEDCOM 7.0 Files

The following files are provided for testing.

| File     | Notes                  |
|----------|------------------------|
| [age.ged](/testfiles/gedcom70/age.ged) | This file contains various test cases for `AGE` payloads. |
| [age-all.ged](/testfiles/gedcom70/age-all.ged) | This file contains many different `AGE` payloads. |
| [escapes.ged](/testfiles/gedcom70/escapes.ged) | This file contains @ characters that are doubled only when they appear at the start of a line string. |
| [date-all.ged](/testfiles/gedcom70/date-all.ged) | This file contains many different `DATE` payloads. |
| [extension-record.ged](/testfiles/gedcom70/extension-record.ged) | This file contains a `_LOC` record, which is referenced from an individual with a _LOC tag. |
| [lang.ged](/testfiles/gedcom70/lang.ged) | This file contains many different `LANG` payloads. |
| [filename-1.ged](/testfiles/gedcom70/filename-1.ged) | This file contains many different `FILE` payloads. |
| [long-url.ged](/testfiles/gedcom70/long-url.ged) | This file contains a URL of a submitter that is very long, to test the ability to parse very long lines. |
| [maximal70.ged](/testfiles/gedcom70/maximal70.ged) | This file attempts to exercise all standard tags in various locations, and all standard enumeration values. |
| [maximal70.gdz](/testfiles/gedcom70/maximal70.gdz) | This FamilySearch GEDZIP 7.0 file attempts to exercise all standard tags in various locations, and all standard enumeration values, and also includes a minimal local audio file.
| [minimal70.ged](/testfiles/gedcom70/minimal70.ged) | This file is the smallest legal FamilySearch GEDCOM 7.0 file. |
| [minimal70.gdz](/testfiles/gedcom70/minimal70.gdz) | This file is the smallest legal FamilySearch GEDZIP 7.0 file. |
| [notes-1.ged](/testfiles/gedcom70/notes-1.ged) | This file contains many different uses of `NOTE` and `SNOTE`. |
| [obje-1.ged](/testfiles/gedcom70/obje-1.ged) | This file contains many different uses of `OBJE` records. |
| [rela_1.ged](/testfiles/gedcom70/rela_1.ged) | This file contains many different uses of `RELA` payloads. |
| [remarriage1.ged](/testfiles/gedcom70/remarriage1.ged) | This file contains a couple who married, divorced, and then later remarried, stored as one family. |
| [remarriage2.ged](/testfiles/gedcom70/remarriage2.ged) | This file contains a couple who married, divorced, and then later remarried, stored as two separate families. |
| [same-sex-marriage.ged](/testfiles/gedcom70/same-sex-marriage.ged) | This file contains a same sex marriage. |
| [sour-1.ged](/testfiles/gedcom70/sour-1.ged) | This file contains many different uses of `SOUR` records and payloads. |
| [voidptr.ged](/testfiles/gedcom70/voidptr.ged) | This file contains several `@VOID@` references. |
| [xref.ged](/testfiles/gedcom70/xref.ged) | This file contains a number of different cross-reference identifier formats. |

## Extension Registry

As part of publishing each version of the [FamilySearch GEDCOM 7 specification](https://gedcom.io/specs/#familysearch-gedcom-version-7), a set of YAML files are generated describing each structure type, enumeration set, enumeration value, calendar, and month.
The format is [documented](/terms/format)
and served at the URIs documented in the specification (e.g., <https://gedcom.io/terms/v7/HEAD>).

The full set of YAML files, together with some synthesis information such as parsing metadata and lists of all structure types, can be found in the [GEDCOM-registries github repository](https://github.com/familysearch/gedcom-registries).
The GEDCOM-registries repository also hosts YAML files for extensions to the specification,
facilitating interoperability beyond the official specification.

## Machine-Readable Specification Files

Machine-readable files are automatically generated from the specification, as discussed in a
[README file](https://github.com/FamilySearch/GEDCOM/tree/main/extracted-files/README.md).
These files include:

| File     | Notes                  |
|----------|------------------------|
| [cardinalities.tsv](https://github.com/FamilySearch/GEDCOM/blob/main/extracted-files/cardinalities.tsv) | This tab-separated-values (TSV) file contains (superstructure type, substructure type, cardinality of substructure) triples. |
| [enumerations.tsv](https://github.com/FamilySearch/GEDCOM/blob/main/extracted-files/enumerations.tsv) | This tab-separated-values (TSV) file contains (enumeration set, enumeration value) pairs. |
| [enumerationsets.tsv](https://github.com/FamilySearch/GEDCOM/blob/main/extracted-files/enumerations.tsv) | This tab-separated-values (TSV) file contains (structure type, enmeration set) pairs. |
| [grammar.abnf](https://github.com/FamilySearch/GEDCOM/blob/main/extracted-files/grammar.abnf) | This file contains all of the ABNF blocks from the specification concatenated into one file. |
| [grammar.gedstruct](https://github.com/FamilySearch/GEDCOM/blob/main/extracted-files/grammar.gedstruct) | This file contains all of the blocks from the specification in the structure organization metasyntax concatenated into one file. |
| [payloads.tsv](https://github.com/FamilySearch/GEDCOM/blob/main/extracted-files/payloads.tsv) | This tab-separated-values (TSV) file contains (structure type, payload type) pairs. |
| [substructures.tsv](https://github.com/FamilySearch/GEDCOM/blob/main/extracted-files/substructures.tsv) | This tab-separated-values (TSV) file contains (superstructure type, substructure tag, substructure type) triples. |
| [tags](https://github.com/FamilySearch/GEDCOM/blob/main/extracted-files/tags) | This directory contains YAML files for all URI-identified terms defined in the specification, including structure types, enumeration values and sets, calendar identifiers, and month names. The contents of this directory is mirrored into directories in the [Extension Registry](#extension-registry). |

## Other Development Tools

Other development, conversions tools and sample files will be posted here as they become available.
If you have a FamilySearch GEDCOM 7 tool that we should list, post an announcement of the tool on the [GEDCOM Discussions](https://github.com/FamilySearch/GEDCOM/discussions).
