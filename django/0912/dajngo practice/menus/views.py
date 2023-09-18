from django.shortcuts import render

# Create your views here.
def menu(request):

    menu = [
        "창평순대국밥", "명동칼국수"
    ]

    context = {
        "menu": menu
    }
    return render(request, "menu.html", context)