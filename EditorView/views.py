import ast
from django.shortcuts import render, redirect, HttpResponse
from EditorView.models import Category, PatternResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from Chat.chat import get_response

import json


# ------------------
# This function handles everything on the dashboard page
def dashboard(request):
    return render(request, 'dashboard.html')

# ------------------
# This function handles everything on the login page


def login(request):
    return render(request, 'login.html')


# ------------------
# This function handles everything on the "Categorias" page
def categorias(request):
    # Get all the categories in the DB
    all_categories = Category.objects.all()

    export2json()

    # This will check for a POST from a form and decide what to do depending on the data in POST
    if request.method == 'POST':
        try:
            # Search for all patterns with the selected category
            if request.POST.get("form_type") == 'searchForm':
                select = request.POST['categorySelection']
                data = PatternResponse.objects.filter(
                    category__category__contains=select)

                # Send an empty variable to the template if no data was found
                if len(data) == 0:
                    return render(request, 'categorias.html', {"categorias": all_categories, "empty": {True}, "titulo": select})

                # Split the comma separated data to make it look better in the UI
                for item in data:
                    item.notModifiedPattern = item.pattern
                    item.notModifiedResponse = item.response
                    item.pattern = item.pattern.split(',')
                    item.response = item.response.split(',')

                return render(request, 'categorias.html', {"categorias": all_categories, "patterns": data, "titulo": select})

            # Add a new category POST
            elif request.POST.get("form_type") == 'addForm':
                name = request.POST['categoriaNueva']
                categoria = Category(category=name)
                categoria.save()
                return redirect('categorias')

            # Delete a new category MODAL
            elif request.POST.get("form_type") == 'eliminarForm':
                select = request.POST.get("eliminar")
                Category.objects.filter(category=select).delete()
                return redirect('categorias')

            # Add a new Pattern Modal
            elif request.POST.get("form_type") == 'patronModal':
                print(request.POST)
                select = request.POST.get("categoriatitulo")
                category = Category.objects.filter(category=select)[0]

                pregunta = request.POST['preguntaNueva']
                patrones = request.POST['patronesNuevo']
                respuesta = request.POST['respuestaNueva']
                new = PatternResponse(
                    category=category, tag=pregunta, pattern=patrones, response=respuesta)
                new.save()

                data = PatternResponse.objects.filter(
                    category__category__contains=select)

                for item in data:
                    item.notModifiedPattern = item.pattern
                    item.notModifiedResponse = item.response
                    item.pattern = item.pattern.split(',')
                    item.response = item.response.split(',')

                return render(request, 'categorias.html', {"categorias": all_categories, "patterns": data, "titulo": select})

        except Exception as e:
            return render(request, 'categorias.html', {"categorias": all_categories})

    else:
        return render(request, 'categorias.html', {"categorias": all_categories})


# ------------------
# This handles everything on the pattern edition page
def editar_patron(request, patron):
    all_categories = Category.objects.all()
    try:
        if request.method == 'POST':
            data = PatternResponse.objects.filter(tag=patron)[0]

            data.tag = request.POST["preguntaNueva"]
            data.pattern = request.POST["patrones"]
            data.response = request.POST["respuestaNueva"]

            data.save()

            return redirect('categorias')

        else:
            data = PatternResponse.objects.filter(tag=patron)[0]
            return render(request, 'editar.html', {"data": data})

    except Exception as e:
        return render(request, 'categorias.html', {"categorias": all_categories})


# ------------------
# This handles patten removal
def eliminar_patron(request, patron):
    PatternResponse.objects.filter(tag=patron).delete()
    return redirect('categorias')


# ------------------
# This handles chatbot page
def chatbot(request):
    return render(request, 'chatbot.html')


@csrf_exempt
def predict(request):
    for element in request:
        print(element)
        response = ast.literal_eval(element.decode('utf-8'))

    prediction = chatbot_prediction(response["message"])

    return HttpResponse(json.dumps({"answer": prediction}))


def chatbot_prediction(message):
    return get_response(message)


def export2json():
    all_patterns = PatternResponse.objects.all()
    with open(r'intents.json', "w") as out:
        data = {
            "intents": []
        }
        for pattern in all_patterns:
            data['intents'].append({
                "tag": pattern.tag,
                "patterns": pattern.pattern,
                "responses": pattern.response,
                "context_set": ""
            })

        out.write(json.dumps(data))


# ------------------
# Handles everything on the Reportes page
def reportes(request):
    return render(request, 'reportes.html')
