from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Photo(models.Model):
    category = models.ForeignKey(Category, default="others", on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.description


class Team(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    facebook_url = models.CharField(max_length=250, null=True, blank=True)
    youtube_url = models.CharField(max_length=250, null=True, blank=True)
    twitter_url = models.CharField(max_length=250, null=True, blank=True)
    linkedin_url = models.CharField(max_length=250, null=True, blank=True)
    instagram_url = models.CharField(max_length=250, null=True, blank=True)
    whatsapp_url = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.description


class Contact(models.Model):
    email = models.CharField(max_length=255,blank=True)
    first_name = models.CharField(max_length=255,blank=True)
    last_name = models.CharField(max_length=255,blank=True)
    subject = models.CharField(max_length=255,blank=True)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.email