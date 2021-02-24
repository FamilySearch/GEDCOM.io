---
title: Migrating 5.5.1 to 7.0
permalink: /migrate/
toc: true
toc_label: "Issues on this Page"
toc_sticky: true
---
# How do I replace GEDCOM 5.5.1 tags that were removed in GEDCOM 7.0?

## ROMN, FONE

These were replaced by the more versatile `TRAN`.

Thus, this 5.5.1:

```
1 NAME /橘/ 逸勢
2 ROMN /Tachibana/ no Hayanari
3 TYPE romanji
2 FONE /たちばな/ の はやなり
3 TYPE kana
```

becomes this 7.0:

```
1 NAME /橘/ 逸勢
2 TRAN /Tachibana/ no Hayanari
3 LANG ja-Latn
2 TRAN /たちばな/ の はやなり
3 LANG ja-hrkt
```

If we have extra knowledge, we could be more precise, as e.g. knowing that the above phonetic system was actually hiragana, a subset of kana:

```
2 TRAN /たちばな/ の はやなり
3 LANG ja-hira
```

The full mapping of 5.5.1 types is is

- `FONE`.`TYPE hangul` = `TRAN`.`LANG ko-hang`

- `FONE`.`TYPE kana` = `TRAN`.`LANG jp-hrkt`

- `ROMN`.`TYPE pinyin` = `TRAN`.`LANG und-Latn-pinyin`
    
    Note: pinyin could be either `zh-Latn-pinyin` or `bo-Latn-pinyin`; thus, from 5.5.1 alone we can't deduce the language, only the script and variant, hence the `und` (undetermined) language above.

- `ROMN`.`TYPE romanji` = `TRAN`.`LANG jp-Latn`

- `ROMN`.`TYPE wadegiles` = `TRAN`.`LANG zh-Latn-wadegile`


## AFN, RFN, RIN

These have been replaced by `EXID` and `REFN`.
Thus this 5.5.1:

```
0 @5@ INDI
1 AFN 123456789
1 RIN 9876
1 RFN MySystem:5431
```

becomes this 7.0:

```
0 @5@ INDI
1 EXID 123456789
2 TYPE https://www.familysearch.org/wiki/en/Ancestral_File
1 REFN 9876
2 TYPE RIN
1 EXID 5431
2 TYPE https://gedcom.io/RFN#MySystem
```

> **FIX ME**: pick the right URIs for AFN and RFN

## SUBN

These were defined to be specific to the Ancestral File and TempleReady systems. As these systems are no longer in use, this record and its corresponding pointer have been removed. If other applications were using this record for some other purpose, they should switch to an extension to handle that purpose.

## RELA

This has been replaced by `ROLE`.
`ROLE` is an enumerated value where `RELA` was free text.

If the 5.5.1 `RELA` value maps to one of the 7.0 `ROLE` enumerations, use the `ROLE` enumeration.

This 5.5.1:

```
0 @I1@ INDI
1 ASSO @I2@
2 RELA Witness
```

becomes this 7.0:

```
0 @I1@ INDI
1 ASSO @I2@
2 ROLE WITN
```

If the 5.5.1 `RELA` value is not equivalent to one of the 7.0 `ROLE` enumerations, use the `OTHER` enumeration with a `PHRASE` subrecord.

This 5.5.1:

```
0 @I1@ INDI
1 ASSO @I2@
2 RELA Honorary uncle
```

becomes this 7.0:

```
0 @I1@ INDI
1 ASSO @I2@
2 ROLE OTHER
3 PHRASE Honorary uncle
```

## NOTE_RECORD

GEDCOM 5.5.1 allowed the same tag in the same context to have different meaning depending on its payload type. This added significant implementation complexity and has been removed from GEDCOM 7.0.

Any NOTE_RECORD in 5.5.1 should be replaced with a [SHARED_NOTE_RECORD](https://gedcom.io/specifications/GEDCOM7rc.html#SHARED_NOTE_RECORD) in 7.0.

This 5.5.1:

```
0 @I8@ INDI
1 NAME Gordon //
2 NOTE @N1@
0 @N1@ NOTE From the Scottish surname Gordon, of uncertain origin
1 SOUR Wikipedia "Gordon_(given_name)", retrieved JAN 2021
1 CHAN 5 JAN 2021
```

becomes this 7.0:

```
0 @I8@ INDI
1 NAME Gordon //
2 SNOTE @N1@
0 @N1@ SNOTE From the Scottish surname Gordon, of uncertain origin
1 SOUR Wikipedia "Gordon_(given_name)", retrieved JAN 2021
1 CHAN 5 JAN 2021
```

## Non-pointer OBJE Substructures

GEDCOM 5.5.1 allowed the same tag in the same context to have different meaning depending on its payload type. This added significant implementation complexity as has been removed from GEDCOM 7.0.

A non-pointer `OBJE` substructure should be converted to an `OBJE` pointer with an associated `OBJE` record.

This 5.5.1:

```
0 @I1@ INDI
1 NAME John /Smith/
1 OBJE
2 FILE d:\Media\1896-02-04-John-Smith.jpg
3 FORM jpg
2 TITL John Smith, February 4, 1896
```

becomes this 7.0:

```
0 @I1@ INDI
1 NAME John /Smith/
1 OBJE @O1@

0 @O1@
1 FILE file:///d//Media/1896-02-04-John-Smith.jpg
2 FORM jpg
2 TITL John Smith, February 4, 1896
```

Take care to convert the `TITL` tag correctly. In the GEDCOM 5.5.1 MULTIMEDIA_LINK structure, the `TITL` tag is a substructure of the `OBJE` tag, but in the [MULTIMEDIA_RECORD](https://gedcom.io/specifications/GEDCOM7rc.html#MULTIMEDIA_RECORD) in both GEDCOM 5.5.1 and GEDCCOM 7.0, the `TITL` tag is a substructure of the `FILE` tag.

## Non-pointer SOUR Substructures

GEDCOM 5.5.1 allowed the same tag in the same context to have different meaning depending on its payload type. This added significant implementation complexity as has been removed from GEDCOM 7.0.

This 5.5.1:

```
1 DEAT
2 DATE 1910
2 SOUR Letter from Alice Smith, 13 April 1946
3 PAGE According to his grand-daughter, who was present.
```

becomes this 7.0:

```
1 DEAT
2 DATE 1910
2 SOUR @S1@
3 PAGE According to his grand-daughter, who was present.

0 @S1@ SOUR
1 TITL Letter from Alice Smith, 13 April 1946
```

## Age Words

GEDCOM 5.5.1 defined three words for ages:

- `CHILD` was defined to mean `< 8y`
- `INFANT` was defined to mean `< 1y`
- `STILLBORN` was defined to mean `0y` and also to imply the existence of a `DEAT` event

These have been removed from 7.0 in preference for their simpler and more expressive year-based forms.
A `PHRASE` may be used to clarify the age category of a person.

This 5.5.1:

```
2 AGE CHILD
```

becomes this 7.0:

```
2 AGE < 8y
3 PHRASE Child
```

See also [How do I record a stillborn child?](#how-do-i-record-a-stillborn-child)