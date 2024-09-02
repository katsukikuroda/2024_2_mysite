from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect  # redirect を追加

from .models import Question, Example, Choice  # Choice を追加


def index(request):
    # 新しいものから 5 個
    latest_question_list = Question.objects.all()
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        "question": question,
    }
    return render(request, "polls/detail.html", context)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        "question": question,
    }
    return render(request, "polls/results.html", context)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])  # pk が POST の choice の値と等しいものがあれば、データベースから取得する
    except (KeyError, Choice.DoesNotExist):  # 例外処理
        # フォームを再度表示する
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 10
        selected_choice.save()
        # POST データを正常に処理した後は、redirect() を返します。これにより、ユーザーが「戻る」ボタンを押した場合にデータが 2 回投稿されるのを防ぎます。
        return redirect('polls:results', question.id)


def resets(request, question_id):
    choices_to_reset = request.POST.getlist('resets')
    for choice_id in choices_to_reset:
        choice = get_object_or_404(Choice, pk=choice_id)
        choice.votes = 0  # 投票数をリセット
        choice.save()  # データベースに保存
        # POST データを正常に処理した後は、redirect() を返します。これにより、ユーザーが「戻る」ボタンを押した場合にデータが 2 回投稿されるのを防ぎます。
    return redirect('polls:results', question_id)
    

def ensyu(request, question_id):
    example_data = get_object_or_404(Example, pk=question_id)
    choices_data = example_data.choices.all()
    context = {
        "example": example_data,
        "choices_list": choices_data,
    }
    return render(request, "polls/ensyu.html", context)
