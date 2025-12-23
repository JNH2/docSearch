import re

def parse_message(message: str) -> dict:
    patterns = {
        "Last Name": r"Last Name is\s*(.+?)(,|\n|$)",
        "First Name": r"First Name is\s*(.+?)(,|\n|$)",
        "Company Name": r"Company Name is\s*(.+?)(,|\n|$)",
        "Date": r"Date is\s*(.+?)(,|\n|$)"
    }

    data = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, message, re.IGNORECASE)
        if match:
            data[key] = match.group(1).strip()

    return data
