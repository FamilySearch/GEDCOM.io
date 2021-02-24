---
title: DATE
permalink: /terms/v7/DATE.html
layout: none
redirect-from:
  - /terms/v7/DATE
...

```

%YAML 1.2
---
type: structure

tag: DATE

superstructures: [ADOP, ANUL, BAPM, BARM, BASM, BIRT, BLES, BURI, CAST, 
  CENS, CHR, CHRA, CONF, CREM, DATA, DEAT, DIV, DIVF, DSCR, EDUC, EMIG, 
  ENGA, FACT, FCOM, GRAD, IDNO, IMMI, MARB, MARC, MARL, MARR, MARS, NATI, 
  NATU, NCHI, NMR, OCCU, ORDN, PROB, PROP, RELI, RESI, RETI, SSN, TITL, 
  WILL]

substructures:
  PHRASE: "{0:1}"
  TIME: "{0:1}"

payload: DateValue

descriptions:
  - The principle date of the subject of the superstructure. The payload is
    a DateValue, and the DATE structure may have a PHRASE substructure.
...

```