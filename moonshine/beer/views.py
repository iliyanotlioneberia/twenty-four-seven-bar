from rest_framework import generics
from rest_framework import status, views
from rest_framework.response import Response

from beer.models import BeerModel
from beer.serializers import BeerModelSerializer


class BeerView(views.APIView):

    def get(self, request, pk=None):
        """
            Method:             GET
            Url:                /api/beer/pk/
            Request headers:
                                {
                                    "Content-Type": "application/json",
                                    "Accept": "application/json",
                                }
            Request body:       None
            Response:
                                {
                                    beer.object.dict
                                }
        """
        try:
            beer = BeerModel.objects.get(id=pk)
            beer_serializer = BeerModelSerializer(beer)

            return Response(
                beer_serializer.data,
                status=status.HTTP_200_OK)

        except Exception as e:

            return Response(
                {'message': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

    def post(self, request):
        try:
            beer = BeerModel.objects.create(
                name = request.data.get('name'),
                beer_type = request.data.get('beer_type'),
                description = request.data.get('description'))

            beer.save()
            return Response(
                {'message':'OK'},
                 status=status.HTTP_200_OK
                )

        except Exception as e:
            return Response(
                {'message': str(e)},
                 status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )


class BeerListView(generics.ListAPIView):
    queryset = BeerModel.objects.all()
    serializer_class = BeerModelSerializer

    def get(self, request, *args, **kwargs):
        """
            Method:             GET
            Url:                /api/beers/
            Request headers:
                                {
                                    "Content-Type": "application/json",
                                    "Accept": "application/json",
                                }
            Request body:       None
            Response:
                                {
                                    beer.object.all.dict
                                }
        """
        return self.list(request, *args, **kwargs)
