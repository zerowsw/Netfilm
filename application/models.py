#!/usr/bin/python
#coding:utf-8
 
from django.db import models
 
class movie(models.Model):
    budget = models.IntegerField(null = True,blank=True)#,blank=True
    id = models.IntegerField(primary_key=True)
    imdb_id = models.CharField(max_length = 20,null = True,blank=True)
    original_language = models.CharField(max_length = 10,null = True,blank=True)
    popularity = models.FloatField(null = True,blank=True)
    release_date = models.CharField(max_length = 15,null = True,blank=True)
    revenue = models.IntegerField(null = True,blank=True)
    runtime = models.IntegerField(null = True,blank=True)
    status = models.CharField(max_length = 10,null = True,blank=True)
    title = models.CharField(default="",max_length = 30)
    video = models.CharField(max_length = 6,null = True,blank=True)
    vote_average = models.FloatField(null = True,blank=True)
    vote_count =  models.IntegerField(null = True,blank=True)

    # def __unicode__(self):
    #     return self.id

class user(models.Model):
    email = models.EmailField(default="")
    pw = models.CharField(max_length = 100,default="")

# class tweet(models.Model):
#     pass

# class comment(models.Model):
#     pass

# class rate(models.Model):
#     pass

# class post(models.Model):
#     pass

# class recommend(models.Model):
#     pass

class friendship(models.Model):
    id1 = models.IntegerField()
    id2 = models.IntegerField()
