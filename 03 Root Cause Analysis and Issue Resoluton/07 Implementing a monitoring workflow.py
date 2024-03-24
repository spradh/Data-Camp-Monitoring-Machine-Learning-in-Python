#1

# Estimate the performance
estimator.fit(reference)
estimated_results = estimator.estimate(analysis)
estimated_results.plot().show()



#2

# Calculate multivariate drift
mv_calc = nannyml.DataReconstructionDriftCalculator(column_names=features, chunk_size=5000)
mv_calc.fit(reference)
mv_results = mv_calc.calculate(analysis)
mv_results.filter(period='analysis').compare(estimated_results).plot().show()

#3

# Calculate univariate drift
uv_calculator.fit(reference)
uv_results = uv_calculator.calculate(analysis)

# Check the most drifting features
alert_count_ranked_features = alert_count_ranker.rank(uv_results)
display(alert_count_ranked_features.head())

#4
#Larger population of younger individuals.
