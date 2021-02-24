---
title: FAM.EVEN
permalink: /terms/v7/FAM.EVEN.html
layout: none
redirect-from:
  - /terms/v7/FAM.EVEN
...

```

%YAML 1.2
---
type: structure

tag: EVEN

superstructures: [FAM]

substructures:
  ADDR: "{0:1}"
  AGNC: "{0:1}"
  ASSO: "{0:M}"
  CAUS: "{0:1}"
  EMAIL: "{0:M}"
  EVEN.DATE: "{0:1}"
  FAX: "{0:M}"
  HUSB: "{0:1}"
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
  WIFE: "{0:1}"
  WWW: "{0:M}"

payload: Text

descriptions:
  - Tag abbreviated from "Event"
  - A type of FAMILY_EVENT_STRUCTURE
  - |
    An event: a noteworthy happening related to an individual or family. If
    a specific event type exists, it should be used instead of a generic
    EVEN structure. Each EVEN must be classified by a subordinate use of the
    TYPE tag and may be further described in the structure's payload.
    
    A person that signed a lease for land dated October 2, 1837 and a lease
    for mining equipment dated November 4, 1837 would be written in GEDCOM
    as:
    
        0 @I1@ INDI
        1 EVEN
        2 TYPE Land Lease
        2 DATE 2 OCT 1837
        1 EVEN Mining equipment
        2 TYPE Equipment Lease
        2 DATE 4 NOV 1837
...

```