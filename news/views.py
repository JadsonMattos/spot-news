from django.shortcuts import render, redirect, get_object_or_404
from news.forms import CreateCategoriesForm, CreateNewsForm
from .models import Category, News, User
from rest_framework import viewsets
from .serializers import CategorySerializer, UserSerializer, NewsSerializer


def index(request):
    context = {"news": News.objects.all()}
    return render(request, "home.html", context)


def news_details(request, id):
    context = {"news_details": get_object_or_404(News, id=id)}
    return render(request, "news_details.html", context)


def categories_form(request):
    if request.method == 'POST':
        form = CreateCategoriesForm(request.POST)
        if form.is_valid():
            Category.objects.create(**form.cleaned_data)
            return redirect('home-page')
    else:
        form = CreateCategoriesForm()
    context = {'form': form}
    return render(request, 'categories_form.html', context)


def news_form(request):
    if request.method == 'POST':
        form = CreateNewsForm(request.POST, request.FILES)
        if form.is_valid():
            categories = form.cleaned_data.pop('categories')
            news = News.objects.create(**form.cleaned_data)
            news.categories.set(categories)
            return redirect('home-page')
    else:
        form = CreateNewsForm()
    context = {'form': form, 'categories': Category.objects.all()}
    return render(request, 'news_form.html', context)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
