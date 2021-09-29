import xml.etree.ElementTree as ET

from .exceptions import BadAggregateReport


class AggregateReport:

    def __init__(self, file):
        self._file = None
        self._org_name = None
        self._email = None
        self._extra_contact_info = None
        self._report_id = None
        self._date_begin = None
        self._date_end = None
        self._errors = []
        self._domain = None
        self._adkim = None
        self._aspf = None
        self._p = None
        self._sp = None
        self._pct = None
        self._records = []

        # Initialize attributes

        self.file = file
        root = ET.parse(self.file).getroot()
        # Parse <report_metadata><org_name>
        if root.find('report_metadata/org_name') is not None:
            self.org_name = root.find('report_metadata/org_name').text
        else:
            raise BadAggregateReport('<report_metadata><org_name>' + ' is missing from the report.')
        # Parse <report_metadata><email>
        if root.find('report_metadata/email') is not None:
            self.email = root.find('report_metadata/email').text
        else:
            raise BadAggregateReport('<report_metadata><email>' + ' is missing from the report.')
        # Parse <report_metadata><extra_contact_info>
        if root.find('report_metadata/extra_contact_info') is not None:
            self.extra_contact_info = root.find('report_metadata/extra_contact_info').text
        # Parse <report_metadata><report_id>
        if root.find('report_metadata/report_id') is not None:
            self.report_id = root.find('report_metadata/report_id').text
        else:
            raise BadAggregateReport('<report_metadata><report_id>' + ' is missing from the report.')
        # Parse <report_metadata><date_range><begin>
        if root.find('report_metadata/date_range/begin') is not None:
            self.date_begin = root.find('report_metadata/date_range/begin').text
        else:
            raise BadAggregateReport('<report_metadata><date_range><begin>' + ' is missing from the report.')
        # Parse <report_metadata><date_range><end>
        if root.find('report_metadata/date_range/end') is not None:
            self.date_end = root.find('report_metadata/date_range/end').text
        else:
            raise BadAggregateReport('<report_metadata><date_range><end>' + ' is missing from the report.')
        # Parse multiple <report_metadata><error>
        if root.findall('report_metadata/error') is not None:
            self.errors = [node.text for node in root.findall('report_metadata/error')]
        # Parse <policy_published><domain>
        if root.find('policy_published/domain') is not None:
            self.domain = root.find('policy_published/domain').text
        else:
            raise BadAggregateReport('<policy_published><domain>' + ' is missing from the report.')
        # Parse <policy_published><adkim>
        if root.find('policy_published/adkim') is not None:
            self.adkim = root.find('policy_published/adkim').text
        else:
            raise BadAggregateReport('<policy_published><adkim>' + ' is missing from the report.')
        # Parse <policy_published><aspf>
        if root.find('policy_published/aspf') is not None:
            self.aspf = root.find('policy_published/aspf').text
        else:
            raise BadAggregateReport('<policy_published><aspf>' + ' is missing from the report.')
        # Parse <policy_published><p>
        if root.find('policy_published/p') is not None:
            self.p = root.find('policy_published/p').text
        else:
            raise BadAggregateReport('<policy_published><p>' + ' is missing from the report.')
        # Parse <policy_published><sp>
        if root.find('policy_published/sp') is not None:
            self.sp = root.find('policy_published/sp').text
        else:
            raise BadAggregateReport('<policy_published><sp>' + ' is missing from the report.')
        # Parse <policy_published><pct>
        if root.find('policy_published/pct') is not None:
            self.pct = root.find('policy_published/pct').text
        else:
            raise BadAggregateReport('<policy_published><pct>' + ' is missing from the report.')
        # Parse multiple <record>
        if root.findall('record') is not None:
            self.records = [Record(element) for element in root.findall('record')]

    # Properties

    @property
    def file(self):
        return self._file

    @property
    def org_name(self):
        return self._org_name

    @property
    def email(self):
        return self._email

    @property
    def extra_contact_info(self):
        return self._extra_contact_info

    @property
    def report_id(self):
        return self._report_id

    @property
    def date_begin(self):
        return self._date_begin

    @property
    def date_end(self):
        return self._date_end

    @property
    def errors(self):
        return self._errors

    @property
    def domain(self):
        return self._domain

    @property
    def adkim(self):
        return self._adkim

    @property
    def aspf(self):
        return self._aspf

    @property
    def p(self):
        return self._p

    @property
    def sp(self):
        return self._sp

    @property
    def pct(self):
        return self._pct

    @property
    def records(self):
        return self._records

    # Setters

    @file.setter
    def file(self, value):
        self._file = value

    @org_name.setter
    def org_name(self, value):
        self._org_name = value

    @email.setter
    def email(self, value):
        self._email = value

    @extra_contact_info.setter
    def extra_contact_info(self, value):
        self._extra_contact_info = value

    @report_id.setter
    def report_id(self, value):
        self._report_id = value

    @date_begin.setter
    def date_begin(self, value):
        self._date_begin = value

    @date_end.setter
    def date_end(self, value):
        self._date_end = value

    @errors.setter
    def errors(self, value):
        self._errors = value

    @domain.setter
    def domain(self, value):
        self._domain = value

    @adkim.setter
    def adkim(self, value):
        POSSIBLE_VALUES = [
            'r',
            's'
        ]
        if value in POSSIBLE_VALUES:
            self._adkim = value
        else:
            raise BadAggregateReport('Invalid <policy_published><adkim> value.')

    @aspf.setter
    def aspf(self, value):
        POSSIBLE_VALUES = [
            'r',
            's'
        ]
        if value in POSSIBLE_VALUES:
            self._aspf = value
        else:
            raise BadAggregateReport('Invalid <policy_published><aspf> value.')

    @p.setter
    def p(self, value):
        POSSIBLE_VALUES = [
            'none',
            'quarantine',
            'reject',
        ]
        if value in POSSIBLE_VALUES:
            self._p = value
        else:
            raise BadAggregateReport('Invalid <policy_published><p> value.')

    @sp.setter
    def sp(self, value):
        POSSIBLE_VALUES = [
            'none',
            'quarantine',
            'reject',
        ]
        if value in POSSIBLE_VALUES:
            self._sp = value
        else:
            raise BadAggregateReport('Invalid <policy_published><sp> value.')

    @pct.setter
    def pct(self, value):
        self._pct = value

    @records.setter
    def records(self, value):
        self._records = value

    # Methods

    def __str__(self):
        output = '----- Aggregate Report -----\n'
        output = output + f'org_name: {self.org_name}\n'
        output = output + f'email: {self.email}\n'
        output = output + f'extra_contact_info: {self.extra_contact_info}\n'
        output = output + f'report_id: {self.report_id}\n'
        output = output + f'date_begin: {self.date_begin}\n'
        output = output + f'date_end: {self.date_end}\n'
        output = output + f'errors:\n'
        for error in self.errors:
            output = output + '\t' + f'{error}\n'
        output = output + f'domain: {self.domain}\n'
        output = output + f'adkim: {self.adkim}\n'
        output = output + f'aspf: {self.aspf}\n'
        output = output + f'p: {self.p}\n'
        output = output + f'sp: {self.sp}\n'
        output = output + f'pct: {self.pct}\n'
        output = output + f'records:\n'
        for record in self.records:
            output = output + f'{record.__str__(1)}'
        return output


