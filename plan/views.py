from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Recipe, Ingredient


#def cost(obj):
#	return obj.cost

def index(request):
	latest_recipe_list = Recipe.objects.order_by('id')[:5]

	ingredient_list = []
	for recipe in latest_recipe_list:
		for ingredient in recipe.ingredient_set.all():
			ingredient_list.append(ingredient)

	ingredient_list = sorted(ingredient_list, key=(lambda x: x.cost), reverse=True)

	context = {
		'latest_recipe_list': latest_recipe_list,
		'ingredient_list': ingredient_list,
	}
	return render(request, 'plan/index.html', context)
'''
class IndexView(generic.ListView):
	template_name = 'plan/index.html'
	context_object_name = 'latest_recipe_list'

	def get_queryset(self):
		return Recipe.objects.order_by('id')[:5]
'''
class DetailView(generic.DetailView):
	model = Recipe
	template_name = 'plan/detail.html'