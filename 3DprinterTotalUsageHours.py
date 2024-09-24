import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_name = 'report_get_audit_report_for_datatable_20230904_20240427.csv'
df = pd.read_csv(file_name)

# Remove timezone information by replacing "EST" and "EDT" with an empty string
df['Date/Time'] = df['Date/Time'].str.replace(r'\s*\b(EST|EDT)\b', '', regex=True)

# Convert 'Date/Time' to datetime format without timezone information
df['Date/Time'] = pd.to_datetime(df['Date/Time'], errors='coerce')

# Extract the date (without time) for aggregation
df['Date'] = df['Date/Time'].dt.date

# Filter the data for the entire date range
start_date = pd.to_datetime('2024-01-15').date()
end_date = pd.to_datetime('2024-04-27').date()
date_range_mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
filtered_df = df[date_range_mask]

# Aggregate the total print time by date within the specified range
daily_usage = filtered_df.groupby('Date')['Real print time (h)'].sum().reset_index()

# Force inclusion of all dates even if no data, filling missing dates with 0
all_dates = pd.date_range(start=start_date, end=end_date).date
daily_usage = daily_usage.set_index('Date').reindex(all_dates, fill_value=0).reset_index()
daily_usage.columns = ['Date', 'Real print time (h)']

# Plot the data
plt.figure(figsize=(12, 6))
plt.plot(daily_usage['Date'], daily_usage['Real print time (h)'], linestyle='-', color='b')
plt.title('Total 3D Printer Usage Over Time (15th Jan 2024 - 27th April 2024)')
plt.xlabel('Date')
plt.ylabel('Total Print Time (Hours)')
plt.grid(True)
plt.xticks(rotation=45)

# Add vertical spans for the Fall 2023 sprints
# plt.axvspan(pd.to_datetime('2023-10-16'), pd.to_datetime('2023-10-16') + pd.Timedelta(days=7), alpha=0.3, color='green')
# plt.axvspan(pd.to_datetime('2023-10-30'), pd.to_datetime('2023-10-30') + pd.Timedelta(days=7), alpha=0.3, color='yellow')
# plt.axvspan(pd.to_datetime('2023-11-10'), pd.to_datetime('2023-11-10') - pd.Timedelta(days=5), alpha=0.3, color='red')

# Add vertical spans for the Spring 2024 sprints
plt.axvspan(pd.to_datetime('2024-02-19'), pd.to_datetime('2024-02-19') + pd.Timedelta(days=7), alpha=0.3, color='purple')
plt.axvspan(pd.to_datetime('2024-03-04'), pd.to_datetime('2024-03-04') + pd.Timedelta(days=7), alpha=0.3, color='orange')
plt.axvspan(pd.to_datetime('2024-04-01'), pd.to_datetime('2024-04-01') + pd.Timedelta(days=7), alpha=0.3, color='blue')
plt.axvspan(pd.to_datetime('2024-04-12'), pd.to_datetime('2024-04-12') - pd.Timedelta(days=5), alpha=0.3, color='pink')

plt.tight_layout()
plt.show()
