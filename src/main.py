import json
import os

from pdf_reader import extract_text_from_pdf
from text_reader import extract_text_from_txt
from extractor import extract_fields
from router import route_claim

MANDATORY_FIELDS = [
    "policyNumber",
    "policyholderName",
    "dateOfLoss",
    "location",
    "description",
    "estimatedDamage"
]

from validator import (
    validate_policy_number,
    validate_name,
    validate_date_mmddyyyy,
    validate_time,
    validate_location,
    validate_description,
    validate_amount,
    validate_claim_type,
    validate_phone_10_digits,
    validate_email
)


def check_missing_fields(extracted: dict) -> list:
    """
    Check if any mandatory fields are missing from extracted fields.
    """
    missing = []
    for field in MANDATORY_FIELDS:
        if not extracted.get(field):
            missing.append(field)
    return missing


def load_document_text(file_path: str) -> str:
    """
    Load text from a PDF or TXT file.
    """
    if file_path.lower().endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path.lower().endswith(".txt"):
        return extract_text_from_txt(file_path)
    else:
        raise ValueError("Unsupported file type. Use PDF or TXT only.")


def main():
    """
    Main function to process a FNOL claim.
    """
    # Change this to test different cases
    file_path = "data/test_cases/case1_fasttrack.txt"
    # file_path = "data/test_cases/case2_manual_missing.txt"
    # file_path = "data/test_cases/case3_investigation.txt"
    # file_path = "data/test_cases/case4_injury.txt"
    # file_path = "data/sample_fnol.pdf"

    text = load_document_text(file_path)
    extracted = extract_fields(text)

    missing_fields = check_missing_fields(extracted)
    inconsistent_fields = []

    # Mandatory validations
    if extracted.get("policyNumber") and not validate_policy_number(extracted["policyNumber"]):
        inconsistent_fields.append("policyNumber")

    if extracted.get("policyholderName") and not validate_name(extracted["policyholderName"]):
        inconsistent_fields.append("policyholderName")

    if extracted.get("dateOfLoss") and not validate_date_mmddyyyy(extracted["dateOfLoss"]):
        inconsistent_fields.append("dateOfLoss")

    if extracted.get("timeOfLoss") and not validate_time(extracted["timeOfLoss"]):
        inconsistent_fields.append("timeOfLoss")

    if extracted.get("location") and not validate_location(extracted["location"]):
        inconsistent_fields.append("location")

    if extracted.get("description") and not validate_description(extracted["description"]):
        inconsistent_fields.append("description")

    if extracted.get("estimatedDamage") and not validate_amount(extracted["estimatedDamage"]):
        inconsistent_fields.append("estimatedDamage")

    if extracted.get("claimType") and not validate_claim_type(extracted["claimType"]):
        inconsistent_fields.append("claimType")


    recommended_route, reasoning = route_claim(extracted, missing_fields)

    if inconsistent_fields:
        recommended_route = "Manual review"
        reasoning = "Some fields are inconsistent/invalid, so claim needs manual review."
    else:
        recommended_route, reasoning = route_claim(extracted, missing_fields)

    final_output = {
        "extractedFields": extracted,
        "missingFields": missing_fields,
        "inconsistentFields": inconsistent_fields,
        "recommendedRoute": recommended_route,
        "reasoning": reasoning
    }

    os.makedirs("output", exist_ok=True)
    with open("output/result.json", "w") as f:
        json.dump(final_output, f, indent=4)

    print("Claim processed successfully!")
    print(json.dumps(final_output, indent=4))


if __name__ == "__main__":
    main()

