# kobo-update-status

## Overview
This Python script allows you to update the validation statuses of submissions in KoboToolbox using a batch process. Submission IDs are read from an Excel file, and the updates are performed via KoboToolbox's API using a bulk update endpoint.

## Features
- **Batch Processing from Excel**: Read submission IDs from an Excel file for bulk updates.
- **Bulk Updates**: Efficiently update multiple submissions in one API call.
- **Error Handling**: Provides detailed error messages for invalid input or API failures.

## Requirements

### Dependencies
- Python 3.x
- Required Python packages:
  - `requests`
  - `pandas`
  - `openpyxl` (for reading Excel files)

Install dependencies with:
```bash
pip install requests pandas openpyxl
```

### File Requirements
- An Excel file with a column named `_id` containing submission IDs to update.

## Usage

### Setup
1. Clone the repository or download the script:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Modify the following variables in the script:
   - `KF_URL`: Your KoboToolbox API URL (e.g., `https://KPI`).
   - `TOKEN`: Your KoboToolbox API token.
   - `ASSET_UID`: The UID of the form you want to update submissions for.

### Running the Script

1. Prepare your Excel file:
   - The Excel file must have a column named `_id` with the submission IDs to update.
   - Save the file as `_id.xlsx` or provide a custom path during execution.

2. Run the script:
   ```bash
   python update_status.py
   ```

3. The script updates the submissions and prints the results to the console.

### Customizing Input
- **Excel File**: Change the `EXCEL_FILE` variable in the script to the path of your Excel file.
- **Validation Status**: Set the `VALIDATION_STATUS` variable in the script to one of the following:
  - `validation_status_approved`
  - `validation_status_not_approved`
  - `validation_status_on_hold`

### Example
Given an Excel file `_id.xlsx` with the following content:

| _id       |
|-----------|
| 123       |
| 456       |
| 789       |

To mark these submissions as `validation_status_not_approved`:

1. Set `VALIDATION_STATUS` to `validation_status_not_approved`.
2. Run:
   ```bash
   python update_status.py
   ```

The output will indicate whether each update was successful.

## Notes
- Ensure your API token has sufficient permissions to update submissions.
- Test the script with a small dataset before using it in production.



