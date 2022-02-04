from xml.etree.ElementTree import Comment
from django.shortcuts import render, redirect
from .models import PlaceModel, PlaceComment
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, TemplateView

# Create your views here.
def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/info')
    else:
        return render(request, 'user/home.html')

def place(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            # 이곳에 모델을 넣어서 추천 장소를 불러옴
            # 
            # 
            # 
            # 
            return render(request, 'place/place_main.html')
        else:
            return redirect('/')


@login_required
def delete_place(request, id):
    place = PlaceModel.objects.get(id=id)
    place.delete()
    return redirect('/info')

@login_required
def detail_place(request, id):
    place_detail = PlaceModel.objects.get(id=id)
    place_comment = PlaceComment.objects.filter(place_id=id).order_by('-created_at')
    return render(request, 'place/place_detail.html', {'place':place_detail, 'comment':place_comment})


@login_required
def write_comment(request, id):
    if request.method == 'POST':
        current_place = PlaceModel.objects.get(id=id)
        comment = request.POST.get("comment","")
        rating = request.POST.get("rating","")

        PC = PlaceComment()
        PC.comment = comment
        PC.rating = rating
        PC.place = current_place
        PC.author = request.user
        PC.save()

        return redirect('/info/'+str(id))

@login_required
def delete_comment(request, id):
    comment = PlaceComment.objects.get(id=id)
    current_place = comment.place.id
    comment.delete()
    return redirect('/info/'+str(current_place))