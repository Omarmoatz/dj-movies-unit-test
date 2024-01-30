from django.db import models
from django.contrib.auth.models import User

SHOW_CHOICES = (
    ('Movie','Movie'),
    ('Series','Series'),
    ('Theater','Theater'),
    ('Animation','Animation'),
)

class Show(models.Model):
    user = models.ForeignKey(User, related_name='user_show', on_delete=models.CASCADE)
    title = models.CharField(max_length=100,default='default_show', blank=True)
    description = models.TextField(max_length=5000,default='default_description', blank=True)
    image = models.ImageField( upload_to='show/',blank=True, null=True)
    rating = models.DecimalField( max_digits=4, decimal_places=2)
    type = models.CharField(max_length=50,choices=SHOW_CHOICES, blank=True)
    category = models.ForeignKey('Category', related_name='category_show', on_delete=models.SET_DEFAULT,default='default_ctg')
    main_actor = models.ForeignKey('Actor', related_name='mainActor_show', on_delete=models.SET_DEFAULT,default='somebody')
    sub_actor = models.ForeignKey('Actor', related_name='subActor_show', on_delete=models.SET_DEFAULT,default='somebody2')

    def __str__(self):
        return self.title


ACTOR_GENDER = (
    ('Male','Male'),
    ('Female','Female'),
)
class Actor(models.Model):
    name = models.CharField( max_length=100, default='somebody', blank=True)
    age = models.PositiveIntegerField( default=20, blank=True)
    gender = models.CharField( max_length=50, choices=ACTOR_GENDER, blank=True)
    image = models.ImageField( upload_to='actor/',blank=True, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField( max_length=100, default='default_ctg', blank=True)
    image = models.ImageField( upload_to='category/',blank=True, null=True)

    def __str__(self):
        return self.title