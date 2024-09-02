from django.urls import path  # path() 関数をインポート

from . import views  # ビュー関数を登録するため、views.py をインポート

app_name = "polls"
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("ensyu<int:question_id>/", views.ensyu, name="ensyu"),
    path("<int:question_id>/resets/", views.resets, name="resets"),
]