from django.shortcuts import render,redirect
from django.views import View,generic
from django.contrib import messages
from django.forms.widgets import FileInput
from .forms import *
from django import contrib
from .models import Notes
from youtubesearchpython import VideosSearch
import requests,wikipedia
from django.http import HttpResponse


def home_view(request,*args,**kwargs):
    return render(request,"app/home.html",{})
def base_view(request,*args,**kwargs):
    return render(request,"app/base.html",{})

class UserRegistrationView(View):
    def get(self,request):
        form=UserRegistrationForm()
        return render(request, 'app/registration.html', locals())
    def post(self, request):
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Congratulations {username}! From now,You can have access to our courses")
            return redirect('login')
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, 'app/registration.html', locals())
def notes(request):
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            notes = Notes(user == request.POST['user'],title == request.POST['title'],description== request.POST['description'])
            notes.save()
        messages.success(request,f"Notes Added from {{user.username}}Successfully")
    else:
        form = NotesForm()
    notes = Notes.objects.filter(user=request.user)
    context = {'notes':notes,'form':form}
    return render(request,'app/Notes.html',context)
def deleteNote(request,pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect("notes")
class notesDetailView(generic.DetailView):
    model = Notes

def homework(request):
    if request.method == "POST":
        form = HomeworkForm(request.POST)
        if form.is_valid():
            try:
                finished = request.POST['is_finished']
                if finished == 'on':
                    finished = True
                else:
                    finished = False
            except:
                    finished = False
            homeworks = Homeworks(
                user = request.user,
                subject = request.POST['subject'],
                title = request.POST['title'],
                description = request.POST['description'],
                due = request.POST['due'],
                is_finished = finished
            )
            homeworks.save()
            messages.success(request,f'Homework Added from {request.user.username}!!')
    else:
        form = HomeworkForm()
    homework = Homeworks.objects.filter(user = request.user)
    if len(homework) == 0:
        homework_done = True
    else:
        homework_done = False

    context = {'homeworks': homework,'homeworks_done':homework_done,'form':form,}
    return render(request,'app/homework.html',context)

def UpdateHomework(request,pk = None):
        homework = Homework.objects.get(id = pk)
        if homework.is_finished == True:
            homework.is_finished == False
        else:
            homework.is_finished == True
        homework.save()
        return redirect('homework')
def delete_homework(request , pk = None):
    homework.objects.get(id = pk).delete()
    return redirect('homework')

liste_cours = ['HTML','CSS','C#','Csharp','django','xml','XML','mysql','MYSQL','Mysql','Databases','Bases de donnees','java','JAVA','PYTHON','python','Python','php','PHP','English','Anglais','english','anglais']

def youtube(request,val):
    if request.method == "POST":
        if request.POST['text'] in liste_cours:
            form = DashbordForm(request.POST)
            text = request.POST['text']
            video = VideosSearch(text,limit=10)
            result_list = []
            for i in video.result()['result']:
                result_dict = {
                    'input':text,
                    'title':i['title'],
                    'duration':i['duration'],
                    'thumbnail':i['thumbnails'][0]['url'],
                    'channel':i['channel']['name'],
                    'link':i['link'],
                    'views':i['viewCount']['short'],
                    'published':i['publishedTime'],
                }
                desc = '' 
                if i['descriptionSnippet']:
                    for j in i['descriptionSnippet']:
                        desc += j['text']
                result_dict['description'] = desc
                result_list.append(result_dict)
                context = {
                    'form':form,
                    'results':result_list
                }
            return render(request,'app/youtube.html',context)
        else:
            messages.warning(request,"Votre recherche est incompatible avec les options existentes")
            return HttpResponse("<h1 class='text-center text-info' style='margin-top:20%;' >Désolé! Votre recherche est incompatible avec les options existentes</h1>")
    else:
        form = DashbordForm() 
    context ={'form':form}                
    return render(request,"app/youtube.html",context)

def todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            try:
                finished = request.POST['is_finished']
                if finished == 'on':
                    finished = True
                else:
                    finished = False
            except:
                finished = False
            todos = Todo(
                user = request.user,
                title = request.POST['title'],
                is_finished = finished
            )
            todos.save()
            messages.success(request,f"Todo Added from {request.user.username}!!")
    else:
        form = TodoForm()
    todo = Todo.objects.filter(user = request.user)
    if len(todo)==0:
        todos_done = True
    else:
        todos_done = False
    context = {
        'form':form,
        'todos':todo,
        'todos_done':todos_done
    }
    return render(request,'app/todo.html',context)

def update_todo(request,pk=None):
    todo = Todo.objects.get(id = pk)
    if todo.is_finished == True:
        todo.is_finished = False
    else:
        todo.is_finished = True
    todo.save()
    return redirect('todo')

def delete_todo(request,pk=None):
    Todo.objects.get(id=pk).delete()
    return redirect('todo')

def book(request):
    if request.method == "POST":
        form = DashbordForm(request.POST)
        text = request.POST['text']
        url = "https://www.googleapis.com/books/v1/volumes?q=" +text
        r = requests.get(url)
        answer = r.json()
        result_list = []
        for i in range(10):
            result_dict = {
                'title':answer['items'][i]['volumeInfo']['title'],
                'subtitle':answer['items'][i]['volumeInfo'].get('subtitle'),
                'description':answer['items'][i]['volumeInfo'].get('description'),
                'count':answer['items'][i]['volumeInfo'].get('pageCount'),
                'categories':answer['items'][i]['volumeInfo'].get('categories'),
                'rating':answer['items'][i]['volumeInfo'].get('pageRating'),
                'thumbnail':answer['items'][i]['volumeInfo'].get('imageLinks').get('thumbnail'),
                'preview':answer['items'][i]['volumeInfo'].get('previewLink')
            }
            
            result_list.append(result_dict)
            context = {
                'form':form,
                'results':result_list
            }
        return render(request,'app/books.html',context)
    else:
        form = DashbordForm()
    context = {'form':form}
    return render(request,"app/books.html",context)

def dictionary(request):
    if request.method == "POST":
        form = DashbordForm(request.POST)
        text = request.POST['text']
        url = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"+text
        r = requests.get(url)
        answer = r.json()
        try:
            phonetics = answer[0]['phonetics'][0]['text']
            audio = answer[0]['phonetics'][0]['audio']
            definition = answer[0]['meanings'][0]['definitions'][0]['definition']
            example = answer[0]['meanings'][0]['definitionS'][0]['example']
            synonyms = answer[0]['meanings'][0]['definitions'][0]['synonyms']
            context = {
                'form': form,
                'input':text,
                'phonetics':phonetics,
                'audio': audio,
                'definition': definition,
                'example':example,
                'synonyms':synonyms
            }
        except:
            context = {
                'form':form,
                'input':''
            }
        return render(request,"app/dictionary.html",context)
    else:
        form = DashbordForm()
        context = {
            'form':form
        }
    return render(request,"app/dictionary.html",context)

def wiki(request):
    if request.method == "POST":
        text = request.POST['text']
        form = DashbordForm(request.POST)
        search = wikipedia.page(text)
        context = {
            'form':form,
            'title':search.title,
            'link':search.url,
            'details':search.summary
        }
        return render(request,"app/wikip.html",context)
    else:
        form = DashbordForm()
        context = {
            'form':form
        }
    return render(request,"app/wikip.html",context)

def profile(request):
    homeworks = Homeworks.objects.filter(is_finished = False,user = request.user)
    todos = Todo.objects.filter(is_finished = False,user = request.user)
    if len(homeworks)== 0:
        homework_done = True
    else:
        homework_done = False
    if len(todos) == 0:
        todos_done = False
    context = {
        'homeworks':homeworks,
        'todos':todos,
        'homework_done':homework_done,
        'todos_done':todos_done
    }
    return render(request,"app/profile.html",context)

class Course(View):
    def get(self, request,val):
        p_file = FichierPdf.objects.filter(fileType = val)
        title = FichierPdf.objects.filter(fileType = val).values('title')
        return render(request, 'app/files.html',locals()) 

class CourseTitle(View):
    def get(self,request,val):
        p_file=FichierPdf.objects.filter(title=val)
        #recuperer le title des produits de chaque valeur de category 
        title = FichierPdf.objects.filter(fileType=p_file[0].fileType).values('title')
        return render(request, "app/files.html", locals())

def about_view(request):
    return render(request,"app/about.html")

def contact_view(request):
    return render(request,"app/contact.html")

        