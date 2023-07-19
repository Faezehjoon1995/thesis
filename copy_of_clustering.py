# -*- coding: utf-8 -*-
"""Copy of clustering.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Pbo4DZwjAxN6KRC_56ylU2RY2mJYZEF5
"""

pip install hdbscan

pip install umap-learn

with open('w.txt') as f:
  lines = [line.rstrip('\n') for line in f]

embeddings=list()

import pandas as pd

embeddings=pd.read_csv('w.txt', sep='\t', header=0,encoding='UTF-8')

import umap
umap_embeddings = umap.UMAP(n_neighbors=2, n_components=2, metric='cosine').fit_transform(embeddings)

import hdbscan
cluster = hdbscan.HDBSCAN(min_cluster_size=3, metric='euclidean', cluster_selection_method='eom').fit(embeddings)

#fit(umap_embedings)

import matplotlib.pyplot as plt
import pandas as pd
# Prepare data
##umap_data = umap.UMAP(n_neighbors=3, n_components=2, min_dist=0.0, metric='cosine').fit_transform(embeddings) #کاهش بعد به 2
result = pd.DataFrame(embeddings, columns=['x', 'y'])
result['labels'] = cluster.labels_

# Visualize clusters
fig, ax = plt.subplots(figsize=(10, 10))
outliers = result.loc[result.labels == -1, :]
clustered = result.loc[result.labels != -1, :]
plt.scatter(outliers.x, outliers.y, color='#BDBDBD', s=0.05)
plt.scatter(clustered.x, clustered.y, c=clustered.labels, s=0.05, cmap='hsv_r')
plt.colorbar()
plt.savefig('myfig.png')

print(len(cluster.labels_))

print(cluster.labels_)