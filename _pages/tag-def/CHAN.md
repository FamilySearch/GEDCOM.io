---
title: CHAN
permalink: /terms/v7/CHAN.html
layout: none
redirect-from:
  - /terms/v7/CHAN
...

```

%YAML 1.2
---
type: structure

tag: CHAN

superstructures: [FAM, INDI, OBJE, REPO, SNOTE, SOUR, SUBM]

substructures:
  CHAN.DATE: "{1:1}"
  COMM: "{0:M}"

payload: None

descriptions:
  - also called CHANGE_DATE
  - Tag abbreviated from "Change"
  - The date of the most recent modification of the superstructure,
    optionally with notes about that modification.
  - The most recent change to the superstructure. This is metadata about the
    structure itself, not data about its subject. See CHANGE_DATE for more.
...

```