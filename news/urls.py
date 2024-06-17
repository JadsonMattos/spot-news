from django.urls import path, include
from news.views import index, news_details, categories_form, news_form
from rest_framework import routers
from news.views import CategoryViewSet, UserViewSet, NewsViewSet


URL = "http://127.0.0.1:8000"

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'users', UserViewSet)
router.register(r'news', NewsViewSet)

urlpatterns = [
    path("URL", index, name="home-page"),
    path("URL/news/<int:id>", news_details, name="news-details-page"),
    path("URL/categories/", categories_form, name="categories-form"),
    path("URL/news/", news_form, name="news-form"),
    path("api/", include(router.urls)),
]
