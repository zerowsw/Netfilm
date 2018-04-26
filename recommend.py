import sqlite3
import numpy as np
import random as rd
import math

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
# c.execute('''
# 	select
# 	from rate, movie
# 	where rate.movie_id = movie.movie_id
# 	''')
rate_data = list(c.execute("select * from application_rate"))
sample_rate_data = rd.sample(rate_data,2000)

# print(rate_data)

movie_audience_dict = {}
movie_proj_dict = {}
movie_anti_proj_dict = {}
for instance in sample_rate_data:
    # instance in format 41084(id)|294()|36401(movie_id)|4.0(rate)|1138983041(timestamp)
    # instance[0]:id  instance[1]:user_id  instance[2]:movie_id
    movie_id = instance[2]
    user_id = instance[1]

    if movie_id not in movie_anti_proj_dict:
        movie_proj_dict[len(movie_proj_dict)] = movie_id
        movie_anti_proj_dict[movie_id] = len(movie_anti_proj_dict)
        # movie_anti_proj_dict2[movie_id] = len(movie_anti_proj_dict)

    if movie_id in movie_audience_dict:
        movie_audience_dict[movie_id].add(user_id)
    else:
        movie_audience_dict[movie_id] = set()
        movie_audience_dict[movie_id].add(user_id)

print("proj",len(movie_proj_dict),movie_proj_dict)
print("anti_proj",len(movie_anti_proj_dict),movie_anti_proj_dict)
co_occur = np.zeros((len(movie_proj_dict),len(movie_proj_dict)))
# print(len(co_occur),co_occur)

for id1 in movie_audience_dict:
    for id2 in movie_audience_dict:
        index1 = movie_anti_proj_dict[id1]
        index2 = movie_anti_proj_dict[id2]
        co_occur[index1][index2] = co_occur[index2][index1] = len(movie_audience_dict[id1]&movie_audience_dict[id2])

np_cooccur = np.asarray(co_occur)
for i in range(0,np_cooccur.shape[0]):
    np_cooccur /= sum(np_cooccur[1])






