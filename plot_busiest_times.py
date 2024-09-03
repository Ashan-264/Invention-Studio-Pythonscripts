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

# Step 5: Function to filter data and create line chart for each weekday
def plot_busiest_times_for_weekday(data, start_date, end_date, title):
    # Filter data within the specified date range
    filtered_data = data[(data['Start Date Time'] >= start_date) & (data['Start Date Time'] <= end_date)]
    
    # Further filter data for weekdays (Monday to Friday)
    filtered_data = filtered_data[filtered_data['Start Date Time'].dt.weekday < 5]  # 0 = Monday, 4 = Friday
    
    # Filter data to include only records between 11 AM and 5 PM
    filtered_data = filtered_data[(filtered_data['Start Date Time'].dt.hour >= 11) & 
                                  (filtered_data['Start Date Time'].dt.hour < 17)]
    
    # Define the mapping of weekday names to numbers
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    
    for i, weekday in enumerate(weekdays):
        # Filter data for the specific weekday
        weekday_data = filtered_data[filtered_data['Start Date Time'].dt.weekday == i]
        
        # Extract the hour and date for grouping
        weekday_data['Hour'] = weekday_data['Start Date Time'].dt.hour
        weekday_data['Date'] = weekday_data['Start Date Time'].dt.date
        
        # Group by 'Date' and 'Hour' and count the occurrences to find the busiest times
        busiest_times = weekday_data.groupby(['Date', 'Hour']).size().unstack(fill_value=0)
        
        # Plot the data in a line chart
        plt.figure(figsize=(14, 8))
        for hour in busiest_times.columns:
            plt.plot(busiest_times.index, busiest_times[hour], marker='o', label=f'{hour}:00')

        plt.title(f'Busiest Times on {weekday} ({title})')
        plt.xlabel('Date')
        plt.ylabel('Number of Records')
        plt.xticks(rotation=45)
        plt.legend(title="Hour of Day")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

# Step 6: Generate the line charts for the specified date range
plot_busiest_times_for_weekday(data, '2023-08-22', '2024-05-15', 'August 22 2023 - May 15 2024')
