---
title: Recommended Practices
permalink: /practices/
toc: true
toc_label: "Contents of this Page"
toc_sticky: true
---
# How do I list two places in an emigration?

Have paired immigration/emigration events:

```gedcom
1 EMIG
2 PLAC Nice, Nice, Alpes-Maritimes, Provence-Alpes-Côte d'Azur, France
3 FROM City, Arrondissement, Department, Provence, Country
2 DATE 3 MAR 1903
1 IMMI
2 PLAC Manhattan, New York,  New York, USA
3 FROM Borough, City, State, Country
2 DATE 8 MAR 1903
```

# How do I record a stillborn child?

Use a `PHRASE` under the `AGE` at death

```gedcom
1 DEAT
2 AGE 0d
3 PHRASE Stillborn
```

# How do I record a miscarriage?

Not all researchers wish to include miscarriages in their families, but some do. For those who do, we recommend a non-pointer `CHIL` if no details are known:

```gedcom
1 CHIL @VOID@
2 PHRASE Miscarried after 6 months
```

or an `INDI` with `NO BIRT` if there is more to say about the child:

```gedcom
0 @EX1@ INDI
1 NAME Roman /Hernandez/
1 NO BIRT
2 PHRASE Miscarried after 6 months
```

# Why can an attribute have an age?

Once case is when the attribute has a clear start time; for example, educational degrees tend to be awarded at a measurable time

```gedcom
1 EDUC Ph.D. in Computer Science
2 AGE 26y
```

Another case is when an attribute was expected to be temporary and observed at a particular time; for example, physical descriptions tend to be temporary

```gedcom
1 DESC Mostly bald with bushy mustachios
2 AGE 38y
```

When birth date and date range of attribute are both known, `DATE` is generally better than `AGE`, but sometimes sources contain claims like "I weighed 6 stone when I was 12" without clear dates, hence the provision of `AGE` for attributes.

# How do I record illegitimate children?

This is one of many relationship situations with many possible technical complications, the best solutions to which are being discussed for possible revision in subsequent versions of GECDOM.

At present, the best available tool is `INDI.FAMC.PEDI`, one for each family:

```gedcom
0 @I1@ INDI
1 FAMC @F1@
2 PEDI BIRTH
3 PHRASE Illegitimate child
1 FAMC @F2@
2 PEDI BIRTH
3 PHRASE Born into this family, but not the father's own
```

Because the nature of `BIRTH` is unclear (is it about the biological progenitors of the child or the social family unit into which it is born?) and a topic some researchers have strong feelings about, either or both of the above may be recorded `PEDI OTHER` instead of `PEDI BIRTH` by some researchers.

# How do I mark a parent-child relationship as confidential?

There is no standard way to do this. However, this is an excellent use of the simplest form of extension: using a standard tag (`RESN` in this case) in a non-standard location (`FAMC` and `CHIL` in this case).

```gedcom
0 @I2@ INDI
1 FAMC @F3@
2 RESN CONFIDENTIAL
0 @F3@ FAM
1 CHIL @I2@
2 RESN CONFIDENTIAL
```

Note that with all confidential communications, it is important not only to mark the data as confidential but also to ensure that the recipient of the data understands in what cases they are to remove the confidential data and agrees to do so. `RESN` communicates the confidential nature, but does not enforce the desired behavior.

# There are so many languages; how do I pick LANG payloads?

