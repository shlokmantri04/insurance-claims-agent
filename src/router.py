def route_claim(extracted_fields: dict, missing_fields: list) -> tuple:
    """
    Returns: (recommendedRoute, reasoning)
    """

    # Rule 1: If any mandatory field missing → Manual review
    if missing_fields:
        return "Manual review", "Some mandatory fields are missing, so claim needs manual review."

    description = extracted_fields.get("description", "") or ""
    claim_type = extracted_fields.get("claimType", "") or ""

    # Rule 2: Fraud keywords → Investigation Flag
    fraud_words = ["fraud", "inconsistent", "staged"]
    for word in fraud_words:
        if word.lower() in description.lower():
            return "Investigation Flag", f"Description contains suspicious keyword: '{word}'."

    # Rule 3: Claim type injury → Specialist Queue
    if claim_type.lower() == "injury":
        return "Specialist Queue", "Claim type is injury, so it should go to specialist queue."

    # Rule 4: Damage < 25000 → Fast-track
    damage = extracted_fields.get("estimatedDamage")
    if damage:
        damage_num = int(damage.replace(",", ""))
        if damage_num < 25000:
            return "Fast-track", f"Estimated damage ({damage_num}) is below 25000."

    return "Manual review", "Claim does not match fast-track conditions, needs manual review."
