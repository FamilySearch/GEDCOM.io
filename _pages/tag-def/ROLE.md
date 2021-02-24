---
title: ROLE
permalink: /terms/v7/ROLE.html
layout: none
redirect-from:
  - /terms/v7/ROLE
...

```

%YAML 1.2
---
type: structure

tag: ROLE

superstructures: [ASSO, EVEN]

substructures:
  PHRASE: "{0:1}"

payload: Enum

enumeraton values: [CHIL, CLERGY, FATH, FRIEND, GODP, HUSB, MOTH, 
  MULTIPLE, NGHBR, OFFICIATOR, OTHER, PARENT, SPOU, WIFE, WITN]

descriptions:
  - Tag abbreviated from "Role"
  - |
    An enumerated value indicating what role this person played in an event
    or person's life.
    
    The following indicates a child's birth record as the source of the
    mother's name:
    
        0 @I1@ INDI
        1 NAME Mary //
        2 SOUR @S1@
        3 EVEN BIRT
        4 ROLE MOTH
    
    The following indicates that a person's best friend was a witness at
    their baptism:
    
        0 @I2@ INDI
        1 ASSO @I3@
        2 ROLE FRIEND
        3 PHRASE best friend
        1 BAPM
        2 ASSO @I3@
        3 ROLE WITN
...

```