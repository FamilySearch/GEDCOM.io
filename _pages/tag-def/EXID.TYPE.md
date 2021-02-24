---
title: EXID.TYPE
permalink: /terms/v7/EXID.TYPE.html
layout: none
redirect-from:
  - /terms/v7/EXID.TYPE
...

```

%YAML 1.2
---
type: structure

tag: TYPE

superstructures: [EXID]

substructures:

payload: Text

descriptions:
  - |
    The authority issuing the EXID, represented as a URI. It is recommended
    that this be a URL.
    
    If the authority maintains stable URLs for each identifier it issues, it
    is recommended that the TYPE payload be selected such that appending the
    EXID payload to it yields that URL. However, this is not required and a
    different URI for the set of issued identifiers may be used instead.
...

```