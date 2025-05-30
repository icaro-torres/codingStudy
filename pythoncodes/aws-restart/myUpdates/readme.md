# ☁️ Cloud School Labs - Python & AWS Development Log

This repository serves as a technical log documenting my progress and projects developed during the practical labs at **AWS re/Start** program. The focus is on applying Python programming principles and leveraging AWS technologies. Each entry details the lab's objectives, technical challenges encountered, implemented solutions, and key takeaways.

## 🔗 README index

* [May 30, 2025 - JSON Data Handling & Insulin Molecular Weight Calculation](#may-30-2025---json-data-handling--insulin-molecular-weight-calculation)

## 🗓️ Update Log

### May 30, 2025 - JSON Data Handling & Insulin Molecular Weight Calculation

**Lab Description:**
This lab focused on developing a Python system for **retrieving and analyzing molecular information, specifically for human insulin, from a JSON data source**.

**Technical Objectives:**
* **Module Development:** Implement `jsonFileHandler.py` for robust JSON file I/O operations and `calc_weight_json.py` as the primary application logic module. This reinforces best practices in code modularity and reusability.
* **JSON Data Parsing:** Utilize Python's built-in `json` module to open, load, and parse structured JSON data (`insulin.json`). This involved extracting specific key-value pairs representing amino acid sequences and their corresponding molecular weights.
* **Computational Biology Application:** Reimplement the logic for calculating the approximate molecular weight of insulin by summing the weighted counts of its constituent amino acids, based on data retrieved from the JSON structure.

**Technical Challenges & Resolution:**
A primary obstacle encountered was an `IOError: Could not read file` during file access. Initial troubleshooting focused on `open()` function parameters. However, the root cause was identified as an **incorrect relative file path**.

**Root Cause Analysis:**
The lab's instructions implied creating a `files` subdirectory for `insulin.json`. My initial project setup placed `insulin.json` at the same hierarchical level as the `calc_weight_json.py` and `jsonFileHandler.py` scripts. Consequently, specifying paths like `'files/insulin.json'` or `'sequenceCleaning/insulin.json'` resulted in file not found errors from the execution context.

**Solution Implemented:**
* **`jsonFileHandler.py` Refinement:** The `readJsonFile` function was updated to correctly utilize the `fileName` parameter passed during invocation. This ensures dynamic file path handling. Error robustness was enhanced by incorporating `try-except` blocks to specifically catch `IOError` (for file system issues) and `json.JSONDecodeError` (for malformed JSON content).
* **`calc_weight_json.py` Path Correction:** The call to `jsonFileHandler.readJsonFile()` was adjusted to pass the correct relative path: `'insulin.json'`. This resolves the file access issue by correctly referencing the JSON data file within the same directory as the executing script.

**Key Technical Takeaways:**
* **Relative vs. Absolute Paths:** A clear understanding of how relative paths are resolved from the execution directory is critical for robust file I/O.
* **Python Module Design:** Effective encapsulation of functionalities (e.g., file handling) into separate modules enhances code organization and maintainability.
* **Robust Error Handling:** Proactive use of `try-except` blocks is essential for gracefully managing runtime exceptions, such as file not found or data parsing errors.
* **JSON Data Interoperability:** Practical experience in parsing and leveraging JSON for structured data exchange in scientific computing contexts.

### 📸 Lab Screenshots

![Screenshot - Project code + Terminal output](/pythoncodes/aws-restart/myUpdates/images/300525-image(1).png)

<br>

![Screenshot - jsonFileHandler file](/pythoncodes/aws-restart/myUpdates/images/300525-image(2).png)

<br>

![Screenshot - json file](/pythoncodes/aws-restart/myUpdates/images/300525-image(3).png)

<br>

![Screenshot - Reorganizing files](/pythoncodes/aws-restart/myUpdates/images/reorganizing.png)


## ✨ Core Technologies

* Python
* JSON
* AWS Cloud9 IDE
* Visual Studio Code



## 📚 Resources & References

* [Link to AWS re/Start page](https://aws.amazon.com/pt/training/restart/)
* [Any specific documentation used for a lab, e.g., Python JSON docs, AWS docs]()