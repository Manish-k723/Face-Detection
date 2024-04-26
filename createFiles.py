import os
import pickle

actors = os.listdir("ActorsFaceData")
filenames = []

for actor in actors:
    for file in os.listdir(os.path.join('ActorsFaceData', actor)):
        filenames.append(os.path.join('ActorsFaceData', actor, file))

pickle.dump(filenames, open("actors.pkl", "wb"))
