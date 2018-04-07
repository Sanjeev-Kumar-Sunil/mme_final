from django.conf.urls import url
from django.contrib.auth import views as auth_views
from blog import views


app_name = 'blogs'
urlpatterns = [
     url(r'^detailpage/(?P<pk>\d+)/$',views.PostDetailView.as_view(),name='postsdetailpage'),
     url(r'^listpage/$',views.PostListView.as_view(),name='postslistpage'),
     url(r'^new/$',views.PostCreateView.as_view(),name='post_new'),
     url(r'^(?P<pk>\d+)/comment/$',views.add_comment_to_post,name='add_comment_to_post'),

]