# Create standard deviation thresholds
stdt = StandardDeviationThreshold(std_lower_multiplier=2, std_upper_multiplier=1)

# Define feature columns
feature_column_names = ['country', 'lead_time', 'parking_spaces', 'hotel']

# Intialize, fit, and show results of multivariate drift calculator
mv_calc = nannyml.DataReconstructionDriftCalculator(
    column_names=feature_column_names,
	threshold = stdt,
    timestamp_column_name='timestamp',
    chunk_period='m')
mv_calc.fit(reference)
mv_results = mv_calc.calculate(analysis)
mv_results.filter(period='analysis').compare(perf_results).plot().show()
