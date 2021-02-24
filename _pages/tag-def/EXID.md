---
title: EXID
permalink: /terms/v7/EXID.html
layout: none
redirect-from:
  - /terms/v7/EXID
...

```

%YAML 1.2
---
type: structure

tag: EXID

superstructures: [FAM, INDI, OBJE, PLAC, REPO, SNOTE, SOUR, SUBM]

substructures:
  EXID.TYPE: "{0:1}"

payload: Special

descriptions:
  - A type of IDENTIFIER_STRUCTURE
  - Tag abbreviated from "External Identifier"
  - |
    An identifier for the subject of the superstructure. The identifier is
    maintained by some external authority; the authority owning the
    identifier is provided in the TYPE substructure; see EXID.TYPE for more.
    
    Depending on the maintaining authority, an EXID may be a unique
    identifier for the subject, an identifier for one of several views of
    the subject, or an identifier for the externally-maintained copy of the
    same information as is contained in this structure. However, unlike UID
    and REFN, EXID does not identify a GEDCOM structure and structures with
    the same EXID may have originated independently rather than by edits
    from the same starting point.
...

```