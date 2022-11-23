from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.contrib import messages
from zoodb.models import animal,ticket,zoo
from zoodb.forms import zooforms
from django.db import connection


def index(request):
    template = loader.get_template('index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def showzoo(request):
    showall=zoo.objects.all()
    context = {
        'data': showall
    }
    return render(request,'showzoo.html',context)

def InsertZoo(request):
    if request.method=="POST":
        if request.POST.get('zoo_id') and request.POST.get('zoo_name') and request.POST.get('state') and request.POST.get('pincode') and request.POST.get('ticket_id') and request.POST.get('hospital_id') :
            saverecord = zoo()
            saverecord.zoo_id=request.POST.get('zoo_id')
            saverecord.zoo_name=request.POST.get('zoo_name')
            saverecord.state=request.POST.get('state')
            saverecord.pincode=request.POST.get('pincode')
            saverecord.ticket_id=request.POST.get('ticket_id')
            saverecord.hospital_id=request.POST.get('hospital_id')
            saverecord.save()
            messages.success(request,'Zoo'+saverecord.zoo_name+' is saved successfully..!')
            return render(request,'InsertZoo.html')
    else:
        return render(request, 'InsertZoo.html')

def showticket(request):
    showall=ticket.objects.all()
    context = {
        'data': showall
    }
    return render(request,'showticket.html',context)

def Insertticket(request):
    if request.method=="POST":
        if request.POST.get('ticket_id') and request.POST.get('ticket_price')  :
            saverecord = ticket()
            saverecord.ticket_id=request.POST.get('ticket_id')
            saverecord.ticket_price=request.POST.get('ticket_price')
            
            saverecord.save()
            messages.success(request,'Ticket'+saverecord.ticket_id+' is saved successfully..!')
            return render(request,'Insertticket.html')
    else:
        return render(request, 'Insertticket.html')

def showanimal(request):
    showall=animal.objects.all()
    context = {
        'data': showall
    }
    return render(request,'showanimal.html',context)

def Insertanimal(request):
    if request.method=="POST":
        if request.POST.get('animal_id') and request.POST.get('animal_name') and request.POST.get('count') and request.POST.get('extinction_id') and request.POST.get('health_id')  :
            saverecord = animal()
            saverecord.animal_id=request.POST.get('animal_id')
            saverecord.animal_name=request.POST.get('animal_name')
            saverecord.count=request.POST.get('count')
            saverecord.extinction_id=request.POST.get('extinction_id')
            saverecord.health_id=request.POST.get('health_id')
            saverecord.save()
            messages.success(request,'Animal '+saverecord.animal_name+' is saved successfully..!')
            return render(request,'Insertanimal.html')
    else:
        return render(request, 'Insertanimal.html')

def delzoo(request,id):
    delzooObj=zoo.objects.get(zoo_id=id)
    delzooObj.delete()
    showall=zoo.objects.all()
    messages.success(request,'Record deleted succesfully!!')
    context={
        "Game":delzooObj
    }
    return render(request,'delzoo.html',context)

def delticket(request,id):
    delticketObj=ticket.objects.get(ticket_id=id)
    delticketObj.delete()
    showall=ticket.objects.all()
    messages.success(request,'Record deleted succesfully!!')
    context={
        "ticket":delticketObj
    }
    return render(request,'delticket.html',context)

def delanimal(request,id):
    delanimalObj=animal.objects.get(animal_id=id)
    delanimalObj.delete()
    showall=animal.objects.all()
    context={
        "animal":delanimalObj
    }
    return render(request,'delanimal.html',context)

def sortzoo(request):
    if request.method=="POST":
        if request.POST.get('Sort'):
            type=request.POST.get('Sort')
            sorted=zoo.objects.all().order_by(type)
            context = {
                'data': sorted
            }
            return render(request,'sortzoo.html',context)
    else:
        return render(request,'sortzoo.html')

def sortticket(request):
    if request.method=="POST":
        if request.POST.get('Sort'):
            type=request.POST.get('Sort')
            sorted=ticket.objects.all().order_by(type)
            context = {
                'data': sorted
            }
            return render(request,'sortticket.html',context)
    else:
        return render(request,'sortticket.html')

def sortanimal(request):
    if request.method=="POST":
        if request.POST.get('Sort'):
            type=request.POST.get('Sort')
            sorted=animal.objects.all().order_by(type)
            context = {
                'data': sorted
            }
            return render(request,'sortanimal.html',context)
    else:
        return render(request,'sortanimal.html')

def editzoo(request,id):
    Editzoo=zoo.objects.get(zoo_id=id)
    return render(request,'Editzoo.html',{"zoo":Editzoo})
 
def updatezoo(request,id):
    Updatezoo=zoo.objects.get(zoo_id=id)
    form=zooforms(request.POST,instance=Updatezoo)
    if form.is_valid():
        form.save()
        messages.success(request,'Record updates succesfully!!')
        return render(request,'Editzoo.html',{"zoo":Updatezoo})

def editticket(request,id):
    Editticket=ticket.objects.get(ticket_id=id)
    return render(request,'Editticket.html',{"ticket":Editticket})
 
def updateticket(request,id):
    Updateticket=ticket.objects.get(ticket_id=id)
    form=zooforms(request.POST,instance=Updateticket)
    if form.is_valid():
        form.save()
        messages.success(request,'Record updates succesfully!!')
        return render(request,'Editticket.html',{"ticket":Updateticket})

def InputCustomQuery(request):
    return render(request, 'Query.html', {})


def runQueryzoo(request):
    raw_query = "select \"zoo\".\"zoo_id\",\"zoo\".\"zoo_name\",\"zoo\".\"state\",\"zoo\".\"pincode\",\"zoo\".\"hospital_id\",\"zoo\".\"ticket_id\" from \"zoo\" "
    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata = cursor.fetchall()

    return render(request, 'Query.html', {'data': alldata})


def ProcessCustomQuery(request):
    raw_query = request.POST.get('query')

    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata = cursor.fetchall()
    colnames = [desc[0] for desc in cursor.description]
   
    return render(request,'runQueryzoo.html',{'data':alldata,'colnames':colnames, 'lencol':range(len(colnames))})

# Query for Ticket

def runQueryticket(request):
    raw_query = "select \"ticket\".\"ticket_id\",\"ticket\".\"ticket_price\" from \"ticket\" "
    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata = cursor.fetchall()

    return render(request, 'Query_ticket.html', {'data': alldata})


def ProcessCustomQueryforticket(request):
    raw_query = request.POST.get('query')

    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata = cursor.fetchall()
    colnames = [desc[0] for desc in cursor.description]
    print(colnames)
    print(alldata)

    return render(request, 'runQueryticket.html', {'data': alldata})



