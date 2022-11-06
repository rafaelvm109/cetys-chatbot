from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "ChatIndex.html")


# Get User Input
def user_input(input):
    text = input
