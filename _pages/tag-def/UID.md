---
title: UID
permalink: /terms/v7/UID.html
layout: none
redirect-from:
  - /terms/v7/UID
...

```

%YAML 1.2
---
type: structure

tag: UID

superstructures: [ADOP, ANUL, BAPM, BARM, BASM, BIRT, BLES, BURI, CAST, 
  CENS, CHR, CHRA, CONF, CREM, DEAT, DIV, DIVF, DSCR, EDUC, EMIG, ENGA, 
  EVEN, FACT, FAM, FCOM, GRAD, IDNO, IMMI, INDI, MARB, MARC, MARL, MARR, 
  MARS, NATI, NATU, NCHI, NMR, OBJE, OCCU, ORDN, PROB, PROP, RELI, REPO, 
  RESI, RETI, SNOTE, SOUR, SSN, SUBM, TITL, WILL]

substructures:

payload: Special

descriptions:
  - A type of IDENTIFIER_STRUCTURE
  - Tag abbreviated from "Unique Identifier"
  - |
    A globally-unique identifier of the superstructure, to be preserved
    across edits. If a globally-unique identifier for the record already
    exists, it should be used without modification, not even whitespace or
    letter case normalization. New globally unique identifiers should be
    created and formatted as described in RFC 4122.
    
    This is metadata about the structure itself, not data about its subject.
    Multiple structures describing different aspects of the same subject
    would have different UID values.
    
    Some systems used a 16-byte UUID with a custom 2-byte checksum for a
    total of 18 bytes:
    
    -   checksum byte 1 = (sum of (byte_(i)) for i 1 through 16) mod 256
    -   checksum byte 2 = (sum of ((16 − i) × (byte_(i))) for i 1
        through 16) mod 256
    
    Use of checksums for UIDs is discouraged except in cases where
    error-prone input is expected and an appropriate action to take in case
    of an error is known.
...

```