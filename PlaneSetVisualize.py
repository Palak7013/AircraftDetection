# Visualization of DataSet
import json 
import glob
import shutil
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.image as mimg
from pathlib import Path
from os import listdir, makedirs, getcwd, remove
import pandas as pd
import os
from os.path import isfile, join, abspath, exists, isdir, expanduser

#%matplotlib qt


input_path = Path("Aircraft/planesnet")
planes_path = input_path


planes = []

all_planes = os.listdir(planes_path)
    # Add them to the list
for ac in all_planes:
    planes.append((ac[0],str(planes_path)+"/"+str(ac)))

# Build a dataframe        
planes = pd.DataFrame(data=planes, columns=['label','image_path'], index=None)
planes.sample(5)


print("Total number of planes images in the dataset: ", len(planes))
ac_count = planes['label'].value_counts()
plt.figure(figsize=(12,8))
sns.barplot(x=ac_count.index, y=ac_count.values)
plt.title("Images count for each category", fontsize=16)
plt.xlabel("Label", fontsize=14)
plt.ylabel("Count", fontsize=14)
plt.show()


random_samples = []

for item in planes.sample(20).iterrows():
    random_samples.append((item[1].label, item[1].image_path))

f, ax = plt.subplots(5,4, figsize=(20,20))
for i,sample in enumerate(random_samples):
    ax[i//4, i%4].imshow(mimg.imread(random_samples[i][1]))
    ax[i//4, i%4].set_title(random_samples[i][0])
    ax[i//4, i%4].axis('off')
plt.show()   