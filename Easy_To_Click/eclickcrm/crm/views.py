from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import *
from .forms import *
from django.shortcuts import redirect
from string import Template
from django.db.models import Sum
from django.core.mail import send_mail
from django.conf import settings
import os

now = timezone.now()


def customer_new(request, pk):
    email_photographer = Photographer.objects.get(pk=pk)
    email_photographer.save()
    photo_full_name = str(email_photographer.first_name + " " + email_photographer.last_name)
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            custName = str(customer.first_name + " " + customer.last_name)
            send_email(custName, str(customer.email), photo_full_name, str(email_photographer.company), str(email_photographer.phone_number), str(email_photographer.email))
            customer.created_date = timezone.now()
            customer.updated_date = timezone.now()
            customer.save()
            customers = Customer.objects.filter(created_date__lte=timezone.now())
            #return render (request,'crm/home.html')
            return redirect(reverse('crm:capture_successful'))

    else:
        form = CustomerForm()
        return render(request, 'crm/customer_new.html', {'form': form})
        if form.is_valid():
            form.save()

    return render(request, 'crm/customer_new.html', {'form': form})


#@login_required
def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
    # update
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.updated_date = timezone.now()
            customer.save()
            customer = Customer.objects.filter(created_date__lte=timezone.now())
            return render(request, 'crm/customer_list.html',
                          {'customers': customer})
    else:  # edit
        form = CustomerForm(instance=customer)
        # this indicates location of the html with the corresponding information nested crm
        return render(request, 'crm/customer_edit.html', {'form': form})


@login_required
def photographer_new(request):
    if request.method == "POST":
        form = PhotographerForm(request.POST)
        if form.is_valid():
            photographer = form.save(commit=False)
            photographer.created_date = timezone.now()
            photographer.save()
            photographer = photographer.objects.filter(created_date__lte=timezone.now())
            return render(request, 'crm/photographer_list.html',
                          {'photographers': photographer})
    else:
        form = PhotographerForm()
        # print("Else")
        return render(request, 'crm/photographer_new.html', {'form': form})


@login_required
def photographer_edit(request, pk):
    photographer = get_object_or_404(Photographer, pk=pk)
    if request.method == "POST":
    # update
        form = PhotographerForm(request.POST, instance=photographer)
        if form.is_valid():
            photographer = form.save(commit=False)
            photographer.updated_date = timezone.now()
            photographer.save()
            photographer = Photographer.objects.filter(created_date__lte=timezone.now())
            return render(request, 'crm/photographer_list.html',
                          {'photographers': photographer})
    else:  # edit
            form = PhotographerForm(instance=photographer)
    # this indicates location of the html with the corresponding information nested crm
    return render(request, 'crm/photographer_edit.html', {'form': form})


@login_required
def payment_new(request):
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.save()
            payment = payment.objects.filter()
            return render(request, 'crm/payment_list.html',
                          {'payments': payment})
    else:
        form = PaymentForm()
        # print("Else")
        return render(request, 'crm/payment_new.html', {'form': form})


@login_required
def payment_edit(request, pk):
    payment = get_object_or_404(Photographer, pk=pk)
    if request.method == "POST":
    # update
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.updated_date = timezone.now()
            payment.save()
            payment = Payment.objects.filter()
            return render(request, 'crm/payment_list.html',
                          {'payment': payment})
    else:  # edit
        form = PaymentForm(instance=payment)
        # this indicates location of the html with the corresponding information nested crm
        return render(request, 'crm/payment_edit.html', {'form': form})


@login_required
def photo_new(request):
    if request.method == "POST":
        form = PhotoForm(request.POST)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()
            photo = photo.objects.filter()
            return render(request, 'crm/photo_list.html',
                          {'photos': photo})
    else:
        form = PhotoForm()
        # print("Else")
        return render(request, 'crm/photo_new.html', {'form': form})


@login_required
def photo_edit(request, pk):
    photo = get_object_or_404(Photographer, pk=pk)
    if request.method == "POST":
    # update
        form = PhotoForm(request.POST, instance=photo)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.updated_date = timezone.now()
            photo.save()
            return render(request, 'crm/photo_list.html',
                          {'photo': photo})
    else:  # edit
        form = PhotoForm(instance=photo)
        # this indicates location of the html with the corresponding information nested crm
        return render(request, 'crm/photo_edit.html', {'form': form})

