from django.urls import path,include
from posts import views
urlpatterns = [
    path('home/',views.home),
    path('addpost/',views.addPosts),
    path('like/<post_id>/',views.add_likes),

    path('logout/',views.log_out)
]