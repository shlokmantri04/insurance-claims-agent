## 🧠 Approach

This project is a lightweight **FNOL (First Notice of Loss) Claims Processing Agent** that automates the first step of insurance claim intake.

### 1) Input Handling
- The agent accepts FNOL documents in **PDF** or **TXT** format.
- PDF text is extracted using `pdfplumber`.
- TXT files are directly read as plain text (used for reliable testing).

### 2) Field Extraction
- The extracted document text is parsed to collect key claim fields such as:
  - Policy Number, Policyholder Name
  - Date/Time/Location of Loss
  - Incident Description
  - Claim Type
  - Estimated Damage, Attachments, Initial Estimate
  - Asset Type and Asset ID
- TXT documents are extracted using label-based patterns like:
  `Policy Number: POL-1001`

### 3) Validation (Missing Field Detection)
- A list of mandatory fields is checked.
- If any mandatory field is missing, it is added to `missingFields`.

### 4) Routing Decision Engine
The agent recommends a workflow route using predefined rules:
- Estimated damage < 25,000 → **Fast-track**
- Missing mandatory fields → **Manual review**
- Fraud keywords in description → **Investigation Flag**
- Claim type = injury → **Specialist Queue**

### 5) JSON Output
The final result is returned in JSON format containing:
- `extractedFields`
- `missingFields`
- `recommendedRoute`
- `reasoning`

---------------


## 🚀 Steps to Run (Windows + Mac/Linux)

### 📥 Clone the Repository
First, clone the repository to your local machine:
```bash
git clone https://github.com/shlokmantri04/insurance-claims-agent.git
cd insurance-claims-agent
```

### 🪟 Windows Setup & Run

#### ✅ 1) Create a Virtual Environment
```bash
python -m venv venv
```

#### ✅ 3) Activate the Virtual Environment
```bash
venv\Scripts\activate
```
You should see: `(venv)`

#### ✅ 4) Install Dependencies
```bash
pip install -r requirements.txt
```

#### ✅ 5) Select an Input File
Open `src/main.py` and set:
```python
file_path = "data/test_cases/case1_fasttrack.txt"
```
OR you can select a PDF available in the `data/` folder:
```python
file_path = "data/sample_fnol.pdf"
```


#### ✅ 6) Run the Project
```bash
python src/main.py
```

#### ✅ 7) Output
The result will be printed in the terminal and saved to: `output/result.json`

---

### 🍎 Mac / Linux Setup & Run

#### ✅ 1) Open the Project Folder in Terminal
Example:
```bash
cd ~/Desktop/insurance-claims-agent
```

#### ✅ 2) Create a Virtual Environment
```bash
python3 -m venv venv
```

#### ✅ 3) Activate the Virtual Environment
```bash
source venv/bin/activate
```
You should see: `(venv)`

#### ✅ 4) Install Dependencies
```bash
pip install -r requirements.txt
```

#### ✅ 5) Select an Input File
Open `src/main.py` and set:
```python
file_path = "data/test_cases/case1_fasttrack.txt"
```
OR you can select a PDF available in the `data/` folder:
```python
file_path = "data/sample_fnol.pdf"
```

#### ✅ 6) Run the Project
```bash
python src/main.py
```

#### ✅ 7) Output
The result will be printed in the terminal and saved to: `output/result.json`
