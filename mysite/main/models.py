from django.contrib.postgres.fields import ArrayField
from django.db import models


class Booking(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    phone = models.CharField(max_length=20, blank=False, null=False)
    date = models.CharField(max_length=100, blank=False, null=False)
    time = models.CharField(max_length=100, blank=False, null=False)
    guest = models.PositiveIntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.name

    class Meta:
        db_table = 'booking'


class Category(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.name

    class Meta:
        db_table = 'category'


class Product(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    price = models.PositiveIntegerField(blank=False, null=False)
    image = models.ImageField(upload_to='products/', blank=False, null=False)
    ingredient = models.TextField(blank=False, null=False)
    category = models.ForeignKey(Category, blank=False, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.name

    class Meta:
        db_table = 'product'


class Chef(models.Model):
    full_name = models.CharField(max_length=100, blank=False, null=False)
    position = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to='chef/', blank=False, null=False)
    about = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.full_name

    class Meta:
        db_table = 'chef'


class Blog(models.Model):
    author = models.CharField(max_length=200, blank=False, null=False)
    about_author = models.TextField(blank=False, null=False)
    author_image = models.ImageField(upload_to='blogs/', blank=False, null=False)
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to='blogs/', blank=False, null=False)
    tags = ArrayField(models.CharField(max_length=200), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.name

    class Meta:
        db_table = 'blog'


class Subscribe(models.Model):
    email = models.EmailField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.email

    class Meta:
        db_table = 'subscribe'


class Instagram(models.Model):
    image = models.ImageField(upload_to='social/', blank=False, null=False)
    link = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return str(self.pk)

    class Meta:
        db_table = 'social'


class User(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)
    email = models.EmailField(max_length=120, blank=False, null=False)
    subject = models.CharField(max_length=120, blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.name

    class Meta:
        db_table = 'user'


class Commentary(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)
    email = models.EmailField(max_length=120, blank=False, null=False)
    website = models.CharField(max_length=120, blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    blog = models.ForeignKey(Blog,blank=False,null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.name

    class Meta:
        db_table = 'commentary'
