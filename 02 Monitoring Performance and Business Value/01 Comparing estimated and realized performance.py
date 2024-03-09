# Intialize the calculator
calculator = nannyml.PerformanceCalculator(
    y_true='tip_amount',
    y_pred='y_pred',
    chunk_period='d',
  	metrics=['mae'],
    timestamp_column_name='lpep_pickup_datetime',
    problem_type='regression')

# Fit the calculator
calculator.fit(reference)
realized_results = calculator.calculate(analysis)

# Show comparison plot for realized and estimated performance
realized_results.compare(estimated_results).plot().show()
