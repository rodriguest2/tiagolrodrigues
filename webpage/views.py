from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.mail import send_mail
from webpage import forms
from django.conf import settings
from django.views.generic import View, TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView
from webpage.models import Post, Category, Comment
from webpage.forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    #will order the posts by post_date, newest first
    ordering = ['-post_date']

    #will pull category data from Category
    #not used in code yet
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryView(request,cats):
    #category is refering to model field category
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'category.html', {'cats':cats,'category_posts':category_posts})

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class CreatePost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_create.html'

    #will fill in author field for you automatically
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreatePost, self).form_valid(form)

class UpdatePost(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_edit.html'

class DeletePost(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    #get_absolute_url won't work here, so success_url is required
    success_url = reverse_lazy('post_list')

class CommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'post_comment.html'

    #will fill in post field for you automatically
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super(CommentView, self).form_valid(form)

    #will return pk of post and bring you back to detail page
    def get_success_url(self):
        post_id = self.kwargs['pk']
        return reverse_lazy('post_detail', kwargs={'pk':post_id})

#delete comment
@login_required
def comment_remove(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    post_pk=comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)

def contact(request):
    form=forms.ContactForm()

    if request.method=="POST":
        form=forms.ContactForm(request.POST)

        if form.is_valid():
            message_name = form.cleaned_data['name']
            message_email = form.cleaned_data['email']
            message_phone = form.cleaned_data['phone']
            message_message = form.cleaned_data['message']

            send_mail(
            "Web Dev Inquiry: " + message_name,
            "Message from: " + message_name + "\nPhone Number: " + message_phone + "\n\n" + message_message,
            settings.EMAIL_HOST_USER,
            [message_email, settings.EMAIL_HOST_USER],
            fail_silently=False
            )

            messages.success(request, 'Thank you for your message, we will contact you soon!')

            return redirect('contact')

        else:
            return render(request, 'contact.html', {'form':form})

    else:
        return render(request, 'contact.html', {'form':form})

def index(request):
    return render(request, 'index.html', {})

def services(request):
    return render(request, 'services.html', {})

def projects(request):
    return render(request, 'projects.html', {})
