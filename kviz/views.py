from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from .models import Category, Question, Answers

def index(request):
	seznam_kategorij = Category.objects.all()
	context = {'seznam_kategorij': seznam_kategorij}
	return render(request, 'kviz/index.html', context)

def detail(request, category_id):
	kategorija = get_object_or_404(Category, pk=category_id)
	vprasanja = Question.objects.all()
	odgovori = Answers.objects.all()
	context = {'kategorija': kategorija, 'vprasanja': vprasanja, 'odgovori': odgovori}
	return render(request, 'kviz/detail.html', context)

def results(request, category_id):
	kategorija = get_object_or_404(Category, pk=category_id)
	odgovori = Answers.objects.all()
	selected_answer_list = request.POST.getlist('izbran_odgovor')
	selected_answer = map(int, selected_answer_list)
	
	counter = odgovori.count()
	pravilni = 0
	for odgovor in odgovori:
		for i in selected_answer_list:
			if int(i) == odgovor.id and odgovor.solution:
				pravilni+=1

	context = {'kategorija': kategorija, 'odgovori': odgovori, 'selected_answer': selected_answer, 'counter': counter, 'pravilni': pravilni}
	return render(request, 'kviz/results.html', context)

