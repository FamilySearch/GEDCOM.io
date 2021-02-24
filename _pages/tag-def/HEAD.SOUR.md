---
title: HEAD.SOUR
permalink: /terms/v7/HEAD.SOUR.html
layout: none
redirect-from:
  - /terms/v7/HEAD.SOUR
...

```

%YAML 1.2
---
type: structure

tag: SOUR

superstructures: [HEAD]

substructures:
  CORP: "{0:1}"
  HEAD.SOUR.DATA: "{0:1}"
  NAME: "{0:1}"
  VERS: "{0:1}"

payload: Special

descriptions:
  - Tag abbreviated from "Source System"
  - An identifier for the product producing this GEDCOM document. A
    registration process for these identifiers existed for a time, but no
    longer does. If an existing identifier is known, it should be used.
    Otherwise, a URI owned by the product should be used instead.
...

```