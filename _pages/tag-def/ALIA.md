---
title: ALIA
permalink: /terms/v7/ALIA.html
layout: none
redirect-from:
  - /terms/v7/ALIA
...

```

%YAML 1.2
---
type: structure

tag: ALIA

superstructures: [INDI]

substructures:
  PHRASE: "{0:1}"

payload: xref:INDI

descriptions:
  - Tag abbreviated from "Alias"
  - |
    A single individual may have facts distributed across multiple
    individual records, connected by ALIA pointers (named after "alias" in
    the computing sense, not the pseudonym sense).
    
    This standard does not define how to connect INDI records with ALIA.
    Some systems organize ALIA pointers to create a tree structure, with the
    root INDI record containing the composite view of all facts in the leaf
    INDI records. Others distribute events and attributes between INDI
    records mutually linked by symmetric pairs of ALIA pointers. A future
    version of GEDCOM may adjust the definition of ALIA.
...

```