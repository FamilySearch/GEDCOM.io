---
title: OBJE
permalink: /terms/v7/OBJE.html
layout: none
redirect-from:
  - /terms/v7/OBJE
...

```

%YAML 1.2
---
type: structure

tag: OBJE

superstructures: [ADOP, ANUL, BAPM, BARM, BASM, BIRT, BLES, BURI, CAST, 
  CENS, CHR, CHRA, CONF, CREM, DEAT, DIV, DIVF, DSCR, EDUC, EMIG, ENGA, 
  EVEN, FACT, FAM, FCOM, GRAD, IDNO, IMMI, INDI, MARB, MARC, MARL, MARR, 
  MARS, NATI, NATU, NCHI, NMR, OCCU, ORDN, PROB, PROP, RELI, RESI, RETI, 
  SOUR, SSN, SUBM, TITL, WILL]

substructures:
  CROP: "{0:1}"

payload: xref:OBJE

descriptions:
  - Tag abbreviated from "Object"
  - also called MULTIMEDIA_LINK
  - Links the superstructure to the MULTIMEDIA_RECORD with the given
    pointer, optionally indicating a subregion of an image that represents
    or applies to the superstructure.
  - An external file containing information pertinent to the subject of the
    superstructure if a substructure, or a description of such a file if a
    record. See MULTIMEDIA_RECORD and MULTIMEDIA_LINK for more.
...

```