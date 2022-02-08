from django.shortcuts import render, redirect
from .models import UserModel
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def sign_up_view(request):
    if request.method =='GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/sign_up.html')
    elif request.method == 'POST':
        # id는 db에 username으로 저장됨
        username = request.POST.get('userID', '')
        # 와이어프레임과달리 패스워드 확인이필요
        password = request.POST.get('userPW', '')
        password2 = request.POST.get('userPW2', '')
        # 이름은 first_name에 저장함
        name = request.POST.get('userName', '')
        email = request.POST.get('userEmail','')
        
        if password != password2:
            # password다르다고알람
            return render(request, 'user/sign_up.html', {'error':'패스워드를 확인해주세요!'})
        else:
            if username == '' or password == '':
                return render(request, 'user/sign_up.html', {'error':'사용자이름과 패스워드는 필수입니다!'})

            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'user/sign_up.html', {'error':'사용자가 존재합니다!'})
            else:
                UserModel.objects.create_user(username=username, password=password, first_name=name, email=email)
                return redirect('/sign-in')


def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        me = auth.authenticate(request, username=username, password=password)
        
        if me is not None:
            auth.login(request, me)
            return redirect('/')
        else:
            return render(request, 'user/sign_in.html', {'error':'유저이름 혹은 패스워드를 확인해주세요!'})
        
    elif request.method == "GET":
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/sign_in.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required
def tags(request):
    if request.method == "GET":
        user = request.user
        tag_list = list(user.prefer_tags.names())
        return render(request, 'user/user_tag.html', {'tag_list':tag_list})
    elif request.method == 'POST':
        user = request.user
        user_tags = request.POST.get('tags', '')
        user_tags = user_tags.split('#')
        user.prefer_tags.clear()
        for tag in user_tags:
            tag = tag.strip()
            if tag != '': # 태그를 작성하지 않았을 경우에 저장하지 않기 위해서
                user.prefer_tags.add(tag)
        user.save()
        
        return redirect('/tags')