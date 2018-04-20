#!/usr/bin/python
#coding:utf-8

from django.db import models

class movie(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    budget = models.IntegerField(null = True,blank=True)#,blank=True
    imdb_id = models.CharField(max_length = 20,null = True,blank=True)
    original_language = models.CharField(max_length = 10,null = True,blank=True)
    popularity = models.FloatField(null = True,blank=True)
    release_date = models.CharField(max_length = 15,null = True,blank=True)
    revenue = models.IntegerField(null = True,blank=True)
    runtime = models.IntegerField(null = True,blank=True)
    status = models.CharField(max_length = 10,null = True,blank=True)
    title = models.CharField(default="",max_length = 30)                #important field
    video = models.CharField(max_length = 6,null = True,blank=True)
    vote_average = models.FloatField(null = True,blank=True)
    vote_count =  models.IntegerField(null = True,blank=True)

class user(models.Model):
    user_id = models.IntegerField(default=0,primary_key=True)
    name = models.CharField(max_length=30, default="")
    email = models.EmailField(default="")
    pw = models.CharField(max_length = 100, default="")

class comment(models.Model):
    #Comment (content, timestamp)
    name = models.CharField(max_length=30, default="")
    title = models.CharField(default="",max_length = 30)
    content = models.TextField(default="")
    timestamp = models.TextField(default="")
    class Meta:
        unique_together = ("name", "timestamp")

class rate(models.Model):
    user_id = models.IntegerField(default=0)
    movie_id = models.IntegerField(default = 0)
    rating = models.FloatField(null = True,blank=True)
    timestamp = models.TextField(max_length = 30,default="")
    class Meta:
        unique_together = ("user_id", "movie_id")


class friendship(models.Model):
    #Frinends (email, email)
    name1 = models.CharField(max_length=30, default="")
    name2 = models.CharField(max_length=30, default="")
    class Meta:
        unique_together = ("name1", "name2")
