from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from rest_framework.generics import ListAPIView
from .serializers import questionSerializer,choiceSerializer
# Create your views here.
class index(ListView):
    success_url = reverse_lazy('details')
    template_name = 'index.html'
    # if we donot use context_object_name then we get all list by 'object_list' in html file
    context_object_name = 'questions'

    def get_queryset(self):
        return Question.objects.all().order_by('-pub_date')

class details(DetailView):
    model = Question
    success_url = reverse_lazy('vote')
    template_name = 'details.html'
    
    
# def index(req):
#     # order questions in descending order (-date)
#     questions = Question.objects.order_by('-pub_date')
#     #questions = Question.objects.all()
#     return render(req, 'index.html',{'questions':questions})

# def details(req, pk):
#     # choice = Question.objects.get(pk=pk)
#     choice = get_object_or_404(Question, pk=pk)
#     return render(req, 'details.html', {'choice':choice})

def vote(req,pk):
    question = get_object_or_404(Question, pk=pk)
    session_key = 'viewed_ques_{}'.format(question.pk)
    if not req.session.get(session_key, False):
        question.viewsofquestion += 1
        question.save()
        req.session[session_key] = True
    try:
        selected_choice = question.choice_set.get(pk=req.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(req, 'details.html', {'choice':question, 'msg':'Please select a option'})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return render(req, 'result.html',{'ques':question})


class questionList(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = questionSerializer
