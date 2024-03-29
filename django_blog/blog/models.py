from django.db import models
from helper.models import BaseModel
from user.models import User
from taggit.managers import TaggableManager


class Post(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True) # imageField 사용시 Plillow pip 설치
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    tags = TaggableManager()

    def __str__(self):
        return '%s - %s' % (self.id, self.title)

    def total_likes(self):
        return self.likes.count()

class Comment(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    
    def __str__(self):
        return '%s - %s' % (self.id, self.user)