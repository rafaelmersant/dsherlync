from django.shortcuts import render
from .models import Grupo
from django.http import HttpResponse
import json


from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response


class GrupoList(APIView):

	def get(self, request, format=None):
		grupos = Grupo.objects.all()

		# response = self.serialized_producto(productos,many=True)
		# return Response(dumps(grupos))

		return HttpResponse(json.dumps(grupos), content_type="application/json")

grupos_view = GrupoList.as_view()
