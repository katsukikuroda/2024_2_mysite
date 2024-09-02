from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)  # 質問の内容
    pub_date = models.DateTimeField("date published")  # 作成日時
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # どの質問に対する回答か
    choice_text = models.CharField(max_length=200)  # 回答の選択肢
    votes = models.IntegerField(default=0)  # 投票数
    def __str__(self):
        return self.choice_text


class Example(models.Model):
    name = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    choices = models.ManyToManyField(Choice)  # 多対多の関係、中間テーブル（example_choices）を自動作成
    def __str__(self):
        return self.name