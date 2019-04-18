from django.shortcuts import render, redirect
from core.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
# Create your views here.

@login_required('')
def index(request):
	return render(request,'index.html', {'title':'Página inickjkkkkkkial'})

@permission_required('core.add_friend')
def persons(request):
	lista = Person.objects.all()
	return render(request,'persons.html', {'lista':lista})



from django.core import serializers
from django.http import JsonResponse

def get_persons_json(request):
	name = request.GET.get('name')
	print(name)
	lista = Person.objects.all()
	return JsonResponse(serializers.serialize('json', lista), safe=False)

def add_person(request):
	if request.method == 'POST':
		person = Person()
		person.first_name = request.POST.get('first_name')
		person.last_name  = request.POST.get('last_name')
		person.age        = request.POST.get('age')
		person.save()
		return redirect('/persons/')

	else:
		title = 'Cadastro de Pessoa'


	return render(request, 'person_add.html',{'title':title})

def add_user(request):
	if request.method == 'POST':
		user = User()
		user.first_name = request.POST.get('first_name')
		user.last_name  = request.POST.get('last_name')

		user.save()
		return redirect('/user/')

	else:
		title = 'Cadastro de Pessoa'


	return render(request, 'person_add.html',{'title':title})


def edit_person(request, person_id):
	person = Person.objects.get(id=int(person_id))
	print(person)
	if request.method == 'POST':
		#person = Person()
		person.first_name = request.POST.get('first_name')
		person.last_name  = request.POST.get('last_name')
		person.age        = request.POST.get('age')
		person.save()
		return redirect('/persons/')
	else:
		title = 'Edição de Pessoa'
	return render(request, 'person_edit.html',{'title':title, 'person':person})
