import requests
import pandas as pd

# Define the Kobo API parameters
KF_URL = "https://[kpi]"  # Replace with your KoboToolbox URL
TOKEN = "your token here"  # Replace with your actual API token
ASSET_UID = "asset UID"  # Replace with your actual asset UID

# Define the Kobo API headers
HEADERS = {
    "Authorization": f"Token {TOKEN}",
    "Content-Type": "application/json"
}

# Function to bulk update validation statuses for multiple submissions
def bulk_update_validation_status(submission_ids, validation_status):
    BULK_UPDATE_URL = f"{KF_URL}/api/v2/assets/{ASSET_UID}/data/validation_statuses/"
    
    # Correct payload structure
    payload = {
        "payload": {  # Encapsulate data in a "payload" key
            "submission_ids": submission_ids,
            "validation_status.uid": validation_status
        }
    }
    
    print(f"Bulk updating submissions {submission_ids} with status {validation_status}...")
    response = requests.patch(BULK_UPDATE_URL, headers=HEADERS, json=payload)
    
    if response.status_code in [200, 204]:
        print(f"Successfully updated validation status for submissions: {submission_ids}")
        return True
    else:
        print(f"Failed to update validation statuses. Status: {response.status_code}, Response: {response.text}")
        return False

# Function to process submissions from an Excel file
def batch_update_from_excel(excel_file, validation_status):
    df = pd.read_excel(excel_file)
    
    if '_id' not in df.columns:
        print("Error: The Excel file must contain a column named '_id'.")
        return
    
    submission_ids = df['_id'].dropna().astype(int).tolist()
    if not submission_ids:
        print("No valid submission IDs found in the Excel file.")
        return
    
    # Perform a bulk update
    bulk_update_validation_status(submission_ids, validation_status)

# Main execution
if __name__ == "__main__":
    EXCEL_FILE = "_id.xlsx"  # Replace with your Excel file path
    VALIDATION_STATUS = "validation_status_not_approved"  # Replace with your desired status

    # Start the batch update process
    batch_update_from_excel(EXCEL_FILE, VALIDATION_STATUS)
