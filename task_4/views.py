from django.shortcuts import render

# Create your views here.

def moscow_view(request):
    page_name = "МОСКОВСКОЕ МЕТРО"
    stations = ["Черкизовская", "Сокольники", "ВДНХ"]
    context = {
        "page_name": page_name,
        "stations": stations
    }
    return render(request, "moscow.html", context)

def petersburg_view(request):
    page_name = "ПЕТЕРБУРГСКОЕ МЕТРО"
    stations = ["Автово", "Спортивная", "Зенит"]
    context = {
        "page_name": page_name,
        "stations": stations
    }
    return render(request, "saint-petersburg.html", context)

def menu_view(request):
    metros = {"moscow": "Москва", "saint-petersburg": "Санкт-Петербург"}
    context = {
        "metros": metros,
    }
    return render(request, "menu.html", context)