#1
# Define analyzed column
analyzed_column = ['lead_time']

# Intialize sum values calculator
sum_calc = nannyml.SummaryStatsSumCalculator(
    column_names=analyzed_column, 
    chunk_period='m', 
    timestamp_column_name='timestamp'
)

# Fit, calculate and plot the results
sum_calc.fit(reference)
sum_calc_res = sum_calc.calculate(analysis)
sum_calc_res.plot().show()



#2

# Define analyzed column
analyzed_column = ['lead_time']

# Intialize median values calculator
med_calc = nannyml.SummaryStatsMedianCalculator(
    column_names=analyzed_column, 
    chunk_period='m', 
    timestamp_column_name='timestamp'
)

# Fit, calculate and plot the results
med_calc.fit(reference)
med_calc_res = med_calc.calculate(analysis)
med_calc_res.filter(period='analysis').plot().show()


#3

# Define analyzed column
analyzed_column = ['lead_time']

# Intialize standard deviation values calculator
std_calc = nannyml.SummaryStatsStdCalculator(
    column_names=analyzed_column, 
    chunk_period='m', 
    timestamp_column_name='timestamp'
)

# Fit, calculate and plot the results
std_calc.fit(reference)
std_calc_res = std_calc.calculate(analysis)
std_calc_res.filter(period="analysis").plot().show()
