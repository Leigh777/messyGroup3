from django import forms
from .models import Customer, Photographer, Comment, Payment, Photo, SocialLink, Post


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email','phone_number', 'created_date')


class PhotographerForm(forms.ModelForm):
    class Meta:
        model = Photographer
        fields = ('first_name', 'last_name', 'company', 'email', 'address', 'city', 'state', 'zipcode', 'phone_number',
                  'created_date')


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('photographer_id', 'payment_type', 'card_number', 'expiration_date', 'pin', 'p_description')


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('photographer_id', 'photo', 'uploaded_at')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('customer_id', 'photographer_id', 'publish', 'photo', 'uploaded_at')


class LinkForm(forms.ModelForm):
    class Meta:
        model = SocialLink
        fields = ('photographer_id', 'site', 'link')

class LoginForm (forms.Form):
        username = forms.CharField()
        password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)