---
title: ASSO
permalink: /terms/v7/ASSO.html
layout: none
redirect-from:
  - /terms/v7/ASSO
...

```

%YAML 1.2
---
type: structure

tag: ASSO

superstructures: [ADOP, ANUL, BAPM, BARM, BASM, BIRT, BLES, BURI, CAST, 
  CENS, CHR, CHRA, CONF, CREM, DEAT, DIV, DIVF, DSCR, EDUC, EMIG, ENGA, 
  EVEN, FACT, FAM, FCOM, GRAD, IDNO, IMMI, INDI, MARB, MARC, MARL, MARR, 
  MARS, NATI, NATU, NCHI, NMR, OCCU, ORDN, PROB, PROP, RELI, RESI, RETI, 
  SSN, TITL, WILL]

substructures:
  NOTE: "{0:M}"
  PHRASE: "{0:1}"
  ROLE: "{1:1}"
  SNOTE: "{0:M}"
  SOUR: "{0:M}"

payload: xref:INDI

descriptions:
  - Tag abbreviated from "Associates"
  - also called ASSOCIATION_STRUCTURE
  - A pointer to an associated individual. See ASSOCIATION_STRUCTURE for
    more.
  - |
    An individual associated with the subject of the superstructure. The
    nature of the association is indicated in the ROLE substructure.
    
    A voidPtr and PHRASE can be used to describe associations to people not
    referenced by any INDI record.
    
    The following indicates that "Mr Stockdale" was the individual's teacher
    and that individual @I2@ was the clergy officiating at their baptism.
    
        0 @I1@ INDI
        1 ASSO @VOID@
        2 PHRASE Mr Stockdale
        2 ROLE OTHER
        3 PHRASE Teacher
        1 BAPM
        2 DATE 1930
        2 ASSO @I2@
        3 ROLE CLERGY
...

```