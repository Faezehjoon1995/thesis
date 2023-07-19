# -*- coding: utf-8 -*-
"""clustering4 jshannon distance.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kiJ4Hl-rljCOK7lyDUn9KwU3cYAk0rTN

# **2 kMeans**
"""

#pip install joblib==1.1.0

pip install umap-learn

import pandas as pd

embeddings=pd.read_csv('w.txt', sep='\t', header=0,encoding='UTF-8')

print(embeddings[:121])

import umap
umap_embeddings = umap.UMAP(n_neighbors=15, n_components=5, metric='cosine').fit_transform(embeddings)
#کاهش بعد به 5---همسایه های محلی 15

#print(umap_embeddings)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

feature_columns = ['1','2','3'	,'4'	,'5'	,'6',	'7',	'8',	'9',	'10',	'11',	'12',	'13',	'14',	'15',	'16',	'17',
                   '18',	'19',	'20',	'21',	'22',	'23',	'24',	'25',	'26',	'27',	'28',	'29',	'30',	'31',	'32',	'33',
                   '34',	'35',	'36',	'37',	'38',	'39',	'40',	'41',	'42',	'43',	'44',	'45',	'46',	'47',	'48',	'49',
                   '50',	'51',	'52',	'53',	'54',	'55',	'56',	'57',	'58',	'59',	'60',	'61',	'62',	'63',	'64',	'65',
                   '66',	'67',	'68',	'69',	'70',	'71',	'72',	'73',	'74',	'75',	'76',	'77',	'78',	'79',	'80',	'81',
                   '82',	'83',	'84',	'85',	'86',	'87',	'88',	'89',	'90',	'91',	'92',	'93', '94',	'95',	'96',	'97',
                   '98',	'99',	'100',	'101'	,'102',	'103',	'104',	'105',	'106',	'107',	'108',	'109',	'110',
                   '111',	'112',	'113',	'114',	'115',	'116',	'117',	'118',	'119',	'120']

X = embeddings[feature_columns]

from sklearn.cluster import KMeans
from sklearn.metrics import davies_bouldin_score

#from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 4, max_iter = 300, random_state = 0)
kmeans.fit(X)

results = {}
import scipy.stats
import scipy.spatial
import numpy as np
from scipy.spatial import distance
import matplotlib.pyplot as plt
import pandas as pd
# Prepare data


for i in range(0,30):
  umap_data = umap.UMAP(n_neighbors=3, n_components=2, min_dist=0.0, metric='cosine').fit_transform(embeddings)
  result = pd.DataFrame(umap_data, columns=['x', 'y'])
  js_distance_scipy = scipy.spatial.distance.jensenshannon(result.x, result.y)
  print(js_distance_scipy)
  results.update({i: js_distance_scipy})
#result['labels'] = kmeans.labels_

plt.plot(list(results.keys()), list(results.values()))
plt.xlabel("k")
plt.ylabel("Jensen-Shannon Distance")
plt.show()

centers = kmeans.cluster_centers_
#print(centers)

kmeans.labels_

print(kmeans.labels_)

#from sklearn.metrics import davies_bouldin_score
db_index = davies_bouldin_score(umap_embeddings, kmeans.labels_)
print(db_index)

results = {}

for i in range(3,10):
    cluster = KMeans(n_clusters = i, max_iter = 300, random_state = 0).fit(umap_embeddings)
    umap_data = umap.UMAP(n_neighbors=2, n_components=2, min_dist=0.0, metric='cosine').fit_transform(embeddings)
    result = pd.DataFrame(umap_data, columns=['x', 'y'])
    result['labels'] = cluster.labels_
    db_index = davies_bouldin_score(umap_embeddings, cluster.labels_)
    print(db_index)
    results.update({i: db_index})

    #kmeans = KMeans(n_clusters=i, random_state=30)
   # labels= kmeans.fit_predict(umap_embeddings)
  #  db_index = davies_bouldin_score(umap_embeddings, cluster.labels_)
   # results.update({i: db_index})

plt.plot(list(results.keys()), list(results.values()))
plt.xlabel("k")
plt.ylabel("Davies-Bouldin")
plt.show()

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
# %matplotlib inline

results = {}

for i in range(3,10):
    cluster = KMeans(n_clusters = i, max_iter = 300, random_state = 0).fit(umap_embeddings)
   # cluster = hdbscan.HDBSCAN(min_cluster_size=i, metric='euclidean', cluster_selection_method='eom').fit(umap_embeddings)
    umap_data = umap.UMAP(n_neighbors=2, n_components=2, min_dist=0.0, metric='cosine').fit_transform(embeddings)
    result = pd.DataFrame(umap_data, columns=['x', 'y'])
    result['labels'] = cluster.labels_
    #db_index = davies_bouldin_score(umap_embeddings, cluster.labels_)
    silhouette = silhouette_score(umap_embeddings, cluster.labels_)
    print(silhouette)
    results.update({i: silhouette})

