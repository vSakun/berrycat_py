from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, TemplateView

# Create your views here.
class GrowView(TemplateView):
	template_name = 'growbox/main.html'
	context_object_name = 'data'


	# def get_context_data(self):
	# 	ctx = ({
	# 		'title': 'GrowBox',
	# 		'h1': 'Tommato'
	# 		})
	# 	return ctx