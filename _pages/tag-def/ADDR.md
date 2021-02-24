---
title: ADDR
permalink: /terms/v7/ADDR.html
layout: none
redirect-from:
  - /terms/v7/ADDR
...

```

%YAML 1.2
---
type: structure

tag: ADDR

superstructures: [ADOP, ANUL, BAPM, BARM, BASM, BIRT, BLES, BURI, CAST, 
  CENS, CHR, CHRA, CONF, CORP, CREM, DEAT, DIV, DIVF, DSCR, EDUC, EMIG, 
  ENGA, EVEN, FACT, FCOM, GRAD, IDNO, IMMI, MARB, MARC, MARL, MARR, MARS, 
  NATI, NATU, NCHI, NMR, OCCU, ORDN, PROB, PROP, RELI, REPO, RESI, RETI, 
  SSN, SUBM, TITL, WILL]

substructures:
  ADR1: "{0:1}"
  ADR2: "{0:1}"
  ADR3: "{0:1}"
  CITY: "{0:1}"
  CTRY: "{0:1}"
  POST: "{0:1}"
  STAE: "{0:1}"

payload: Special

descriptions:
  - Tag abbreviated from "Address"
  - also called ADDRESS_STRUCTURE
  - The location of, or most relevant to, the subject of the superstructure.
    See ADDRESS_STRUCTURE for more.
  - |
    A specific building, plot, or location. The payload is the full
    formatted address as it would appear on a mailing label, including
    appropriate line breaks (encoded using CONT tags). The expected order of
    address components varies by region; the address should be organized as
    expected by the addressed region.
    
    Optionally, additional substructures such as STAE and CTRY are provided
    to be used by systems that have structured their addresses for indexing
    and sorting. If the substructures and ADDR payload disagree, the ADDR
    payload shall be taken as correct. Because the regionally-correct order
    and formatting of address components cannot be determined from the
    substructures alone, the ADDR payload is required, even if its content
    appears to be redundant with the substructures.
...

```