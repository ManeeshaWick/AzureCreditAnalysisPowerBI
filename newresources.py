import pandas as pd
import gdown
from datetime import datetime, timedelta

# Google Drive CSV file link
google_drive_link = "https://drive.google.com/uc?id=1OyTT1xFxsrwhtqtZAM8VQ6RQqdHUGYFM"

# File path where the downloaded CSV will be saved
output_file = "data.csv"

# Download the file
gdown.download(google_drive_link, output_file, quiet=False)

# Read the downloaded CSV into a pandas DataFrame
data = pd.read_csv(output_file)

# Get the current month and previous two months
today = datetime.today()
current_month = today.month
previous_month_1 = (today.month - 1) % 12
previous_month_2 = (today.month - 2) % 12

# Calculate the first day of the current and previous two months
first_day_of_current_month = today.replace(day=1)
first_day_of_previous_month_1 = (first_day_of_current_month - timedelta(days=first_day_of_current_month.day)).replace(day=1)
first_day_of_previous_month_2 = (first_day_of_previous_month_1 - timedelta(days=first_day_of_previous_month_1.day)).replace(day=1)

# Filter data for the current and previous two months
filtered_current_month = data[pd.to_datetime(data['Date']) >= first_day_of_current_month]
filtered_previous_month_1 = data[(pd.to_datetime(data['Date']) >= first_day_of_previous_month_1) & (pd.to_datetime(data['Date']) < first_day_of_current_month)]
filtered_previous_month_2 = data[(pd.to_datetime(data['Date']) >= first_day_of_previous_month_2) & (pd.to_datetime(data['Date']) < first_day_of_previous_month_1)]

# Extract ResourceGUIDs for each period
current_month_resource_guids = set(filtered_current_month['ResourceGuid'])
previous_month_1_resource_guids = set(filtered_previous_month_1['ResourceGuid'])
previous_month_2_resource_guids = set(filtered_previous_month_2['ResourceGuid'])

# Find new ResourceGUIDs created in the current month compared to the previous two months
new_resource_guids = current_month_resource_guids - (previous_month_1_resource_guids | previous_month_2_resource_guids)

# Display new ResourceGUIDs
if new_resource_guids:    
    print(new_resource_guids)