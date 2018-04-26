import sqlite3
import numpy as np
import random as rd

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
# c.execute('''
# 	select
# 	from rate, movie
# 	where rate.movie_id = movie.movie_id

# 	''')
rate_data = list(c.execute("select * from application_rate"))
sample_rate_data = rd.choice(rate_data,size = 2000)

print(rate_data)

movie_audience_dict = {}
movie_proj_dict = {}
for instance in sample_rate_data:
    # instance in format 41084(id)|294()|36401(movie_id)|4.0(rate)|1138983041(timestamp)
    # instance[0]:id  instance[1]:user_id  instance[2]:movie_id
    movie_id = instance[2]
    user_id = instance[1]

    if movie_id not in movie_proj_dict:
        movie_proj_dict[len(movie_proj_dict)] = movie_id

    if movie_id in movie_audience_dict:
        movie_audience_dict[movie_id].add(user_id)
    else:
        movie_audience_dict[movie_id] = set()
        movie_audience_dict[movie_id].add(user_id)

print(movie_audience_dict)
print(len(movie_proj_dict),movie_proj_dict)

co_occur = np.zeros((len(movie_proj_dict),len(movie_proj_dict)))
print(len(co_occur),co_occur)

for movie_id in movie_audience_dict:
    pass