class Reason:

    def __init__(self, element):
        self._type = None
        self._comment = None
        # Parse <type>
        if element.find('type') is not None:
            self.type = element.find('type').text
        else:
            raise BadAggregateReport('<type>' + ' is missing from the report.')
        # Parse <comment>
        if element.find('comment') is not None:
            self.comment = element.find('comment').text

    # Properties

    @property
    def type(self):
        return self._type

    @property
    def comment(self):
        return self._comment

    # Setters

    @type.setter
    def type(self, value):
        POSSIBLE_VALUES = [
            'forwarded',
            'sampled_out',
            'trusted_forwarder',
            'mailing_list',
            'local_policy',
            'other',
        ]
        if value in POSSIBLE_VALUES:
            self._type = value
        else:
            raise BadAggregateReport('Invalid <reason><type> value.')

    @comment.setter
    def comment(self, value):
        self._comment = value

    # Methods

    def __str__(self, indentation=0):
        output = '\t' * indentation + '----- Reason -----\n'
        output = output + '\t' * indentation + f'type: {self.type}\n'
        output = output + '\t' * indentation + f'comment: {self.comment}'
        return output


class DKIMAuthentication:

    def __init__(self, element):
        self._domain = None
        self._selector = None
        self._result = None
        # Parse <domain>
        if element.find('domain') is not None:
            self.domain = element.find('domain').text
        else:
            raise BadAggregateReport('<domain>' + ' is missing from the report.')
        # Parse <selector>
        if element.find('selector') is not None:
            self.selector = element.find('selector').text
        # Parse <result>
        if element.find('result') is not None:
            self.result = element.find('result').text
        else:
            raise BadAggregateReport('<result>' + ' is missing from the report.')

    # Properties

    @property
    def domain(self):
        return self._domain

    @property
    def selector(self):
        return self._selector

    @property
    def result(self):
        return self._result

    # Setters

    @domain.setter
    def domain(self, value):
        self._domain = value

    @selector.setter
    def selector(self, value):
        self._selector = value

    @result.setter
    def result(self, value):
        POSSIBLE_VALUES = [
            'none',
            'pass',
            'fail',
            'policy',
            'neutral',
            'temperror',
            'permerror',
        ]
        if value in POSSIBLE_VALUES:
            self._result = value
        else:
            raise BadAggregateReport('Invalid <dkim><result> value.')

    # Methods

    def __str__(self, indentation=0):
        output = '\t' * indentation + '----- DKIM Authentication -----\n'
        output = output + '\t' * indentation + f'domain: {self.domain}\n'
        output = output + '\t' * indentation + f'selector: {self.selector}\n'
        output = output + '\t' * indentation + f'result: {self.result}'
        return output


