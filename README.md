# DMARC Reports #

The Python package for parsing, validation and storage of DMARC reports.

## Installation ##

If you use `pip`, you can install it with:

```
pip install dmarc-reports
```

## Usage ##

Parse and validate an aggregate report `.xml` file into an `AggregateReport` class:

```
from dmarc_reports.classes import AggregateReport

try:
    with open('aggregate-report.xml','r') as FILE:
        report = AggregateReport(FILE)
except BadAggregateReport as error:
    print(error)
```

## Resources ##

* [DMARC](https://dmarc.org/)
