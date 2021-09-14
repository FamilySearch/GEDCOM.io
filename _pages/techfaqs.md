---
title: Technical FAQs
permalink: /techfaqs/
toc: true
toc_label: "Questions on this Page"
toc_sticky: true
---
# How do I list two places in an emigration?

Use paired immigration/emigration events:

```
1 EMIG
2 PLAC Nice, Nice, Alpes-Maritimes, Provence-Alpes-Côte d'Azur, France
3 FORM City, Arrondissement, Department, Provence, Country
2 DATE 3 MAR 1903
1 IMMI
2 PLAC Manhattan, New York,  New York, USA
3 FORM Borough, City, State, Country
2 DATE 8 MAR 1903
```

# How do I record a stillborn child?

Use a `PHRASE` under the `AGE` at death:

```
1 DEAT
2 AGE 0d
3 PHRASE Stillborn
```

Note that the `PHRASE` must be in the default language (if any) specified in
the `<<HEADER>>`.

# How do I record a miscarriage?

For researchers who want to include a miscarriage as a child in a family, we recommend a non-pointer `CHIL` if no details are known:

```
1 CHIL @VOID@
2 PHRASE Miscarried after 6 months
```

If there is more to say about the child, we recommend an `INDI` with `NO BIRT`:

```
0 @EX1@ INDI
1 NAME Roman /Hernandez/
1 NO BIRT
2 PHRASE Miscarried after 6 months
```

For researchers who want to record a miscarriage, but do not want to include the child in a family, we recommend a family event:

```
0 @F1@ FAM
1 WIFE @I1@
1 HUSB @I2@
1 EVEN
2 TYPE Miscarriage
2 DATE 13 JUN 1948
```

# Why can an attribute have an age?

One case is when the attribute has a clear start time; for example, educational degrees tend to be awarded at a measurable time:

```
1 EDUC Ph.D. in Computer Science
2 AGE 26y
```

Another case is when an attribute was expected to be temporary and observed at a particular time; for example, physical descriptions tend to be temporary:

```
1 DESC Mostly bald with bushy mustachios
2 AGE 38y
```

When birth date and date range of attribute are both known, `DATE` is generally better than `AGE`, but sometimes sources contain claims like "I earned my degree when I was 15" without clear dates, hence the provision of `AGE` for attributes.

# How do I record illegitimate children?

This is one of many relationship situations with many possible technical complications, the best solutions to which are being discussed for possible revision in subsequent versions of FamilySearch GECDOM.

At present, the best available tool is `INDI.FAMC.PEDI`, one for each family:

