# urls in our profiles_api app

from django.urls import path
from profiles_api import views # which contains our APIViews


# Next, we need to create a new variable of list:
urlpatterns = [
    path('hello-view', views.HelloApiView.as_view()),  # 'hello-view' is the name of our url, and we are mapping it to views.** views
]
