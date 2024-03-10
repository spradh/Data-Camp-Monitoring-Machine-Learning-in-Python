#1
reference, analysis, analysis_gt = nannyml.load_us_census_ma_employment_data()

# Initialize the CBPE algorithm
cbpe = nannyml.CBPE(
    y_pred_proba='predicted_probability',
    y_pred='prediction',
    y_true='employed',
    metrics = ['roc_auc', 'accuracy'],
    problem_type = 'classification_binary',
    chunk_size = 5000,
)

cbpe = cbpe.fit(reference)
estimated_results = cbpe.estimate(analysis)
estimated_results.plot().show()


#2
reference, analysis, analysis_gt = nannyml.load_us_census_ma_employment_data()

# Initialize the CBPE algorithm
cbpe = nannyml.CBPE(
    y_pred_proba='predicted_probability',
    y_pred='prediction',
    y_true='employed',
    metrics = ['roc_auc', 'accuracy', 'f1'],
    problem_type = 'classification_binary',
	chunk_number = 8,
)

cbpe = cbpe.fit(reference)
estimated_results = cbpe.estimate(analysis)
estimated_results.plot().show()
