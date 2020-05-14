from django.shortcuts import render, get_object_or_404
from .models import Question
from django.http import HttpResponse, Http404
# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/index.html', {'latest_question_list': latest_question_list})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def result(request, question_id):
    response = "You're looking at the results of the questions of %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're votes on question on %s " % question_id)
