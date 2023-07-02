from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from django.urls import reverse_lazy, reverse

from django.shortcuts import redirect, get_object_or_404, render

from django.http import JsonResponse

from .forms import CommentForm

from .models import Article, Like, Comment


class CommentGet(DetailView):
    model = Article
    template_name = "article_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


class CommentPost(SingleObjectMixin, FormView):
    model = Article
    form_class = CommentForm
    template_name = "article_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        article = self.object
        return reverse("article_detail", kwargs={"pk": article.pk})


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "article_new.html"
    fields = ("title", "body")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "article_list.html"


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "article_detail.html"
    context_object_name = "article"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.object
        comments = Comment.objects.filter(article=article)
        likes = Like.objects.filter(article=article, is_dislike=False)
        dislikes = Like.objects.filter(article=article, is_dislike=True)
        comment_form = CommentForm()
        context["comments"] = comments
        context["likes"] = likes
        context["dislikes"] = dislikes
        context["comment_form"] = comment_form
        return context

    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = (
        "title",
        "body",
    )
    template_name = "article_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


def like_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if Like.objects.filter(
        user=request.user, article=article, is_dislike=False
    ).exists():
        return redirect(reverse("article_detail", kwargs={"pk": pk}))
    existing_dislike = Like.objects.filter(
        user=request.user, article=article, is_dislike=True
    ).first()

    if existing_dislike:
        existing_dislike.delete()

    like = Like(user=request.user, article=article, is_dislike=False)
    like.save()

    return redirect(reverse("article_detail", kwargs={"pk": pk}))


def dislike_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if Like.objects.filter(
        user=request.user, article=article, is_dislike=True
    ).exists():
        return redirect(reverse("article_detail", kwargs={"pk": pk}))
    existing_like = Like.objects.filter(
        user=request.user, article=article, is_dislike=False
    ).first()

    if existing_like:
        existing_like.delete()

    like = Like(user=request.user, article=article, is_dislike=True)
    like.save()

    return redirect(reverse("article_detail", kwargs={"pk": pk}))
