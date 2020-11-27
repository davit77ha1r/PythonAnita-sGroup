from django.shortcuts import render, redirect

# Create your views here.

def main(request):
    return redirect("/index")
def index_page(request):
    return render(request, "main/index.html")
def about(request):
    return render(request, "main/about.html")
