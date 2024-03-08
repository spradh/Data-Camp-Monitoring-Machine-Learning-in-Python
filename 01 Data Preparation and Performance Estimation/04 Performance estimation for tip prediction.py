estimator = nannyml.DLE(y_pred='y_pred',
    timestamp_column_name='lpep_pickup_datetime',
    feature_column_names=features,
    chunk_period='d',
    y_true='tip_amount',
    metrics=['mse'])

# Fit the reference data to the DLE algorithm
estimator.fit(reference)

# Estimate the performance on the analysis data
results = estimator.estimate(analysis)

# Plot and show the results
results.plot().show()