plt.plot(list(results.keys()), list(results.values()))
plt.xlabel("k")
plt.ylabel("Silhouette")
plt.show()

from sklearn import metrics

results = {}

for i in range(3,10):
    cluster = KMeans(n_clusters = i, max_iter = 300, random_state = 0).fit(umap_embeddings)
   # cluster = hdbscan.HDBSCAN(min_cluster_size=i, metric='euclidean', cluster_selection_method='eom').fit(umap_embeddings)
    umap_data = umap.UMAP(n_neighbors=2, n_components=2, min_dist=0.0, metric='cosine').fit_transform(embeddings)
    result = pd.DataFrame(umap_data, columns=['x', 'y'])
    result['labels'] = cluster.labels_
    #db_index = davies_bouldin_score(umap_embeddings, cluster.labels_)
    #silhouette = silhouette_score(umap_embeddings, cluster.labels_)
    CH = metrics.calinski_harabasz_score(umap_embeddings, cluster.labels_)
    print(CH)
    results.update({i: CH})

plt.plot(list(results.keys()), list(results.values()))
plt.xlabel("k")
plt.ylabel("Calinski Harabasz")
plt.show()

# Visualize clusters
fig, ax = plt.subplots(figsize=(10, 10))
outliers = result.loc[result.labels == -1, :]
clustered = result.loc[result.labels != -1, :]
plt.scatter(outliers.x, outliers.y, color='#BDBDBD', s=0.05)
plt.scatter(clustered.x, clustered.y, c=clustered.labels, s=0.05, cmap='hsv_r')
plt.colorbar()
plt.savefig('myfig.png')

sse = []
for K in range(1, 10):
    model = KMeans(n_clusters=K)
    model.fit(X)
    sse.append(model.inertia_)

sse = model.inertia_

print(sse)

import matplotlib.pyplot as plt
import pandas as pd
plt.plot(sse)
plt.xlabel("K ")
plt.ylabel("Elbow")
plt.show()

"""# **BEFORE UMAP**"""

embedd=list()

import pandas as pd

embedd=pd.read_csv('w.txt', sep='\t', header=0,encoding='UTF-8')

#print(embedd[:121])

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

feature_columns = ['1','2','3'	,'4'	,'5'	,'6',	'7',	'8',	'9',	'10',	'11',	'12',	'13',	'14',	'15',	'16',	'17',
                   '18',	'19',	'20',	'21',	'22',	'23',	'24',	'25',	'26',	'27',	'28',	'29',	'30',	'31',	'32',	'33',
                   '34',	'35',	'36',	'37',	'38',	'39',	'40',	'41',	'42',	'43',	'44',	'45',	'46',	'47',	'48',	'49',
                   '50',	'51',	'52',	'53',	'54',	'55',	'56',	'57',	'58',	'59',	'60',	'61',	'62',	'63',	'64',	'65',
                   '66',	'67',	'68',	'69',	'70',	'71',	'72',	'73',	'74',	'75',	'76',	'77',	'78',	'79',	'80',	'81',
                   '82',	'83',	'84',	'85',	'86',	'87',	'88',	'89',	'90',	'91',	'92',	'93', '94',	'95',	'96',	'97',
                   '98',	'99',	'100',	'101'	,'102',	'103',	'104',	'105',	'106',	'107',	'108',	'109',	'110',
                   '111',	'112',	'113',	'114',	'115',	'116',	'117',	'118',	'119',	'120']

Z = embedd[feature_columns]

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 4, max_iter = 300, random_state = 0)
kmeans.fit(Z)

centers = kmeans.cluster_centers_
#print(centers)

kmeans.labels_

from sklearn.metrics import davies_bouldin_score
db_index = davies_bouldin_score(embedd, kmeans.labels_)
print(db_index)

print(len(embedd))

print(len(kmeans.labels_))

#print(embedd)

import matplotlib.pyplot as plt
import pandas as pd
# Prepare data
##umap_data = umap.UMAP(n_neighbors=3, n_components=2, min_dist=0.0, metric='cosine').fit_transform(embeddings) #کاهش بعد به 2
result = pd.DataFrame(embedd, columns=['x', 'y'])
result['labels'] = kmeans.labels_

print(len(embedd))

