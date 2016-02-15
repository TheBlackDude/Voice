from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from .models import Question, Event, Host, Post
from .forms import QuestionForm, ContactForm

def home(request):
    context = Event.objects.all()
    return render(request, 'voice/home.html', {'context': context})

def contact(request):
    form = ContactForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse_lazy('contact'))
    return render(request, 'voice/contact.html', {'form': form})

def question(request):
    context = Question.objects.all().order_by('-submit_date')[:10]
    form = QuestionForm()
    if request.method == 'POST':
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('faq'))
    return render(request, 'voice/faq.html', {'context': context, 'form': form})


def education(request):
    return render(request, 'voice/education.html')

def dawa(request):
    hosts = Host.objects.all()

    posts = Post.objects.all()
    return render(request, 'voice/dawa.html', {'hosts': hosts, 'posts': posts})

def research(request):
    return render(request, 'voice/research.html')
