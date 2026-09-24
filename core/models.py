from django.db import models


class SiteSettings(models.Model):
    company_name = models.CharField(max_length=200)
    tagline = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.company_name


class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    client = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='insights/', blank=True, null=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Founder(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200, blank=True)
    bio = models.TextField()
    image = models.ImageField(upload_to='founder/', blank=True, null=True)

    def __str__(self):
        return self.name
