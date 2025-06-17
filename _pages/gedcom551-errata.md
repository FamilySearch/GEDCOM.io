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
|  6 | 13 | Modifications in Version 5.5.1 | data may not have been supplied in the transmission. (see \<\<FAMILY_RECORD\>\>, page 24.) | data may not have been supplied in the transmission (see \<\<FAM_RECORD\>\>, page 24). | FAMILY_RECORD should be FAM_RECORD |
|  7 |  4 | The following tags were added: | | **ADR3**     Address line 3. | Add ADR3 before EMAIL |
| 32 | 36 | FAMILY_EVENT_STRUCTURE | n RESI | n RESI     {1:1} | Add cardinality |
| 35 |  4 | EVEN | n **EVEN**     {1:1} | n **EVEN** [\<EVENT_DESCRIPTOR\> \| \<NULL\>]     {1:1} | Allow EVENT_DESCRIPTOR payload |
| 37 |  6 | MULTIMEDIA_LINK |            | [ | Add open bracket before first line of MULTIMEDIA_LINK |
| 37 |  8 | MULTIMEDIA_LINK | n **OBJE** | n **OBJE**     {1:1} | Add cardinality |
| 37 | 12 | MULTIMEDIA_LINK |            | ] | Add close bracket after last line of MULTIMEDIA_LINK |
| 37 | 36 | PERSONAL_NAME_PIECES | \<NAME_PIECE_SURNAME_PREFIX | \<NAME_PIECE_SURNAME_PREFIX\> | Add matching angle bracket |
| 54 |  4 | MULTIMEDIA_FORMAT | {Size=3:4} | {Size=3:3} | Maximum size is 3 since all values are size 3 |
| 56 | 15 | NAME_TYPE | {Size=5:30} | {Size=3:30} | Minimum size is 3 due to accommodate "aka" |
| 57 | 33 | PHONETIC_TYPE | {Size=5:30} | {Size=4:30} | Minimum size is 4 to accommodate "kana" |
| 58 |  2 | PHONETIC_TYPE | \<user define\> | \<user defined\> | Change "define" to "defined" |
| 58 | 21 | PLACE_LATITUDE | {Size=5:8} | {Size=5:10} | Maximum size is 10 to accommodate the example in line 25 |
| 58 | 32 | PLACE_LONGITUDE | {Size=5:8} | {Size=5:11} | Maximum size is 11 to accommodate the example in line 35 |
| 59 |  9 | PLACE_PHONETIC_VARIATION | the same form as&nbsp; was the place name | the same form as was the place name | Remove extra space before "was" |
| 59 | 11 | PLACE_PHONETIC_VARIATION | for example if hiragana was used to provide a reading of a a | for example if hiragana was used to provide a reading of a | Remove duplicate "a" |
| 60 | 19 | RESTRICTION_NOTICE | {Size=6:7} | {Size=6:12} | Maximum size is 12 to accommodate "confidential" |
| 61 |  9 | ROLE_IN_EVENT | {Size=1:15} | {Size=1:27} | Accommodate a ROLE_DESCRIPTOR of length 25 |
| 62 |  8 | SOURCE_DESCRIPTIVE_TITLE | For An _unpublished_ work such as: | For an _unpublished_ work such as: | Lower case "an" |
| 62 | 14 | SOURCE_FILED_BY_ENTRY | {Size= 1:60} | {Size=1:60} | Remove space |
| 62 | 22 | SOURCE_MEDIA_TYPE | {Size=1:15} | {Size=3:10) | All alternatives are within size range 3 to 10 |
| 84 |  7 | ANCE | Pertaining to forbearers of an individual. | Pertaining to forebearers of an individual. | Change "forbearers" to "forebearers" |
| 83 | 28 | Lineage-Linked GEDCOM Tag Definitions | | **ADR3 {ADDRESS3}:=** | Add ADR3 after ADR2 |
| 83 | 28 | Lineage-Linked GEDCOM Tag Definitions | | The third line of an address. | |
| 84 | 16 | BAPL | **BAPL {BAPTISM-LDS}:=** | **BAPL {BAPTISM_LDS}:=** | Change "-" to "_" |
| 87 | 12 | EMAI | **EMAI {EMAIL}:=** | **EMAIL {EMAIL}:=** | Change EMAI to EMAIL |
| 88 |  7 | FAX | **FAX {FACIMILIE}:=** | **FAX {FACSIMILE}:=** | Change FACIMILIE to FACSIMILE |
| 88 |  8 | FAX | Electronic facimilie transmission. | Electronic facsimile transmission. | Change facimilie to facsimile |
| 88 | 15 | FONE | **FONE {PHONETIC}** | **FONE {PHONETIC}:=** | Add ":=" |
| 88 | 16 | FONE | A phonetic variation of a superior text string | A phonetic variation of a superior text string. | Add period |
| 88 | 19 | GIVN | **GIVN {GIVEN_NAME}** | **GIVN {GIVEN_NAME}:=** | Add ":=" |
| 90 |  9 | NICK | A descriptive or familiar that is used | A descriptive or familiar name that is used | Insert "name" |
