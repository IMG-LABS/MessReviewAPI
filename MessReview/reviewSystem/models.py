import datetime

from django.db import models
from django.utils import timezone
# here from tut 4
# from pygments.lexers import get_lexer_by_name
# from pygments.formatters.html import HtmlFormatter
# from pygments import highlight

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=30)
    item_id=models.CharField(max_length=10)
    item_rating=models.IntegerField(default=0)  #this has to be computed one that is mean of respected
    #below two lines for the ownership privilege
    #owner = models.ForeignKey('auth.User', related_name='item_owner')
    #highlighted = models.TextField()

    def __unicode__(self):  # Python 3: def __str__(self):
         return u'%s' % (self.item_name)
    

class Category(models.Model):
    item=models.ForeignKey(Item ,related_name='category_type')
    items_type=models.CharField(max_length=30,choices=(('BreakFast','BreakFast'),('Lunch','Lunch'),('Dinner','Dinner'))) 

    def __unicode__(self):  # Python 3: def __str__(self):
        return u'%s' % (self.items_type)  
   
class User(models.Model):
    user_id=models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    tiemstamp=models.DateTimeField('date recently rated')

    def __unicode__(self):
        return u'%s %s' % (self.first_name,self.last_name)  
        #return self.email

class Rating(models.Model):
    item=models.ForeignKey(Item)
    ratings=models.IntegerField(default=0)
    timestamp=models.DateTimeField('date rated')
    user=models.ForeignKey(User,related_name='user_rating')
    def was_published_recently(self):
        return self.timestamp >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'timestamp'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'    

    def __unicode__(self):
        return u'%s %s %s' % (self.item,str(self.ratings),self.timestamp)
    
    #__unicode__ is just like toString of java  
    """
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.rate 
    """
    #return a string here ! to define the object
    #check tab error
    #python -m tabnanny admin.py
    #in model , class Meta ??? does what ?? ordering ??


# def save(self, *args, **kwargs):
#     """
#     Use the `pygments` library to create a highlighted HTML
#     representation of the code snippet.
#     """
#     lexer = get_lexer_by_name(self.language)
#     linenos = self.linenos and 'table' or False
#     options = self.title and {'title': self.title} or {}
#     formatter = HtmlFormatter(style=self.style, linenos=linenos,
#                               full=True, **options)
#     self.highlighted = highlight(self.code, lexer, formatter)
#     super(Snippet, self).save(*args, **kwargs)

