# Data Automation Tool

A simple Python tool that demonstrates automated data processing workflows.

## What It Does

Reads data from a CSV file, processes it (cleans, validates, enriches), 
and outputs as JSON or CSV.

**Real use case:** 
Customer data comes in messy. This tool cleans it up, validates email 
addresses, adds timestamps, and outputs ready-to-use data.

## How To Use

### 1. Prepare your data

Create a CSV file with your data:

name,email,phone
John Smith,john@example.com,555-1234
Jane Doe,jane@example.com,555-5678

### 2. Run the tool
```bash
python data_processor.py
```

### 3. Get output

Check `output.json` for processed data.

## Customization

Edit `data_processor.py` to add your own processing logic:
- Validate data (email, phone, URLs)
- Enrich data (lookup from API, calculate values)
- Transform data (format changes, calculations)
- Filter data (keep only certain rows)

## Tech

- Python 3.8+
- Standard library only (no dependencies needed)

## Example

**Input:**
name,email
john,JOHN@EXAMPLE.COM

**Output:**

{
"name": "john",
"email": "john@example.com",
"email_valid": true,
"processed_at": "2025-03-10T14:32:45.123456"
}

That's it. Use this for your own data automation needs.
