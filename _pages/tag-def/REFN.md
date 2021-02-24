---
title: REFN
permalink: /terms/v7/REFN.html
layout: none
redirect-from:
  - /terms/v7/REFN
...

```

%YAML 1.2
---
type: structure

tag: REFN

superstructures: [FAM, INDI, OBJE, REPO, SNOTE, SOUR, SUBM]

substructures:
  TYPE: "{0:1}"

payload: Special

descriptions:
  - A type of IDENTIFIER_STRUCTURE
  - Tag abbreviated from "Reference"
  - |
    A user-defined number or text that the submitter uses to identify the
    superstructure. For instance, it may be a record number within the
    submitter's automated or manual system, or it may be a page and position
    number on a pedigree chart.
    
    This is metadata about the structure itself, not data about its subject.
    Multiple structures describing different aspects of the same subject
    would have different REFN values.
...

```