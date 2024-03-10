# Filter and create drift plots
drift_results = uv_results.filter(
    period='analysis',
    column_names=['hotel', 'country']
    ).plot(kind='drift')

# Filter and create distribution plots
distribution_results = uv_results.filter(
    period='analysis',
    column_names=['hotel', 'country']
    ).plot(kind='distribution')

# Show the plots
drift_results.show()
distribution_results.show()
