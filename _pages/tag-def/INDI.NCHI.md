---
title: INDI.NCHI
permalink: /terms/v7/INDI.NCHI.html
layout: none
redirect-from:
  - /terms/v7/INDI.NCHI
...

```

%YAML 1.2
---
type: structure

tag: NCHI

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
  TYPE: "{0:1}"
  UID: "{0:M}"
  WWW: "{0:M}"

payload: Integer

descriptions:
  - Tag abbreviated from "number of children"
  - A type of INDIVIDUAL_ATTRIBUTE_STRUCTURE
  - The number of children that this person is known to be the parent of
    (all marriages).
...

```