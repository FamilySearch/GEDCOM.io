---
title: WILL
permalink: /terms/v7/WILL.html
layout: none
redirect-from:
  - /terms/v7/WILL
...

```

%YAML 1.2
---
type: structure

tag: WILL

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

payload: None

descriptions:
  - Tag abbreviated from "will"
  - A type of INDIVIDUAL_EVENT_STRUCTURE
  - A legal document treated as an event, by which a person disposes of his
    or her estate. It takes effect after death. The event date is the date
    the will was signed while the person was alive. (See also PROB)
...

```