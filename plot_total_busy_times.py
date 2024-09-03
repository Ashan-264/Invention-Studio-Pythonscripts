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

# Step 5: Function to filter data and create a line chart for each time of day
def plot_busiest_times_by_day(data, start_date, end_date, title):
    # Filter data within the specified date range
    filtered_data = data[(data['Start Date Time'] >= start_date) & (data['Start Date Time'] <= end_date)]
    
    # Further filter data for weekdays (Monday to Friday)
    filtered_data = filtered_data[filtered_data['Start Date Time'].dt.weekday < 5]  # 0 = Monday, 4 = Friday
    
    # Filter data to include only records between 11 AM and 5 PM
    filtered_data = filtered_data[(filtered_data['Start Date Time'].dt.hour >= 11) & 
                                  (filtered_data['Start Date Time'].dt.hour < 18)]
    
    # Define the mapping of weekday names to numbers
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    
    # Initialize a dictionary to hold the data for plotting
    weekday_data = {day: [] for day in weekdays}
    
    # Populate the dictionary with the total records for each hour
    for i, weekday in enumerate(weekdays):
        day_data = filtered_data[filtered_data['Start Date Time'].dt.weekday == i]
        hourly_counts = day_data.groupby(day_data['Start Date Time'].dt.hour).size()
        
        # Ensure we have data for each hour between 11 and 16
        for hour in range(11, 18):
            weekday_data[weekday].append(hourly_counts.get(hour, 0))
    
    # Plot the data
    plt.figure(figsize=(14, 8))
    for weekday in weekdays:
        plt.plot(range(11, 18), weekday_data[weekday], marker='o', label=weekday)
    
    plt.title(f'Busiest Times by Day of the Week ({title})')
    plt.xlabel('Time of Day (Hour)')
    plt.ylabel('Number of Records')
    plt.xticks(range(11, 18), [f'{hour}:00' for hour in range(11, 18)])
    plt.legend(title="Day of the Week")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Step 6: Generate the line chart for the specified date range
plot_busiest_times_by_day(data, '2023-08-22', '2023-12-15', 'August 22 2023 - December 15 2023')
