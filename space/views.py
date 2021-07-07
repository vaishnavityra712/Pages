from django.http import HttpResponse
from django.shortcuts import render
from space.models import Write

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def write(request):

    context = {'success' : False}
    if request.method == "POST":
        # handle the form
        title = request.POST['title']
        desc = request.POST['desc']
        print(title, desc)
        ins = Write(page_Heading=title, page_description=desc)
        ins.save()
        context = {'success' : True}
        


    return render(request, 'write.html', context)

def notes(request):
    all = Write.objects.all()

    '''
    print(all)
    for item in all:
        print(item.page_Heading,"-" ,item.page_description, "-", item.time)
    '''
    context = {'notes' : all}
    return render(request, 'notes.html', context)

