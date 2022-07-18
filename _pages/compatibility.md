---
title: FamilySearch GEDCOM Compatibility Guide
permalink: /compatibility/
sidebar:
  nav: "compatibility"
---
***Helpful information and requirements to become a FamilySearch GEDCOM Compatible product***


## Compatibility Requirements

* READ/WRITE FAMILYSEARCH GEDCOM FILE
> The vendor needs to demonstrate the ability to both read and write a FamilySearch GEDCOM file and prove that the result is valid FamilySearch GEDCOM 7.  The [maximal70.ged](..\testfiles\gedcom70\maximal70.ged) file can be used to determine a [compatibility score](https://magikeygedcomconverter.azurewebsites.net/Compatibility), and the [GEDCOM validator](http://ged-inline.elasticbeanstalk.com/) can be used to show validity, although it is still in beta.

* READ FAMILYSEARCH GEDCOM FILE
> The vendor needs to demonstrate the ability to read the [maximal70.ged](../testfiles/gedcom70/maximal70.ged) file and display the contents in their own environment.


* WRITE FAMILYSEARCH GEDCOM FILE
> The vendor needs to demonstrate the ability to write a sample FamilySearch GEDCOM file and prove that it is valid FamilySearch GEDCOM 7. For example, the [GEDCOM validator](http://ged-inline.elasticbeanstalk.com/) can be used, although it is still in beta.
>
* PACKAGE GEDZIP
>
The vendor needs to demonstrate the ability to make according to specifications a .gdz file that includes the .ged file that points to both included local and online resources using the multimedia link as defined by the FamilySearch GEDCOM specification.
>
* UNPACKAGE GEDZIP
>
The vendor needs to demonstrate unzipping a .gdz file and how the unpackaged resources are accessible with the FamilySearch GEDCOM Compatible product that was used to unzip the file and how the multimedia links do point to both included local and online resources.

<!-- ## Compatibility Categories

Like [FamilySearch API compatibility](https://www.familysearch.org/developers/docs/certification), FamilySearch GEDCOM file compatibility can be broken down into several categories.

### Minimal Compatibility

Support for the following structures are required for *all* categories: `CONT`, `GEDC`, `HEAD`, `TRLR`, and `GEDC`.`VERS`.

### Tree Compatibility

**Level 1**: In addition to the Minimal Compatibility requirements, the implementation must support the following structures: `ABBR`, `AUTH`, `BIRT`, `BURI`, `CHIL`, `CHR`, `<<EVENT_DETAIL>>`.`DATE`, `DEAT`, `FAM` (`<<FAMILY_RECORD>>`), `FAM`.`SOUR`, `INDI`.`FAMC`, `FAMS`, `FAM`.`HUSB`, `INDI` (`<<INDIVIDUAL_RECORD>>`), `INDI`.`SOUR`, `MARR`, `INDI`.`NAME`, `INDI`.`NOTE`, `PAGE`, `<<EVENT_DETAIL>>`.`PLAC`, `PUBL`, `SEX`, `SOUR` (`<<SOURCE_RECORD>>`), `SOUR`.`TITL`, and `FAM`.`WIFE`, where `<<EVENT_DETAIL>>` refers to all individual events required for this level.

**Level 2**: In addition to the Level 1 requirements, the implementation must support the following structures.

* `<<INDIVIDUAL_ATTRIBUTE_STRUCTURE>>` structures: `CAST`, `DSCR`, `EDUC`, `IDNO`, `NATI`, `NCHI`, `NMR`, `OCCU`, `PROP`, `RELI`, `RESI`, `SSN`, `INDI`.`TITL`, `FACT`, and `TYPE`.
* `<<INDIVIDUAL_EVENT_STRUCTURE>>` structures: `BAPM`, `BARM`, `BASM`, `BLES`, `CENS`, `CHRA`, `CONF`, `CREM`, `EMIG`, `FCOM`, `GRAD`, `IMMI`, `NATU`, `ORDN`, `PROB`, `RETI`, `WILL`, `ADOP`, `EVEN`, and `TYPE`.
* `<<FAMILY_ATTRIBUTE_STRUCTURE>>` structures: `NCHI`, `RESI`, `FACT`, and `TYPE`.
* `<<FAMILY_EVENT_STRUCTURE>>` structures: `ANUL`, `CENS`, `DIV`, `DIVF`, `ENGA`, `MARB`, `MARC`, `MARL`, `MARS`, `EVEN`, and `TYPE`.
* Detailed source citations: `<<EVENT_DETAIL>>.SOUR`, `INDI`.`NAME`.`SOUR`, and `NOTE`.`SOUR`, where `<<EVENT_DETAIL>>` refers to all required individual and family attributes and events.
* Detailed notes: `<<EVENT_DETAIL>>.NOTE`, where `<<EVENT_DETAIL>>` refers to all required individual and family attributes and events.

### Memories Compatibility

**Level 1**: The implementation must support at least Level 1 of Tree Compatibility, and also support the following structures: `INDI`.`OBJE`, `OBJE` (i.e., `<<MULTIMEDIA_RECORD>>`), `OBJE`.`FILE`, and `OBJE`.`FILE`.`FORM`.

**Level 2**: In addition to the Level 1 requirements, the implementation must also support the following structures:
```
FAM.OBJE
<<EVENT_DETAIL>>.OBJE
SOUR.OBJE
```
where `<<EVENT_DETAIL>>` refers to all events in the Tree Compability level supported by the implementation.
Note that `SUBM.OBJE` support is not required for Level 2.

### Latter-day Saints Services Compatibility

The implementation must support at least Level 1 of Tree Compatibility, and also support the following structures:
`BAPL`, `CONL`, `<<LDS_ORDINANCE_DETAIL>>`.`DATE`, `ENDL`, `INIL`, `SLGC`, `SLGS`, and `TEMP`.
-->
## Development Tools
There are sample code for converting, parsing, and validating. These tools are authored and maintained by third parties and may vary in license, quality, and correctness. Learn about them and access the code by choosing the [Tools](/tools/) menu item.

## Sample Files
There are many sample files that show how to properly encode GEDCOM 7 files to accomodate data for various situations. These can be use to determine importability and to read to learn how to implement GEDCOM 7 for many different scenarios, such as for converting, parsing, and validating. Learn about and download these sample files by choosing the [Tools](/tools/) menu item.

## Implementation Progress
Organizations and Authors that are planning, working on, or finalized their implementation can be viewed by going to [Implementation Progress](https://www.familysearch.org/en/GEDCOM/implementation-progress).
