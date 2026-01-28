# Q1: Regex Solutions
# Student: Adabala Charishma
# Course: CS5760 Natural Language Processing

import re

zip_code = r"\b\d{5}([ -]\d{4})?\b"
non_capital = r"\b[a-z][a-zA-Z]*(?:['-][a-zA-Z]+)*\b"
number = r"[+-]?(?:\d{1,3}(?:,\d{3})*|\d+)(?:\.\d+)?(?:[eE][+-]?\d+)?"
email = r"(?i)\be[ -–]?mail\b"
go_pattern = r"\bgo+\b[!.,?]?"
quote_end = r"\?\s*[\"')\]’”]*$"
