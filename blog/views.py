from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,CommentAndLikes
from .forms import PostForm,CommentAndLikesForm
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,CreateView,
                                  UpdateView,DeleteView,
                                  DetailView,ListView)
# Create your views here.


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')


class PostCreateView(CreateView):
    form_class = PostForm
    model = Post

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post


@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentAndLikesForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blogs:postsdetailpage',pk=post.pk)
    else:
        form = CommentAndLikesForm()
    return render(request,'blog/comment_form.html',{'form':form})