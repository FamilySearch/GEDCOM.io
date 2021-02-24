---
title: CORP
permalink: /terms/v7/CORP.html
layout: none
redirect-from:
  - /terms/v7/CORP
...

```

%YAML 1.2
---
type: structure

tag: CORP

superstructures: [SOUR]

substructures:
  ADDR: "{0:1}"
  EMAIL: "{0:M}"
  FAX: "{0:M}"
  PHON: "{0:M}"
  WWW: "{0:M}"

payload: Text

descriptions:
  - Tag abbreviated from "Corporate name"
  - The name of the business, corporation, or person that produced or
    commissioned the product.
...

```