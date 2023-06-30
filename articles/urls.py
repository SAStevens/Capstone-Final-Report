from django.urls import path

from .views import (
    ArticleCreateView,
    ArticleListView,
    ArticleDetailView,
    ArticleUpdateView,
    ArticleDeleteView,
    like_article,
    dislike_article,
)

urlpatterns = [
    path("new/", ArticleCreateView.as_view(), name="article_new"),
    path("", ArticleListView.as_view(), name="article_list"),
    path("<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path("<int:pk>/edit/", ArticleUpdateView.as_view(), name="article_edit"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
    path("like/<int:pk>", like_article, name="like_article"),
    path("dislike/<int:pk>", dislike_article, name="dislike_article"),
]
