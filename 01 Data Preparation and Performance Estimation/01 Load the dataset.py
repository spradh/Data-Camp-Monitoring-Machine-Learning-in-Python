# Import nannyml
import nannyml

# Load US Census Employment dataset
reference, analysis, analysis_gt = nannyml.load_us_census_ma_employment_data()

# Print head of the reference data
print(reference.head())

# Print head of the analysis data
print(analysis.head())
