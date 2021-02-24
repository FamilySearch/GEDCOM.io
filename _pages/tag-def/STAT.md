---
title: STAT
permalink: /terms/v7/STAT.html
layout: none
redirect-from:
  - /terms/v7/STAT
...

```

%YAML 1.2
---
type: structure

tag: STAT

superstructures: [BAPL, CONL, ENDL, INIT, SLGC, SLGS]

substructures:
  STAT.DATE: "{1:1}"

payload: Enum

enumeraton values: [BIC, CANCELED, CHILD, COMPLETED, DNS, DNS_CAN, 
  EXCLUDED, INFANT, PRE_1970, STILLBORN, SUBMITTED, UNCLEARED]

descriptions:
  - Tag abbreviated from "Status"
  - An enumerated value assessing of the state or condition of something.
    Expected values differ by context; see FAMC.STAT and (Latter-Day Saint
    Ordinance).STAT for more.
...

```