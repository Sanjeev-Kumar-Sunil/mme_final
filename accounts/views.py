from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from django.core.mail import send_mail,BadHeaderError
from . import forms

# Create your views here.


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class ContactUsView(View):
    data_sent= False
    form_class = forms.ContactUsForm
    initial = {'key': 'value'}
    template_name = 'contact_us.html'

    def get(self,request,*args,**kwargs):
        form= self.form_class(initial=self.initial)
        return render(request,self.template_name,{'form':form})

    def post(self,request,*args,**kwargs):
        form= self.form_class(request.POST)
        if form.is_valid():
            form.save()
            data_sent= True
        else:
            print("Errors")
        return render(request, 'contact_us.html',
                      {'data_sent':data_sent,
                       'form':form})