class SPFAuthentication:

    def __init__(self, element):
        self._domain = None
        self._result = None
        # Parse <domain>
        if element.find('domain') is not None:
            self.domain = element.find('domain').text
        else:
            raise BadAggregateReport('<domain>' + ' is missing from the report.')
        # Parse <result>
        if element.find('result') is not None:
            self.result = element.find('result').text
        else:
            raise BadAggregateReport('<result>' + ' is missing from the report.')

    # Properties

    @property
    def domain(self):
        return self._domain

    @property
    def result(self):
        return self._result

    # Setters

    @domain.setter
    def domain(self, value):
        self._domain = value

    @result.setter
    def result(self, value):
        POSSIBLE_VALUES = [
            'none',
            'neutral',
            'pass',
            'fail',
            'softfail',
            'temperror',
            'permerror',
        ]
        if value in POSSIBLE_VALUES:
            self._result = value
        else:
            raise BadAggregateReport('Invalid <spf><result> value.')

    # Methods

    def __str__(self, indentation=0):
        output = '\t' * indentation + '----- SPF Authentication -----\n'
        output = output + '\t' * indentation + f'domain: {self.domain}\n'
        output = output + '\t' * indentation + f'result: {self.result}'
        return output


class Record:

    def __init__(self, element):
        self._source_ip = None
        self._count = None
        self._disposition = None
        self._dkim = None
        self._spf = None
        self._reasons = []
        self._envelope_to = None
        self._header_from = None
        self._dkim_auths = []
        self._spf_auths = []

        # Parse <row><source_ip>
        if element.find('row/source_ip') is not None:
            self.source_ip = element.find('row/source_ip').text
        else:
            raise BadAggregateReport('<row><source_ip>' + ' is missing from the report.')
        # Parse <row><count>
        if element.find('row/count') is not None:
            self.count = element.find('row/count').text
        else:
            raise BadAggregateReport('<row><count>' + ' is missing from the report.')
        # Parse <row><policy_evaluated><disposition>
        if element.find('row/policy_evaluated/disposition') is not None:
            self.disposition = element.find('row/policy_evaluated/disposition').text
        else:
            raise BadAggregateReport('<row><policy_evaluated><disposition>' + ' is missing from the report.')
        # Parse <row><policy_evaluated><dkim>
        if element.find('row/policy_evaluated/dkim') is not None:
            self.dkim = element.find('row/policy_evaluated/dkim').text
        else:
            raise BadAggregateReport('<row><policy_evaluated><dkim>' + ' is missing from the report.')
        # Parse <row><policy_evaluated><spf>
        if element.find('row/policy_evaluated/spf') is not None:
            self.spf = element.find('row/policy_evaluated/spf').text
        else:
            raise BadAggregateReport('<row><policy_evaluated><spf>' + ' is missing from the report.')
        # Parse multiple <reasons>
        if element.findall('row/policy_evaluated/reason') is not None:
            self.reasons = [Reason(e) for e in element.findall('row/policy_evaluated/reason')]
        # Parse <identifiers><envelope_to>
        if element.find('identifiers/envelope_to') is not None:
            self.envelope_to = element.find('identifiers/envelope_to').text
        # Parse <identifiers><header_from>
        if element.find('identifiers/header_from') is not None:
            self.header_from = element.find('identifiers/header_from').text
        else:
            raise BadAggregateReport('<identifiers><header_from>' + ' is missing from the report.')
        # Parse multiple <dkim_auths><dkim>
        if element.findall('auth_results/dkim') is not None:
            self.dkim_auths = [DKIMAuthentication(e) for e in element.findall('auth_results/dkim')]
        # Parse multiple <spf_auths><dkim>
        if element.findall('auth_results/spf') is not None:
            self.spf_auths = [SPFAuthentication(e) for e in element.findall('auth_results/spf')]

    # Properties

    @property
    def source_ip(self):
        return self._source_ip

    @property
    def count(self):
        return self._count

    @property
    def disposition(self):
        return self._disposition

    @property
    def dkim(self):
        return self._dkim

    @property
    def spf(self):
        return self._spf

    @property
    def reasons(self):
        return self._reasons

    @property
    def envelope_to(self):
        return self._envelope_to

    @property
    def header_from(self):
        return self._header_from

    @property
    def dkim_auths(self):
        return self._dkim_auths

    @property
    def spf_auths(self):
        return self._spf_auths

    # Setters

    @source_ip.setter
    def source_ip(self, value):
        self._source_ip = value

    @count.setter
    def count(self, value):
        self._count = value

    @disposition.setter
    def disposition(self, value):
        POSSIBLE_VALUES = [
            'none',
            'quarantine',
            'reject',
        ]
        if value in POSSIBLE_VALUES:
            self._disposition = value
        else:
            raise BadAggregateReport('Invalid <dkim><result> value.')

    @dkim.setter
    def dkim(self, value):
        POSSIBLE_VALUES = [
            'pass',
            'fail',
        ]
        if value in POSSIBLE_VALUES:
            self._dkim = value
        else:
            raise BadAggregateReport('Invalid <row><disposition><dkim> value.')

    @spf.setter
    def spf(self, value):
        POSSIBLE_VALUES = [
            'pass',
            'fail',
        ]
        if value in POSSIBLE_VALUES:
            self._spf = value
        else:
            raise BadAggregateReport('Invalid <row><disposition><spf> value.')

    @reasons.setter
    def reasons(self, value):
        self._reasons = value

    @envelope_to.setter
    def envelope_to(self, value):
        self._envelope_to = value

    @header_from.setter
    def header_from(self, value):
        self._header_from = value

    @dkim_auths.setter
    def dkim_auths(self, value):
        self._dkim_auths = value

    @spf_auths.setter
    def spf_auths(self, value):
        self._spf_auths = value

    # Methods

    def __str__(self, indentation=0):
        output = '\t' * indentation + '----- Record -----\n'
        output = output + '\t' * indentation + f'source_ip: {self.source_ip}\n'
        output = output + '\t' * indentation + f'count: {self.count}\n'
        output = output + '\t' * indentation + f'disposition: {self.disposition}\n'
        output = output + '\t' * indentation + f'dkim: {self.dkim}\n'
        output = output + '\t' * indentation + f'spf: {self.spf}\n'
        output = output + '\t' * indentation + f'reasons:\n'
        for reason in self.reasons:
            output = output + f'{reason.__str__(indentation+1)}\n'
        output = output + '\t' * indentation + f'envelope_to: {self.envelope_to}\n'
        output = output + '\t' * indentation + f'header_from: {self.header_from}\n'
        output = output + '\t' * indentation + f'dkim_auths:\n'
        for dkim_auth in self.dkim_auths:
            output = output + f'{dkim_auth.__str__(indentation+1)}\n'
        output = output + '\t' * indentation + f'spf_auths:\n'
        for spf_auth in self.spf_auths:
            output = output + f'{spf_auth.__str__(indentation+1)}\n'
        return output