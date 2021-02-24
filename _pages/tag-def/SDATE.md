---
title: SDATE
permalink: /terms/v7/SDATE.html
layout: none
redirect-from:
  - /terms/v7/SDATE
...

```

%YAML 1.2
---
type: structure

tag: SDATE

superstructures: [ADOP, ANUL, BAPM, BARM, BASM, BIRT, BLES, BURI, CAST, 
  CENS, CHR, CHRA, CONF, CREM, DEAT, DIV, DIVF, DSCR, EDUC, EMIG, ENGA, 
  EVEN, FACT, FCOM, GRAD, IDNO, IMMI, MARB, MARC, MARL, MARR, MARS, NATI, 
  NATU, NCHI, NMR, OCCU, ORDN, PROB, PROP, RELI, RESI, RETI, SSN, TITL, 
  WILL]

substructures:
  PHRASE: "{0:1}"
  TIME: "{0:1}"

payload: DateValue

descriptions:
  - Tag abbreviated from "Sort date"
  - |
    A date to be used as a sorting hint. It is intended for use when the
    actual date is unknown, but the display order may be dependent on date.
    
    If both a DATE and SDATE are present in the same structure, the SDATE
    should be used for sorting and positioning while the DATE should be
    displayed as the date of the structure.
...

```