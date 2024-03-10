# Import custom thresholds
from nannyml.thresholds import ConstantThreshold, StandardDeviationThreshold

# Initialize custom thresholds
stdt = StandardDeviationThreshold(
    std_lower_multiplier=2, 
    std_upper_multiplier=2
)
ct = ConstantThreshold(
    lower=.9, 
    upper=.98
)

# Initialize the CBPE algorithm
estimator = nannyml.CBPE(
    problem_type='classification_binary',
    y_pred_proba='predicted_probability',
    y_pred='prediction',
    y_true='employed',
    metrics=['roc_auc', 'accuracy', 'f1'],
    thresholds={'f1': ct, 'accuracy': stdt}
    )
