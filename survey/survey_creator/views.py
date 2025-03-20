from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from polls.models import Survey, Question, Choice
from .forms import SurveyForm, QuestionForm, ChoiceForm

def create_survey(request):
    if request.method == 'POST':
        survey_form = SurveyForm(request.POST)
        if survey_form.is_valid():
            survey = survey_form.save()
            return redirect('survey_creator:add_questions', survey_id=survey.id)
    else:
        survey_form = SurveyForm()
    return render(request, 'survey_creator/create_survey.html', {'survey_form': survey_form})

def add_questions(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        choice_forms = [ChoiceForm(request.POST, prefix=str(i)) for i in range(3)]  # 3 варианта по умолчанию
        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.survey = survey
            question.save()
            if question.question_type != 'text':
                for choice_form in choice_forms:
                    if choice_form.is_valid() and choice_form.cleaned_data['text']:
                        choice = choice_form.save(commit=False)
                        choice.question = question
                        choice.save()
            return redirect('survey_creator:add_questions', survey_id=survey.id)
    else:
        question_form = QuestionForm()
        choice_forms = [ChoiceForm(prefix=str(i)) for i in range(3)]
    return render(request, 'survey_creator/add_questions.html', {
        'survey': survey,
        'question_form': question_form,
        'choice_forms': choice_forms,
    })