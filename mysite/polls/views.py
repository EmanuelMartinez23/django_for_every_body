from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question



def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = { "latest_question_list" : latest_question_list }
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    quuestion = get_object_or_404(Question, pk = question_id)

    return render(request, "polls/details.html", {"question": question } )

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HHttpResponse("You're voting on question %s." % question_id)



def owner(request):
    return HttpResponse("Hello, world. 11cf6447 iis the polls index." )


