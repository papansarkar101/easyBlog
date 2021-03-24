from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm, CategoryForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('article', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-post_date']
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        ctgs_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["ctgs_menu"] = ctgs_menu
        return context


def CategoryView(request, ctgs):
    category_posts = Post.objects.filter(category=ctgs.replace('-', ' '))
    return render(request, 'categories.html', {'ctgs': ctgs.title().replace('-', ' '), 'category_posts': category_posts})


class ArticleView(DetailView):
    model = Post
    template_name = 'article.html'

    def get_context_data(self, *args, **kwargs):
        ctgs_menu = Category.objects.all()
        context = super(ArticleView, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["ctgs_menu"] = ctgs_menu
        context['total_likes'] = total_likes

        context['liked'] = liked

        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'addpost.html'

    def get_context_data(self, *args, **kwargs):
        ctgs_menu = Category.objects.all()
        context = super(AddPostView, self).get_context_data(*args, **kwargs)
        context["ctgs_menu"] = ctgs_menu
        return context

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')


class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'add_category.html'

    def get_context_data(self, *args, **kwargs):
        ctgs_menu = Category.objects.all()
        context = super(AddCategoryView, self).get_context_data(
            *args, **kwargs)
        context["ctgs_menu"] = ctgs_menu
        return context

    success_url = reverse_lazy('home')

    

class UpdateArticleView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'updatepost.html'

    def get_context_data(self, *args, **kwargs):
        ctgs_menu = Category.objects.all()
        context = super(UpdateArticleView, self).get_context_data(
            *args, **kwargs)
        context["ctgs_menu"] = ctgs_menu
        return context


class DeleteArticleView(DeleteView):
    model = Post
    template_name = 'deletepost.html'

    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        ctgs_menu = Category.objects.all()
        context = super(DeleteArticleView, self).get_context_data(
            *args, **kwargs)
        context["ctgs_menu"] = ctgs_menu
        return context
