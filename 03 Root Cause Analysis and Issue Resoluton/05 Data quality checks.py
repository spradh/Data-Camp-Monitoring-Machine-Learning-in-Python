#1
# Define analyzed columns
selected_columns = ['country', 'lead_time', 'parking_spaces', 'hotel']

# Intialize missing values calculator
ms_calc = nannyml.MissingValuesCalculator(
    column_names=selected_columns,
    timestamp_column_name='timestamp'
)

# Fit, calculate and plot the results
ms_calc.fit(reference)
ms_results = ms_calc.calculate(analysis)
ms_results.plot().show()


#2
# Define analyzed categorical columns
categorical_columns = ['country', 'hotel']

# Intialize unseen values calculator
us_calc = nannyml.UnseenValuesCalculator(
  	column_names=categorical_columns, 
  	chunk_period='m', 
  	timestamp_column_name='timestamp'
)

# Fit, calculate and plot the results
us_calc.fit(reference)
us_results = us_calc.calculate(analysis)
us_results.filter(period='analysis').plot().show()
