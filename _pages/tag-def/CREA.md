---
title: CREA
permalink: /terms/v7/CREA.html
layout: none
redirect-from:
  - /terms/v7/CREA
...

```

%YAML 1.2
---
type: structure

tag: CREA

superstructures: [FAM, INDI, OBJE, REPO, SNOTE, SOUR, SUBM]

substructures:
  CREA.DATE: "{1:1}"

payload: None

descriptions:
  - also called CREATION_DATE
  - Tag abbreviated from "Creation"
  - The initial creation of the superstructure. This is metadata about the
    structure itself, not data about its subject. See CREATION_DATE for
    more.
  - The date of the initial creation of the superstructure. Because this
    refers to the initial creation, it should not be modified after the
    structure is created.
...

```