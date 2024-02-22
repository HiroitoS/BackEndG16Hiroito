from rest_framework import serializers
from .models import Plato

class PlatoSerializers(serializers.ModelSerializer):
    class Meta:
        # el modelo en el cual se utilizaran de referencia para convertir la data de la bd y viceversa
        model= Plato
        # fields> indicar que comulnas quiero mostrar
        # exclude> indicar que colmunas quiero excluir
        # NOTA: solo se puede utilizar uno de los dos, no los dos
        # fields=['id', 'nombre','foto']
        # si estoy utilizando todos los atributos 

        fields = '__all__'
        # exclude = ['id']