import pandas as pd

# Read the cleaned CSV
df = pd.read_csv('./data_folder/processed_data_2022.csv')

# Extract unique values for dimension tables
unique_countries = df['Population growth and indicators of fertility and mortality'].unique()
unique_series = df['Series'].unique()
unique_years = df['Year'].unique()

# Print unique countries to check if the names are correct
print("Unique Countries:", unique_countries)

# Create DataFrame for Dim_Country
df_dim_country = pd.DataFrame({
    'Country_ID': range(1, len(unique_countries) + 1),  # Generate sequential IDs starting from 1
    'Country_Name': unique_countries
})

# Check the Dim_Country DataFrame to ensure the mapping is correct
print("Dim_Country DataFrame:")
print(df_dim_country)

# Create DataFrame for Dim_Series
df_dim_series = pd.DataFrame({
    'Series_ID': range(1, len(unique_series) + 1),  # Generate sequential IDs starting from 1
    'Series_Name': unique_series,
    'Description': [''] * len(unique_series)  # Optional: Add a description field
})

# Create DataFrame for Dim_Time
df_dim_time = pd.DataFrame({
    'Year_ID': range(1, len(unique_years) + 1),  # Generate sequential IDs starting from 1
    'Year': unique_years
})

# Map Country_Name, Series_Name, and Year to IDs in the original DataFrame
country_id_map = df_dim_country.set_index('Country_Name')['Country_ID'].to_dict()
series_id_map = df_dim_series.set_index('Series_Name')['Series_ID'].to_dict()
year_id_map = df_dim_time.set_index('Year')['Year_ID'].to_dict()

df['Country_ID'] = df['Population growth and indicators of fertility and mortality'].map(country_id_map)
df['Series_ID'] = df['Series'].map(series_id_map)
df['Year_ID'] = df['Year'].map(year_id_map)

# Check the mapping
print(df[['Population growth and indicators of fertility and mortality', 'Country_ID', 'Series', 'Series_ID', 'Year', 'Year_ID']].head())

# Create the Fact Table
df_fact_health_indicators = df[['Country_ID', 'Year_ID', 'Series_ID', 'Value']].copy()

# Drop any NaN values in 'Value' if they exist
df_fact_health_indicators.dropna(subset=['Value'], inplace=True)

# Check the fact table (optional)
print(df_fact_health_indicators.head())

# Define output directory
output_dir = './data_folder/'

# Save dimension tables to CSV
df_dim_country.to_csv(output_dir + 'Dim_Country.csv', index=False)
df_dim_series.to_csv(output_dir + 'Dim_Series.csv', index=False)
df_dim_time.to_csv(output_dir + 'Dim_Time.csv', index=False)

# Save fact table to CSV
df_fact_health_indicators.to_csv(output_dir + 'Fact_HealthIndicators.csv', index=False)

print("CSV files for each table have been created successfully.")
