---
title: EMAIL
permalink: /terms/v7/EMAIL.html
layout: none
redirect-from:
  - /terms/v7/EMAIL
...

```

%YAML 1.2
---
type: structure

tag: EMAIL

superstructures: [ADOP, ANUL, BAPM, BARM, BASM, BIRT, BLES, BURI, CAST, 
  CENS, CHR, CHRA, CONF, CORP, CREM, DEAT, DIV, DIVF, DSCR, EDUC, EMIG, 
  ENGA, EVEN, FACT, FCOM, GRAD, IDNO, IMMI, MARB, MARC, MARL, MARR, MARS, 
  NATI, NATU, NCHI, NMR, OCCU, ORDN, PROB, PROP, RELI, REPO, RESI, RETI, 
  SSN, SUBM, TITL, WILL]

substructures:

payload: Special

descriptions:
  - Tag abbreviated from "Email"
  - |
    An electronic mail address, as defined by any relevant standard such as
    RFC 3696, RFC 5321, or RFC 5322.
    
    If an invalid email address is present upon import, it should be
    preserved as-is on export.
    
    GEDCOM 5.5.1 contained a typo where this tag was sometimes written EMAI
    and sometimes written EMAIL. EMAIL should be used in GEDCOM 7.0 and
    later.
...

```