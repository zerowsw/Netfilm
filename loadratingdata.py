#import rating data
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Netfilm.settings")

import django
django.setup()


import json
from application.models import rate as r

r.objects.all().delete()

with open("dataset/ratings_small.json",encoding = 'utf-8') as data:
	d = json.load(data)
	List = []

for i in range(0,len(d)):
	user_id = d[i]["userId"]
	movie_id = d[i]["movieId"]
	rating = d[i]["rating"]
	timestamp = d[i]["timestamp"]
	instance = r(user_id = user_id, movie_id = movie_id, rating =rating,timestamp =timestamp)
	List.append(instance)

print("number of insert data entries:",len(List))

r.objects.bulk_create(List)
print("Done!")

