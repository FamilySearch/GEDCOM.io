---
title: INDI.CENS
permalink: /terms/v7/INDI.CENS.html
layout: none
redirect-from:
  - /terms/v7/INDI.CENS
...

```

%YAML 1.2
---
type: structure

tag: CENS

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

payload: None

descriptions:
  - Tag abbreviated from "census"
  - A type of INDIVIDUAL_EVENT_STRUCTURE
  - Periodic count of the population for a designated locality, such as a
    national or state Census.
...

```