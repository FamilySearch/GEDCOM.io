---
title: SNOTE
permalink: /terms/v7/SNOTE.html
layout: none
redirect-from:
  - /terms/v7/SNOTE
...

```

%YAML 1.2
---
type: structure

tag: SNOTE

superstructures: [ADOP, ANUL, ASSO, BAPL, BAPM, BARM, BASM, BIRT, BLES, 
  BURI, CAST, CENS, CHR, CHRA, CONF, CONL, CREM, DATA, DEAT, DIV, DIVF, 
  DSCR, EDUC, EMIG, ENDL, ENGA, EVEN, FACT, FAM, FAMC, FAMS, FCOM, GRAD, 
  IDNO, IMMI, INDI, INIT, MARB, MARC, MARL, MARR, MARS, NAME, NATI, NATU, 
  NCHI, NMR, NO, OBJE, OCCU, ORDN, PLAC, PROB, PROP, RELI, REPO, RESI, 
  RETI, SLGC, SLGS, SOUR, SSN, SUBM, TITL, WILL]

substructures:

payload: xref:SNOTE

descriptions:
  - A type of NOTE_STRUCTURE
  - Tag abbreviated from "Shared Note"
  - A note that is shared by multiple structures (if a record) or a pointer
    to such a note (if a substructure). See SHARED_NOTE_RECORD and
    NOTE_STRUCTURE for more.
...

```