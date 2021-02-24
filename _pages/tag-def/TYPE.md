---
title: TYPE
permalink: /terms/v7/TYPE.html
layout: none
redirect-from:
  - /terms/v7/TYPE
...

```

%YAML 1.2
---
type: structure

tag: TYPE

superstructures: [ADOP, ANUL, BAPM, BARM, BASM, BIRT, BLES, BURI, CAST, 
  CENS, CHR, CHRA, CONF, CREM, DEAT, DIV, DIVF, DSCR, EDUC, EMIG, ENGA, 
  EVEN, FACT, FCOM, GRAD, IDNO, IMMI, MARB, MARC, MARL, MARR, MARS, NATI, 
  NATU, NCHI, NMR, OCCU, ORDN, PROB, PROP, REFN, RELI, RESI, RETI, SSN, 
  TITL, WILL]

substructures:

payload: Text

descriptions:
  - |
    A descriptive word or phrase used to further classify the
    superstructure.
    
    When both a NOTE and free-text TYPE are permitted as substructures of
    the same structure, the displaying systems should always display the
    TYPE value when they display the data from the associated structure;
    NOTE will typically be visible only in a detailed view.
    
    TYPE must be used whenever the generic EVEN, FACT and IDNO tags are
    used. It may also be used for any other event or attribute.
    
    Using the subordinate TYPE classification method provides a further
    classification of the superstructure but does not change its basic
    meaning.
    
    A MARR with a TYPE could clarify what kind of marriage was performed:
    
        0 @I1@ INDI
        1 MARR
        2 TYPE Common Law
    
    This classifies the entry as a common law marriage but the event is
    still a marriage event.
    
    Other descriptor values might include, for example,
    
    -   "Stillborn" as a qualifier to BIRT (birth)
    -   "Tribal Custom" as a qualifier to MARR (marriage)
    -   "College" as a qualifier to GRAD (graduation)
    
    See also FACT and EVEN for additional examples.
...

```