from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return render(request, 'cart.html')


# Create your views here.
def homePage(request):
    return render(request, 'home.html')
def servicePage(request):
    return render(request, 'services.html')
def galleryPage(request):
    return render(request, 'gallery.html')
def aboutPage(request):
    return render(request, 'about.html')
def contactPage(request):
    return render(request, 'contact.html')
def Sgift(request):
    return render(request, 'gift_pack.html')
def Sbirth(request):
    return render(request, 'birth_pack.html')
def Sevent(request):
    return render(request, 'event_pack.html')
def Sphoto(request):
    return render(request, 'photo_pack.html')
def Splan(request):
    return render(request, 'plan_pack.html')
def testPage(request):
    return render(request, 'test.html')


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist")
            return redirect('home')
        if User.objects.filter(email=email):
            messages.error(request, "email already registered")
            return redirect('home')
        if pass1 != pass2:
            messages.error(request, "Password didnot match")

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        messages.success(request, "Your Account has been sucessfully created.")
        return redirect('signin')
        
    return render(request, 'auth/signup.html')


def signin(request):
    if request.method=="POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.username 
            #return render(request, 'overview.html', {'fname': fname})
            return redirect('home')
             
        else:
            messages.error(request, "Bad Credentials!")
            return redirect('signin')

    return render(request, 'auth/signin.html')


def signout(request):
    logout(request)
    messages.error(request, "Logged Out Successfully!")
    return redirect('home')


def index(request):
    return render(request, 'auth/index.html')

def overview(request):
    return render(request, 'overview.html')

def cart(request):
    return render(request, 'cart.html')
def cart2(request):
    return render(request, 'cart2.html')
def cart3(request):
    return render(request, 'cart3.html')
def cart4(request):
    return render(request, 'cart4.html')
def bill(request):
    return render(request, 'bill.html')