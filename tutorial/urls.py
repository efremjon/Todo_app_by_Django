
from unicodedata import name
from django.urls import path,re_path
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('list/',views.List,name='list'),
    path('Courslist/',views.List2,name='Courslist'),
    path('center/',views.List3,name='Center'),
    path('index/<int:cours_id>/',views.new,name='index'),
    path('ditel/<int:cours_id>/<int:titel_id>',views.ditel,name='ditel'),
    path('addCatagory/',views.addCatagory,name='addCatagory'),
    path('updateCatagory/<int:cata_id>',views.updateCatagory,name='updateCatagory'),
    path('addCours/',views.addCours,name='addCours'),
    path('addTutor/',views.addTutorials,name='addTutors'),
    path('addBody/',views.addBody,name='addDesc'),
    path('<str:cours_name>/',views.home,name='home'),
    path('next/<int:cours_id>/<int:titel_id>',views.next,name='next'),
    path('group/<int:cata_id>/',views.catagory,name='group'),
    path('admin_center/',views.admin_center,name='admin_cen')
]
