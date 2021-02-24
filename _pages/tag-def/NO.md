---
title: NO
permalink: /terms/v7/NO.html
layout: none
redirect-from:
  - /terms/v7/NO
...

```

%YAML 1.2
---
type: structure

tag: NO

superstructures: [FAM, INDI]

substructures:
  NO.DATE: "{0:1}"
  NOTE: "{0:M}"
  SNOTE: "{0:M}"
  SOUR: "{0:M}"

payload: Enum

enumeraton values: [ADOP, ANUL, BAPM, BARM, BASM, BIRT, BLES, BURI, CAST, 
  CENS, CENS, CHR, CHRA, CONF, CREM, DEAT, DIV, DIVF, DSCR, EDUC, EMIG, 
  ENGA, FCOM, GRAD, IDNO, IMMI, MARB, MARC, MARL, MARR, MARS, NATI, NATU, 
  NCHI, NCHI, NMR, OCCU, ORDN, PROB, PROP, RELI, RESI, RESI, RETI, SSN, 
  TITL, WILL]

descriptions:
  - also called NON_EVENT_STRUCTURE
  - Tag abbreviated from "Did not happen"
  - An enumerated value identifying an event type which did not occur to the
    superstructure's subject. See NON_EVENT_STRUCTURE for more.
  - |
    Indicates that an event, given in the payload, did not happen within a
    given date period (or never happened if there is no DATE substructure).
    
    Substructures may provide discussion about the non-occurrence of the
    event but must not limit the meaning of what did not occur. No
    substructure other than DATE may restrict the breadth of that negative
    assertion.
    
    1 NO DEAT means "no death occurred"
    
        1 NO MARR
        2 DATE TO 24 MAR 1880
    
    means "no marriage had occurred as of March 24^(th), 1880"
...

```