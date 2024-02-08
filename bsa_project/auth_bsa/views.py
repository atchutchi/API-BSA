from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from rest_framework import generics
from .models import Domain
from .serializers import DomainSerializer

def home(request):
    # Redirecionar para a página que deseja exibir após o login
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Mensagem de erro
            pass
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')


from rest_framework import generics
from .models import Domain
from .serializers import DomainSerializer

class DomainListCreateAPIView(generics.ListCreateAPIView):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer

class DomainRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer

