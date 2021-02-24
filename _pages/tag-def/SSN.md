---
title: SSN
permalink: /terms/v7/SSN.html
layout: none
redirect-from:
  - /terms/v7/SSN
...

```

%YAML 1.2
---
type: structure

tag: SSN

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

payload: Special

descriptions:
  - A type of INDIVIDUAL_ATTRIBUTE_STRUCTURE
  - Tag abbreviated from "social security number"
  - A number assigned by the United States Social Security Administration,
    used for tax identification purposes. It is a type of IDNO.
...

```