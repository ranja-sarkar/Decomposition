#author: ranja.sarkar@gmail.com

import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
#from sklearn.ensemble import IsolationForest
#from sklearn.svm import OneClassSVM
import matplotlib.pyplot as plt

from warnings import simplefilter
simplefilter(action = 'ignore', category = FutureWarning)

# Return Series of distances between points and distances from the closest centroid
def getDistanceByPoint(data, model):
    distance = pd.Series()
    for i in range(0,len(data)):
        Xa = np.array(data.loc[i])
        Xb = model.cluster_centers_[model.labels_[i]-1]
        distance.at[i] = np.linalg.norm(Xa-Xb)
    return distance

df = pd.read_csv("ambient_temperature_system_failure.csv")
#print(df.info())

outliers_fraction = 0.01     #1% of data is assumed to have outlying points

# Change timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# "Int" timestamp to plot easily
df['time_epoch'] = (df['timestamp'].astype(np.int64)/100000000000).astype(np.int64)

# Change temperature to Celsius
df['value'] = (df['value'] - 32) * 5/9

# Plot the original data
df.plot(x = 'time_epoch', y = 'value')

# standardize features
data = df[['value', 'time_epoch']]
min_max_scaler = preprocessing.StandardScaler()
np_scaled = min_max_scaler.fit_transform(data)
data = pd.DataFrame(np_scaled)

# Reduce to 2 importants features, default 'auto' is too large
pca = PCA(n_components = 2)
data = pca.fit_transform(data)

# Standardize 2 new features
min_max_scaler = preprocessing.StandardScaler()
np_scaled = min_max_scaler.fit_transform(data)
data = pd.DataFrame(np_scaled)

# Calculate with different number of centroids to see the loss plot (elbow method)
n_cluster = range(1, 20)
kmeans = [KMeans(n_clusters = i, random_state = 42).fit(data) for i in n_cluster]

# Choose 15 centroids arbitrarily and add these data to the central dataframe
df['cluster'] = kmeans[14].predict(data)
df['principal_feature1'] = data[0]
df['principal_feature2'] = data[1]
df['cluster'].value_counts()

# bigger distances are considered as anomalies
distance = getDistanceByPoint(data, kmeans[14])
number_of_outliers = int(outliers_fraction*len(distance))
threshold = distance.nlargest(number_of_outliers).min()
df['anomaly'] = (distance >= threshold).astype(int)

fig, ax = plt.subplots()
a = df.loc[df['anomaly'] == 1, ['time_epoch', 'value']]
ax.plot(df['time_epoch'], df['value'], color='blue')
ax.scatter(a['time_epoch'],a['value'], color='red')
plt.show()