print(len(kmeans.labels_))

print(kmeans.labels_)

from sklearn.metrics import davies_bouldin_score
db_index = davies_bouldin_score(embedd, kmeans.labels_)
print(db_index)

#import hdbscan
#cluster = hdbscan.HDBSCAN(min_cluster_size=5, metric='euclidean', cluster_selection_method='eom').fit(umap_embeddings)
#import matplotlib.pyplot as plt
#import pandas as pd
# Prepare data
#umap_data = umap.UMAP(n_neighbors=3, n_components=2, min_dist=0.0, metric='cosine').fit_transform(embeddings) #کاهش بعد به 2
#result = pd.DataFrame(umap_data, columns=['x', 'y'])
#result['labels'] = cluster.labels_

results = {}

for i in range(3,10):
    cluster = KMeans(n_clusters = i, max_iter = 300, random_state = 0).fit(embedd)
   # cluster = hdbscan.HDBSCAN(min_cluster_size=i, metric='euclidean', cluster_selection_method='eom').fit(umap_embeddings)
   # umap_data = umap.UMAP(n_neighbors=2, n_components=2, min_dist=0.0, metric='cosine').fit_transform(embedding)
    result = pd.DataFrame(embedd, columns=['x', 'y'])
    result['labels'] = cluster.labels_
    db_index = davies_bouldin_score(embedd, cluster.labels_)
    print(db_index)
    results.update({i: db_index})

    #kmeans = KMeans(n_clusters=i, random_state=30)
   # labels= kmeans.fit_predict(umap_embeddings)
  #  db_index = davies_bouldin_score(umap_embeddings, cluster.labels_)
   # results.update({i: db_index})

plt.plot(list(results.keys()), list(results.values()))
plt.xlabel("k")
plt.ylabel("Davies-Boulding Index")
plt.show()

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
# %matplotlib inline

results = {}

for i in range(3,10):
    cluster = KMeans(n_clusters = i, max_iter = 300, random_state = 0).fit(embedd)
   # cluster = hdbscan.HDBSCAN(min_cluster_size=i, metric='euclidean', cluster_selection_method='eom').fit(umap_embeddings)
  #  umap_data = umap.UMAP(n_neighbors=2, n_components=2, min_dist=0.0, metric='cosine').fit_transform(embeddings)
    result = pd.DataFrame(embedd, columns=['x', 'y'])
    result['labels'] = cluster.labels_
    #db_index = davies_bouldin_score(umap_embeddings, cluster.labels_)
    silhouette = silhouette_score(embedd, cluster.labels_)
    print(silhouette)
    results.update({i: silhouette})

plt.plot(list(results.keys()), list(results.values()))
plt.xlabel("k")
plt.ylabel("Silhouette")
plt.show()

from sklearn import metrics

results = {}

for i in range(3,10):
    cluster = KMeans(n_clusters = i, max_iter = 300, random_state = 0).fit(embedd)
   # cluster = hdbscan.HDBSCAN(min_cluster_size=i, metric='euclidean', cluster_selection_method='eom').fit(umap_embeddings)
   # umap_data = umap.UMAP(n_neighbors=2, n_components=2, min_dist=0.0, metric='cosine').fit_transform(embeddings)
    result = pd.DataFrame(embedd, columns=['x', 'y'])
    result['labels'] = cluster.labels_
    #db_index = davies_bouldin_score(umap_embeddings, cluster.labels_)
    #silhouette = silhouette_score(umap_embeddings, cluster.labels_)
    CH = metrics.calinski_harabasz_score(embedd, cluster.labels_)
    print(CH)
    results.update({i: CH})

plt.plot(list(results.keys()), list(results.values()))
plt.xlabel("k")
plt.ylabel("Calinski Harabasz")
plt.show()

# Visualize clusters
fig, ax = plt.subplots(figsize=(10, 10))
outliers = result.loc[result.labels == -1, :]
clustered = result.loc[result.labels != -1, :]
plt.scatter(outliers.x, outliers.y, color='#BDBDBD', s=0.05)
plt.scatter(clustered.x, clustered.y, c=clustered.labels, s=0.05, cmap='hsv_r')
plt.colorbar()
plt.savefig('myfig.png')

sse = model.inertia_

sse = []
for K in range(1, 10):
    model = KMeans(n_clusters=K)
    model.fit(Z)
    sse.append(model.inertia_)

print(sse)

import matplotlib.pyplot as plt
import pandas as pd
plt.plot(sse)
plt.xlabel("K ")
plt.ylabel("Elbow")
plt.show()

print(len(cluster.labels_))

print(cluster.labels_)