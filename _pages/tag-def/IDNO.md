---
title: IDNO
permalink: /terms/v7/IDNO.html
layout: none
redirect-from:
  - /terms/v7/IDNO
...

```

%YAML 1.2
---
type: structure

tag: IDNO

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
  TYPE: "{1:1}"
  UID: "{0:M}"
  WWW: "{0:M}"

payload: Special

descriptions:
  - Tag abbreviated from "identifying number"
  - A type of INDIVIDUAL_ATTRIBUTE_STRUCTURE
  - A number or other string assigned to identify a person within some
    significant external system. It must have a TYPE substructure to define
    what kind of identification number is being provided.
...

```