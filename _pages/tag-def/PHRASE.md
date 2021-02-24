---
title: PHRASE
permalink: /terms/v7/PHRASE.html
layout: none
redirect-from:
  - /terms/v7/PHRASE
...

```

%YAML 1.2
---
type: structure

tag: PHRASE

superstructures: [ADOP, AGE, ALIA, ASSO, CHIL, DATE, EVEN, HUSB, MEDI, 
  PEDI, ROLE, SDATE, STAT, TYPE, WIFE]

substructures:

payload: Text

descriptions:
  - |
    Textual information that cannot be expressed in the superstructure due
    to the limitations of its datatype.
    
    A date interpreted from the phrase "The Feast of St John" might be
    
        2 DATE 24 JUNE 1852
        3 PHRASE During the feast of St John
    
    A record using 1648/9 to indicate a change in new year might become
    
        2 DATE 30 JAN 1649
        3 PHRASE 30th of January, 1648/9
    
    A record using 1648/9 to indicate uncertainty in the year might become
    
        2 DATE BET 1648 AND 1649
        3 PHRASE 1648/9
    
    A record using Q1 1867 to indicate an event occurred sometime within the
    first quarter of 1867 might become
    
        2 DATE BET 1 JAN 1867 AND 31 MAR 1867
        3 PHRASE Q1 1867
    
    A record defining the Maid of Honor in a marriage might become
    
        1 MARR
        2 ASSO @I2@
        3 ROLE OTHER
        4 PHRASE Maid of Honor
    
    A name given to a foundling orphan might be
    
        1 NAME Mary //
        2 GIVN Mary
        2 TYPE OTHER
        3 PHRASE given by orphanage
...

```