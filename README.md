
# 📚 Studio Usage Data Analysis Project

This repository showcases a data analysis project focused on understanding and visualizing patterns in studio usage. The project involves analyzing time-based data, identifying peak usage periods, and presenting insights through a series of visualizations. The scripts are designed to work with data from specific time ranges and provide insights into user behavior and resource utilization.

## 📝 Project Description

The goal of this project is to provide a clear understanding of how a studio is utilized over time. By analyzing data such as user activity, busiest hours, and 3D printer usage, we aim to uncover trends that can inform better resource allocation and scheduling decisions.

### Key Features
- **Detailed Time Analysis**: Break down usage data by minute-level intervals to identify the busiest times.
- **Day-by-Day Breakdown**: Analyze which days of the week see the most activity.
- **3D Printer Usage**: Track the daily utilization of 3D printers, helping to plan maintenance and optimize usage.
- **Programming Language Insights**: Understand which programming languages are most popular in the studio environment.

## 📊 Scripts Overview

- **minute_level_plot.py**: Generates line charts showing activity levels at 10-minute intervals throughout weekdays.
- **plot_busiest_times.py**: Visualizes activity for each day of the week, focusing on specific time slots.
- **plot_language_stats.py**: Displays the distribution of programming language usage through a clean bar chart.
- **plot_total_busy_times.py**: Analyzes and visualizes the total busy hours across weekdays.
- **Studio busy hours script.py**: Highlights which days of the week have the highest user activity.
- **Studio Users per date.py**: Plots total daily user hours for specific date ranges.
- **3DprinterTotalUsageHours.py**: Summarizes daily 3D printer usage to identify peak usage days.
- **busiest_days.py**: Generates bar charts to show which days have the highest activity during specified periods.

## 📂 Data Requirements

This project uses time-based data stored in Excel or CSV files, including:
- **Excel File**: `Usage Report Raw Data.xlsx` for most scripts.
- **CSV File**: Required for the `3DprinterTotalUsageHours.py` script.
- Data columns include:
  - `Start Date Time` and `End Date Time` for analysis over time.
  - `Real print time (h)` for 3D printer-specific analysis.

## 🚀 Getting Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/repo-name.git
   cd repo-name
Install Dependencies: Ensure you have Python 3 installed, then run:

bash
Copy code
pip install pandas matplotlib
Prepare Data Files:

Place your Usage Report Raw Data.xlsx or CSV file in the project directory.
Update the file_path variable in each script if the file name or path differs.
Run the Analysis Scripts: Use the following command to execute any script:

bash
Copy code
python script_name.py
Replace script_name.py with the name of the script you want to run.

## 📈 Visualization Examples
### 📅 Busiest Days of the Week
Understand which days of the week have the most activity:



### ⏲️ 3D Printer Usage Over Time
Track daily 3D printer usage to optimize scheduling:



### 🔢 Programming Language Stats
Analyze which programming languages are most used in the studio:



## 📋 Insights & Learnings
This project reveals:

Peak Usage Hours: Identifying times when resources are most in demand.
Weekly Trends: Spotting days with consistent high or low usage to guide staffing and operational decisions.
Resource Optimization: Insights into when 3D printers and other resources are most used, helping to minimize downtime.

## 🤝 Contributing
Contributions are welcome! If you have suggestions for new analysis methods or improvements, feel free to open an issue or submit a pull request.
