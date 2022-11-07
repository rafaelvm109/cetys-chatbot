from django.shortcuts import render, get_object_or_404
from .models import Category, PatternResponse
import time


# Inicio del programa
def index(request):
    all_categories = Category.objects.all()
    return render(request, 'index.html', {"categories": all_categories})


# Se muestra cuando le dan click a una categoria
def get_category(request, category_id):
    all_categories = Category.objects.all()
    all_patterns = PatternResponse.objects.all()
    data = []
    for item in all_patterns:
        if category_id.lower() in item.tag:
            data.append(item)
    return render(request, 'index.html', {"categories": all_categories, "patterns": data, "category": category_id})


# Se muestra cuando le dan editar a un patron
def edit_pattern(request, tag_id):
    pattern = PatternResponse.objects.filter(tag=tag_id)
    data = []
    for item in pattern:
        data.append(item)
    return render(request, 'add.html', {"pattern": data[0]})


def add_pattern(request, category_id):
    cat = Category.objects.get(category=category_id)

    new = PatternResponse()
    new.category = cat
    new.tag = category_id.lower() + "." + str(time.time())
    new.pattern = ""
    new.response = ""
    new.save()

    all_categories = Category.objects.all()
    all_patterns = PatternResponse.objects.all()
    data = []
    for item in all_patterns:
        if category_id.lower() in item.tag:
            data.append(item)
    return render(request, 'index.html', {"categories": all_categories, "patterns": data, "category": category_id})


# Se muestra cuando le dan guardar a un patron
def push_edit(request, tag_id):
    pattern = PatternResponse.objects.get(tag=tag_id)
    pattern.tag = request.POST['tag']
    pattern.pattern = request.POST['pattern']
    pattern.response = request.POST['response']
    pattern.save()

    all_categories = Category.objects.all()
    all_patterns = PatternResponse.objects.all()
    data = []
    for item in all_patterns:
        if pattern.category.category.lower() in item.tag:
            data.append(item)

    return render(request, 'index.html',
                  {"categories": all_categories, "patterns": data, "category": pattern.category.category})


def add_category(request):
    return render(request, 'category.html')


def go_home(request):
    all_categories = Category.objects.all()
    return render(request, 'index.html', {"categories": all_categories})


def commit_category(request):
    new_cat = Category()
    new_cat.category = request.POST["NewCategory"]
    new_cat.save()

    all_categories = Category.objects.all()

    return render(request, 'index.html', {"categories": all_categories})


def remove_category(request):
    all_categories = Category.objects.all()

    return render(request, 'remove.html', {"categories": all_categories})


def commit_remove_category(request):
    cat = Category.objects.get(category=request.POST["remove"])
    cat.delete()

    all_categories = Category.objects.all()

    return render(request, 'index.html', {"categories": all_categories})