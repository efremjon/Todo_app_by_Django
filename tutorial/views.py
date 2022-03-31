from importlib.resources import contents
from multiprocessing import context
from django.shortcuts import redirect
from django.shortcuts import render
from .models import Cataory,Coures, Tutoris
from .forms import Cataoryform,CouresForm,TutorisForm,BodycorsForms,UpdateCataoryform
# Create your views here.

def home(request):
    all_catagory=Cataory.objects.all()
    all_Cours=Coures.objects.all()
    context={
        'all_catagory':all_catagory,
        'all_Cours':all_Cours
        }
    return render(request,'home.html',context)
def new(request,cours_id):
    all_catagory=Cataory.objects.all()
    all_Cours=Coures.objects.all()
    specfic_cours=Coures.objects.get(pk=cours_id)
    context={
        'all_catagory':all_catagory,
        'all_Cours':all_Cours,
        'specfic_cours':specfic_cours, 
        }
    return render(request,'index.html',context)


def next(request,cours_id,titel_id):
    next=titel_id
    all_catagory=Cataory.objects.all()
    all_Cours=Coures.objects.all()
    if request.method == 'POST':
        next=next+1
        specfic_cours=Coures.objects.get(pk=cours_id)
        selecte_titel=specfic_cours.tutoris_set.get(pk=next)
        context={

        'all_catagory':all_catagory,
        'all_Cours':all_Cours,
        'specfic':specfic_cours,
        'selecte_titel':selecte_titel,

        }
    return render(request,'view.html',context)


def ditel(request,cours_id,titel_id):
   
    all_catagory=Cataory.objects.all()
    all_Cours=Coures.objects.all()
    specfic_cours=Coures.objects.get(pk=cours_id)
    selecte_titel=Tutoris.objects.get(pk=titel_id)
   
    context={
        'all_catagory':all_catagory,
        'all_Cours':all_Cours,
        'specfic':specfic_cours,
        'selecte_titel':selecte_titel,
        
        }
    return render(request,'view.html',context)

def addCatagory(request):
    if request.method == 'POST':
        form = Cataoryform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=Cataoryform()
    context={'form':form,}
    return render(request,'addCatagory.html',context)

def addCours(request):
    if request.method == 'POST':
        form = CouresForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=CouresForm()

    context={'form':form,}
    return render(request,'addCours.html',context)
def addTutorials(request):
    if request.method == 'POST':
        form = TutorisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=TutorisForm()
    context={'form':form,}
    return render(request,'addTutorial.html',context)
def addBody(request):
    if request.method == 'POST':
        form = BodycorsForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=BodycorsForms()
    context={'form':form,}
    return render(request,'addBody.html',context)

def List(request):
   
    all_catagory=Cataory.objects.all()
  
    context={
        'all_catagory':all_catagory,
      
        
        }
    return render(request,'catagoryList.html',context)


def List2(request):
   
   
    all_Cours=Coures.objects.all()
    context={
      
        'all_Cours':all_Cours,
        
        }
    return render(request,'CoursList.html',context)

def List3(request):
   
   
    all_Cours=Coures.objects.all()
    context={
      
        'all_Cours':all_Cours,
        
        }
    return render(request,'admin_center.html',context)


def updateCatagory(request, id1):
    if request.user.is_authenticated:
        current_user = request.user
        tasks=current_user.task_set.get(pk=id1)
    
        if request.method == 'POST':
            form = UpdateCataoryform(request.POST,instance=tasks)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = UpdateCataoryform(instance=tasks)
    
    context={
           'form':form,
           }
    return render(request,'updateCataroy.html',context)

def catagory(request, cata_id):
    all_catagory=Cataory.objects.all()
    all_Cours=Coures.objects.all()
    eachcatagory=Cataory.objects.get(pk=cata_id)
  
    context={
        'all_catagory':all_catagory,
        'all_Cours':all_Cours,
        'eachcatagory':eachcatagory,
        }
    return render(request,'catagorycours.html',context)

def admin_center(request):
    name='efrem'
    return render(request,'admin_center.html',{'name':name})