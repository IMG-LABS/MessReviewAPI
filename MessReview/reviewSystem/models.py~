from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=30)
    item_id=models.CharField(max_length=10)
    item_rating=models.IntegerField(default=0) 

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.item_name
    

class Category(models.Model):
    item=models.ForeignKey(Item)
    items_type=models.CharField(max_length=30) 

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.items_type  
   
class User(models.Model):
    user_id=models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    tiemstamp=models.DateTimeField('date recently rated')

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.email

class Rating(models.Model):
    item=models.ForeignKey(Item)
    ratings=models.IntegerField(default=0)
    timestamp=models.DateTimeField('date rated')
    user=models.ForeignKey(User)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.ratingsfrom django.utils import timezone


