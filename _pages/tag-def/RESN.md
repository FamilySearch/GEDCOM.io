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

tag: RESN

superstructures: [ADOP, ANUL, BAPM, BARM, BASM, BIRT, BLES, BURI, CAST, 
  CENS, CHR, CHRA, CONF, CREM, DEAT, DIV, DIVF, DSCR, EDUC, EMIG, ENGA, 
  EVEN, FACT, FAM, FCOM, GRAD, IDNO, IMMI, INDI, MARB, MARC, MARL, MARR, 
  MARS, NATI, NATU, NCHI, NMR, OBJE, OCCU, ORDN, PROB, PROP, RELI, RESI, 
  RETI, SSN, TITL, WILL]

substructures:

payload: List:Enum

enumeraton values: [CONFIDENTIAL, LOCKED, PRIVACY]

descriptions:
  - Tag abbreviated from "Restriction"
  - |
    An [List] of enumerated values signifying access to information may be
    denied or otherwise restricted.
    
    The RESN structure is provided to assist software in filtering data that
    should not be exported or otherwise used in a particular context. It is
    recommended that tools provide an interface to allow users to filter
    data on export such that certain RESN structure payload entries result
    in the RESN structure and its superstructure being removed from the
    export. Such removal must not violate GEDCOM constraints: see Removing
    data for more.
    
    This is metadata about the structure itself, not data about its subject.
...

```