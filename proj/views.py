from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required

# Create your views here.
@permission_required('proj.add_ped', login_url='/cadastrar/')
def index(request):
	user = get_object_or_404(User, username=request.user)
	perm = user.has_perm('proj.add_ped')
	print(perm)
	return HttpResponse('<h1>Bem vindo</h1>')


@login_required(login_url='/admin') #verifica o suario
def cadastro_user(request):
	#user = User.objects.all().filter(is_superuser=True)
	user_session = request.user
	user = User.objects.get(username=user_session)

	print(user.is_superuser)

	if user.is_superuser == True:
	 	print('Permissao concedida', user)
	else:
		messages.warning(request,'Usuário não tem Permissao')
		return HttpResponse('Usuário não tem Permissao')

	return render(request, 'cadastro_user.html')

@login_required(login_url='/admin')
def cadastrar(request):
	if request.POST:
		usuario = request.POST['usuario']
		email = request.POST['email']
		senha = request.POST['senha']
		p_nome = request.POST['p_nome']
		u_nome = request.POST['u_nome']

		try:
			existe = User.objects.get(username=usuario)
		except User.DoesNotExist as e:
			existe = None

		if existe is None:
			user = User.objects.create_user(usuario, email, senha, is_staff=True) #is_staff define que o usuario pode acessar o admin
			user.first_name = p_nome
			user.last_name = u_nome
			user.groups.add(1) #define o grupo
			user.save()
			messages.success(request, "Usuário cadastrado")
			return render(request, 'cadastro_user.html')
		else:
			messages.error(request, 'Usuario indisponivel.')
			return render(request, 'cadastro_user.html')

	else:
		return render(request, 'cadastro_user.html')

def logout(request):
	logout(request)