@login_required
def comment_new(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            comment = comment.objects.filter()
            return render(request, 'crm/comment_list.html',
                          {'comments': comment})
    else:
        form = CommentForm()
        # print("Else")
        return render(request, 'crm/comment_new.html', {'form': form})


@login_required
def comment_edit(request, pk):
    comment = get_object_or_404(Photographer, pk=pk)
    if request.method == "POST":
    # update
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.updated_date = timezone.now()
            comment.save()
            comment = Comment.objects.filter()
            return render(request, 'crm/comment_list.html',
                          {'comments': comment})
    else:  # edit
        form = CommentForm(instance=comment)
        # this indicates location of the html with the corresponding information nested crm
        return render(request, 'crm/comment_edit.html', {'form': form})


@login_required
def link_new(request):
    if request.method == "POST":
        form = LinkForm(request.POST)
        if form.is_valid():
            link = form.save(commit=False)
            link.save()
            link = link.objects.filter()
            return render(request, 'crm/link_list.html',
                          {'links': link})
    else:
        form = LinkForm()
        # print("Else")
        return render(request, 'crm/link_new.html', {'form': form})


@login_required
def link_edit(request, pk):
    link = get_object_or_404(Photographer, pk=pk)
    if request.method == "POST":
    # update
        form = LinkForm(request.POST, instance=link)
        if form.is_valid():
            link = form.save(commit=False)
            link.updated_date = timezone.now()
            link.save()
            link = SocialLink.objects.filter()
            return render(request, 'crm/link_list.html',
                          {'link': link})
    else:  # edit
        form = LinkForm(instance=link)
        # this indicates location of the html with the corresponding information nested crm
        return render(request, 'crm/link_edit.html', {'form': form})


def customer_list(request):
    customer = Customer.objects.filter(created_date__lte=timezone.now())
    return render(request, 'crm/customer_list.html', {'customers': customer})


def photographer_list(request):
    photographer = Photographer.objects.filter()
    return render(request, 'crm/photographer_list.html', {'photographers': photographer})


def comment_list(request):
    comment = Comment.objects.filter()
    return render(request, 'crm/comment_list.html', {'comments': comment})


def link_list(request):
    link = SocialLink.objects.filter()
    return render(request, 'crm/link_list.html', {'link': link})


def payment_list(request):
    payment = Payment.objects.filter()
    return render(request, 'crm/payment_list.html', {'payment': payment})


def photo_list(request):
    photo = Photo.objects.filter(uploaded_at__lte=timezone.now())
    return render(request, 'crm/photo_list.html', {'photo': photo})


def home(request):
    return render(request, 'crm/home.html', {'crm': home})


def gallery(request):
    return render(request, 'crm/gallery.html', {'crm': gallery })

def read_template(filename):
    """
    Returns a Template object comprising the contents of the
    file specified by filename.
    """

    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


def send_email(customername, customeremail, photo_full_name, photocompany, photophone, photoemail):
    message_template = read_template('email_template.txt')
    # add in the actual person name to the message template
    message = message_template.substitute(PHOTO_NAME = photo_full_name, PHOTO_COMPANY=photocompany, PHOTO_PHONE=photophone, PHOTO_EMAIL=photoemail, PERSON_NAME = customername)
    message_template2 = read_template('email_photographer_template.txt')
    message2 = message_template2.substitute(PERSON_NAME = customername, PERSON_EMAIL=customeremail, PHOTO_NAME = photo_full_name)

    try:
        send_mail("Thank you for showing your interest with KLICK2EASY!",
              message, "isqa4900group3@gmail.com",
              [customeremail], fail_silently=False)
        print("Email sent to customer")
    except Exception as e:
        print(e, "ERROR SENDING TO CUSTOMER")
    try:
        send_mail("Thank you for showing your interest with KLICK2EASY!",
                  message2, "isqa4900group3@gmail.com",
                  [photoemail], fail_silently=False)
        print("Email sent to client")
    except Exception as e:
        print(e, "ERROR SENDING TO CLIENT")




def read_template(filename):
    """
    Returns a Template object comprising the contents of the
    file specified by filename.
    """
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, filename)

    with open(file_path, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()

    return Template(template_file_content)

def success(request):
    # a view signifying the transcation was successful
    return render(request, 'crm/capture_successful.html', {})

