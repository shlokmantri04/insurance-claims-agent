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

def check_missing_fields(extracted: dict) -> list:
    missing = []
    for field in MANDATORY_FIELDS:
        if not extracted.get(field):
            missing.append(field)
    return missing

def load_document_text(file_path: str) -> str:
    if file_path.lower().endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path.lower().endswith(".txt"):
        return extract_text_from_txt(file_path)
    else:
        raise ValueError("Unsupported file type. Use PDF or TXT only.")

def main():
    # ✅ Change this to test different cases
    # file_path = "data/test_cases/case1_fasttrack.txt"
    # file_path = "data/test_cases/case2_manual_missing.txt"
    # file_path = "data/test_cases/case3_investigation.txt"
    file_path = "data/test_cases/case4_injury.txt"


    text = load_document_text(file_path)
    extracted = extract_fields(text)

    missing_fields = check_missing_fields(extracted)
    recommended_route, reasoning = route_claim(extracted, missing_fields)

    final_output = {
        "extractedFields": extracted,
        "missingFields": missing_fields,
        "recommendedRoute": recommended_route,
        "reasoning": reasoning
    }

    os.makedirs("output", exist_ok=True)
    with open("output/result.json", "w") as f:
        json.dump(final_output, f, indent=4)

    print("✅ Claim processed successfully!")
    print(json.dumps(final_output, indent=4))

if __name__ == "__main__":
    main()
