# PCA 
Typically in unsupervised learning, a minor percentage of datapoints are assumed as outliers. Principal Component Analysis (PCA) uses a cluster method to detect an anomaly, assumes
the inliers (normal datapoints) belong to large and dense clusters and the outliers/anomalies belong to either smaller and sparse clusters or none. The algorithm PCA determines what constitutes
a normal class. 


Considering time-series data (refer to csv file and notebook) and assuming 1% outliers in the dataset, here's the result of PCA (red points are anomalies).
 
<img width="202" alt="mm" src="https://github.com/user-attachments/assets/a6f9baae-dfc6-4eef-a6e6-5f1b11da95a0">


Learn more about PCA from **Chapter 3** of my book "A handbook of mathematical models with python". 

<img width="173" alt="mm" src="https://github.com/user-attachments/assets/a41c6d0d-de7b-4767-a4a0-488593c606f6">

Buy at Amazon: https://a.co/d/2JY2rdj

Among other anomaly detection methods in an unsupervised setting, there is Isolation Forest. Find a demo of this algorithm applied on time-series data here:

https://www.kaggle.com/code/ranja7/timeseries-anomaly-detection-isolation-forest

In general, evaluating an unsupervised learning method is hard. Yet, a few known metrics have been discussed here: 
https://ranjas.substack.com/p/exploring-metrics-in-unsupervised

Apart from PCA, in matrix factorization problems we come across methods like Independent Component Analysis (ICA), factor analysis. An overview of all of them can be found at scikit-learn's page: 

https://scikit-learn.org/stable/modules/decomposition.html


