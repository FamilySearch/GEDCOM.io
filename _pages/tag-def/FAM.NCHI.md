---
title: FAM.NCHI
permalink: /terms/v7/FAM.NCHI.html
layout: none
redirect-from:
  - /terms/v7/FAM.NCHI
...

```

%YAML 1.2
---
type: structure

tag: NCHI

superstructures: [FAM]

substructures:
  ADDR: "{0:1}"
  AGNC: "{0:1}"
  ASSO: "{0:M}"
  CAUS: "{0:1}"
  DATE: "{0:1}"
  EMAIL: "{0:M}"
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
  TYPE: "{0:1}"
  UID: "{0:M}"
  WIFE: "{0:1}"
  WWW: "{0:M}"

payload: Integer

descriptions:
  - A type of FAMILY_ATTRIBUTE_STRUCTURE
  - Tag abbreviated from "number of children"
  - The number of children that belong to this family.
...

```