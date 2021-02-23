---
title: Migrating 5.5.1 to 7.0
permalink: /migrate/
toc: true
toc_label: "Issues on this Page"
toc_sticky: true
---
# GEDCOM 5.5.1 had an X tag, but 7.0 does not

## ROMN, FONE

These were replaced by the more versatile `TRAN`

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
    
    Note: pinyin could be either `zh-Latn-pinyin` or `bo-Latn-pinyin`; thus, from 5.5.1 alone we can't reduce the language, only the script and variant, hence the `und` (undetermined) language above.

- `ROMN`.`TYPE romanji` = `TRAN`.`LANG jp-Latn`

- `ROMN`.`TYPE wadegiles` = `TRAN`.`LANG zh-Latn-wadegile`


## AFN, RFN, RIN

These have been replaced by `EXID` and `REFN`.
Thus this 5.5.1

```
0 @5@ INDI
1 AFN 123456789
1 RIN 9876
1 RFN MySystem:5431
```

becomes this 7.0

```
0 @5@ INDI
1 EXID 123456789
2 TYPE https://www.familysearch.org/wiki/en/Ancestral_File
1 REFN 9876
2 TYPE RIN
1 EXID 5431
2 TYPE https://gedcom.io/RFN#MySystem
```

<!-- **FIX ME**: pick the right URIs for AFN and RFN -->

<!-- **Question**: Should AFN and RFN also be REFN because they identify records, not subjects? -->

## SUBN

These were defined to be specific to the Ancestral File or the TempleReady systems. As these systems are no longer in use, this record and its corresponding pointer has been removed. If other applications were using this record for some other purpose, they should switch to an extension to handle that purpose.

## RELA

This has been replaced by `ROLE`.
`ROLE` is an enumerated value where `RELA` was free text, so unless you know the correct mapping to the enumertion it is likely you'd convert as `OTHER`:

This 5.5.1

```
0 @6@ INDI
1 ASSO @7@
2 RELA Honorary uncle
```

becomes this 7.0

```
0 @6@ INDI
1 ASSO @7@
2 ROLE OTHER
3 PHRASE Honorary uncle
```


## NOTE_RECORD

5.5.1 allowed the same tag in the same context to have different meaning depending on its payload type. This added significant implementation complexity has been removed from 7.0.

Any NOTE_RECORD in 5.5.1 should be replaced with a NOTE_STRUCTURE in 7.0. Most systems we surveyed did not use pointers to the same NOTE_RECORD from multiple locations, but those that did should duplicate the NOTE_RECORD's payload and substructures in each NOTE_STRUCTURE in each of those locations.

This 5.5.1

```
0 @8@ NOTE From the Scottish surname Gordon, of uncertain origin
1 REFN Name origin Gordon
2 TYPE Name origins
1 SOUR Wikipedia "Gordon_(given_name)", retrieved JAN 2021
1 CHAN 5 JAN 2021
0 @9@ INDI
1 NAME Gordon //
2 NOTE @8@
```

becomes this 7.0

```
0 @9@ INDI
1 NAME Gordon //
2 NOTE From the Scottish surname Gordon, of uncertain origin
3 REFN Gordon
4 TYPE Name origins
3 SOUR @VOID@
4 PHRASE Wikipedia "Gordon_(given_name)", retrieved JAN 2021
1 CHAN 5 JAN 2020
```

<!-- Note that `REFN` and `CHAN` are not documented as substructures of the `NOTE_STRUCTURE` in 7.0, but are permitted there as extensions. -->

## non-pointer OBJE and SOUR substructures

5.5.1 allowed the same tag in the same context to have different meaning depending on its payload type. This added significant implementation complexity has been removed from 7.0.

Non-pointer OBJE substructures should be made into OBJE records and pointed to.

This 5.5.1

```
0 @10@ INDI
1 OBJE 
2 FILE face.jpg
3 FORM jpeg
4 MEDI photo
2 TITL studio portrait from 1880
```

becomes this 7.0

```
0 @10@ INDI
1 OBJE @11@
0 @11@ OBJE
1 FILE face.jpg
2 FORM jpeg
3 MEDI PHOTO
1 TITL studio portrait from 1880
```


Non-pointer SOUR substructures may be made into SOUR records, as outlined above, or into `@VOID@` pointer with one or more `PHRASE` containing the original payload.

This 5.5.1

```
1 SOUR Roadside marker near mile marker 12 of I 90 in Ohio
```

becomes this 7.0

```
1 SOUR @VOID@
2 PHRASE Roadside marker near mile marker 12 of I 90 in Ohio
```


## Age Words

GEDCOM 5.5.1 defined three words for ages:

- `CHILD` was defined to mean `< 8y`
- `INFANT` was defined to mean `< 1y`
- `STILLBORN` was defined to mean `0y` and also to imply the existence of a `DEAT` event

These have been removed from 7.0 in preference for their simpler and more expressive year-based forms.
A `PHRASE` may be used to clarify the age category of a person.

Thus 5.5.1's `2 AGE CHILD` should become 7.0's 

```
2 AGE < 8y
3 PHRASE Child
```

See also [How do I record a stillborn child?](#how-do-i-record-a-stillborn-child)

## Multi-file OBJE

GEDCOM 5.5.1 allowed multiple files in the same OBJE. The explanation given for this was

>  The file reference occurs one to many times so that multiple files
can be grouped together, each pertaining to the same context. For example, if you wanted to associate a sound clip and a photo, you would reference each multimedia file and indicate the format using the FORM tag subordinate to each file reference.

However, it was not defined how this grouping differed from having multiple `MULTIMEDIA_LINK` in a single structure.
Conversations with various GEDCOM producers and consumers suggested no consensus on the meaning of multi-FILE OBJE as opposed to multiple single-file OBJE, so support for multi-file OBJE was removed from 5.5.1.
Thus, this 5.5.1

```
0 @XYZ@ INDI
1 OBJE @O1@
0 @O1@ OBJE
1 FILE image.jpg
2 FORM jpg
1 FILE sound.wav
2 FORM wav
```

should be covered to this 7.0

```
0 @XYZ@ INDI
1 OBJE @O1_1@
1 OBJE @O1_2@
0 @O1_1@ OBJE
1 FILE image.jpg
2 FORM image/jpeg
0 @O1_2@ OBJE
1 FILE sound.wav
2 FORM audio/vnd.wave
```
