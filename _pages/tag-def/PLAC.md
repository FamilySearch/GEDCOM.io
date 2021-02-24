---
title: PLAC
permalink: /terms/v7/PLAC.html
layout: none
redirect-from:
  - /terms/v7/PLAC
...

```

%YAML 1.2
---
type: structure

tag: PLAC

superstructures: [ADOP, ANUL, BAPL, BAPM, BARM, BASM, BIRT, BLES, BURI, 
  CAST, CENS, CHR, CHRA, CONF, CONL, CREM, DEAT, DIV, DIVF, DSCR, EDUC, 
  EMIG, ENDL, ENGA, EVEN, FACT, FCOM, GRAD, IDNO, IMMI, INIT, MARB, MARC, 
  MARL, MARR, MARS, NATI, NATU, NCHI, NMR, OCCU, ORDN, PROB, PROP, RELI, 
  RESI, RETI, SLGC, SLGS, SSN, TITL, WILL]

substructures:
  EXID: "{0:M}"
  LANG: "{0:1}"
  MAP: "{0:1}"
  NOTE: "{0:M}"
  PLAC.FORM: "{0:1}"
  PLAC.TRAN: "{0:M}"
  SNOTE: "{0:M}"

payload: List:Text

descriptions:
  - Tag abbreviated from "Place"
  - also called PLACE_STRUCTURE
  - The principle place in which the superstructure's subject occurred.
  - |
    A place, which may be represented in several ways:
    
    -   The payload contains a comma-separated list of region names, ordered
        from smallest to largest. The specific meaning of each element is
        given by the FORM substructure, or in the HEAD.PLAC.FORM if there is
        no FORM substructure. Elements should be left blank if they are
        unknown, do not apply to the location, or are too specific for the
        region in question.
    
        A record describing births throughout Oneida county could be
        recorded as
    
            0 @S1@ SOUR
            1 DATA
            2 EVEN BIRT
            3 PLAC , Oneida, Idaho, USA
            4 FORM City, County, State, Country
    
    -   The payload may be translated or transliterated into different
        languages or scripts using the TRAN substructure. It should use the
        same FORM as the payload.
    
    -   Global coordinates may be presented in the MAP substructure
    
    GEDCOM currently does not support places where a region name contains a
    comma. An alternative system for representing locations is likely to be
    added in a later version of GEDCOM.
...

```