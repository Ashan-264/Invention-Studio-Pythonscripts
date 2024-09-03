import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the Excel file
file_path = 'Usage Report Raw Data.xlsx'  # Replace with your file path
xls = pd.ExcelFile(file_path)

# Step 2: Load the data from the first sheet
data = pd.read_excel(xls, 'Sheet1')

# Step 3: Convert 'Start Date Time' to datetime
data['Start Date Time'] = pd.to_datetime(data['Start Date Time'])

# Step 4: Define the date ranges
date_ranges = [
    ('2023-08-29', '2023-12-15'),
    ('2024-01-16', '2024-05-15')
]

# Step 5: Function to filter data and create bar graph
def plot_busiest_days(data, start_date, end_date, title):
    # Filter data within the specified date range
    filtered_data = data[(data['Start Date Time'] >= start_date) & (data['Start Date Time'] <= end_date)]
    
    # Extract the day of the week
    filtered_data['Day of Week'] = filtered_data['Start Date Time'].dt.day_name()
    
    # Group by 'Day of Week' and count the occurrences to find the busiest days
    busiest_days = filtered_data['Day of Week'].value_counts().sort_index()
    
    # Plot the data in a bar chart
    plt.figure(figsize=(10, 6))
    bars = busiest_days.plot(kind='bar', color='skyblue')
    
    # Annotate each bar with the count value
    for index, value in enumerate(busiest_days):
        plt.text(index, value + 10, str(value), ha='center', va='bottom')
    
    plt.title(f'Busiest Days of the Week ({title})')
    plt.xlabel('Day of the Week')
    plt.ylabel('Number of Records')
    plt.xticks(rotation=45)
    plt.show()

# Step 6: Generate the two bar graphs
#plot_busiest_days(data, '2023-08-29', '2023-12-15', 'August 29 - December 15')
plot_busiest_days(data, '2024-01-16', '2024-05-15', 'January 16 - May 15')
