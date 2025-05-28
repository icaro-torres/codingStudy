# Insulin Sequence Processing

This project is a simple **Python exercise** for practicing text processing, file handling, and validation logic.

## 📋 Overview

The script performs the following tasks:

1. **Reads** the raw preproinsulin sequence from a text file.
2. **Cleans** the sequence by removing all non-letter characters and converting it to lowercase.
3. **Splits** the cleaned sequence into parts:
   - **Signal peptide** (24 amino acids)
   - **B chain** (30 amino acids)
   - **C peptide** (35 amino acids)
   - **A chain** (21 amino acids)
4. **Saves** each part to its own file.
5. **Validates** that each file has the correct length.


## How to Run

1. Place the raw sequence file named `preproinsulin-seq.txt` in the same directory as the script.

2. Run the script:

```bash
python analyze-insulin.py
```

3. Check the output files:

    - ```preproinsulin-seq-clean.txt```
    - ```lsinsulin-seq-clean.txt```
    - ```binsulin-seq-clean.txt```
    - ```cinsulin-seq-clean.txt```
    - ```ainsulin-seq-clean.txt```

4. Review the console output to confirm validation results.


### Requirements

- Python 3.x
- No additional libraries required (only re from Python standard library).

###  Example Output

```
Cleaned sequence: 116 characters
lsinsulin-seq-clean.txt saved with 24 characters.
binsulin-seq-clean.txt saved with 30 characters.
cinsulin-seq-clean.txt saved with 35 characters.
ainsulin-seq-clean.txt saved with 21 characters.

=== Validation ===
❌ preproinsulin-seq-clean.txt: ERROR! 116/110 characters
✅ lsinsulin-seq-clean.txt: OK! 24/24 characters
✅ binsulin-seq-clean.txt: OK! 30/30 characters
✅ cinsulin-seq-clean.txt: OK! 35/35 characters
✅ ainsulin-seq-clean.txt: OK! 21/21 characters
```

⚠️ Note: If the cleaned sequence has more than 110 characters, review the raw input file for extra or invalid characters.

##  Key Concepts Practiced

- Regular expressions for data cleaning.
- String slicing to extract subsequences.
- File operations: reading, writing, validating.
- Error handling with try-except.

## Author

[Ícaro Torres]([github](https://github.com/icaro-torres)) — Software development student, always learning and improving Python skills.