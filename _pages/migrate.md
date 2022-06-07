---
title: Migrating v5.5.1 to v7.0
permalink: /migrate/
toc: true
toc_label: "Issues on this Page"
toc_sticky: true
---
# How do I replace GEDCOM 5.5.1 tags that were removed in FamilySearch GEDCOM 7.0?

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

- `FONE`.`TYPE kana` = `TRAN`.`LANG ja-hrkt`

- `ROMN`.`TYPE pinyin` = `TRAN`.`LANG und-Latn-pinyin`
    
    Note: pinyin could be either `zh-Latn-pinyin` or `bo-Latn-pinyin`; thus, from 5.5.1 alone we can't deduce the language, only the script and variant, hence the `und` (undetermined) language above.

- `ROMN`.`TYPE romanji` = `TRAN`.`LANG ja-Latn`

- `ROMN`.`TYPE wadegiles` = `TRAN`.`LANG zh-Latn-wadegile`


## AFN, RFN, RIN

These have been replaced by `EXID`.
Thus this 5.5.1:

```
0 HEAD
1 SOUR MySystem
0 @5@ INDI
1 AFN 123456789
1 RIN 9876
1 RFN Resource:5431
```

becomes this 7.0:

```
0 @5@ INDI
1 EXID 123456789
2 TYPE https://gedcom.io/terms/v7/AFN
1 EXID 9876
2 TYPE https://gedcom.io/terms/v7/RIN#MySystem
1 EXID 5431
2 TYPE https://gedcom.io/terms/v7/RFN#Resource
```

See [EXID TYPE Base URIs](exid-type/index.md) for the table of currently registered base URIs
for `EXID`.`TYPE`.

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

GEDCOM 5.5.1 allowed the same tag in the same context to have different meaning depending on its payload type. This added significant implementation complexity and has been removed from v7.0.

Any NOTE_RECORD in 5.5.1 should be replaced with a [SHARED_NOTE_RECORD](https://gedcom.io/specifications/FamilySearchGEDCOMv7.html#SHARED_NOTE_RECORD) in 7.0.

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

GEDCOM 5.5.1 allowed the same tag in the same context to have different meaning depending on its payload type. This added significant implementation complexity as has been removed from v7.0.

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
2 FORM image/jpeg
2 TITL John Smith, February 4, 1896
```

Take care to convert the `TITL` tag correctly. In the GEDCOM 5.5.1 MULTIMEDIA_LINK structure, the `TITL` tag is a substructure of the `OBJE` tag, but in the [MULTIMEDIA_RECORD](https://gedcom.io/specifications/FamilySearchGEDCOMv7.html#MULTIMEDIA_RECORD) in both GEDCOM 5.5.1 and FamilySearch GEDCCOM 7.0, the `TITL` tag is a substructure of the `FILE` tag.

Similarly, the `FORM` tag must be converted correctly.  In the GEDCOM 5.5.1 MULTIMEDIA_FORMAT structure, the `FORM` tag is a set of enumerated values, but in FamilySearch GEDCOM 7.0, it must be a valid [media type](https://www.iana.org/assignments/media-types/media-types.xhtml).

## Non-pointer SOUR Substructures

GEDCOM 5.5.1 allowed the same tag in the same context to have different meaning depending on its payload type. This added significant implementation complexity and has been removed from v7.0.

This 5.5.1:

```
1 DEAT
2 DATE 1910
2 SOUR Letter from Alice Smith, 13 April 1946
3 TEXT My father passed away back in 1910.
```

becomes this 7.0:

```
1 DEAT
2 DATE 1910
2 SOUR @S1@

0 @S1@ SOUR
1 TITL Letter from Alice Smith, 13 April 1946
1 TEXT My father passed away back in 1910.
```

## Age Words

GEDCOM 5.5.1 defined three words for ages:

- `CHILD` was defined to mean `< 8y`
- `INFANT` was defined to mean `< 1y`
- `STILLBORN` was defined to mean "died just prior, at, or near birth, 0 years" (page 42) and "approximately 0 days old" (page 68); thus, it may mean either `0y` or `0d`.

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

The English word "stillborn" and its parallels in other languages are used to mean death at various ages depending on the culture of the person using the term. It may mean anywhere from "died in the womb" to "died within a few days of birth while still too young to perform a particular religious rite for infants." Note that the `STILLBORN` value of `SLGC`.`STAT` is [defined](https://www.churchofjesuschrist.org/study/ensign/1987/09/i-have-a-question/can-we-put-the-names-of-our-miscarried-or-stillborn-children-on-our-family-group-records?lang=eng) by The Church of Jesus Christ of Latter-day Saints for purposes of handling temple ordinances and remains in FamilySearch GEDCOM 7.

It is recommended that if `AGE STILLBORN` appears under any event in 5.5.1, then to maximize compatibility with various uses of stillbirth you should do all of the following when converting to 7.0:

1. Ensure there is a `DEAT` event with `AGE 0y` (unless a different `DEAT`.`AGE` was already present), and
2. Ensure there is a `BIRT` event with `TYPE Stillborn` (unless a different birth type was already present), and
3. Remove the original `AGE STILLBORN` line entirely, optionally adding a `NOTE Stillborn` to preserve the information that this event was tagged with that "age".

## Ordinance Status Values

Some GEDCOM 5.5.1 ordinance status values were renamed in Family Search GEDCOM 7.0:

- `DNS/CAN` was changed to `DNS_CAN`.
- `PRE-1970` was changed to `PRE_1970`.

# FAMC.STAT, NAME.TYPE, PEDI, RESN Values

The values in GEDCOM 5.5.1 appear in all lower case, but must be all upper case in Family Search GEDCOM 7.0.

Examples:

- `FAMC`.`STAT challenged` becomes `FAMC`.`STAT CHALLENGED`.
- `NAME`.`TYPE birth` becomes `NAME`.`TYPE BIRTH`.
- `PEDI birth` becomes `PEDI BIRTH`.
- `RESN confidential` becomes `RESN CONFIDENTIAL`.
