---
title: PEDI
permalink: /terms/v7/PEDI.html
layout: none
redirect-from:
  - /terms/v7/PEDI
...

```

%YAML 1.2
---
type: structure

tag: PEDI

superstructures: [FAMC]

substructures:
  PHRASE: "{0:1}"

payload: Enum

enumeraton values: [ADOPTED, BIRTH, FOSTER, OTHER, SEALING]

descriptions:
  - Tag abbreviated from "Pedigree"
  - An enumerated value indicating the type of child-to-family relationship
    represented by the superstructure.
...

```