```
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

The standard `RESN` tag is used to mark data confidential but it is not a substructure under the `FAM.FAMC` or `FAM.CHIL` tags. You can implement a custom extension tag, perhaps `_RESN`, and add a `SCHMA` entry to indicate the extension has the same meaning as `RESN`:

```
0 HEAD
1 SCHMA
2 TAG _RESN https://gedcom.io/terms/v7/RESN
0 @I2@ INDI
1 FAMC @F3@
2 _RESN CONFIDENTIAL
0 @F3@ FAM
1 CHIL @I2@
2 _RESN CONFIDENTIAL
```

Note that with all confidential communications, it is important not only to mark the data as confidential but also to ensure that the recipient of the data understands in what cases they are to remove the confidential data and agrees to do so. `_RESN` communicates the confidential nature, but does not enforce the desired behavior.

# How do I choose LANG payloads?

If you know the GEDCOM 5.5.1 language name, [FHISO has a look-up table](https://github.com/fhiso/legacy-format/blob/master/languages.tsv). You can also look at the lists embedded in the reference 5.5.1-to-7.0 converter program.

If you know the language you want, [r12a has a very flexible search function](https://r12a.github.io/app-subtags/).

You can also look through the [IANA registry](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry) manually and assemble the appropriate tags as outlined in [BCP 47](https://tools.ietf.org/html/bcp47), though that's something of an expert-mode approach.

# How do I record the sex of an intersex person?

The enumerated value on the `SEX` tag in GEDCOM 7.0 was amended to include "X" to describe [intersex](https://en.wikipedia.org/wiki/Intersex) individuals:

```
0 @I1@ INDI
1 SEX X
```

Birth records in some jurisdictions use intersex as the sex value for a child who does not conform to the traditional biological definitions of male or female at birth.

The `SEX` tag is only for anatomical or biological sex at birth. For any related concept that might change and/or manifest later in life, an individual attribute should be used instead.

# How do I record polygamous families?

A `FAM` record should be used for each couple procreating or rearing offspring.
This may result in many `FAM` records for one social family unit.

A `FAM` record may also be used to represent the social family unit.
If it is desirable that all the spouses appear structurally equal, they may be linked using `ASSO` pointers with `ROLE SPOU` instead of `HUSB` and `WIFE` pointers.

Some applications may have more complete handling of `HUSB` and `WIFE` than they have for `ASSO`.

# How do I record a date without a year?

All dates in the `DateValue` datatype must have a year. Thus, you cannot use yearless dates as `DateValue`s.

However, you can add any date information as a `PHRASE`:

```
2 DATE
3 PHRASE March 3rd (year unknown)
```

You might also consider bounding the year if possible:

```
2 DATE BET 1820 AND 1840
3 PHRASE March 3rd (year unknown)
```

# How do I link to individual structures within a FamilySearch GEDCOM file?

Inside a GEDCOM file, pointers do this using the cross-reference identifiers. However, cross-reference identifiers are *not* durable across import-export cycles and should not be used outside of a GEDCOM file.

If you wish to reference a part of a FamilySearch GEDCOM file from outside that file, you should use one of the durable identifier structures: `UID`, `REFN`, or `EXID`. There is currently no standard way to do this, so any implementation will need to decide how the links will be navigated. The following show a few examples, using all three kinds of identifiers in three different external files:

```
0 @I23@ INDI
1 NAME Arthur /Pendragon/
1 REFN King Arthur
2 TYPE English Royalty
1 EXID K1
2 TYPE https://example.com/MyIds
1 UID 4bd2c474-ec84-43cb-86ef-b51ab09c2ed2
```

HTML
```
<span gedlink="somefile.ged?UID=4bd2c474-ec84-43cb-86ef-b51ab09c2ed2">King Author</span>
```

XML
```
<Person>
  <InGed>
    <File>somefile.ged</File>
    <EXID type="https://example.com/MyIds">K1</EXID>
  </InGed>
  <Name>Arthur Pendragon</Name>
</Person>
```

JSON
```
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

# How do I flag a primary or profile photo?

Make it the first [MULTIMEDIA_LINK](https://gedcom.io/specifications/GEDCOM7rc.html#MULTIMEDIA_LINK).
As noted in the specification,

> Unless otherwise specified, the first is the most-preferred value.
> For example, the display name would be the first name structure,
> the profile image the first image structure.

The only "otherwise specified" in the current draft is for `FAM`.`CHIL`, where the specification says

> The preferred order of the `CHIL` (children) pointers within a `FAM` (family) structure is chronological by birth.

# How do I record nick names?

Use the `NICK` part type under the [PERSONAL_NAME_STRUCTURE](https://gedcom.io/specifications/GEDCOM7rc.html#PERSONAL_NAME_STRUCTURE):

```
1 NAME Bill /Miller/
2 NICK Bill
2 SURN Miller
```

When recording a name with an embedded nick name, such as "William 'Bill' Miller", use two `NAME` records:

```
1 NAME William /Miller/
2 GIVN William
2 SURN Miller
1 NAME Bill /Miller/
2 TYPE AKA
2 NICK Bill
2 SURN Miller
```

For systems that are limited to a single personal name, there is no satisfactory solution. Such systems may export names with an embedded nick name:

```
1 NAME William "Bill" /Miller/
2 GIVN William
2 NICK Bill
2 SURN Miller
```
