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

# Step 5: Function to filter data and create a line chart for each 10-minute interval
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
    
    # Create a complete time range for the x-axis labels
    time_range = pd.date_range("11:00", "17:50", freq="10min").time
    time_labels = [f'{t.hour}:{t.minute:02d}' for t in time_range]
    
    # Initialize a dictionary to hold the data for plotting
    weekday_data = {day: [0] * len(time_range) for day in weekdays}
    
    # Group the data into 10-minute intervals
    filtered_data = filtered_data.set_index('Start Date Time')
    filtered_data = filtered_data.resample('10min').size().reset_index(name='Count')
    filtered_data['Time'] = filtered_data['Start Date Time'].dt.time
    
    # Populate the dictionary with the total records for each 10-minute interval
    for i, weekday in enumerate(weekdays):
        day_data = filtered_data[filtered_data['Start Date Time'].dt.weekday == i]
        ten_minute_counts = day_data.groupby('Time')['Count'].sum()  # Sum to ensure a single value per interval
        
        # Fill in data for each 10-minute interval between 11:00 AM and 5:00 PM
        for idx, minute in enumerate(time_range):
            weekday_data[weekday][idx] = ten_minute_counts.get(minute, 0)  # Directly assign the summed value
    
    # Debugging: Check if all lists are flat and of the same length
    for day in weekdays:
        print(f"Day: {day}, Length of data: {len(weekday_data[day])}")
        print(f"Sample data for {day}: {weekday_data[day][:5]}...")  # Print the first few elements
        if len(weekday_data[day]) != len(time_labels):
            raise ValueError(f"Data length mismatch for {day}. Expected {len(time_labels)} but got {len(weekday_data[day])}.")
        if any(isinstance(i, list) for i in weekday_data[day]):
            raise ValueError(f"Data for {day} contains nested lists or sequences.")

    # Plot the data
    plt.figure(figsize=(14, 8))
    for weekday in weekdays:
        plt.plot(range(len(time_labels)), weekday_data[weekday], marker='o', label=weekday)
    
    plt.title(f'Busiest Times by Day of the Week ({title})')
    plt.xlabel('Time of Day (10-Minute Intervals)')
    plt.ylabel('Number of Records')
    plt.xticks(range(len(time_labels)), time_labels, rotation=45)
    plt.legend(title="Day of the Week")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Step 6: Generate the line chart for the specified date range
plot_busiest_times_by_day(data, '2024-01-16', '2024-05-01', 'Jan 16 2024 - May 05 2024')
