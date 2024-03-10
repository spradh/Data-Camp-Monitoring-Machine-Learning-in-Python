# Filter estimated results for the roc_auc metric and convert them to a dataframe
display(estimated_results.filter(metrics=['roc_auc']).to_df())

# Filter estimated results for the reference period and convert them to a dataframe
display(estimated_results.filter(period='reference').to_df())

# Filter the estimated results for the accuracy metric
display(estimated_results.filter(metrics=['accuracy']).plot().show())

# Filter the estimated results for the analysis period, as well as for accuracy and roc_auc metrics
display(estimated_results.filter(period='analysis', metrics=['accuracy', 'roc_auc']).plot().show())
