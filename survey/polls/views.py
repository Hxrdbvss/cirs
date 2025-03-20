from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Survey, Question, Choice, TextResponse

def index(request):
    surveys = Survey.objects.all()
    return render(request, 'polls/index.html', {'surveys': surveys})

def detail(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    return render(request, 'polls/detail.html', {'survey': survey})

def vote(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    if request.method == 'POST':
        for question in survey.question_set.all():
            if question.question_type == 'text':
                response_text = request.POST.get(f'text_{question.id}')
                if response_text:
                    TextResponse.objects.create(question=question, response=response_text)
            else:
                choice_ids = request.POST.getlist(f'choice_{question.id}')
                for choice_id in choice_ids:
                    choice = Choice.objects.get(pk=choice_id)
                    choice.votes += 1
                    choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(survey.id,)))
    return render(request, 'polls/detail.html', {'survey': survey})

def results(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    return render(request, 'polls/results.html', {'survey': survey})