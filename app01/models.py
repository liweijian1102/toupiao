from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class vote(models.Model):
    vote_title=models.CharField(max_length=32)
    vote_start=models.DateTimeField()
    vote_end=models.DateTimeField()
    vote_zuozhe=models.CharField(max_length=32,blank=True)
    def __unicode__(self):
        return self.vote_title

class vote_content(models.Model):
    vote_bt=models.CharField(max_length=32)
    vote_a=models.CharField(max_length=32,blank=True)
    vote_b=models.CharField(max_length=32,blank=True)
    vote_c=models.CharField(max_length=32,blank=True)
    vote_d=models.CharField(max_length=32,blank=True)
    vote_e=models.CharField(max_length=32,blank=True)
    vote_f=models.CharField(max_length=32,blank=True)
    vote_type=models.CharField(max_length=32,blank=True)
    content_zuozhe=models.OneToOneField(User)
    def __unicode__(self):
        return self.vote_bt

class vote_result(models.Model):
    result_bt=models.CharField(max_length=32)
    result_aa=models.IntegerField(max_length=10,blank=True)
    result_bb=models.IntegerField(max_length=10,blank=True)
    result_cc=models.IntegerField(max_length=10,blank=True)
    result_dd=models.IntegerField(max_length=10,blank=True)
    result_ee=models.IntegerField(max_length=10,blank=True)
    result_ff=models.IntegerField(max_length=10,blank=True)
    content_zuozhe=models.CharField(max_length=32,blank=True)
    def __unicode__(self):
        return self.result_bt
class vote_ip(models.Model):
    voteip=models.IPAddressField()
    def __unicode__(self):
        return self.voteip
    
