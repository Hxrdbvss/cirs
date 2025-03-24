from django.shortcuts import render, redirect
from django.forms import formset_factory
from polls.models import Survey, Question, Choice
from .forms import SurveyForm, QuestionFormSet, ChoiceFormSet

def create_survey(request):
    if request.method == 'POST':
        survey_form = SurveyForm(request.POST)
        question_formset = QuestionFormSet(request.POST, prefix='questions')
        
        if survey_form.is_valid() and question_formset.is_valid():
            survey = survey_form.save()
            
            # Обрабатываем каждый вопрос
            for question_form in question_formset:
                if question_form.cleaned_data and not question_form.cleaned_data.get('DELETE', False):
                    question = question_form.save(commit=False)
                    question.survey = survey
                    question.save()
                    
                    # Обрабатываем варианты ответа для этого вопроса
                    choice_formset = ChoiceFormSet(request.POST, prefix=f'choices-{question_form.prefix}')
                    if question.question_type != 'text' and choice_formset.is_valid():
                        for choice_form in choice_formset:
                            if choice_form.cleaned_data and not choice_form.cleaned_data.get('DELETE', False):
                                choice = choice_form.save(commit=False)
                                choice.question = question
                                choice.save()
            
            return redirect('polls:index')
    else:
        survey_form = SurveyForm()
        question_formset = QuestionFormSet(prefix='questions')
    
    # Подготавливаем вложенные ChoiceFormSet для каждого вопроса
    choice_formsets = []
    for i in range(question_formset.total_form_count()):
        choice_formsets.append(ChoiceFormSet(prefix=f'choices-questions-{i}'))
    
    return render(request, 'survey_creator/create_survey.html', {
        'survey_form': survey_form,
        'question_formset': question_formset,
        'choice_formsets': choice_formsets,
    })