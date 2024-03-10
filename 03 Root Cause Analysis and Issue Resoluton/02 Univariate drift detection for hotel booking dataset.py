# Intialize the univariate drift calculator
uv_calc = nannyml.UnivariateDriftCalculator(
    column_names=feature_column_names,
    timestamp_column_name='timestamp',
    chunk_period='m',
    continuous_methods=['jensen_shannon', 'wasserstein'],
    categorical_methods=['l_infinity', 'chi2'],
)

# Plot the results
uv_calc.fit(reference)
uv_results = uv_calc.calculate(analysis)
uv_results.plot().show()
