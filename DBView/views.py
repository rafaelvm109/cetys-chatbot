import json

from django.shortcuts import render


# Create your views here.
def index(request):
    # Opening JSON file
    data = []
    with open('DBView/static/intents.json') as json_file:
        data = json.load(json_file)

    data = data["intents"]
    categories = []

    for item in data:
        item["category"] = item["tag"].split('.')[0]
        categories.append(item["category"])

    # Eliminate duplicates
    categories = list(dict.fromkeys(categories))

    # return response
    return render(request, "test.html", {"categories": categories})


def category(request, category_id: str):
    # Opening JSON file
    data = []
    with open('DBView/static/intents.json') as json_file:
        data = json.load(json_file)

    data = data["intents"]
    categories = []

    for item in data:
        item["category"] = item["tag"].split('.')[0]
        categories.append(item["category"])

    # Eliminate duplicates
    categories = list(dict.fromkeys(categories))

    category_data = []
    for item in data:
        if item["category"] == category_id:
            category_data.append(item)

    return render(request, "test.html", {"categories": categories, "category_data": category_data})
