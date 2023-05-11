from enum import Enum


class FormFinderMode(Enum):
    BASIC = 'BASIC'


class FormParserMode(Enum):
    NONE = 'NONE'
    BASIC = 'BASIC'


class FormFillerMode(Enum):
    FIXED = 'FIXED'
    RANDOM = 'RANDOM'
    GPT3 = 'GPT3'
    GPT35 = 'GPT3.5'
    GPT4 = 'GPT4'
