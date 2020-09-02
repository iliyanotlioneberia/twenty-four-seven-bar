from rest_framework import fields, serializers
from beer.models import BeerModel


class BeerModelSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length=50)
    beer_type = serializers.ChoiceField(
         choices=(('AL', 'Ale'), ('LA', 'Lager'), ('ST', 'Stout')))
    description = serializers.CharField(max_length=500)

    class Meta:
        model = BeerModel

        fields = (
            'id',
            'name',
            'beer_type',
            'description',
        )
