"""zoodb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('showzoo', views.showzoo, name="showzoo"),
    path('InsertZoo', views.InsertZoo, name="InsertZoo"),
    path('Insertticket', views.Insertticket, name="Insertticket"),
     path('showticket', views.showticket, name="showticket"),
     path('showanimal', views.showanimal, name="showanimal"),
     path('Insertanimal', views.Insertanimal, name="Insertanimal"),
     path('delzoo/<int:id>', views.delzoo, name="delzoo"),
     path('delticket/<int:id>', views.delticket, name="delticket"),
     path('delanimal/<int:id>', views.delanimal, name="delanimal"),
     path('sortzoo',views.sortzoo,name="sortzoo"),
     path('sortticket',views.sortticket,name="sortticket"),
      path('sortanimal',views.sortanimal,name="sortanimal"),
      path('Editzoo/<int:id>',views.editzoo,name="Editzoo"),
    path('updatezoo/<int:id>', views.updatezoo, name="updatezoo"),
    path('Editticket/<int:id>',views.editticket,name="Editticket"),
    path('updateticket/<int:id>', views.updatezoo, name="updateticket"),
    path('ProcessCustomQuery/', views.ProcessCustomQuery, name="ProcessCustomQuery"),
    path('InputCustomQuery/', views.InputCustomQuery, name="InputCustomQuery"),
    path('runQueryzoo',views.runQueryzoo,name="runQueryzoo"),
     path('runQueryticket',views.runQueryticket,name="runQueryticket"),
    path('ProcessCustomQueryforticket/', views.ProcessCustomQueryforticket, name="ProcessCustomQueryforticket"),
    # path('EditEvent/<int:id>',views.EditEvent,name="EditEvent"),
    path("", views.index,name='index'),
]


