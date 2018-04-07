from django import forms
from expert.models import Expert,Feedback

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


class ExpertForm(forms.ModelForm):
    department = forms.ChoiceField(choices=DEPARTMENT, required=True)
    profession = forms.ChoiceField(choices=PROFESSION, required=True)

    class Meta():
        model = Expert
        fields = ('profile_name','profile_pic','profession','department','achievements','about','linkedin_Profile',
                  'appointment_fee','emailid','address')


class FeedbackForm(forms.ModelForm):
    rating = forms.ChoiceField(choices=RATING,required=True)
    class Meta():
        model = Feedback
        fields = ('user','title','description','rating')




