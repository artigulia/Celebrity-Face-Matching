# storing the path of all images ina  list

import os
import pickle

actors = os.listdir('Dataset')
filenames = []

# Iterate over the directories in the specified path
for actor in actors:
    # Exclude the .DS_Store file
    if actor != '.DS_Store':
        # Join the directory and actor name
        for file in os.listdir(os.path.join('Dataset', actor)):
            filenames.append(os.path.join('Dataset', actor, file))

# Dumping all files in binary format
pickle.dump(filenames, open('filenames.pkl','wb'))