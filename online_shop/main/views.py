from django.shortcuts import render, redirect
from .models import Item
import smtplib as root
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

CATEGORIES = {"kitchen":7, "candy":6, "fish":5, "fruits":4, "juice":3, "souse":2, "pasta":1}

# Create your views here.
def send_mail(request,):
    login = 'ourdjangoshop@mail.ru'
    password = '$python333$'
    url = 'smtp.mail.ru'
    toaddr = 'ourdjangoshop@mail.ru'
    topic = request.POST.get('subject')
    contact_message = request.POST.get('message')
    contact_email = request.POST.get('email')
    name = request.POST.get('name')
    message = 'New message from contact template:\n\nTopic: {}\n\nName: {}\n\nMessage : {}\n\nEmail: {}'.format(topic,
                                                                                                                name,
                                                                                                                contact_message,
                                                                                                                contact_email)
    msg = MIMEMultipart()
    msg['Subject'] = topic
    msg['From'] = login
    body = message
    msg.attach(MIMEText(body, 'plain'))
    server = root.SMTP_SSL(url, 465)
    server.login(login, password)
    server.sendmail(login, toaddr, msg.as_string())
def send_mail_name(request):
    login = 'ourdjangoshop@mail.ru'
    password = '$python333$'
    url = 'smtp.mail.ru'
    toaddr = 'ourdjangoshop@mail.ru'
    topic = 'New Subscribation!'
    contact_email = request.POST.get('email')
    message = 'User {} subscribed to our shop Now we can send messages to this mail !\nUser: {} \nMail: {}'.format(request.user.username,request.user.username,request.POST.get('email'))
    msg = MIMEMultipart()
    msg['Subject'] = topic
    msg['From'] = login
    body = message
    msg.attach(MIMEText(body, 'plain'))
    server = root.SMTP_SSL(url, 465)
    server.login(login, password)
    server.sendmail(login, toaddr, msg.as_string())


def main(request):
    return redirect("/index")
def index_page(request):
    if request.method == 'POST':
        send_mail_name(request)
    items = Item.objects.all()
    content = {"items": items}
    return render(request, "main/index.html", content)
def about(request):
    if request.method == 'POST':
        send_mail_name(request)
    return render(request, "main/about.html")
def contact(request):
    if request.method == 'POST':
        send_mail(request)
    return render(request, "main/contact.html")

def shoplocator(request):
    if request.method == 'POST':
        send_mail_name(request)
    return render(request, "main/shoplocator.html")
def help(request):
    if request.method == 'POST':
        send_mail_name(request)
    return render(request, "main/help.html")
def privacy(request):
    if request.method == 'POST':
        send_mail_name(request)
    return render(request, "main/privacy.html")
def terms(request):
    if request.method == 'POST':
        send_mail_name(request)
    return render(request, "main/terms.html")
def search(request):
    if request.method == 'POST':
        send_mail_name(request)
    if request.method == 'POST':
        search = request.POST.get('search')
        if search == "":
            items = Item.objects.all()
            content = {"items": items}
            return render(request, "main/search.html", content, search)
        else:
            items = Item.objects.all()
            content = {"items": items,"search": search}
            return render(request, "main/search.html", content)
    return render(request, "main/search.html", content)
def checkout(request):
    if request.method == 'POST':
        send_mail_name(request)
    return render(request, "main/checkout.html")