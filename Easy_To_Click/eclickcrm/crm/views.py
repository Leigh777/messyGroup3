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


def customer_new(request):
  #  photographer = get_object_or_404(Photographer, pk=pk)
    if request.method == "POST":
    #    form1 = CustomerForm(request.POST)
        form = CustomerForm(request.POST)
    #    form2 = PhotographerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)

            custName = customer.first_name + " " + customer.last_name
            print("Customer name is " + custName)
            print("Customer email is " + customer.email)
            send_email(custName, customer.email)

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
#  object_list = Photographer.objects.all()
#  filtered_photographer = Photographer.objects.filter(created_date__lte=timezone.now())
#  current_order_photographer = []
#  if filtered_photographer.exists():
#      user_photographer = filtered_photographer[0]

#  context = {
#      'object_list': object_list,
#      'user_photographer': user_photographer
#  }
#  print (context)
    return render(request, 'crm/photographer_list.html', {'photographers': photographer})
#    return render(request, "crm/photographer_list.html", context)


def email_add_photographer(request, pk):
   # photographer = get_object_or_404(Photographer, pk=pk)
   # user_profile = get_object_or_404(Profile, user=request.user)
    photographer = Photographer.objects.filter(pk= pk)
   # order_item, status = OrderItem.objects.get_or_create(schedule=schedule)
    # create order associated with the user
   # user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
   # user_order.items.add(order_item)
   # if status:
   #  # generate a reference code
   #  user_order.ref_code = generate_order_id()
   #  user_order.save()
    messages.info(photographer.pk, "photographer info received")
    # show confirmation message and redirect back to the same page
   # messages.info(request, "item added to cart")
    return redirect(request, ('crm:customer_new'))
#return redirect(reverse('sis:schedule_list'))

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


# def read_template(filename):
#     """
#     Returns a Template object comprising the contents of the
#     file specified by filename.
#     """
#
#     with open(filename, 'r', encoding='utf-8') as template_file:
#         template_file_content = template_file.read()
#     return Template(template_file_content)


def send_email(customerName, customerEmail):
    message_template = read_template('email_template.txt')

    # add in the actual person name to the message template
    message = message_template.substitute(PERSON_NAME=customerName) #customer_name.title())

    # add in the actual person name to the message template
    # message = message_template.substitute(PHOTO_NAME='GuhaAmin') #photographer_name.title())

    print("About to send email")
    # Param1 - Email subject
    # Param2 - Email body
    # Param3 - from email
    # Param4 - to email (tuple or array)
    try:
        send_mail("Thank you for showing your interest with KLICK2EASY!",
              message,
              "isqa4900group3@gmail.com",
              [customerEmail],
                  fail_silently=False)
        print("Email sent")
    except Exception as e:
        print(e)
    print("Outside try catch block.")


def read_template(filename):
    """
    Returns a Template object comprising the contents of the
    file specified by filename.
    """
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, filename)

    with open(file_path, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()

    # return template_file_content
    # template_file_content.replace('PERSON_NAME', 'Rashmik')
    # template_file_content.replace('PHOTO_NAME', 'Guha Amin')
    return Template(template_file_content)

def success(request, **kwargs):
    # a view signifying the transcation was successful
    return render(request, 'crm/capture_successful.html', {})

def my_profile(request):
    my_user_profile = Profile.objects.filter(user=request.user).first()
    my_photographer = Photographer.objects.filter(is_chosen=True, owner=my_user_profile)
    context = {
        'my_photograper':my_photographer
    }
    return render(request, "profile.html", context)

