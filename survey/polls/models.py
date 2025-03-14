from django.db import models

class Survey(models.Model):
    title = models.CharField(max_length=200)  # Название опроса
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания

    def __str__(self):
        return self.title

class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)  # Связь с опросом
    text = models.CharField(max_length=200)  # Текст вопроса

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # Связь с вопросом
    text = models.CharField(max_length=200)  # Текст варианта
    votes = models.IntegerField(default=0)  # Количество голосов

    def __str__(self):
        return self.text