---
title: RESN
permalink: /terms/v7/RESN.html
layout: none
redirect-from:
  - /terms/v7/RESN
...

```

%YAML 1.2
---
type: structure

uri: https://gedcom.io/terms/v7/RESN

standard tag: RESN

descriptions:
  - Restriction
  - |
    A [List] of enumerated values signifying access to information may be
    denied or otherwise restricted.
    
    The RESN structure is provided to assist software in filtering data that
    should not be exported or otherwise used in a particular context. It is
    recommended that tools provide an interface to allow users to filter data
    on export such that certain RESN structure payload entries result in the
    RESN structure and its superstructure being removed from the export. Such
    removal must abode by some constraints: see Removing data for more.
    
    This is metadata about the structure itself, not data about its subject.

payload: https://gedcom.io/terms/v7/type-List#Enum

enumeration values:
  CONFIDENTIAL: https://gedcom.io/terms/v7/enum-CONFIDENTIAL
  LOCKED: https://gedcom.io/terms/v7/enum-LOCKED
  PRIVACY: https://gedcom.io/terms/v7/enum-PRIVACY

substructures: []

superstructures:
  "https://gedcom.io/terms/v7/ADOP": "{0:1}"
  "https://gedcom.io/terms/v7/ANUL": "{0:1}"
  "https://gedcom.io/terms/v7/BAPM": "{0:1}"
  "https://gedcom.io/terms/v7/BARM": "{0:1}"
  "https://gedcom.io/terms/v7/BASM": "{0:1}"
  "https://gedcom.io/terms/v7/BIRT": "{0:1}"
  "https://gedcom.io/terms/v7/BLES": "{0:1}"
  "https://gedcom.io/terms/v7/BURI": "{0:1}"
  "https://gedcom.io/terms/v7/CAST": "{0:1}"
  "https://gedcom.io/terms/v7/CHR": "{0:1}"
  "https://gedcom.io/terms/v7/CHRA": "{0:1}"
  "https://gedcom.io/terms/v7/CONF": "{0:1}"
  "https://gedcom.io/terms/v7/CREM": "{0:1}"
  "https://gedcom.io/terms/v7/DEAT": "{0:1}"
  "https://gedcom.io/terms/v7/DIV": "{0:1}"
  "https://gedcom.io/terms/v7/DIVF": "{0:1}"
  "https://gedcom.io/terms/v7/DSCR": "{0:1}"
  "https://gedcom.io/terms/v7/EDUC": "{0:1}"
  "https://gedcom.io/terms/v7/EMIG": "{0:1}"
  "https://gedcom.io/terms/v7/ENGA": "{0:1}"
  "https://gedcom.io/terms/v7/FAM-CENS": "{0:1}"
  "https://gedcom.io/terms/v7/FAM-EVEN": "{0:1}"
  "https://gedcom.io/terms/v7/FAM-FACT": "{0:1}"
  "https://gedcom.io/terms/v7/FAM-NCHI": "{0:1}"
  "https://gedcom.io/terms/v7/FAM-RESI": "{0:1}"
  "https://gedcom.io/terms/v7/FCOM": "{0:1}"
  "https://gedcom.io/terms/v7/GRAD": "{0:1}"
  "https://gedcom.io/terms/v7/IDNO": "{0:1}"
  "https://gedcom.io/terms/v7/IMMI": "{0:1}"
  "https://gedcom.io/terms/v7/INDI-CENS": "{0:1}"
  "https://gedcom.io/terms/v7/INDI-EVEN": "{0:1}"
  "https://gedcom.io/terms/v7/INDI-FACT": "{0:1}"
  "https://gedcom.io/terms/v7/INDI-NCHI": "{0:1}"
  "https://gedcom.io/terms/v7/INDI-RELI": "{0:1}"
  "https://gedcom.io/terms/v7/INDI-RESI": "{0:1}"
  "https://gedcom.io/terms/v7/INDI-TITL": "{0:1}"
  "https://gedcom.io/terms/v7/MARB": "{0:1}"
  "https://gedcom.io/terms/v7/MARC": "{0:1}"
  "https://gedcom.io/terms/v7/MARL": "{0:1}"
  "https://gedcom.io/terms/v7/MARR": "{0:1}"
  "https://gedcom.io/terms/v7/MARS": "{0:1}"
  "https://gedcom.io/terms/v7/NATI": "{0:1}"
  "https://gedcom.io/terms/v7/NATU": "{0:1}"
  "https://gedcom.io/terms/v7/NMR": "{0:1}"
  "https://gedcom.io/terms/v7/OCCU": "{0:1}"
  "https://gedcom.io/terms/v7/ORDN": "{0:1}"
  "https://gedcom.io/terms/v7/PROB": "{0:1}"
  "https://gedcom.io/terms/v7/PROP": "{0:1}"
  "https://gedcom.io/terms/v7/RETI": "{0:1}"
  "https://gedcom.io/terms/v7/SSN": "{0:1}"
  "https://gedcom.io/terms/v7/WILL": "{0:1}"
  "https://gedcom.io/terms/v7/record-FAM": "{0:1}"
  "https://gedcom.io/terms/v7/record-INDI": "{0:1}"
  "https://gedcom.io/terms/v7/record-OBJE": "{0:1}"
...

```