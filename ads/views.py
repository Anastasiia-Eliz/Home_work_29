import json

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Ads, Categories


def index(request):
	return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdsView(View):
	model = Ads

	def get(self, request):
		ads = Ads.objects.all()
		response = []
		for ad in ads:
			response.append({
				"id": ad.id,
				"name": ad.name,
				"author": ad.author,
				"price": ad.price,
				"address": ad.address,
				"description": ad.description,
				"is_published": ad.is_published
			})

		return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})

	def post(self, request):
		ads_data = json.loads(request.body)

		ads = Ads.objects.create(
			name=ads_data['name'],
			author=ads_data['author'],
			price=ads_data['price'],
			address=ads_data['address'],
			description=ads_data['description'],
			is_published=ads_data['is_published']
		)

		return JsonResponse({
			"id": ads.id,
			"name": ads.name,
			"author": ads.author,
			"price": ads.price,
			"address": ads.address,
			"description": ads.description,
			"is_published": ads.is_published
		}, safe=False, json_dumps_params={"ensure_ascii": False})


class AdDetailView(DetailView):
	model = Ads

	def get(self, *args, **kwargs):
		ad = self.get_object()

		response = {
			'id': ad.id,
			'author': ad.author,
			'name': ad.name,
			'price': ad.price,
			'description': ad.description,
			'address': ad.address,
			'is_published': ad.is_published
		}
		return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesView(View):
	model = Categories

	def get(self, request):
		cats = Categories.objects.all()

		response = []
		for cat in cats:
			response.append({
				"id": cat.id,
				"name": cat.name,
			})

		return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})

	def post(self, request):
		cats_data = json.loads(request.body)
		cats = Categories.objects.create(
			name=cats_data['name'],
		)
		return JsonResponse({
			"id": cats.id,
			"name": cats.name},
			safe=False, json_dumps_params={"ensure_ascii": False})


class CategoryDetailView(DetailView):
	model = Categories

	def get(self, *args, **kwargs):
		category = self.get_object()

		return JsonResponse({
			"id": category.id,
			"name": category.name},
			safe=False, json_dumps_params={"ensure_ascii": False})
