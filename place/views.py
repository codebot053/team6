from django.shortcuts import render, redirect
from .models import PlaceModel, PlaceComment
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, TemplateView
from user.models import UserModel
from data_use import item_filter

# Create your views here.
def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/info')
    else:
        return render(request, 'user/home.html')

def place(request):
    if request.method == 'GET':
        is_user = request.user.is_authenticated
        if is_user:
            # 이곳에 추천모델을 넣어서 추천 장소를 불러옴
            tags = list(request.user.prefer_tags.names())
            if tags != []:
                # print(tags)
                prefer_tags = list(map(lambda x:list(PlaceModel.objects.filter(tags__name = x)), tags))
                print(prefer_tags)
            else:
                prefer_tags = []

            user_comment = PlaceComment.objects.filter(author=request.user)
            if user_comment:
                recent_comment = user_comment.latest('updated_at')
                recommend_list = item_filter(recent_comment.place.name)
                print(recommend_list)
                recommend_list = list(map(lambda x :PlaceModel.objects.filter(name = x).first(), recommend_list))
                print(recommend_list)
            else:
                recommend_list = item_filter('우도')
                recommend_list = list(map(lambda x :PlaceModel.objects.get(name = x), recommend_list))
                print(recommend_list)

            place_list = PlaceModel.objects.all()

            popular_list = list(place_list)[:10]
            # 
            return render(request, 'place/place_main.html', {'place_list':place_list, 'prefer_tags':prefer_tags, 'recommend_list':recommend_list, 'popular_list':popular_list, 'tags':tags})

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
    place_tags = place_detail.tags.all()
    place_comment = PlaceComment.objects.filter(place_id=id).order_by('-created_at')
    print(place_detail.name)
    # 만약 세부정보페이지에서 다른 장소도 추천한다면 추천모델 필요

    return render(request, 'place/place_connect.html', {'place':place_detail, 'comment':place_comment, 'place_tags':place_tags})


@login_required
def write_comment(request, id):
    if request.method == 'POST':
        current_place = PlaceModel.objects.get(id=id)
        comment = request.POST.get("comment","")
        rating = request.POST.get("rating","")

        PC = PlaceComment()
        PC.comment = comment
        # PC.rating = rating
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

@login_required
def connect(request):
    return render(request, 'place/place_connect.html')
