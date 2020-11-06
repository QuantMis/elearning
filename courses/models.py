from django.db import models

class Player(models.Model):
    class Rank(models.TextChoices):
        ONE = '1', "Dummy"
        TWO = '2', "Techy"
        THREE = '3', "All Rounder"
        FOUR = '4', "Ultra Learner"
        FIVE = '5', "Mad Genius"


    rank = models.CharField(max_length=100, choices=Rank.choices, default=Rank.FIVE)
    logic = models.IntegerField()
    creativity = models.IntegerField()
    calculation = models.IntegerField()
    speed = models.IntegerField()
    efficiency = models.IntegerField()

class Course(models.Model):
    title = models.CharField(max_length=100)
    progress = models.FloatField()
    stage = models.IntegerField()
