import re

def get_value(label: str, text: str):
    pattern = rf"{label}\s*:\s*(.+)"
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return None

def extract_fields(text: str) -> dict:
    extracted = {}

    # ✅ TXT style extraction
    extracted["policyNumber"] = get_value("Policy Number", text)
    extracted["policyholderName"] = get_value("Policyholder Name", text)

    extracted["dateOfLoss"] = get_value("Date of Loss", text)
    extracted["timeOfLoss"] = get_value("Time of Loss", text)
    extracted["location"] = get_value("Location", text)
    extracted["description"] = get_value("Description", text)

    extracted["estimatedDamage"] = get_value("Estimated Damage", text)
    extracted["claimType"] = get_value("Claim Type", text) or "vehicle"

    extracted["attachments"] = get_value("Attachments", text)
    extracted["initialEstimate"] = get_value("Initial Estimate", text)

    extracted["assetType"] = get_value("Asset Type", text)
    extracted["assetId"] = get_value("Asset ID", text)

    # ✅ PDF fallback (ACORD blank template will still give None - correct)
    if extracted["policyNumber"] is None and "AUTOMOBILE LOSS NOTICE" in text:
        match_damage = re.search(r"ESTIMATE AMOUNT[:\s]*\$?\s*([\d,]+)", text, re.IGNORECASE)
        if match_damage:
            extracted["estimatedDamage"] = match_damage.group(1).strip()

    return extracted
