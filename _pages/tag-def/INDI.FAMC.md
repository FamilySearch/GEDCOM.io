---
title: INDI.FAMC
permalink: /terms/v7/INDI.FAMC.html
layout: none
redirect-from:
  - /terms/v7/INDI.FAMC
...

```

%YAML 1.2
---
type: structure

tag: FAMC

superstructures: [INDI]

substructures:
  FAMC.STAT: "{0:1}"
  NOTE: "{0:M}"
  PEDI: "{0:1}"
  SNOTE: "{0:M}"

payload: xref:FAM

descriptions:
  - Tag abbreviated from "Family child"
  - The family in which an individual appears as a child. It is also used
    with a STAT substructure to show individuals who are not children of the
    family. See FAM and FAMC.STAT for more.
...

```