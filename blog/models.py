from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from easy_thumbnails.fields import ThumbnailerImageField
User = get_user_model()

DEPARTMENT = (
    ('Agriculture', 'Agriculture'),
    ('Automotive', 'Automotive'),
    ('Business', 'Business'),
    ('Career', 'Career'),
    ('Education', 'Education'),
    ('Finance', 'Finance'),
    ('Fitness', 'Fitness'),
    ('Health', 'Health'),
    ('Legal', 'Legal'),
    ('Lifestyle', 'Lifestyle'),
    ('RealEstate', 'RealEstate'),
    ('Spiritual','Spiritual'),
    ('Tax and Accounting', 'Tax and Accounting'),
    ('Technology', 'Technology'),
    ('Travels', 'Travels'),
    ('others', 'others')
)


class Post(models.Model):
    author = models.ForeignKey(User)
    department = models.CharField(max_length=50, choices=DEPARTMENT)
    post_title = models.CharField(max_length=100)
    post_pic = ThumbnailerImageField(upload_to='post_pics/', blank=True, null=False)
    published_date = models.DateTimeField(auto_now=True)
    summary = models.CharField(max_length=400)
    content = models.TextField(null=True)

    def __str__(self):
        return self.post_title

    def post_likes(self):
        return self.comments_and_likes.filter(like_post=True)

    def post_feedback(self):
        return self.comments_and_likes.all()

    def get_absolute_url(self):
        return reverse("blogs:postsdetailpage",kwargs={'pk':self.pk})

    class Meta:
        ordering = ['published_date']


class CommentAndLikes(models.Model):
    post = models.ForeignKey(Post, related_name='comments_and_likes', null=True)
    user = models.CharField(max_length=30, default='anonymous')
    comment_title = models.CharField(max_length=50)
    description = models.TextField()
    commented_date = models.DateTimeField(auto_now=True)
    like_post = models.BooleanField(default=False)

    def like_post_method(self):
        self.like_post = True
        self.save()

    def __str__(self):
        return self.comment_title

