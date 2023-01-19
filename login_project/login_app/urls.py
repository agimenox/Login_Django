from django.urls import path
from login_app.views import login_view


urlpatterns = [

    path('login/', login_view, name="login"),

]