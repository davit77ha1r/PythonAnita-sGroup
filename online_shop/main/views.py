from django.shortcuts import render, redirect
from .models import Item
import smtplib as root
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



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
    if request.method == 'POST':
        def send_mail():
            login = 'ourdjangoshop@mail.ru'
            password = '$python333$'
            url = 'smtp.mail.ru'
            toaddr = 'ourdjangoshop@mail.ru'
            topic = request.POST.get('subject')
            contact_message = request.POST.get('message')
            contact_email = request.POST.get('email')
            name = request.POST.get('name')
            message = 'New message from contact template:\n\nTopic: {}\n\nName: {}\n\nMessage : {}\n\nEmail: {}'.format(topic, name, contact_message, contact_email)

            msg = MIMEMultipart()
            msg['Subject'] = topic
            msg['From'] = login
            body = message
            msg.attach(MIMEText(body, 'plain'))

            server = root.SMTP_SSL(url, 465)
            server.login(login, password)
            server.sendmail(login, toaddr, msg.as_string())
        send_mail()
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
def submited(request):


        return render(request, 'main/submited.html')