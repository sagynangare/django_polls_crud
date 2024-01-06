from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from .forms import QuestionForm, ChoiceForm


def index(request):
	ques=Question.objects.all()

	#output="<br>".join([q.question_text for q in ques])
	#return HttpResponse(output)#
	
	context={"questions":ques}

	return render(request, "polls/index.html", context)

def detail(request, question_id):
	question_detail = get_object_or_404(Question, pk=question_id)
	return render(request, "polls/detail.html", {"question":question_detail})

def vote(request, question_id):
	question_detail = get_object_or_404(Question, pk=question_id)
	try:
		ch=question_detail.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, "polls/detail.html", {"question":question_detail, 
			"error_messages":"You didn't select a choice"})
	else:
		ch.votes+=1
		ch.save()
		return HttpResponseRedirect(reverse("detail", args=(question_detail.id, )))


def add_question(request):
	if request.method=="POST":
		question=QuestionForm(request.POST)
		if question.is_valid():
			question.save()
			return HttpResponseRedirect(reverse("index"))
		else:
			return HttpResponseRedirect(reverse("add_question"))
	else:
		question=QuestionForm()
		return render(request, "polls/add_question.html", {"question":question})


def add_choice(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	if request.method=="POST":
		choice=ChoiceForm(request.POST)
		ch_txt=request.POST.get("choice_text")
		vts=request.POST.get("votes", 0)
		question.choice_set.create(choice_text=ch_txt, votes=vts)
		question.save()
		return HttpResponseRedirect(reverse("detail", args=(question.id, )))
	else:
		choice=ChoiceForm()
		return render(request, "polls/add_choice.html", {"choice":choice, "question":question})



