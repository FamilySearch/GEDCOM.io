---
title: INDI.RELI
permalink: /terms/v7/INDI.RELI.html
layout: none
redirect-from:
  - /terms/v7/INDI.RELI
...

```

%YAML 1.2
---
type: structure

tag: RELI

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
  TYPE: "{0:1}"
  UID: "{0:M}"
  WWW: "{0:M}"

payload: Text

descriptions:
  - Tag abbreviated from "religion"
  - A type of INDIVIDUAL_ATTRIBUTE_STRUCTURE
  - A religious denomination to which a person is affiliated or for which a
    record applies.
  - An individual attribute; see INDIVIDUAL_ATTRIBUTE_STRUCTURE and
    [Individual Attributes] for more.
...

```