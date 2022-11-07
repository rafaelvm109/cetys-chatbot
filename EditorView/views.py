from django.shortcuts import render, get_object_or_404
from .models import Category, PatternResponse

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
    return render(request, 'index.html', {"categories": all_categories, "patterns": data})

# Se muestra cuando le dan editar a un patron
def edit_pattern(request, tag_id):
    pattern = PatternResponse.objects.filter(tag=tag_id)
    data = []
    for item in pattern:
        data.append(item)
    return render(request, 'add.html', {"pattern":data[0]})
    
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
    
    return render(request, 'index.html', {"categories": all_categories, "patterns": data})
