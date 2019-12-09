from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path, re_path, include


app_name = 'crm'
urlpatterns = [ path('', views.home, name='home'),
                path('',views.gallery, name='gallery'),
                #path ('', views.email_add_photographer(<request>,<int:pk>), name= 'email_add_photographer'),

                #re_path(r'^blog-list/genre/(?P<genre_id>\d+)/(?P<genre_name>.+?), views.blog_list_by_genre, name='blog_list_by_genre'),
                #url(r'^email-add-photographer/(?P<pk>[-\w]+)/$', views.email_add_photographer, name="email_add_photographer"),
                url(r'^customer/create/(?P<pk>[-\w]+)/$', views.customer_new, name="customer_new"),

                #path('', views.customer_new('', <int:pk>), name = 'customer_new'),
                path('gallery', views.gallery, name='gallery'),
                path('', views.customer_list, name= 'customer_list'),
                path('customer_list', views.customer_list, name='customer_list'),
                path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
                path('', views.comment_list, name= 'comment_list'),
              #  path('customer/create/', views.customer_new, name='customer_new'),
                path('comment_list', views.comment_list, name='comment_list'),
                path('comment/<int:pk>/edit/', views.comment_edit, name='comment_edit'),
                path('', views.link_list, name= 'link_list'),
                path('link_list', views.link_list, name='link_list'),
                path('link/<int:pk>/edit/', views.link_edit, name='link_edit'),
                path('', views.payment_list, name= 'payment_list'),
                path('payment_list', views.payment_list, name='payment_list'),
                path('payment/<int:pk>/edit/', views.payment_edit, name='payment_edit'),
                path('', views.photo_list, name= 'photo_list'),
                path('photo_list', views.photo_list, name='photo_list'),
                path('photo/<int:pk>/edit/', views.photo_edit, name='photo_edit'),
                path('', views.photographer_list, name= 'photographer_list'),
                path('photographer_list', views.photographer_list, name='photographer_list'),
                path('photographer/<int:pk>/edit/', views.photographer_edit, name='photographer_edit'),
               # path('login/', views.user_login, name = 'login'),
                path('login/', auth_views.LoginView.as_view(), name='login'),
                path('logout/', auth_views.LogoutView.as_view(), name='logout'),
                path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
                path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
                path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
                path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
                path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
                     name='password_reset_confirm'),
                path('capture_successful/', views.success, name = 'capture_successful'),
                path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
                path('crm/', include('django.contrib.auth.urls')),
                # Email
                #path('', include('send.url')),
]

