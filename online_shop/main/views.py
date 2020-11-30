from django.shortcuts import render, redirect
from .models import Item

# Create your views here.

def main(request):
    return redirect("/index")
def index_page(request):
    items = Item.objects.all()
    content = {"items": items}
    return render(request, "main/index.html", content)
def about(request):
    return render(request, "main/about.html")
def contact(request):
    return render(request, "main/contact.html")
def shoplocator(request):
    return render(request, "main/shoplocator.html")
def help(request):
    return render(request, "main/help.html")
def privacy(request):
    return render(request, "main/privacy.html")
def terms(request):
    return render(request, "main/terms.html")
def search(request):
    items = Item.objects.all()
    content = {"items": items}
    return render(request, "main/search.html", content)