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
PROFESSION = (
    ('Doctor', 'Doctor'),
    ('Engineer', 'Engineer'),
    ('Lawyer', 'Lawyer'),
    ('MBA', 'MBA'),
    ('Professor', 'Professor'),
    ('Businessman', 'Businessman'),
    ('Athlete', 'Athlete'),
    ('Actor', 'Actor'),
    ('Consultant', 'Consultant'),
    ('Spiritualist', 'Spiritualist'),
    ('others','others')
)
RATING = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)


class Expert(models.Model):
    user = models.ForeignKey(User)
    department = models.CharField(max_length=50,choices=DEPARTMENT)
    profession = models.CharField(max_length=50,choices=PROFESSION)
    profile_pic = ThumbnailerImageField(upload_to='profile_pics/', blank=True, null=False)
    joined_date = models.DateTimeField(auto_now=True)
    approved_expert = models.BooleanField(default=False)
    mme_id = models.CharField(max_length=10,default='00000000')
    profile_name = models.CharField(max_length=50,null=False)
    achievements = models.CharField(max_length=100,null=False)
    linkedin_Profile = models.URLField()
    appointment_fee = models.IntegerField()
    about = models.TextField(null=True)
    address = models.CharField(max_length=100)
    emailid = models.EmailField()

    def __str__(self):
        return self.profile_name

    def user_feedback(self):
        return self.feedbacks.all()

    def get_absolute_url(self):
            return reverse('experts:expertsdetailpage', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['appointment_fee']


class Feedback(models.Model):
    expert = models.ForeignKey(Expert,related_name='feedbacks',null=True)
    user = models.CharField(max_length=30,default='anonymous')
    title = models.CharField(max_length=50)
    rating = models.IntegerField(choices=RATING)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now=True)

   # def get_absolute_url(self):
        #return reverse('')

    def __str__(self):
        return self.title

