import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the Excel file
file_path = 'Usage Report Raw Data.xlsx'  # Replace with your file path
xls = pd.ExcelFile(file_path)

# Step 2: Load the data from the first sheet
data = pd.read_excel(xls, 'Sheet1')

# Step 3: Convert 'Start Date Time' to datetime and extract the day of the week
data['Start Date Time'] = pd.to_datetime(data['Start Date Time'])
data['Day of Week'] = data['Start Date Time'].dt.day_name()

# Step 4: Group by 'Day of Week' and count the occurrences to find the busiest days
busiest_days = data['Day of Week'].value_counts().sort_index()

# Step 5: Plot the data in a bar chart
plt.figure(figsize=(10, 6))
busiest_days.plot(kind='bar', color='skyblue')
plt.title('Busiest Days of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Records')
plt.xticks(rotation=45)
plt.show()
