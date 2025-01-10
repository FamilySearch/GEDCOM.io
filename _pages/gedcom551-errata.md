---
title: GEDCOM 5.5.1 Errata
permalink: /gedcom551-errata/
sidebar:
  nav: "errata"
---
# GEDCOM 5.5.1 Errata

The following is the current list of errata for [the GEDCOM Standard, Release 5.5.1, published 15 November 2019](https://gedcom.io/specifications/ged551.pdf).

|Page|Line|Heading| Original Text | Corrected Text | Notes |
|----|----|-------|---------------|----------------|-------|
|  6 | 13 | Modifications in Version 5.5.1 | data may not have been supplied in the transmission. (see <<FAMILY_RECORD>>, page 24.) | data may not have been supplied in the transmission (see <<FAM_RECORD>>, page 24). | FAMILY_RECORD should be FAM_RECORD |
| 32 | 36 | FAMILY_EVENT_STRUCTURE | n RESI | n RESI     {1:1} | Add cardinality |
| 37 |  6 | MULTIMEDIA_LINK |            | [ | Add open bracket before first line of MULTIMEDIA_LINK |
| 37 | 12 | MULTIMEDIA_LINK |            | ] | Add close bracket after last line of MULTIMEDIA_LINK |
| 37 |  8 | MULTIMEDIA_LINK | n **OBJE** | n **OBJE**     {1:1} | Add cardinality |
| 59 |  9 | PLACE_PHONETIC_VARIATION | the same form as \ was the place name | the same form as was the place name | Remove extra space before "was" |
| 59 | 11 | PLACE_PHONETIC_VARIATION | for example if hiragana was used to provide a reading of a a | for example if hiragana was used to provide a reading of a | Remove duplicate "a" |
| 62 |  8 | SOURCE_DESCRIPTIVE_TITLE | For An _unpublished_ work such as: | For an _unpublished_ work such as: | Lower case "an" |
| 62 | 14 | SOURCE_FILED_BY_ENTRY |  {Size= 1:60} | {Size=1:60} | Remove space |
| 84 |  7 | ANCE | Pertaining to forbearers of an individual. | Pertaining to forebearers of an individual. | Change "forbearers" to "forebearers" |
| 84 | 16 | BAPL | **BAPL {BAPTISM-LDS}:=** | **BAPL {BAPTISM_LDS}:=** | Change "-" to "_" |
| 87 | 12 | EMAI | **EMAI {EMAIL}:=** | **EMAIL{EMAIL}:=** | Change EMAI to EMAIL |
| 88 |  7 | FAX | **FAX {FACIMILIE}:=** | **FAX {FACSIMILE}:=** | Change FACIMILIE to FACSIMILE |
| 88 |  8 | FAX | Electronic facimilie transmission. | Electronic facsimile transmission. | Change facimilie to facsimile |
| 88 | 15 | FONE | **FONE {PHONETIC}** | **FONE {PHONETIC}:=** | Add ":=" |
| 88 | 16 | FONE | A phonetic variation of a superior text string | A phonetic variation of a superior text string. | Add period |
| 88 | 19 | GIVN | **GIVN {GIVEN_NAME}** | **GIVN {GIVEN_NAME}:=** | Add ":=" |
| 90 |  9 | NICK | A descriptive or familiar that is used | A descriptive or familiar name that is used | Insert "name" |
