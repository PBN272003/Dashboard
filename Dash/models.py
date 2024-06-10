from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, validate_integer


class User(models.Model):
    intensity = models.IntegerField(default=0)
    likelihood = models.IntegerField(default=0)
    relevance = models.IntegerField(default=0)
    year = models.IntegerField(null=True, blank=True,default=0)  # Make year optional
    country = models.CharField(max_length=100, null=True, blank=True)
    sector = models.CharField(max_length=100, null=True, blank=True)
    insight = models.CharField(max_length=1000, null=True, blank=True)
    impact = models.IntegerField(null=True, blank=True,default=0)
    pestle = models.CharField(max_length=100, null=True, blank=True)
    source = models.CharField(max_length=100, null=True, blank=True)
    topics = models.CharField(max_length=100, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
   
    
    def __str__(self):
        return f"{self.year}-{self.country}-{self.topics}"

# Create your models here.
