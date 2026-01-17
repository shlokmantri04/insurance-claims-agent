import re
from datetime import datetime

def is_empty(value):
    if value is None:
        return True
    if isinstance(value, str) and value.strip() == "":
        return True
    return False

def validate_policy_number(value: str) -> bool:
    if is_empty(value):
        return False
    # Example: POL-1001 / ABC123 / MH12-XYZ
    return bool(re.fullmatch(r"[A-Za-z0-9\-]{4,30}", value.strip()))

def validate_name(value: str) -> bool:
    if is_empty(value):
        return False
    value = value.strip()
    # Must contain alphabets
    return bool(re.search(r"[A-Za-z]", value))

def validate_date_mmddyyyy(value: str) -> bool:
    if is_empty(value):
        return False
    value = value.strip()
    try:
        datetime.strptime(value, "%m/%d/%Y")
        return True
    except ValueError:
        return False

def validate_time(value: str) -> bool:
    if is_empty(value):
        return False
    value = value.strip()
    # Accept formats like: 06:15 PM, 6:15 PM
    return bool(re.fullmatch(r"(0?[1-9]|1[0-2]):[0-5]\d\s?(AM|PM)", value, re.IGNORECASE))

def validate_location(value: str) -> bool:
    if is_empty(value):
        return False
    # At least 3 characters
    return len(value.strip()) >= 3

def validate_description(value: str) -> bool:
    if is_empty(value):
        return False
    value = value.strip()
    # Must be meaningful
    return len(value) >= 10

def validate_amount(value: str) -> bool:
    if is_empty(value):
        return False
    value = str(value).replace(",", "").strip()
    if not value.isdigit():
        return False
    return int(value) > 0

def validate_claim_type(value: str) -> bool:
    if is_empty(value):
        return False
    return value.strip().lower() in ["vehicle", "injury"]

def validate_phone_10_digits(value: str) -> bool:
    if is_empty(value):
        return False
    digits = re.sub(r"\D", "", value)  # remove spaces + symbols
    return bool(re.fullmatch(r"\d{10}", digits))

def validate_email(value: str) -> bool:
    if is_empty(value):
        return False
    value = value.strip()
    return bool(re.fullmatch(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}", value))
