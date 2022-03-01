from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=200)
    birthday_year = models.PositiveIntegerField() 
    national_code = models.CharField(max_length=10, unique=True)
    data = models.JSONField(null=True, blank= True)
    is_active = models.BooleanField(default=True)
    address = models.TextField(max_length=1000)
    dato = models.DateTimeField(null=True, blank=True)
    email = models.EmailField(max_length=254, unique=True)
    identify = models.SlugField(blank=True, null=True)    
    website = models.URLField(null=True, blank=True)
    attach = models.FileField(blank=True, null=True, max_length=254, upload_to='files/')
    pic = models.ImageField(null=True, blank=True, upload_to = 'images/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name +' - '+ self.email

    class Meta:
        ordering = ('-email',)


################################################

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete= models.CASCADE, related_name='books')
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name +' [in]-> '+ self.category.name


class Authur(models.Model):
    book = models.ManyToManyField(Book)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name



