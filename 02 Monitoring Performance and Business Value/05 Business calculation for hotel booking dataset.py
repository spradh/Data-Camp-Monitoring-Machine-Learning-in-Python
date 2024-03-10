# Custom business value thresholds
ct = ConstantThreshold(lower=0, upper=150000)
# Intialize the performance calculator
calc = PerformanceCalculator(problem_type='classification_binary',
			y_pred_proba='y_pred_proba',
  			timestamp_column_name="timestamp", 		
  			y_pred='y_pred',
  			y_true='is_canceled',
            chunk_period='m',
  			metrics=['business_value','roc_auc'],
  			business_value_matrix = [[0, -100],[-200, 1500]],
  			thresholds={'business_value': ct},
			normalize_business_value=None)  
calc = calc.fit(reference)
calc_res = calc.calculate(analysis)
calc_res.filter(period='analysis').plot().show()
