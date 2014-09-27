from django.shortcuts import render

from .models import Grupo
from .serializers import GrupoSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

class GrupoListView(APIView):
	
	serialized_grupos = GrupoSerializer

	def get(self, request, pk=None, format=None):
		if pk != None:
			grupos = Grupo.objects.get(pk=pk)
			many=False	
		else:
			grupos = Grupo.objects.all()
			many=True
		response = self.serialized_grupos(grupos,many=many)
		return Response(response.data)