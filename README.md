# PCA 
Typically in an unsupervised setting, a minor percentage of datapoints are assumed to outliers. Principal Component Analysis (PCA) uses a cluster method to detect an anomaly, assumes
the inliers (normal datapoints) belong to large and dense clustersand the outliers/anomalies belong to either smaller and sparse clusters or none. The algorithm PCA determines what constitutes
a normal class. 
Considering time-series data (refer to the notebook) and assuming 1% outliers in the dataset, here's the result of PCA (red points are anomalies in the dataset).
 
<img width="202" alt="mm" src="https://github.com/user-attachments/assets/a6f9baae-dfc6-4eef-a6e6-5f1b11da95a0">


