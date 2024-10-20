from django.urls import path, include
from . import views
urlpatterns = [
    path("",views.InsertPageView,name="InsertPage"),
    path("insert/",views.InsertData,name="insert"),
    path("showpage/",views.showPage,name="showpage"),
    path("editpage/<int:pk>",views.editPage,name='editpage'),
    path("update/<int:pk>",views.updataData,name='update'),
    path("delete/<int:pk>",views.deleteData,name='delete')
]
