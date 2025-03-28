---
title: type-Date
permalink: /terms/v7/type-Date.html
layout: none
redirect-from:
  - /terms/v7/type-Date
...

```

%YAML 1.2
---
lang: en-US

type: data type

uri: https://gedcom.io/terms/v7/type-Date

specification:
  - |
    The date formats defined in this specification include the ability to store
    approximate dates, date periods, and dates expressed in different calendars.
    
    Technically, there are 3 distinct date data types:
    
    - `DateValue` is a generic type that can express many kinds of dates.
    - `DateExact` is used for timestamps and other fully-known dates.
    - `DatePeriod` is used to express time intervals that span multiple days.
    
    ```abnf
    DateValue   = [ date / DatePeriod / dateRange / dateApprox ]
    DateExact   = day D month D year  ; in Gregorian calendar
    DatePeriod  = [ %s"TO" D date ]
                / %s"FROM" D date [ D %s"TO" D date ]
                ; note both DateValue and DatePeriod can be the empty string
    
    date        = [calendar D] [[day D] month D] year [D epoch]
    dateRange   = %s"BET" D date D %s"AND" D date
                / %s"AFT" D date
                / %s"BEF" D date
    dateApprox  = (%s"ABT" / %s"CAL" / %s"EST") D date
    
    dateRestrict = %s"FROM" / %s"TO" / %s"BET" / %s"AND" / %s"BEF"
                / %s"AFT" / %s"ABT" / %s"CAL" / %s"EST"
    
    calendar = %s"GREGORIAN" / %s"JULIAN" / %s"FRENCH_R" / %s"HEBREW"
             / extTag
    
    day     = Integer
    year    = Integer
    month   = stdTag / extTag  ; constrained by calendar
    epoch   = %s"BCE" / extTag ; constrained by calendar
    ```
    
    In addition to the constraints above:
    
    - The allowable `day`s, `month`s, `year`s, and `epoch`s are determined by the
      `calendar`. All known calendars restrict `day` to be between 1 and a
      month-specific maximum. The largest known maximum is 36, and most months in
      most calendars have a lower maximum.
    - No calendar names, months, or epochs match `dateRestrict`.
    - Extension calendars (those with `extTag` for their `calendar`) must use
      `extTag`, not `stdTag`, for months.
    
    It is recommended that calendars avoid using a single tag to refer to both a
    month and an epoch.
    
    An absent `calendar` is equivalent to the calendar `GREGORIAN`.
    
    The grammar above allows for `date`s to be preceded by various words. The
    meaning of these words is given as follows:
    
    | Production | Meaning                                                                  |
    | :--------- | :----------------------------------------------------------------------- |
    | `FROM` *x* | Lasted for multiple days, beginning on *x*.                              |
    | `TO` *x*   | Lasted for multiple days, ending on *x*.                                 |
    | `BET` *x*  | Exact date unknown, but no earlier than *x*.                             |
    | `AND` *x*  | Exact date unknown, but no later than *x*.                               |
    | `BEF` *x*  | Exact date unknown, but no later than *x*.                               |
    | `AFT` *x*  | Exact date unknown, but no earlier than *x*.                             |
    | `ABT` *x*  | Exact date unknown, but near *x*.                                        |
    | `CAL` *x*  | *x* is calculated from other data.                                       |
    | `EST` *x*  | Exact date unknown, but near *x*; and *x* is calculated from other data. |
    
    Known calendars and tips for handling dual dating and extension calendars are
    given in [Appendix A: Calendars and Dates].
    
    `DateValue` and `DatePeriod` payloads may also be the empty string if no
    suitable form is known but a substructure (such as a `PHRASE` or `TIME`) is
    desired.
    
    <div class="note">
    
    Versions 5.3 through 5.5.1 allowed phrases inside `DateValue` payloads. Date
    phrases were moved to the `PHRASE` substructure in version 7.0. A current
    limitation, however, is that a phrase in the `PHRASE` substructure cannot
    specify a language, so if a non-default language is needed to correctly
    interpret the phrase two options exist:
    
    - `PHRASE` can be used with a documented extension tag for the language, as
      discussed in `https://gedcom.io/terms/v7/LANG`.
    
    - `<<EVENT_DETAIL>>.SOUR.DATA.TEXT` can be used instead along with a `LANG`
      substructure; this loses the connection with the date, but includes the
      language with a standard tag.
    
    </div>
    
    <div class="note">
    
    As defined by the grammar above, every date must have a year. If no year is
    known, the entire date may be omitted.
    
    <div class="example">
    
    The following is an appropriate way to handle a missing year
    
    ```gedcom
    2 DATE
    3 PHRASE 5 January (year unknown)
    ```
    
    </div>
    
    </div>
    
    The URI for the `DateValue` data type is
    `https://gedcom.io/terms/v7/type-Date`.
    
    The URI for the `DateExact` data type is
    `https://gedcom.io/terms/v7/type-Date#exact`.
    
    The URI for the `DatePeriod` data type is
    `https://gedcom.io/terms/v7/type-Date#period`.

contact: "https://gedcom.io/community/"
...

```
