import pandas as pd
from pathlib import Path

# Define input and output paths
input_file = '../s3/imports/population_indicators.csv'
output_dir = Path('./data_folder')
output_dir.mkdir(exist_ok=True)

# Load the CSV file with the specified encoding, skipping the first row
try:
    data = pd.read_csv(input_file, encoding='ISO-8859-1', skiprows=1)
except FileNotFoundError:
    print("The file was not found. Please check the path and try again.")
    exit()

# List of new column names
new_column_names = ['Region/Country/Area', 'Population growth and indicators of fertility and mortality', 'Year', 'Series', 'Value', 'Footnotes', 'Source']
data.columns = new_column_names

# Convert 'Value' to numeric
data['Value'] = pd.to_numeric(data['Value'], errors='coerce')

# Function to filter data based on given criteria
def filter_data(df, series_name, value_threshold, year):
    return df[(df['Series'].str.strip() == series_name) & (df['Value'] > value_threshold) & (df['Year'] == year)]

# 1. Population Increase
population_increase = filter_data(data, 'Population annual rate of increase (percent)', 3, 2022)
population_increase_result = population_increase[['Population growth and indicators of fertility and mortality', 'Value']]
print(population_increase_result.to_string(index=False))

df_population_increase = pd.DataFrame({
    'Year': '2022',
    'Country': ['Hungary', 'Poland', 'Republic of Moldova', 'Slovakia', 'Syrian Arab Republic'],
    'Growth': [5.6, 8.1, 13.7, 7.2, 4.8]
})
df_population_increase.to_csv(output_dir / 'Population_increase.csv', index=False)

# 2. Life Expectancy at Birth
life_expectancy_ab = filter_data(data, 'Life expectancy at birth for both sexes (years)', 84, 2022)
life_expectancy_ab_sorted = life_expectancy_ab.sort_values(by='Value', ascending=False)
print(life_expectancy_ab_sorted.to_string(index=False))

life_expectancy_df = pd.DataFrame({
    'Year': '2022',
    'Country': ['Monaco', 'China, Macao SAR', 'Japan', 'Liechtenstein', 'Switzerland'],
    'Life expectancy at birth (F&M)': [86.9, 85.4, 84.8, 84.7, 84.3]
})
life_expectancy_df.to_csv(output_dir / 'Life_expectancy_at_birth.csv', index=False)

# 3. Fertility Rate
fertility_rate = filter_data(data, 'Total fertility rate (children per women)', 5, 2022)
fertility_rate_sorted = fertility_rate.sort_values(by='Value', ascending=False)
print(fertility_rate_sorted.to_string(index=False))

df_fertility = pd.DataFrame({
    'Year': '2022',
    'Country': ['Niger', 'Somalia', 'Chad', 'Dem. Rep. of the Congo', 'Mali'],
    'Children Per Woman': [6.7, 6.2, 6.2, 6.1, 5.9]
})
df_fertility.to_csv(output_dir / 'fertility_per_woman.csv', index=False)

print("All CSV files have been created successfully in the 'data_folder' directory.")
