from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import View
from django.urls import reverse_lazy
from .form import CommentsForm

# Create your views here.

# class BloglistView(ListView):
#     model = Post
#     template_name = 'home.html'

def BloglistView(request):
    latest_list = Post.objects.order_by('-id')
    return render(request, 'home.html', {"latest_list": latest_list})

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ['title', 'author', 'body', 'data']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy('home')

class AddCommentView(View):
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(f'/{pk}')
