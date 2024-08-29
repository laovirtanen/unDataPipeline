import pandas as pd

# Read the 'cleaned' CSV
df = pd.read_csv('./data_folder/processed_data_2022.csv')

different_countries = df['Population growth and indicators of fertility and mortality'].unique()
different_area_codes = df['Region/Country/Area'].unique()
print(len(different_countries))
print(len(different_area_codes))

different_series = df['Series'].unique()
print(different_series)

num_nan = df['Value'].isna().sum()
print(num_nan)

# No nan values

unique_sources = df['Source'].unique()
print(unique_sources)

