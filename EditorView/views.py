from django.shortcuts import render, redirect

from EditorView.models import Category, PatternResponse


# Inicio del programa
def dashboard(request):
    return render(request, 'dashboard.html')

def login(request):
    return render(request, 'login.html')

def categorias(request):
    all_categories = Category.objects.all()
    if request.method == 'POST':

        if request.POST.get("form_type") == 'searchForm':
            select = request.POST['categorySelection']
            data = PatternResponse.objects.filter(category__category__contains=select)

            if len(data) == 0:
                print('empty')
                return render(request, 'categorias.html', {"categorias": all_categories, "empty": {True}, "titulo": select})

            for item in data:
                item.notModifiedPattern = item.pattern
                item.notModifiedResponse = item.response
                item.pattern = item.pattern.split(',')
                item.response = item.response.split(',')
                
            return render(request, 'categorias.html', {"categorias": all_categories, "patterns":data, "titulo": select})
        
        elif request.POST.get("form_type") == 'addForm':
            name = request.POST['categoriaNueva']
            categoria = Category(category=name)
            categoria.save()
            return redirect('categorias')
        
        elif request.POST.get("form_type") == 'eliminarForm':
            select = request.POST.get("eliminar")
            Category.objects.filter(category=select).delete()
            return redirect('categorias')
        
        elif request.POST.get("form_type") == 'patronModal':
            print(request.POST)
            select = request.POST.get("categoriatitulo")
            category = Category.objects.filter(category=select)[0]

            pregunta = request.POST['preguntaNueva']
            patrones = request.POST['patronesNuevo']
            respuesta = request.POST['respuestaNueva']
            new = PatternResponse(category=category, tag=pregunta, pattern=patrones, response=respuesta)
            new.save()

            data = PatternResponse.objects.filter(category__category__contains=select)

            for item in data:
                item.notModifiedPattern = item.pattern
                item.notModifiedResponse = item.response
                item.pattern = item.pattern.split(',')
                item.response = item.response.split(',')

            return render(request, 'categorias.html', {"categorias": all_categories, "patterns":data, "titulo": select})

    else:
        return render(request, 'categorias.html', {"categorias": all_categories})
    

def editar_patron(request, patron):
    if request.method == 'POST':
        data = PatternResponse.objects.filter(tag=patron)[0]

        print(request.POST)

        data.tag = request.POST["preguntaNueva"]
        data.pattern = request.POST["patrones"]
        data.response = request.POST["respuestaNueva"]

        data.save()
                
        return redirect('categorias')

    else:
        data = PatternResponse.objects.filter(tag=patron)[0]
        return render(request, 'editar.html', {"data": data})
    
def eliminar_patron(request, patron):
    print(patron)
    PatternResponse.objects.filter(tag=patron).delete()
    return redirect('categorias')

def reportes(request):
    return render(request, 'reportes.html')