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
    #Users (names, email, passwords)
    name = models.CharField(max_length=30, default="")
    email = models.EmailField(default="", primary_key=True)
    pw = models.CharField(max_length = 100, default="")

class tweet(models.Model):
    #Tweet (message_id, content, timestamp)
    message_id = models.IntegerField(primary_key=True)
    content = models.TextField(default="")
    timestamp = models.DateTimeField(default="")

class comment(models.Model):
    #Comment (content, timestamp)
    content = models.TextField(default="")
    timestamp = models.DateTimeField(primary_key=True)

class rate(models.Model):
    #Rate (email, title, year, Ratingscores, ratingDate)
    email = models.EmailField(default="")
    title = models.CharField(default="", max_length = 30)
    year = models.IntegerField(null = True,blank=True)
    ratingscores = models.FloatField(null = True,blank=True)
    ratingdate = models.DateField(default="")
    class Meta:
        unique_together = ("email", "title", "year", "ratingdate")

class post(models.Model):
    # Post (email, message_id)
    email = models.EmailField(default="")
    message_id = models.IntegerField(default="")
    class Meta:
        unique_together = ("email", "message_id")

class recommend(models.Model):
    #Recommend (email, title, year)
    email = models.EmailField(default="")
    title = models.CharField(default="", max_length=30)
    year = models.IntegerField(null=True, blank=True)
    class Meta:
        unique_together = ("email", "title", "year")

class friendship(models.Model):
    #Frinends (email, email)
    email1 = models.EmailField(default="")
    email2 = models.EmailField(default="")
    class Meta:
        unique_together = ("email1", "email2")
