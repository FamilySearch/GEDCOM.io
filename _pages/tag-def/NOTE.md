---
title: NOTE
permalink: /terms/v7/NOTE.html
layout: none
redirect-from:
  - /terms/v7/NOTE
...

```

%YAML 1.2
---
type: structure

tag: NOTE

superstructures: [ADOP, ANUL, ASSO, BAPL, BAPM, BARM, BASM, BIRT, BLES, 
  BURI, CAST, CENS, CHR, CHRA, CONF, CONL, CREM, DATA, DEAT, DIV, DIVF, 
  DSCR, EDUC, EMIG, ENDL, ENGA, EVEN, FACT, FAM, FAMC, FAMS, FCOM, GRAD, 
  IDNO, IMMI, INDI, INIT, MARB, MARC, MARL, MARR, MARS, NAME, NATI, NATU, 
  NCHI, NMR, NO, OBJE, OCCU, ORDN, PLAC, PROB, PROP, RELI, REPO, RESI, 
  RETI, SLGC, SLGS, SOUR, SSN, SUBM, TITL, WILL]

substructures:
  LANG: "{0:1}"
  MIME: "{0:1}"
  SOUR: "{0:M}"

payload: Text

descriptions:
  - A type of NOTE_STRUCTURE
  - A NOTE_STRUCTURE, containing additional information provided by the
    submitter for understanding the enclosing data.
...

```