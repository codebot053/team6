import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def item_filter(place):
    # csv 데이터 불러오기
    df = pd.read_csv("place_review_summary.csv")
    # 데이터 테이블 형성
    user_place = df.pivot_table('rating', index='name', columns='author')
    user_place = user_place.fillna(0)
    # 사이킷런을 활용하여 코사인 유사도 계산
    item_based_collab = cosine_similarity(user_place, user_place)
    item_based_collab = pd.DataFrame(item_based_collab, index=user_place.index, columns=user_place.index)
    # 확률이 높은 10개 선택하여 리스트 생성
    return list(item_based_collab[place].sort_values(ascending=False)[1:11].index)