If you know the GEDCOM 5.5.1 language name, [FHISO has a look-up table](https://github.com/fhiso/legacy-format/blob/master/languages.tsv). You can also look at the lists embedded in the reference 5.5.1-to-7.0 converter program.

If you know the language you want, [r12a has a very flexible search function](https://r12a.github.io/app-subtags/).

You can also look through the [IANA registry](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry) manually and assemble the appropriate tags as outlined in [BCP 47](https://tools.ietf.org/html/bcp47), though that's something of an expert-mode approach.

# What does `SEX X` mean?

It is what is officially known as [intersex](https://en.wikipedia.org/wiki/Intersex), and is used in some countries on the birth records of children who do not obviously conform to the traditional biological definitions of male or female at birth.

The `SEX` structure is only for anatomical or biological sex at birth. For any related concept that might change and/or manifest later in life, an individual attribute should be used instead.

# How do I record polygamous families?

A `FAM` record should be used for each couple procreating or rearing offspring.
This may result in many `FAM` records for one social family unit.

A `FAM` record may also be used to represent the social family unit.
If it is desirable that all the spouses appear structurally equal, they may be linked using `ASSO` pointers with `ROLE SPOU` instead of `HUSB` and `WIFE` pointers.

It should be noted that some user interfaces may have more complete handling of `HUSB` and `WIFE` than they have for `ASSO`.

# How do I record a date without a year?

All dates in the `DateValue` datatype must have a year. Thus, you cannot use yearless dates as `DateValue`s.

However, you can add any date information as a `PHRASE`, as

If you could bound the year, you could add them as a PHRASE, as e.g.

```gedcom
2 DATE
3 PHRASE March 3rd (year unknown)
```

You might also consider bounding the year if possible, as e.g.

```gedcom
2 DATE BET 1820 AND 1840
3 PHRASE March 3rd (year unknown)
```

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

```gedcom
1 NAME /橘/ 逸勢
2 TRAN /Tachibana/ no Hayanari
3 LANG ja-Latn
2 TRAN /たちばな/ の はやなり
3 LANG ja-hrkt
```

If we have extra knowledge, we could be more precise, as e.g. knowing that the above phonetic system was actually hiragana, a subset of kana:

```gedcom
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

```gedcom
0 @5@ INDI
1 EXID 123456789
2 TYPE https://www.familysearch.org/wiki/en/Ancestral_File
1 REFN 9876
2 TYPE RIN
1 EXID 5431
2 TYPE https://gedcom.io/RFN#MySystem
```

> **FIX ME**: pick the right URIs for AFN and RFN

> **Question**: Should AFN and RFN also be REFN because they identify records, not subjects?

## SUBN

These were defined to be specific to the Ancestral File the TempleReady systems. As these system is no longer in use, this record and its corresponding pointer has been removed. If other applications were using this record for some other purpose, they should switch to an extension to handle that purpose.

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

```gedcom
0 @6@ INDI
1 ASSO @7@
2 ROLE OTHER
3 PHRASE Honorary uncle
```


## NOTE_RECORD

5.5.1 allowed the same tag in the same context to have different meaning depending on its payload type. This added significant implementation complexity as has been removed from 7.0.

Any NOTE_RECORD in 5.5.1 should be replaced with a NOTE_STRUTURE in 7.0. Most systems we surveyed did not use pointers to the same NOTE_RECORD from multiple locations, but those that did should duplicate the NOTE_RECORD's payload and substructures in each NOTE_STRUCTURE in each of those locations.

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

```gedcom
0 @9@ INDI
1 NAME Gordon //
2 NOTE From the Scottish surname Gordon, of uncertain origin
3 REFN Gordon
4 TYPE Name origins
3 SOUR @VOID@
4 PHRASE Wikipedia "Gordon_(given_name)", retrieved JAN 2021
1 CHAN 5 JAN 2020
```

Note that `REFN` and `CHAN` are not documented as substructures of the `NOTE_STRUCTURE` in 7.0, but are permitted there as extensions.

## non-pointer OBJE and SOUR substructures

5.5.1 allowed the same tag in the same context to have different meaning depending on its payload type. This added significant implementation complexity as has been removed from 7.0.

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

```gedcom
0 @10@ INDI
1 OBJE @11@
0 @11@ OBJE
1 FILE face.jpg
2 FORM jpeg
3 MEDI PHOTO
1 TITL studio portrait from 1880
```


Non-pointer SOUR substructures may be made into SOUR records, as outlined above, or into `@VOID@` pointer with `PHRASE`s containing the original payload.

This 5.5.1

```
1 SOUR Roadside marker near mile marker 12 of I 90 in Ohio
```

becomes this 7.0

```gedcom
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

```gedcom
2 AGE < 8y
3 PHRASE Child
```

See also [How do I record a stillborn child?](#how-do-i-record-a-stillborn-child)

## Multi-file OBJE

GEDCOM 5.5.1 allowed multiple files in the same OBJE. The explanation given for this was

>  The file reference occurs one to many times so that multiple files
can be grouped together, each pertaining to the same context. For example, if you wanted to associate a sound clip and a photo, you would reference each multimedia file and indicate the format using the FORM tag subordinate to each file reference.

However, it was not defined how this grouping differed from having multiple `MULTIMEDIA_LINK`s in a single structure.
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

```gedcom
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

# How do I link to individual structures in my GEDCOM?

Inside a GEDCOM file, pointers do this using the cross-reference identifiers. However, cross-reference identifiers are *not* durable across import-export cycles and should not be used outside of a GEDCOM file.

If you wish to reference a part of a GEDCOM file from outside that file, you should use one of the durable identifier structures: `UID`, `REFN`, or `EXID`. There is currently no standard way to do this, so any implementation will need to decide how the links will be navigated. The following show a few examples, using all three kinds of identifiers in three different external files.

```gedcom
0 @I23@ INDI
1 NAME Arthur /Pendragon/
1 REFN King Arthur
2 TYPE English Royalty
1 EXID K1
2 TYPE https://example.com/MyIds
1 UID 4bd2c474-ec84-43cb-86ef-b51ab09c2ed2
```

```html
<span gedlink="somefile.ged?UID=4bd2c474-ec84-43cb-86ef-b51ab09c2ed2">King Author</span>
```

```xml
<Person>
  <InGed>
    <File>somefile.ged</File>
    <EXID type="https://example.com/MyIds">K1</EXID>
  </InGed>
  <Name>Arthur Pendragon</Name>
</Person>
```

```json
{
    "name": "Arthur",
    "gedcom":[
        {
            "file": "somefile.ged",
            "REFN": "King Arthur",
            "TYPE": "English Royalty"
        }
    ]
}
```
