# Execution Scripts

This folder contains **deterministic Python scripts** that perform the actual work.

## Purpose

Execution scripts handle:
- API calls
- Data processing
- File operations
- Database interactions

## Principles

1. **Deterministic** - Same inputs → same outputs
2. **Well-commented** - Document what the code does
3. **Testable** - Easy to verify correctness
4. **Fast** - Optimized for performance

## Script Template

```python
#!/usr/bin/env python3
"""
Script Name: script_name.py
Purpose: Brief description of what this script does

Usage:
    python script_name.py --arg1 value1 --arg2 value2

Environment Variables:
    - VAR_NAME: Description
"""

import os
import argparse
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(description="Script description")
    parser.add_argument("--arg1", required=True, help="Description")
    args = parser.parse_args()
    
    # Your logic here
    pass


if __name__ == "__main__":
    main()
```

## Naming Convention

- Use snake_case: `scrape_website.py`, `process_data.py`
- Be descriptive: `upload_to_google_sheets.py` not `upload.py`
