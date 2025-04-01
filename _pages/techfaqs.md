---
title: Technical FAQs
permalink: /techfaqs/
toc: true
toc_label: "Questions on this Page"
toc_sticky: true
---
# Names

## How do I record nicknames?

Use the `NICK` part type under the [PERSONAL_NAME_STRUCTURE](https://gedcom.io/specifications/FamilySearchGEDCOMv7.html#PERSONAL_NAME_STRUCTURE):

```
1 NAME Bill /Miller/
2 NICK Bill
2 SURN Miller
```

The name type `AKA` can also be used to indicate that a `NAME` structure is not the primary name.

```
1 NAME William /Miller/
2 GIVN William
2 SURN Miller
1 NAME Bill /Miller/
2 TYPE AKA
2 NICK Bill
2 SURN Miller
```

It is also possible to presented the nickname inline with the other name parts:

```
1 NAME William "Bill" /Miller/
2 GIVN William
2 NICK Bill
2 SURN Miller
```

## How do I record a preferred name among given names?

In many customs a person is given a series of given names, where one of them (often not the first one)
is the name the individual will commonly be known by.

For example, the Wikipedia entry for [German name](https://en.wikipedia.org/wiki/German_name) explains:

> It is common to give a child several given names, one of them intended for everyday use and known as
> the "Rufname" ("appellation name" or "call name").  This _Rufname_ is often underlined on official documents,
> as it is sometimes the second or third name in the sequence of given names on official record,
> even though it is the given name in daily use from childhood.

FamilySearch GEDCOM 7.0 and earlier GEDCOM versions including 5.5.1 do not explicitly define a standard way
to denote this concept, and so a variety of mechanisms have been used by implementations over time.  For example,
for the name "Amalie <u>Emmy</u> Noether", some implementations might use an extension tag such as `_RUFNAME`:

```
1 NAME Amalie Emmy /Noether/
2 GIVN Amalie Emmy
2 _RUFNAME Emmy
2 SURN Noether
```

Such extensions can, however, result in loss of data since they are not standardized and so can be dropped
by other implementations.  A more interoperable form using only standard tags is:

```
1 NAME Emmy /Noether/
2 GIVN Emmy
2 SURN Noether
1 NAME Amalie Emmy /Noether/
2 TYPE birth
2 GIVN Amalie Emmy
2 SURN Noether
```

The above example denotes that the second form is the actual birth name, but the first form was also used by
the person.  Although the specification does not define any semantics to the order among NAME structures,
some implementations are known to infer that the first NAME occuring is a "preferred" one to use
for display.

# Dates and Ages

## How do I record a date without a year?

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

## How do I record the calendar that an age applies to?

When a person has events recorded in the contexts of multiple calendars within their lifetime, such
as `JULIAN` and `GREGORIAN`, or `FRENCH_R` and `GREGORIAN`, their age may have been be calculated
(and recorded) differently depending on the calendar. 

Dates in GEDCOM can have a calendar in the payload, but ages cannot, leading to the question of how
gedcom can store the calendar associated with an age.

One intent of the `AGE` structure is to express the age as it was listed in some source document.
When a `DATE` and an `AGE` are associated with the *same* event, applications reading the GEDCOM file
can infer that the calendar of the `AGE` is the same as the calendar of the `DATE`, especially if
a `SOURCE_CITATION` is provided for the event.

If a source document listed an age without a date, but a user or application has a way to calculate
an estimated date based on the age and calendar used by the source document, then the calendar can
be stored with a calculated date:

```
0 @I1@ INDI
1 BIRT
2 DATE JULIAN 1 SEP 1752
1 CHR
2 DATE CAL GREGORIAN 14 OCT 1752
2 AGE 1m 2d
1 DEAT
2 DATE GREGORIAN 1 NOV 1752
```

In the following example, it is important to record the calendar associated with the age
since the actual date would vary:

```
0 @I2 INDI
1 NOTE The following two birthdates refer to the same day, in different calendars.
1 BIRT
2 DATE FRENCH_R 1 VEND 2
1 BIRT
2 DATE GREGORIAN 23 SEP 1793
1 NOTE If christening was recorded as "1m 10d", the date is different per calendar.
2 CONT "1m 10d" in Gregorian would be GREGORIAN 2 NOV 1793 or FRENCH_R 12 BRUM 2.
2 CONT "1m 10d" in French Republican would be GREGORIAN 1 NOV 1793 or FRENCH_R 11 BRUM 2.
1 CHR
2 DATE CAL FRENCH_R 11 BRUM 2
2 AGE 1m 10d
```

## Why can an attribute have an age?

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

## How do I record the age of an associated individual?

Roles of associated individuals such as witnesses can be provided with the `ASSO` structure,
which does not permit `AGE` as a substructure.  The most interoperable option, which
maximizes the chance that other applications will display and preserve the age, is to use
a `NOTE` structure:

```
2 ASSO @I2@
3 ROLE WITN
3 NOTE 29 years old
```

The `NOTE` structure does not provide a way for an application to reliably
detect the value as an age.  In the unlikely event that an application
needs such an ability, a relocated standard structure can be used.

```
0 HEAD
1 SCHMA
2 TAG _AGE http://gedcom.io/terms/v7/AGE
0 @I1@ INDI
1 BIRT
2 ASSO @I2@
3 ROLE WITN
3 _AGE 29y
```

# Children

## How do I record a stillborn child?

Use a `PHRASE` under the `AGE` at death:

```
1 DEAT
2 AGE 0d
3 PHRASE Stillborn
```

## How do I record a miscarriage?

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

## How do I record illegitimate children?

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

## How do I provide a source citation for a parent-child relationship?

Neither the `FAMC` structure of an individual record nor the `CHIL` structure of a family record supports
having a `SOUR` citation as a substructure.  Today applications often put the `SOUR` directly under the
individual record or the family record, where it lacks specificity in terms of which family or individual
it applies to.

If the source applies to a birth or adoption, specificity can be maintained by placing the `SOUR` citation under an `INDI.BIRT` or `INDI.ADOP`,
as in the following example:

```
0 @I1@ INDI
1 BIRT
2 SOUR @S2@
2 FAMC @F3@
```

## How do I mark a parent-child relationship as confidential?

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

# Places

## How do I list two places in an emigration?

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

## How do I record a place whose jurisdictional level is ambiguous?

Sometimes a source is found indicating a place but it is unclear what jurisdiction level was meant.
For example, if the record says "New York", does it refer to a state or a city? There are many
examples of such places in the world where the city and a larger jurisdiction have the same name,
such as "St. Louis" in Missouri being both a city and a county.

The `PLAC`.`FORM` structure in GEDCOM contains a list of jurisdictional titles, leading to the
issue in GEDCOM of how to represent a place name whose jurisdictional title could potentially
be any of two or more possibilities.  Simply not including a `FORM` with the specific place is
insufficient since `HEAD`.`PLAC`.`FORM` is used with any `PLAC` with no `FORM`.

One might attempt to use a `PLAC` with no `FORM` in a GEDCOM file with no `HEAD`.`PLAC`.`FORM`
since no version of GEDCOM has justified any assumption that levels have any specific meaning
(such as "City, County, State, Country") without a `FORM` explicitly indicating that. In spite
of that, some applications and users have incorrectly defaulted to assuming a `FORM` of 
"City, County, State, Country", and some applications even ignore any `FORM` substructures and
treat payloads with a smaller number of elements as if they had additional blank elements at
the end, leading to problems of interpretation of GEDCOM files.

A `PLAC`.`NOTE` could perhaps be used in such a case.

# Miscellaneous

## How do I choose LANG payloads?

If you know the GEDCOM 5.5.1 language name, [FHISO has a look-up table](https://github.com/fhiso/legacy-format/blob/master/languages.tsv). You can also look at the lists embedded in the reference 5.5.1-to-7.0 converter program.

If you know the language you want, [r12a has a very flexible search function](https://r12a.github.io/app-subtags/).

You can also look through the [IANA registry](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry) manually and assemble the appropriate tags as outlined in [BCP 47](https://tools.ietf.org/html/bcp47), though that's something of an expert-mode approach.

## How do I record the sex of an intersex person?

The enumerated value on the `SEX` tag in GEDCOM 7.0 was amended to include "X" to describe [intersex](https://en.wikipedia.org/wiki/Intersex) individuals:

```
0 @I1@ INDI
1 SEX X
```

Birth records in some jurisdictions use intersex as the sex value for a child who does not conform to the traditional biological definitions of male or female at birth.

The `SEX` tag is only for anatomical or biological sex at birth. For any related concept that might change and/or manifest later in life, an individual attribute should be used instead.

## How do I record polygamous families?

A `FAM` record should be used for each couple procreating or rearing offspring.
This may result in many `FAM` records for one social family unit.

A `FAM` record may also be used to represent the social family unit.
If it is desirable that all the spouses appear structurally equal, they may be linked using `ASSO` pointers with `ROLE SPOU` instead of `HUSB` and `WIFE` pointers.

Some applications may have more complete handling of `HUSB` and `WIFE` than they have for `ASSO`.

## How do I link to individual structures within a FamilySearch GEDCOM file?

Inside a GEDCOM file, pointers do this using the cross-reference identifiers. However, cross-reference identifiers are *not* durable across import-export cycles and should not be used outside of a GEDCOM file.

If you wish to reference a part of a FamilySearch GEDCOM file from outside that file, you should use one of the durable identifier structures: `UID`, `REFN`, or `EXID`. There is currently no standard way to do this, so any implementation will need to decide how the links will be navigated. 

## How do I flag a primary or profile photo?

There is no standard tag for this purpose in version 7.0.
The first [MULTIMEDIA_LINK](https://gedcom.io/specifications/FamilySearchGEDCOMv7.html#MULTIMEDIA_LINK) in a structure
is the "most-preferred" external object, but that does not necessarily mean it is either an image or a profile image.

As noted in the specification,

> The order of substructures of a single type indicates user preference, with the first substructure being the most-preferred value, unless a different meaning is explicitly indicated in the structure's definition.

The only "different meaning" in the current draft is for `FAM`.`CHIL`, where the specification says

> The order of the CHIL (children) pointers within a FAM (family) structure should be chronological by birth; this is an exception to the usual "most preferred value first" rule.


## How do I reference local files?

A `MULTIMEDIA_RECORD` uses `FILE` and `TRAN` structures to reference one or more files, which might be files
on a local filesystem, or might be remote files referenced by URL.  FamilySearch GEDCOM 7.0 permits local files
to be referenced in multiple ways, including:

* A `file:` URL with absolute path. Example: `FILE file:///path/to/file`
* A relative path with no URI scheme. Example: `FILE path/to/file`

Local `file:` URLs are not permitted in FamilySearch GEDZIP but are permitted in FamilySearch
GEDCOM 7.0 although they should be avoided in datasets that are expected to be shared on the web or with
unknown parties.

Relative paths, however, are permitted in both GEDCOM and GEDZIP files and so may be more convenient to
use in both cases.  Any tool that converts FamilySearch GEDCOM 7.0 to GEDZIP should convert local file URLs
to relative paths within the resulting GEDZIP file.

## How do I record the URL of a source?

While `EVENT_DETAIL` and `REPOSITORY_RECORD` both allow a URL to be placed in a `WWW` substructure,
`SOURCE_CITATION`, `SOURCE_RECORD`, and `SOURCE_REPOSITORY_CITATION` do not.

Some applications might put the source URL for an `EVENT_DETAIL` in a `WWW` substructure
in parallel to a `SOURCE_CITATION`. However, since there can be multiple source citations per event, this does not allow associating the URL
with a specific source citation.  Instead, the URL can be placed in the `PAGE` structure.  For example:

```
1 DEAT
2 DATE 14 DEC 1799
2 SOUR @FindAGraveSourceRecord@
3 PAGE Memorial: 1075, URL: https://www.findagrave.com/memorial/1075
```

Similarly, some applications might put the source URL for a `SOURCE_RECORD` in a `PUBL` substructure
as follows:

```
0 @S1@ SOUR
1 TITL Grave of George Washington
1 PUBL https://www.findagrave.com/memorial/1075
```

while others might put it in the `CALN` of a `SOURCE_REPOSITORY_CITATION` as follows:

```
0 @S1@ SOUR
1 TITL Grave of George Washington
1 REPO @FindAGraveRepositoryRecord@
2 CALN https://www.findagrave.com/memorial/1075
```

Note that unlike the `PAGE` structure, the `CALN` structure has no current recommendation about using
label: value pairs.

## How do I record information about one parent?

Parent-child relationships are stored in the `INDI`.`FAMC` structure, which must point to a `FAM` not an `INDI`.
Additional details about that relationship are stored in its `PEDI` substructure.
To describe the relationship of an `INDI` to just one parent, make a `FAM` that has only one partner.

The following example indicates that `@I1@` was part of the family `@F1@`,
but at birth was only related to the mother, not the father.

```
0 @F1@ FAM
1 NOTE The family as it appeared later
1 CHIL @I1@
1 WIFE @I2@
1 HUSB @I3@
0 @I1@ INDI
1 FAMC @F1@
1 FAMC @F2@
0 @F2@ FAM
1 NOTE The birth coupling; not a "family" in the social sense
1 CHIL @I1@
1 WIFE @I2@
```

Certain additional information about specific aspects of a parent-child relationship can be provided in other structures:

- `ADOP`.`FAMC` indicates the parents involved in a child's adoption.

- `ASSO` with a family relationship `ROLE` -- including like `CHIL`, `FATH`, `MOTH`, and `PARENT` -- is for indicating a person acting in that role in a non-family context, such inside a `WILL` indicating relationships the will described for its beneficiaries or inside a `MARR` indicating guests who were present in the capacity of parents.

- `BIRT`.`FAMC` indicates the parents as pertaining to a child's birth.

- `SLGC`.`FAMC` indicates a recognition of a persons parents by the Church of Jesus Christ of Latter-Day Saints.
