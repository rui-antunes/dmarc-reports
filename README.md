# DMARC Reports #

The Python package for parsing, validation and storage of DMARC reports.

## Installation ##

If you use `pip`, you can install it with:

```
pip install dmarc-reports
```

## Usage ##

```
from dmarc_reports.classes import AggregateReport

try:
    with open('aggregate-report.xml','r') as FILE:
        report = AggregateReport(FILE)
except BadAggregateReport as error:
    print(error)
```
