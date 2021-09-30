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
from dmarc_reports.exceptions import BadAggregateReport


try:
    with open('aggregate-report.xml','r') as FILE:
        report = AggregateReport(FILE)
except BadAggregateReport as error:
    print(error)
```

## Resources ##

* [DMARC](https://dmarc.org/)

## License ##

MIT License

Copyright (c) 2021 Rui Antunes

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
