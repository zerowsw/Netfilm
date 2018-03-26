#import rating data
import django
django.setup()

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Netfilm.settings")


import json
from application.models import rate as r

r.objects.all().delete()

with open("dataset/ratings_small.json",encoding = 'utf-8') as data:
	d = json.load(data)
	List = []

for i in range(0,len(d)):
	userId = d[i]["userId"]
	movieId = d[i]["movieId"]
	rating = d[i]["rating"]
	timestamp = d[i]["timestamp"]
	instance = r(userId = userId, movieId = movieId, rating =rating,timestamp =timestamp)
	List.append(instance)


r.objects.bulk_create(List)
print("Done!")

