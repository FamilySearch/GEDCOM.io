---
title: SOUR
permalink: /terms/v7/SOUR.html
layout: none
redirect-from:
  - /terms/v7/SOUR
...

```

%YAML 1.2
---
type: structure

tag: SOUR

superstructures: [ADOP, ANUL, ASSO, BAPL, BAPM, BARM, BASM, BIRT, BLES, 
  BURI, CAST, CENS, CHR, CHRA, CONF, CONL, CREM, DEAT, DIV, DIVF, DSCR, 
  EDUC, EMIG, ENDL, ENGA, EVEN, FACT, FAM, FCOM, GRAD, IDNO, IMMI, INDI, 
  INIT, MARB, MARC, MARL, MARR, MARS, NAME, NATI, NATU, NCHI, NMR, NO, 
  NOTE, OBJE, OCCU, ORDN, PROB, PROP, RELI, RESI, RETI, SLGC, SLGS, SNOTE, 
  SSN, TITL, WILL]

substructures:
  COMM: "{0:M}"
  OBJE: "{0:M}"
  PAGE: "{0:1}"
  QUAY: "{0:1}"
  SNOTE: "{0:M}"
  SOUR.DATA: "{0:1}"
  SOUR.EVEN: "{0:1}"

payload: xref:SOUR

descriptions:
  - Tag abbreviated from "Source"
  - also called SOURCE_CITATION
  - A description of an entire source (if a record) or the relevant part
    thereof to support the containing data (if a substructure). See
    SOURCE_RECORD and SOURCE_CITATION for more.
  - |
    A citation indicating that the pointed-to source record supports the
    claims made in the superstructure. Substructures provide additional
    information about how that source applies to the subject of the
    citation's superstructure:
    
    -   PAGE: where in the source the relevant material can be found.
    -   DATA: the relevant data from the source.
    -   EVEN: what event the relevant material was recording.
    -   QUAY: an estimation of the reliability of the source in regard to
        these claims.
    -   MULTIMEDIA_LINK: digital copies of the cited part of the source
    
    When no source record is available, a voidPtr and accompanying COMM can
    used to describe the source.
    
        1 DSCR Tall enough his head touched the ceiling
        2 SOUR @VOID@
        3 COMM His grand-daughter Lydia told me this in 1980
...

```