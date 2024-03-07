#1

# Load the dataset
dataset_name = "green_taxi_dataset.csv"
data = pd.read_csv(dataset_name)
data.head()


#2
# Load the dataset
dataset_name = "green_taxi_dataset.csv"
data = pd.read_csv(dataset_name)
features = ['lpep_pickup_datetime', 'PULocationID', 'DOLocationID', 'trip_distance', 'fare_amount', 'pickup_time']
target = 'tip_amount'

# Split the training data
X_train = data.loc[data['partition'] == "train", features]
y_train = data.loc[data['partition'] == "train", target]

# Split the test data
X_test = data.loc[data['partition'] == "test", features]
y_test = data.loc[data['partition'] == "test", target]

# Split the prod data
X_prod = data.loc[data['partition'] == "prod", features]
y_prod = data.loc[data['partition'] == "prod", target]
