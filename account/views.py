from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')
        extra_phone_number = request.POST.get('extra_phone_number')
        address = request.POST.get('address')
        User.objects.create_user(
            username = username,
            password = password,
            phone_number = phone_number,
            extra_phone_number = extra_phone_number,
            address = address,
        )
        return redirect("index_url")
    return render(request,'register.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        usr = authenticate(username=username, password=password)
        if usr is not None:
            login(request, usr)
        return redirect("index_url")
    return render(request,'login.html')


def logout_view(request):
    logout(request)
    return redirect('index_url')

def update_view(request, pk):
    if request.method == "POST":
        user = User.objects.get(pk=pk)
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')
        extra_phone_number = request.POST.get('extra_phone_number')

        address = request.POST.get('address')

        if username is not None:
            user.username = username
        if password is not None:
            user.password = password
        if phone_number is not None:
            user.phone_number = phone_number
        if extra_phone_number is not None:
            user.extra_phone_number = extra_phone_number
        if address is not None:
            user.address = address
    return redirect('index_url')










