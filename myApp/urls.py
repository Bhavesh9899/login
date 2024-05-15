from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.form,name="form"),
    path("insert/",views.InsertData,name="insert"),
    path("show",views.ShowPage,name="show"),
    path("edit/<int:pk>",views.EditPage,name="edit"),
    path("update/<int:pk>",views.UpdateData,name="update"),
    path("delete/<int:pk>",views.DeleteData,name="delete"),
    path("login",views.loginpage,name="loginpage"),
    path("loginval",views.login,name="login"),
]