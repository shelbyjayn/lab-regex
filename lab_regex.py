'''Starter functions for the Redacted lab.'''

import re


def has_digit(text):
    '''
    Return True if text contains at least one digit, and False otherwise.

    >>> has_digit('Campus visit #42 booked')
    True
    >>> has_digit('no numbers here')
    False
    '''
    return bool(re.search(r'\d', text))


def find_numbers(text):
    '''
    Return a list of every run of consecutive digits in text, as strings.

    >>> find_numbers('I booked 2 tours for 10 visitors')
    ['2', '10']
    >>> find_numbers('no numbers here')
    []
    '''
    return re.findall(r'\d+', text)


def mask_digits(text):
    '''
    Return text with every digit replaced by a capital 'X'.

    >>> mask_digits('call 909-621-8088')
    'call XXX-XXX-XXXX'
    >>> mask_digits('no digits')
    'no digits'
    '''
    return re.sub(r'\d', 'X', text)


def find_hashtags(text):
    '''
    Return a list of the hashtags in text, each without its leading '#'.

    >>> find_hashtags('Campus visit today! #CMC #Claremont #CMC')
    ['CMC', 'Claremont', 'CMC']
    >>> find_hashtags('no tags in this one')
    []
    '''
    return re.findall(r'#(\w+)', text)


def find_mentions(text):
    '''
    Return a list of the @-handles in text, each without its leading '@'.

    >>> find_mentions('thank you @cmc and @pomona, see you soon @cmc')
    ['cmc', 'pomona', 'cmc']
    >>> find_mentions('nobody is mentioned here')
    []
    '''
    # The lookbehind skips the '@' inside an email address like admission@cmc.edu.
    return re.findall(r'(?<!\w)@(\w+)', text)


def find_urls(text):
    '''
    Return a list of the http and https URLs in text.

    >>> find_urls('read more at https://www.cmc.edu today and http://www.pomona.edu')
    ['https://www.cmc.edu', 'http://www.pomona.edu']
    >>> find_urls('no links in this tweet')
    []
    '''
    return re.findall(r'https?://\S+', text)


def find_phone_numbers(text):
    '''
    Return a list of the US phone numbers in text, in XXX-XXX-XXXX form.

    >>> find_phone_numbers('call 909-621-8088 or 800-770-1333 today')
    ['909-621-8088', '800-770-1333']
    >>> find_phone_numbers('no phone number here')
    []
    '''
    return re.findall(r'\b\d{3}-\d{3}-\d{4}\b', text)


def area_code(phone):
    '''
    Return the three-digit area code of a XXX-XXX-XXXX phone number.

    >>> area_code('909-621-8088')
    '909'
    >>> area_code('800-770-1333')
    '800'
    '''
    match = re.match(r'(\d{3})-\d{3}-\d{4}', phone)
    return match.group(1)


def redact_emails(text):
    '''
    Return text with every email address replaced by the string '[REDACTED]'.

    >>> redact_emails('reach me at admission@cmc.edu or admission@hmc.edu')
    'reach me at [REDACTED] or [REDACTED]'
    >>> redact_emails('this line has no email')
    'this line has no email'
    '''
    return re.sub(r'[\w.+-]+@[\w-]+(?:\.[\w-]+)+', '[REDACTED]', text)


def redact_ssns(text):
    '''
    Return text with every US Social Security number masked as 'XXX-XX-XXXX'.

    >>> redact_ssns('SSN 123-45-6789 on file')
    'SSN XXX-XX-XXXX on file'
    >>> redact_ssns('no ssn in this record')
    'no ssn in this record'
    '''
    return re.sub(r'\b\d{3}-\d{2}-\d{4}\b', 'XXX-XX-XXXX', text)


def mask_last_four(card):
    '''
    Return a 16-digit card number with all but its last four digits masked by '*'.

    >>> mask_last_four('1234567812345678')
    '************5678'
    >>> mask_last_four('4111111111111111')
    '************1111'
    '''
    return re.sub(r'^\d{12}(?=\d{4}$)', '*' * 12, card)


def is_valid_email(s):
    '''
    Return True if the whole string s is a single valid-looking email address.

    >>> is_valid_email('admission@cmc.edu')
    True
    >>> is_valid_email('not-an-email')
    False
    >>> is_valid_email('admission@cmc.edu and some extra text')
    False
    >>> is_valid_email('admission@cmc.edu' + chr(10))
    False
    '''
    return bool(re.fullmatch(r'[\w.+-]+@[\w-]+(?:\.[\w-]+)+', s))
