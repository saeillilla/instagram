from django.urls import path,include
from accounts import views
urlpatterns = [
path('signup/',views.sign_up),
path('login/',views.sign_in)
]