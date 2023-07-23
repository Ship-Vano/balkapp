from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# parent model
class forum(models.Model):
    name = models.CharField(max_length=200)
    #    email = models.CharField(max_length=200, null=True)
    topic = models.CharField(max_length=300)
    description = models.CharField(max_length=1000, blank=True)
    link = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_updated']
        indexes = [
            models.Index(fields=['-date_updated']),
        ]

    def __str__(self):
        return str(self.topic)


# # child model
class Discussion(models.Model):
    forum = models.ForeignKey(forum, blank=True, on_delete=models.CASCADE)
    discuss = models.CharField(max_length=1000)
    participants = models.ManyToManyField(User,
                                          related_name='rooms_joined',
                                          blank=True)

    def __str__(self):
        return str(self.forum)


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/", default="default/user.png")
    def __str__(self):
        return str(self.user)



class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    post_id = models.AutoField
    post_title = models.CharField(max_length=100, default='Новое обсуждение')
    post_content = models.CharField(max_length=5000)
    timestamp = models.DateTimeField(default=now)
    image = models.ImageField(upload_to="images", default="")


class Replie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    reply_id = models.AutoField
    reply_content = models.CharField(max_length=5000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default='')
    timestamp = models.DateTimeField(default=now)
    image = models.ImageField(upload_to="images", default="")