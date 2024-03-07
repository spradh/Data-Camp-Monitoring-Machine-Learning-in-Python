#1
from lightgbm import LGBMRegressor

# Fit the model
model = LGBMRegressor(random_state=111, n_estimators=50, n_jobs=1)
model.fit(X_train, y_train)

# Make predictions
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

# Deploy the model
y_pred_prod = model.predict(X_prod)

#2
from lightgbm import LGBMRegressor

# Fit the model
model = LGBMRegressor(random_state=111, n_estimators=50, n_jobs=1)
model.fit(X_train, y_train)

# Get model's prediction on train, test, and production set
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)
y_pred_prod = model.predict(X_prod)

# Create reference and analysis set
reference = X_test.copy() # Copy test set features
reference['y_pred'] = y_pred_test # Add models predictions on test set
reference['tip_amount'] = y_test # Add labels(ground truth)
reference = reference.join(data['lpep_pickup_datetime']) # Add timestamp column

analysis = X_prod.copy() # Add production set features
analysis['y_pred'] = y_pred_prod # Add models predictions on production set
analysis = analysis.join(data['lpep_pickup_datetime']) # Add timestamp column
