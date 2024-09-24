import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the Excel file
file_path = 'Usage Report Raw Data.xlsx'  # Replace with your file path
xls = pd.ExcelFile(file_path)

# Step 2: Load the data from the first sheet
data = pd.read_excel(xls, 'Sheet1')

# Step 3: Convert 'Start Date Time' and 'End Date Time' to datetime
data['Start Date Time'] = pd.to_datetime(data['Start Date Time'])
data['End Date Time'] = pd.to_datetime(data['End Date Time'])

# Step 4: Calculate the duration in hours for each user
data['User Hours'] = (data['End Date Time'] - data['Start Date Time']).dt.total_seconds() / 3600

# Step 5: Filter the data to include only records from August 15th to December 15th and exclude weekends
start_date = '2024-01-15'
end_date = '2024-04-25'
filtered_data = data[(data['Start Date Time'] >= start_date) & (data['Start Date Time'] <= end_date)]

# Filter out weekends (5 = Saturday, 6 = Sunday)
filtered_data = filtered_data[filtered_data['Start Date Time'].dt.weekday < 5]

# Step 6: Group by the exact date and calculate total user hours for each day
filtered_data['Date'] = filtered_data['Start Date Time'].dt.date
daily_usage_hours = filtered_data.groupby('Date')['User Hours'].sum().reset_index()

# Step 7: Plot the daily total user hours data as a line graph without markers
plt.figure(figsize=(12, 6))
plt.plot(daily_usage_hours['Date'], daily_usage_hours['User Hours'])  # Removed marker argument

# Step 8: Customize the plot
plt.title('Fall 2023 and Spring 2024 Total Studio User Hours by Day (Monday to Friday)')
plt.xlabel('Date')
plt.ylabel('Total User Hours')
plt.xticks(rotation=45)  # Rotate the x-axis labels for better readability
plt.grid(True)

# Add vertical spans for the Fall 2023 time periods
# plt.axvspan(pd.to_datetime('2023-10-16'), pd.to_datetime('2023-10-16') + pd.Timedelta(days=7), alpha=0.3, color='green')
# plt.axvspan(pd.to_datetime('2023-10-30'), pd.to_datetime('2023-10-30') + pd.Timedelta(days=7), alpha=0.3, color='green')
# plt.axvspan(pd.to_datetime('2023-11-10'), pd.to_datetime('2023-11-10') - pd.Timedelta(days=4), alpha=0.3, color='green')


# Add vertical spans for the Spring 2110 time periods
plt.axvspan(pd.to_datetime('2024-02-19'), pd.to_datetime('2024-02-19') + pd.Timedelta(days=7), alpha=0.3, color='green')
plt.axvspan(pd.to_datetime('2024-03-04'), pd.to_datetime('2024-03-04') + pd.Timedelta(days=7), alpha=0.3, color='green')
plt.axvspan(pd.to_datetime('2024-04-01'), pd.to_datetime('2024-04-01') + pd.Timedelta(days=7), alpha=0.3, color='green')
plt.axvspan(pd.to_datetime('2024-04-12'), pd.to_datetime('2024-04-12') - pd.Timedelta(days=1), alpha=0.3, color='green')

plt.tight_layout()

# Step 9: Show the plot
plt.show()
