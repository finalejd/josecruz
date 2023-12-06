from django.db import models

# Create your models here.

class Stadium(models.Model):
        number = models.CharField(primary_key=True, max_length=5)
        nameStadium = models.CharField(max_length=200, null=False)
        capacity = models.CharField(max_length=5)
        boxSize = models.CharField(max_length=20)

        created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
        updated = models.DateTimeField(auto_now_add=False, auto_now=True)

        
        def __str__(self):
            return self.nameStadium

class Teams(models.Model):
        number = models.CharField(primary_key=True, max_length=5)
        nameTeam = models.CharField(max_length=200)
        venue = models.CharField(max_length=100)
        ownerName = models.CharField(max_length=50)

        stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE, null=True)

        created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
        updated = models.DateTimeField(auto_now_add=False, auto_now=True)

        def __str__(self):
            return self.nameTeam
        
class Player(models.Model):
        number = models.CharField(primary_key=True, max_length=5)
        namePlayer = models.CharField(max_length=200, null=False)
        playerNumber = models.CharField(max_length=5)
        playerPosition = models.CharField(max_length=20)
        
        team = models.ForeignKey(Teams, on_delete=models.CASCADE, null=True)

        created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
        updated = models.DateTimeField(auto_now_add=False, auto_now=True)
        
        def __str__(self):
            return self.namePlayer


        
