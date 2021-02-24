---
title: DATA.EVEN
permalink: /terms/v7/DATA.EVEN.html
layout: none
redirect-from:
  - /terms/v7/DATA.EVEN
...

```

%YAML 1.2
---
type: structure

tag: EVEN

superstructures: [DATA]

substructures:
  DATA.EVEN.DATE: "{0:1}"
  PLAC: "{0:1}"

payload: List:Enum

enumeraton values: [ADOP, ANUL, BAPM, BARM, BASM, BIRT, BLES, BURI, CAST, 
  CENS, CENS, CHR, CHRA, CONF, CREM, DEAT, DIV, DIVF, DSCR, EDUC, EMIG, 
  ENGA, FCOM, GRAD, IDNO, IMMI, MARB, MARC, MARL, MARR, MARS, NATI, NATU, 
  NCHI, NCHI, NMR, OCCU, ORDN, PROB, PROP, RELI, RESI, RESI, RETI, SSN, 
  TITL, WILL]

descriptions:
  - A list of enumerated values indicating the types of events that were
    recorded in a particular source. Each event type is separated by a comma
    and space. For example, a parish register of births, deaths, and
    marriages would be BIRT, DEAT, MARR.
...

```