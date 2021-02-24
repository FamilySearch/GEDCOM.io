---
title: HEAD.SOUR.DATA
permalink: /terms/v7/HEAD.SOUR.DATA.html
layout: none
redirect-from:
  - /terms/v7/HEAD.SOUR.DATA
...

```

%YAML 1.2
---
type: structure

tag: DATA

superstructures: [HEAD.SOUR]

substructures:
  COPR: "{0:1}"
  HEAD.SOUR.DATA.DATE: "{0:1}"

payload: Text

descriptions:
  - Tag abbreviated from "Source Data"
  - The electronic data source or digital repository from which this GEDCOM
    document was exported. The payload is the name of that source, with
    substructures providing additional details.
...

```