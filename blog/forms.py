from django import forms
from blog.models import Post,CommentAndLikes

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
    ('others','others')
)


class PostForm(forms.ModelForm):
    department = forms.ChoiceField(choices=DEPARTMENT, required=True)

    class Meta():
        model = Post
        fields = ('department','post_title','post_pic',
                  'summary','content')


class CommentAndLikesForm(forms.ModelForm):
    class Meta():
        model = CommentAndLikes
        fields = ('user','comment_title','description',)




