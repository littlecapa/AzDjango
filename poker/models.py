from django.db import models

class UserStory(models.Model):
    ticketNr = models.IntegerField(primary_key=True)
    summary = models.CharField(max_length=100)

class EstimateChoice(models.Model):
    choice = models.CharField(max_length=10, primary_key=True)
    value = models.IntegerField(default=0)

class Estimate(models.Model):
    ticketNr = models.ForeignKey(UserStory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    estimate = models.ForeignKey(EstimateChoice, on_delete=models.CASCADE)