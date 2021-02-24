---
title: FAM
permalink: /terms/v7/FAM.html
layout: none
redirect-from:
  - /terms/v7/FAM
...

```

%YAML 1.2
---
type: structure

tag: FAM

superstructures: [RECORD]

substructures:
  ANUL: "{0:M}"
  ASSO: "{0:M}"
  CHAN: "{0:1}"
  CHIL: "{0:M}"
  CREA: "{0:1}"
  DIV: "{0:M}"
  DIVF: "{0:M}"
  ENGA: "{0:M}"
  EXID: "{0:M}"
  FAM.CENS: "{0:M}"
  FAM.EVEN: "{0:M}"
  FAM.FACT: "{0:M}"
  FAM.HUSB: "{0:1}"
  FAM.NCHI: "{0:M}"
  FAM.RESI: "{0:M}"
  FAM.WIFE: "{0:1}"
  MARB: "{0:M}"
  MARC: "{0:M}"
  MARL: "{0:M}"
  MARR: "{0:M}"
  MARS: "{0:M}"
  NO: "{0:M}"
  NOTE: "{0:M}"
  OBJE: "{0:M}"
  REFN: "{0:M}"
  RESN: "{0:1}"
  SLGS: "{0:M}"
  SNOTE: "{0:M}"
  SOUR: "{0:M}"
  SUBM: "{0:M}"
  UID: "{0:M}"

payload: None

descriptions:
  - also called FAMILY_RECORD
  - |
    The FAM record was originally structured to represent families where a
    male HUSB (husband or father) and female WIFE (wife or mother) produce
    CHIL (children). The FAM record may also be used for cultural parallels
    to this, including nuclear families, marriage, cohabitation, fostering,
    adoption, and so on, regardless of the gender of the partners. Sex,
    gender, titles, and roles of partners should not be inferred based on
    partner the HUSB or WIFE structure points to.
    
    The individuals pointed to by the HUSB and WIFE are collectively
    referred to as "partners", "parents" or "spouses".
    
    Some displays may be unable to display more than two partners. Displays
    may use HUSB and WIFE as layout hints, for example, by consistently
    displaying the HUSB on the same side of the WIFE in a tree view. It is
    recommended that family structures with more than two partners either
    use several FAM records or use <<ASSOCIATION_STRUCTURE>>s to indicate
    additional partners.
    
    The FAM record will be revised in a future version of GEDCOM to fully
    express the diversity of human family relationships.
    
    The preferred order of the CHIL (children) pointers within a FAM
    (family) structure is chronological by birth. A CHIL with a voidPtr
    indicates a placeholder for an unknown child in this birth order.
    
    If a FAM record uses HUSB or WIFE to point to an INDI record, the INDI
    record must use FAMS to point to the FAM record. If a FAM record uses
    CHIL to point to an INDI record, the INDI record must use a FAMC to
    point to the FAM record.
...

```