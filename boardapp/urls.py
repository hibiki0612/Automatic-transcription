from django.urls import path
from . import views

urlpatterns = [
 
  path("new/",views.new,name="new"),
  path("memo/all/", views.list, name="article_all"), 
  path("memo/<int:pk>/",views.view_article,name="view_article"),
  path("article/<int:pk>/edit/",views.edit,name="edit"),
  path("memo/<int:pk>/delete/",views.delete,name="delete"),
  path('', views.article_all, name='list'),
  path('login/', views.MyLoginView.as_view(), name="login"),
  path('logout/', views.MyLogoutView.as_view(), name="logout"),
  path('create/', views.UserCreateView.as_view(),name="create")
]
