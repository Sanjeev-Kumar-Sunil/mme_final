from django.shortcuts import render,get_object_or_404,redirect
from .models import Expert,Feedback
from .forms import ExpertForm,FeedbackForm
from django.utils import timezone
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,CreateView,
                                  UpdateView,DeleteView,
                                  DetailView,ListView)
# Create your views here.


class ExpertListView(ListView):
    model = Expert

    def get_queryset(self):
        return Expert.objects.filter(joined_date__lte=timezone.now()).order_by('appointment_fee')


class ExpertProfessionListView(ListView):
    model = Expert

    def get_queryset(self):
        return Expert.objects.filter(profession__iexact=self.kwargs.get('profession')).order_by('appointment_fee')


class ExpertDepartmentListView(ListView):
    model = Expert

    def get_queryset(self):
        return Expert.objects.filter(department__iexact=self.kwargs.get('department')).order_by('appointment_fee')


class ExpertAppointmentFeeListView(ListView):
    model = Expert

    def get_queryset(self):
        return Expert.objects.filter(Q(appointment_fee__lte=self.kwargs.get('maximum')),Q(appointment_fee__gte=self.kwargs.get('minimum'))).order_by('appointment_fee')


class ExpertCreateView(CreateView):
    form_class = ExpertForm
    model = Expert

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExpertDetailView(DetailView):
    model = Expert


@login_required
def add_feedback_to_expert(request,pk):
    expert = get_object_or_404(Expert,pk=pk)
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.expert = expert
            feedback.save()
            return redirect('experts:expertsdetailpage',pk=expert.pk)
    else:
        form = FeedbackForm()
    return render(request,'expert/feedback_form.html',{'form':form})