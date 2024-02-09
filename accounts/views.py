from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from .forms import UserUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Commissionaire
from back.models import Formation, Emploi, Achat
from django.contrib.auth import get_user_model


User = get_user_model()


def Register(request):
    template_name = 'accounts/register.html'
    if request.method == 'POST':
        email = request.POST['email']   
        phone = request.POST['phone']
        full_name = request.POST['full_name']
        birthday = request.POST['birthday']
        gender = request.POST['gender']
        profile = request.POST['profile']
        password = request.POST['password']
        if User.objects.filter(email=email):
            messages.warning(request, "Cet email existe déjà")
            return redirect('accounts:register')
        else:
            user = User.objects.create_user(email, password)
            user.phone = phone
            user.full_name = full_name
            user.birthday = birthday
            user.gender = gender
            user.profile = profile
            user.save()
            if user:
                auth = authenticate(username=user.email, password=password)
                if auth is not None:
                    login(request, auth)
                    messages.success(request, "Enregistrement réussit")
                    return redirect('home:home')
    return render(request, template_name, {})


def Login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if request.method=='POST':
        if(User.objects.filter(email=email).exists()):
            user = authenticate(username=email, password=password)
        else:
            messages.error(request, "Données incorrects! Réessayez")
            return redirect('home:home')
        if user is not None:
            login(request, user)
            return redirect('home:home')
        else:
            messages.error(request, "Mot de passe incorrects! Réessayez")
            return redirect('home:home')
    else:
        return render(request, 'home/index.html')


@login_required
def Logout(request):
    logout(request)
    return redirect('home:home')


@login_required
def Profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    comms = Commissionaire.objects.all()
    is_comm = False
    for item in comms:
        if item.user == request.user:
            is_comm = True
    context = {
        'user': user,
        'comms': comms,
        'is_comm': is_comm,
    }
    return render(request, 'accounts/profile.html', context)


@login_required
def UpdateProfile(request, pk):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('accounts:profile', args=[pk]))
        else:
            messages.error(request, "Erreur de mise à jour! Réessayez")
            return HttpResponseRedirect(reverse('accounts:update_profile', args=[pk]))
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'accounts/update_profile.html', {'form': form})
    

@login_required
def MesFormations(request):
    current_user = request.user
    formations = current_user.formation_set.all()
    template_name = 'accounts/formations.html'
    context = {
        'formations': formations,
    }
    return render(request, template_name, context)


@login_required
def MesCommandes(request):
    current_user = request.user
    commandes = Achat.objects.filter(user=current_user, livraison='en cours')
    template_name = 'accounts/commandes.html'
    context = {
        'commandes': commandes,
    }
    return render(request, template_name, context)


@login_required
def MesCommissions(request):
    current_user = request.user
    commissions = Commissionaire.objects.filter(user=current_user)
    template_name = 'accounts/commissions.html'
    context = {
        'commissions': commissions,
    }
    return render(request, template_name, context)
    