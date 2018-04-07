from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


app_name = 'experts'
urlpatterns = [
     url(r'^detailpage/(?P<pk>\d+)/$',views.ExpertDetailView.as_view(),name='expertsdetailpage'),
     url(r'^listpage/$',views.ExpertListView.as_view(),name='expertslistpage'),
     url(r'^new/$',views.ExpertCreateView.as_view(),name='expert_new'),
     url(r'^profession/(?P<profession>\w+)/listpage/$',views.ExpertProfessionListView.as_view(),name='expertsprofessionlistpage'),
     url(r'^department/(?P<department>\w+)/listpage/$',views.ExpertDepartmentListView.as_view(),name='expertdepartmentlistpage'),
     url(r'^appointmentfee/(?P<minimum>\d+)/(?P<maximum>\d+)/listpage/$',views.ExpertAppointmentFeeListView.as_view(),name='expertappointmentfeelistpage'),
     url(r'^(?P<pk>\d+)/comment/$',views.add_feedback_to_expert,name='add_feedback_to_expert'),

]