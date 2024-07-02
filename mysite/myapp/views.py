from django.shortcuts import render, redirect
from .models import Food,Consume
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
# Create your views here.
def index(request):
 
    if request.method =="POST":
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user,food_consumed=consume)
        consume.save()
 
    foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)

    print(foods)
 
    return render(request,'myapp/index.html',{'foods':foods,'consumed_food':consumed_food})
 
def delete_consume(request,id):
    consumed_food = Consume.objects.get(id=id)
    if request.method =='POST':
        consumed_food.delete()
        return redirect('/')
    return render(request,'myapp/delete.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'myapp/login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'myapp/signup.html', {'form': form})
 