from django.contrib import admin

from .models import Customer, Photographer, Comment, Payment, Photo, SocialLink


class CustomerList(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'email', 'phone_number')

    list_filter = ('first_name', 'last_name', 'email', 'phone_number')
    search_fields = ('first_name', 'last_name')
    ordering = ['first_name', 'last_name']


class PhotographerList(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'company', 'email', 'phone_number')

    list_filter = ('first_name', 'last_name', 'email', 'phone_number')
    search_fields = ('first_name', 'last_name')
    ordering = ['first_name', 'last_name']


class PaymentList(admin.ModelAdmin):

    list_display = ('photographer_id', 'payment_type', 'card_number', 'expiration_date')

    list_filter = ('photographer_id', 'payment_type', 'card_number', 'expiration_date')
    search_fields = ('photographer_id', 'payment_type', 'card_number', 'expiration_date')
    ordering = ['photographer_id', 'payment_type', 'card_number', 'expiration_date']


class PhotoList(admin.ModelAdmin):

    list_display = ('photographer_id', 'photo')

    list_filter = ('photographer_id', 'photo')
    search_fields = ('photographer_id', 'photo')
    ordering = ['photographer_id', 'photo']


class CommentList(admin.ModelAdmin):

    list_display = ('customer_id', 'photographer_id', 'photo')

    list_filter = ('customer_id', 'photographer_id', 'photo')
    search_fields = ('customer_id', 'photographer_id', 'photo')
    ordering = ['customer_id', 'photographer_id', 'photo']


class SocialLinkList(admin.ModelAdmin):

    list_display = ('photographer_id', 'site', 'link')

    list_filter = ('photographer_id', 'site', 'link')
    search_fields = ('photographer_id', 'site', 'link')
    ordering = ['photographer_id', 'site', 'link']


admin.site.register(Customer,CustomerList)
admin.site.register(Photographer, PhotographerList)
admin.site.register(Payment, PaymentList)
admin.site.register(Photo, PhotoList)
admin.site.register(Comment, CommentList)
admin.site.register(SocialLink, SocialLinkList)

