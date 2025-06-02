# ☁️ Cloud School Labs - Python & AWS Development Log

This repository serves as a technical log documenting my progress and projects developed during the practical labs at **AWS re/Start** program. The focus is on applying Python programming principles and leveraging AWS technologies. Each entry details the lab's objectives, technical challenges encountered, implemented solutions, and key takeaways.

## 🔗 README index

* [May 30, 2025 - JSON Data Handling & Insulin Molecular Weight Calculation](#may-30-2025---json-data-handling--insulin-molecular-weight-calculation)
* [June 02, 2025 - Python for System Interaction, Debugging, and Problem-Solving](#june-02-2025---python-for-system-interaction-debugging-and-problem-solving)

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

### June 02, 2025 - Python for System Interaction, Debugging, and Problem-Solving

**Lab Description:**
This series of labs focused on building practical Python skills, starting with system command execution, progressing to mastering debugger fundamentals in Visual Studio Code, and culminating in applying these debugging techniques to diagnose and resolve multiple issues in a Caesar cipher program. The overall goal was to move beyond basic syntax to practical script automation and robust code troubleshooting.

**Technical Objectives:**
* Execute Linux/Bash shell commands (e.g., `ls`, `uname`, `ps`) from Python scripts using `os.system` and `subprocess.run`.
* Understand and effectively use core debugger features in VS Code: setting breakpoints, adding watch expressions to monitor variables, and controlling execution flow (Step Over, Step Into, Continue).
* Apply systematic debugging techniques to identify and fix various types of errors in Python code, including `TypeError` exceptions and logical flaws in algorithms.
* Gain proficiency in using VS Code for Python development and debugging.

**Technical Challenges & Resolution:**
* **Challenge:** Correctly formatting commands and arguments for `subprocess.run()`; initial navigation and understanding of the VS Code debugger interface (specifically the WATCH panel).
    * **Resolution:** Clarified syntax through examples for `subprocess.run()`; provided detailed, step-by-step guidance for VS Code debugger UI, including analyzing user-provided screenshots to pinpoint issues and ensure proper debugger setup and use.
* **Challenge:** Diagnosing a `TypeError` in the Caesar cipher due to operations between `int` and `str` types.
    * **Resolution:** Used the debugger to inspect variable types at the point of error, then applied the `int()` type conversion to the string variable (`cipherKey`) before the arithmetic operation.
* **Challenge:** Identifying logical errors in the Caesar cipher, such as partial encryption (due to missing `.upper()` string method) or incorrect decryption results (due to passing the wrong key variable to a function).
    * **Resolution:** Employed the debugger to trace variable states (`currentCharacter`, `position`, `decryptKey`) and execution flow (using "Step Into" for function calls) to pinpoint where the logic deviated. Corrections involved ensuring string methods were applied correctly and the correct variables were used in function arguments.
* **Challenge:** Addressing program halts or unexpected behavior after initial bug fixes (e.g., program stopping after printing the cipher key but before showing encrypted/decrypted messages).
    * **Resolution:** Guided systematic debugging by setting breakpoints at the entry and within the suspected function (`encryptMessage`), stepping through its execution line-by-line to observe behavior and variable states, ensuring the function completed and returned as expected.

**Solution Implemented:**
* Developed Python scripts to execute a variety of system commands, demonstrating automation capabilities.
* Utilized the VS Code debugger to meticulously step through a basic Python script, learning to set breakpoints, watch variable changes, and control program flow.
* Systematically debugged a multi-bug Caesar cipher program by:
    1.  Fixing a `TypeError` related to an incorrect data type for the cipher key.
    2.  Ensuring proper string case handling for consistent encryption.
    3.  Correcting the decryption logic to use the appropriate negative key.
    4.  Debugging unexpected program termination/halts by stepping into function calls and monitoring variable states throughout the encryption process.
    All debugging and code corrections were performed within a single, evolving Python file for clarity and focused learning.

**Key Technical Takeaways:**
* Python provides powerful modules (`os`, `subprocess`) for system-level scripting and automation.
* A debugger is an indispensable tool for software development, crucial for understanding code behavior, diagnosing errors (both crashes and logical flaws), and verifying fixes.
* Mastery of debugger controls (breakpoints, watch, step over/into) significantly accelerates the troubleshooting process.
* A methodical approach to debugging—observing states, forming hypotheses, testing, and iterating—is key to resolving complex issues.
* Understanding data types, type conversions, and control flow is fundamental to writing correct and robust Python programs.


## ✨ Core Technologies

* Python
* JSON
* AWS Cloud9 IDE
* Visual Studio Code



## 📚 Resources & References

* [Link to AWS re/Start page](https://aws.amazon.com/pt/training/restart/)
* [Python debugging in VS Code](https://code.visualstudio.com/docs/python/debugging)
* [Implementing the Caesar Cipher](https://labex.io/pt/tutorials/python-implementing-caesar-cipher-encryption-302693)