---
title: PLAC.FORM
permalink: /terms/v7/PLAC.FORM.html
layout: none
redirect-from:
  - /terms/v7/PLAC.FORM
...

```

%YAML 1.2
---
type: structure

tag: FORM

superstructures: [PLAC]

substructures:

payload: List:Text

descriptions:
  - Tag abbreviated from "Place format"
  - |
    A comma-separated list of jurisdictional titles, which has the same
    number of elements and in the same order as the PLAC structure. Entries
    should be in an order where each is typically subsumed by the next.
    
    The following represents Baltimore, a city that is not within a county.
    
        2 PLAC Baltimore, , Maryland, USA
        3 FORM City, County, State, Country
...

```