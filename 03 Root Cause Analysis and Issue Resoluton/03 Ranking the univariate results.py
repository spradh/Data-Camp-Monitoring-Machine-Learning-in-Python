#1
# Initialize the alert count ranker
alert_count_ranker = nannyml.AlertCountRanker()
alert_count_ranked_features = alert_count_ranker.rank(
    uv_results.filter(methods=['wasserstein', 'l_infinity']))

display(alert_count_ranked_features)


#2

# Initialize the correlation ranker
correlation_ranker = nannyml.CorrelationRanker()
correlation_ranker.fit(perf_results.filter(period='reference'))

correlation_ranked_features = correlation_ranker.rank(
    uv_results.filter(methods=['wasserstein', 'l_infinity']),
    perf_results)
display(correlation_ranked_features)
