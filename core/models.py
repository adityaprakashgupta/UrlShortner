from django.db import models
import random
import string


# Create your models here.
# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     date_posted = models.DateTimeField(auto_now_add=True)
#     slug = models.SlugField(max_length=100, unique=True)
#
#     def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
#         # check if slug is already present
#         if not self.slug:
#             self.slug = self.title.replace(" ", "-").lower()
#         # check if slug is unique
#         while Post.objects.filter(slug=self.slug).exists():
#             random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(5, 6)))
#             self.slug = self.slug + "-" + random_string
#         super(Post, self).save()
#
#     def __str__(self):
#         return self.title

class Url(models.Model):
    original_url = models.URLField(max_length=100000)
    short_url = models.URLField(unique=True, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # check if short_url is already present
        if not self.short_url:
            self.short_url = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        # check if short_url is unique
        while Url.objects.filter(short_url=self.short_url).exists():
            random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
            self.short_url = random_string
        super(Url, self).save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.short_url
