---
title: SOUR.EVEN
permalink: /terms/v7/SOUR.EVEN.html
layout: none
redirect-from:
  - /terms/v7/SOUR.EVEN
...

```

%YAML 1.2
---
type: structure

tag: EVEN

superstructures: [SOUR]

substructures:
  PHRASE: "{0:1}"
  ROLE: "{0:1}"

payload: Enum

enumeraton values: [ADOP, ANUL, BAPM, BARM, BASM, BIRT, BLES, BURI, CENS, 
  CENS, CHR, CHRA, CONF, CREM, DEAT, DIV, DIVF, EMIG, ENGA, FCOM, GRAD, 
  IMMI, MARB, MARC, MARL, MARR, MARS, NATU, ORDN, PROB, RETI, WILL]

descriptions:
  - An enumerated value indicating the type of event which was responsible
    for the source entry being recorded. For example, if the entry was
    created to record a birth of a child, then the type would be BIRT
    regardless of the assertions made from that record, such as the mother's
    name or mother's birth date.
...

```