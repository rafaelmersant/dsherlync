from clientes.models import Cliente
from apartados.models import DeudaCliente, AbonoCliente

from rest_framework import serializers

class AbonoSerializer(serializers.ModelSerializer):
	grupo = serializers.RelatedField(many=False)
	clasificacion = serializers.RelatedField(many=False)
	departamento = serializers.RelatedField(many=False)

	class Meta:
		model = AbonoCliente
		fields = ('id','abono','cliente','fecha',)