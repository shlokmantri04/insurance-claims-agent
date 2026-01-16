import re

BAD_VALUES = {
    "contact", "middle", "last", "first", "name", "insured",
    "policy", "number", "date", "loss", "location"
}

def clean_value(value: str):
    if not value:
        return None

    value = value.strip()

    # Remove extra spaces
    value = re.sub(r"\s+", " ", value)

    # If value is too small, ignore
    if len(value) <= 2:
        return None

    # If it looks like only a label word
    if value.lower() in BAD_VALUES:
        return None

    return value


def find_with_regex(pattern: str, text: str):
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        return clean_value(match.group(1))
    return None
