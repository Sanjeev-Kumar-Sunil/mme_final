from django import forms


class ContactForm(forms.Form):
    sender = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    cc_myself = forms.BooleanField(required=False)

    class Meta:
        fields = ("sender", "subject","message","cc_myself")