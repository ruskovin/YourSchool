from django.shortcuts import render, redirect, get_object_or_404
from .forms import django_user_form, CustomAuthenticationForm
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import User as Student


# Create your views here.
def home_view(request,):
    if request.user.is_authenticated and request.user.username != 'paolo':
        usr = Student.objects.get(username=request.user.username)
        context={"usr":usr
                       }
    else:
        context = {}
    return render(request, 'home.html', context)


class MyLoginView(auth_views.LoginView):
    authentication_form = None
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    form_class = CustomAuthenticationForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={'form': form})

    def get_success_url(self):
        return reverse_lazy('home')

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid Username or Password')
        return self.render_to_response(self.get_context_data(request=self.request, form=form))


# def register_view(request):
#     form = NameForm()
#     if request.method == 'POST':
#         form = NameForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], password=cd['password'])
#             if user is not None:
#                 register(request,user)
#                 # return HttpResponse('Autentication succeed')
#                 return redirect('home')
#             else:
#                 return HttpResponse('Autentication failed')
#     return render(request, 'registration/register.html', {'form':form})


# def register_view(request):
#     if request.method == 'POST':
#         form = Userform(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/home')
#     else:
#         form = Userform()
#     return render(request, 'index.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = django_user_form(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(username=request.POST['username'], first_name=request.POST['first_name'],
                                                last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
            new_user.save()
            form.save()
            return redirect('login')
    else:
        form = django_user_form()
    return render(request, 'registration/register.html', {'form': form})


def profile_view(request):
    if request.user.username != 'paolo':
        profile_info = Student.objects.get(username=request.user.username)
    else:
        profile_info = None
    return render(request, 'profile.html', {'infos':profile_info})