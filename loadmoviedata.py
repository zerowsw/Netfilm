

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Netfilm.settings")
import django
django.setup()

import json
from application.models import movie as m

m.objects.all().delete()

with open("dataset/movies.json",encoding = 'utf-8') as data:
	d = json.load(data)
	List = []
	idset = set()

for i in range(0,len(d)):
	try:
		budget = int(d[i]["budget"])
		id = int(d[i]["id"])
		imdb_id = d[i]["imdb_id"]
		original_language = d[i]["original_language"]
		popularity = float(d[i]["popularity"])
		release_date = d[i]["release_date"]
		revenue = int(d[i]["revenue"])
		runtime = int(d[i]["runtime"])
		status = d[i]["status"]
		title = d[i]["title"]
		video = d[i]["video"]
		vote_count= int(d[i]["vote_count"])
		vote_average= float(d[i]["vote_average"])
	except ValueError:
		continue
	else:
		if(not title):
			continue
		if(id in idset):
			continue
		else:
			idset.add(id)

	instance = m(budget =budget,id=id, imdb_id = imdb_id, original_language =original_language,
		popularity =popularity,release_date=release_date,
		revenue=revenue,runtime=runtime,status=status,
		title=title,video=video,vote_count=vote_count,vote_average=vote_average)
	List.append(instance)


m.objects.bulk_create(List)
print("Done!")