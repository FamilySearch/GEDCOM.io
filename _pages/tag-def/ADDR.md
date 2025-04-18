---
title: ADDR
permalink: /terms/v7/ADDR.html
layout: none
redirect-from:
  - /terms/v7/ADDR
...

```

%YAML 1.2
---
lang: en-US

type: structure

uri: https://gedcom.io/terms/v7/ADDR

standard tag: 'ADDR'

specification:
  - Address
  - The location of, or most relevant to, the subject of the superstructure. See
    `ADDRESS_STRUCTURE` for more details.
  - |
    A specific building, plot, or location. The payload is the full formatted
    address as it would appear on a mailing label, including appropriate line
    breaks (encoded using `CONT` tags). The expected order of address components
    varies by region; the address should be organized as expected by the addressed
    region.
    
    Optionally, additional substructures such as `STAE` and `CTRY` are provided to
    be used by systems that have structured their addresses for indexing and
    sorting. If the substructures and `ADDR` payload disagree, the `ADDR` payload
    shall be taken as correct. Because the regionally-correct order and formatting
    of address components cannot be determined from the substructures alone, the
    `ADDR` payload is required, even if its content appears to be redundant with
    the substructures.
    
    <div class="deprecation">
    
    `ADR1` and `ADR2` were introduced in version 5.5 (1996) and `ADR3` in version
    5.5.1 (1999), defined as "The first/second/third line of an address." Some
    applications interpreted ADR1 as "the first line of the *street* address", but
    most took the spec as-written and treated it as a straight copy of a line of
    text already available in the `ADDR` payload.
    
    Duplicating information bloats files and introduces the potential for
    self-contradiction. `ADR1`, `ADR2`, and `ADR3` should not be added to new
    files.
    
    </div>

label: 'Address'

payload: http://www.w3.org/2001/XMLSchema#string

substructures:
  "https://gedcom.io/terms/v7/ADR1": "{0:1}"
  "https://gedcom.io/terms/v7/ADR2": "{0:1}"
  "https://gedcom.io/terms/v7/ADR3": "{0:1}"
  "https://gedcom.io/terms/v7/CITY": "{0:1}"
  "https://gedcom.io/terms/v7/CTRY": "{0:1}"
  "https://gedcom.io/terms/v7/POST": "{0:1}"
  "https://gedcom.io/terms/v7/STAE": "{0:1}"

superstructures:
  "https://gedcom.io/terms/v7/ADOP": "{0:1}"
  "https://gedcom.io/terms/v7/ANUL": "{0:1}"
  "https://gedcom.io/terms/v7/BAPM": "{0:1}"
  "https://gedcom.io/terms/v7/BARM": "{0:1}"
  "https://gedcom.io/terms/v7/BASM": "{0:1}"
  "https://gedcom.io/terms/v7/BIRT": "{0:1}"
  "https://gedcom.io/terms/v7/BLES": "{0:1}"
  "https://gedcom.io/terms/v7/BURI": "{0:1}"
  "https://gedcom.io/terms/v7/CAST": "{0:1}"
  "https://gedcom.io/terms/v7/CHR": "{0:1}"
  "https://gedcom.io/terms/v7/CHRA": "{0:1}"
  "https://gedcom.io/terms/v7/CONF": "{0:1}"
  "https://gedcom.io/terms/v7/CORP": "{0:1}"
  "https://gedcom.io/terms/v7/CREM": "{0:1}"
  "https://gedcom.io/terms/v7/DEAT": "{0:1}"
  "https://gedcom.io/terms/v7/DIV": "{0:1}"
  "https://gedcom.io/terms/v7/DIVF": "{0:1}"
  "https://gedcom.io/terms/v7/DSCR": "{0:1}"
  "https://gedcom.io/terms/v7/EDUC": "{0:1}"
  "https://gedcom.io/terms/v7/EMIG": "{0:1}"
  "https://gedcom.io/terms/v7/ENGA": "{0:1}"
  "https://gedcom.io/terms/v7/FAM-CENS": "{0:1}"
  "https://gedcom.io/terms/v7/FAM-EVEN": "{0:1}"
  "https://gedcom.io/terms/v7/FAM-FACT": "{0:1}"
  "https://gedcom.io/terms/v7/FAM-NCHI": "{0:1}"
  "https://gedcom.io/terms/v7/FAM-RESI": "{0:1}"
  "https://gedcom.io/terms/v7/FCOM": "{0:1}"
  "https://gedcom.io/terms/v7/GRAD": "{0:1}"
  "https://gedcom.io/terms/v7/IDNO": "{0:1}"
  "https://gedcom.io/terms/v7/IMMI": "{0:1}"
  "https://gedcom.io/terms/v7/INDI-CENS": "{0:1}"
  "https://gedcom.io/terms/v7/INDI-EVEN": "{0:1}"
  "https://gedcom.io/terms/v7/INDI-FACT": "{0:1}"
  "https://gedcom.io/terms/v7/INDI-NCHI": "{0:1}"
  "https://gedcom.io/terms/v7/INDI-RELI": "{0:1}"
  "https://gedcom.io/terms/v7/INDI-RESI": "{0:1}"
  "https://gedcom.io/terms/v7/INDI-TITL": "{0:1}"
  "https://gedcom.io/terms/v7/MARB": "{0:1}"
  "https://gedcom.io/terms/v7/MARC": "{0:1}"
  "https://gedcom.io/terms/v7/MARL": "{0:1}"
  "https://gedcom.io/terms/v7/MARR": "{0:1}"
  "https://gedcom.io/terms/v7/MARS": "{0:1}"
  "https://gedcom.io/terms/v7/NATI": "{0:1}"
  "https://gedcom.io/terms/v7/NATU": "{0:1}"
  "https://gedcom.io/terms/v7/NMR": "{0:1}"
  "https://gedcom.io/terms/v7/OCCU": "{0:1}"
  "https://gedcom.io/terms/v7/ORDN": "{0:1}"
  "https://gedcom.io/terms/v7/PROB": "{0:1}"
  "https://gedcom.io/terms/v7/PROP": "{0:1}"
  "https://gedcom.io/terms/v7/RETI": "{0:1}"
  "https://gedcom.io/terms/v7/SSN": "{0:1}"
  "https://gedcom.io/terms/v7/WILL": "{0:1}"
  "https://gedcom.io/terms/v7/record-REPO": "{0:1}"
  "https://gedcom.io/terms/v7/record-SUBM": "{0:1}"

contact: "https://gedcom.io/community/"
...

```
