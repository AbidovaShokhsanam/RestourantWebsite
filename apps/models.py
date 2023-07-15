from django.contrib.auth.models import AbstractUser
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Food(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField(upload_to='foods/images/%Y/%m/%d', null=True, blank=True)
    category_id = models.ForeignKey('apps.Category', on_delete=models.CASCADE)

    class Meta:
        db_table = 'foods'
        verbose_name = 'Food'
        verbose_name_plural = 'Foods'


class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'contact'
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


class Menu(models.Model):
    category_id = models.ForeignKey('apps.Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField(upload_to='menus/images/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'menu'
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'


class Message(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.full_name


class Message1(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_Number = models.CharField(max_length=255)
    people = models.IntegerField()
    date = models.DateTimeField()
    time = models.DateTimeField()
    message = models.TextField()

    def __str__(self):
        return self.full_name


class News(models.Model):
    image = models.ImageField(upload_to='foods/images/%Y/%m/%d', null=True, blank=True)
    category = models.CharField(max_length=255)
    date = models.DateField()
    cause = models.CharField(max_length=255)

    def __str__(self):
        return self.cause

    class Meta:
        db_table = 'news'
        verbose_name = 'News'
        verbose_name_plural = 'news'


class My_User(AbstractUser):
    job = models.CharField(max_length=255)
    image = models.ImageField(upload_to='user/images/%Y/%m/%d', null=True, blank=True)

    class Meta:
        db_table = 'users'
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Newss(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='newss/images/%Y/%m/%d', null=True, blank=True)
    descriptation = models.CharField(max_length=500)

    def __str__(self):
        return self.name
