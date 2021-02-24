---
title: INDI.FACT
permalink: /terms/v7/INDI.FACT.html
layout: none
redirect-from:
  - /terms/v7/INDI.FACT
...

```

%YAML 1.2
---
type: structure

tag: FACT

superstructures: [INDI]

substructures:
  ADDR: "{0:1}"
  AGE: "{0:1}"
  AGNC: "{0:1}"
  ASSO: "{0:M}"
  CAUS: "{0:1}"
  DATE: "{0:1}"
  EMAIL: "{0:M}"
  FAX: "{0:M}"
  NOTE: "{0:M}"
  OBJE: "{0:M}"
  PHON: "{0:M}"
  PLAC: "{0:1}"
  RELI: "{0:1}"
  RESN: "{0:1}"
  SDATE: "{0:1}"
  SNOTE: "{0:M}"
  SOUR: "{0:M}"
  TYPE: "{1:1}"
  UID: "{0:M}"
  WWW: "{0:M}"

payload: Text

descriptions:
  - A type of INDIVIDUAL_ATTRIBUTE_STRUCTURE
  - |
    A noteworthy attribute or fact concerning an individual or family. If a
    specific attribute type exists, it should be used instead of a generic
    FACT structure. Each FACT must be classified by a subordinate use of the
    TYPE tag and may be further described in the structure's payload.
    
    If the attribute being defined was one of the person's skills, such as
    woodworking, the FACT tag would have the value of "Woodworking",
    followed by a subordinate TYPE tag with the value "Skills".
    
        0 @I1@ INDI
        1 FACT Woodworking
        2 TYPE Skills
...

```