from django import forms
from polls.models import Survey, Question, Choice

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['title']
        labels = {'title': 'Название опроса'}

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text', 'question_type']
        labels = {'text': 'Текст вопроса', 'question_type': 'Тип вопроса'}

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['text']
        labels = {'text': 'Вариант ответа'}