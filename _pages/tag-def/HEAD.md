---
title: HEAD
permalink: /terms/v7/HEAD.html
layout: none
redirect-from:
  - /terms/v7/HEAD
...

```

%YAML 1.2
---
type: structure

tag: HEAD

superstructures: [RECORD]

substructures:
  COPR: "{0:1}"
  DEST: "{0:1}"
  GEDC: "{1:1}"
  HEAD.COMM: "{0:1}"
  HEAD.DATE: "{0:1}"
  HEAD.PLAC: "{0:1}"
  HEAD.SOUR: "{0:1}"
  LANG: "{0:1}"
  SCHMA: "{0:1}"
  SUBM: "{0:1}"

payload: None

descriptions:
  - also called HEADER
  - Tag abbreviated from "Header"
  - A pseudo-structure for storing metadata about the document. See The
    Header and Trailer for more.
  - |
    The header pseudo-structure provides metadata about the entire GEDCOM
    document. A few substructures of note:
    
    -   GEDC gives the GEDCOM standard this document conforms to.
    -   SCHMA gives the meaning of extension tags; see Extensions for more.
    -   SOUR describes the originating software.
        -   SOUR.CORP describes the corporation creating the software.
        -   SOUR.DATA describes a larger database this data is extracted
            from.
    -   LANG and PLAC give a default value for the rest of the document.
...

```