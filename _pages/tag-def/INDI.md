---
title: INDI
permalink: /terms/v7/INDI.html
layout: none
redirect-from:
  - /terms/v7/INDI
...

```

%YAML 1.2
---
type: structure

tag: INDI

superstructures: [RECORD]

substructures:
  ADOP: "{0:M}"
  ALIA: "{0:M}"
  ANCI: "{0:M}"
  ASSO: "{0:M}"
  BAPL: "{0:M}"
  BAPM: "{0:M}"
  BARM: "{0:M}"
  BASM: "{0:M}"
  BIRT: "{0:M}"
  BLES: "{0:M}"
  BURI: "{0:M}"
  CAST: "{0:M}"
  CHAN: "{0:1}"
  CHR: "{0:M}"
  CHRA: "{0:M}"
  CONF: "{0:M}"
  CONL: "{0:M}"
  CREA: "{0:1}"
  CREM: "{0:M}"
  DEAT: "{0:M}"
  DESI: "{0:M}"
  DSCR: "{0:M}"
  EDUC: "{0:M}"
  EMIG: "{0:M}"
  ENDL: "{0:M}"
  EXID: "{0:M}"
  FAMS: "{0:M}"
  FCOM: "{0:M}"
  GRAD: "{0:M}"
  IDNO: "{0:M}"
  IMMI: "{0:M}"
  INDI.CENS: "{0:M}"
  INDI.EVEN: "{0:M}"
  INDI.FACT: "{0:M}"
  INDI.FAMC: "{0:M}"
  INDI.NAME: "{0:M}"
  INDI.NCHI: "{0:M}"
  INDI.RELI: "{0:M}"
  INDI.RESI: "{0:M}"
  INDI.TITL: "{0:M}"
  INIT: "{0:M}"
  NATI: "{0:M}"
  NATU: "{0:M}"
  NMR: "{0:M}"
  NO: "{0:M}"
  NOTE: "{0:M}"
  OBJE: "{0:M}"
  OCCU: "{0:M}"
  ORDN: "{0:M}"
  PROB: "{0:M}"
  PROP: "{0:M}"
  REFN: "{0:M}"
  RESN: "{0:1}"
  RETI: "{0:M}"
  SEX: "{0:1}"
  SLGC: "{0:M}"
  SNOTE: "{0:M}"
  SOUR: "{0:M}"
  SSN: "{0:M}"
  SUBM: "{0:M}"
  UID: "{0:M}"
  WILL: "{0:M}"

payload: None

descriptions:
  - also called INDIVIDUAL_RECORD
  - |
    The individual record is a compilation of facts or hypothesized facts
    about an individual. These facts may come from multiple sources. Source
    citations and notes allow documentation of the source where each of the
    facts were discovered.
    
    A single individual may have facts distributed across multiple
    individual records, connected by ALIA (alias, in the computing sense not
    the pseudonym sense) pointers. See ALIA for more.
    
    Individual records are linked to Family records by use of bi-directional
    pointers. Details about those links are stored as substructures of the
    pointers in the individual record.
    
    Other associations or relationships are represented by the ASSO
    (association) tag. The person's relation or associate is the person
    being pointed to. The association or relationship is stated by the value
    on the subordinate ROLE line.
    
    This records define the INDI with cross-reference identifier "@I2@" is
    the godparent of the current person:
    
        0 @I1@ INDI
        1 ASSO @I2@
        2 ROLE GODP
    
    Events stored as facts within an INDI record may also have FAMC or ASSO
    tags to indicate families and individuals that participated in those
    events. For example, a FAMC pointer subordinate to an adoption event
    indicates a relationship to family by adoption; biological parents can
    be shown by a FAMC pointer subordinate to the birth event; the eulogist
    at a funeral can be shown by an ASSO pointer subordinate to the burial
    event; and so on.
...

```