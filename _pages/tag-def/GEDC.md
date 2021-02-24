---
title: GEDC
permalink: /terms/v7/GEDC.html
layout: none
redirect-from:
  - /terms/v7/GEDC
...

```

%YAML 1.2
---
type: structure

tag: GEDC

superstructures: [HEAD]

substructures:
  GEDC.VERS: "{1:1}"

payload: None

descriptions:
  - Tag abbreviated from "Gedcom"
  - |
    A container for information about the entire document.
    
    It is recommended that applications write GEDC with its required
    subrecord VERS as the first substructure under HEAD.
...

```