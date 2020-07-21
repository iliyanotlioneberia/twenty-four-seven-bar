from rest_framework import generics
from rest_framework import status, views
from rest_framework.response import Response

from beer.models import BeerModel
from beer.serializers import BeerModelSerializer


class BeerView(views.APIView):

    serializer_class = BeerModelSerializer

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
            beer_serializer = self.serializer_class(beer)

            return Response(
                beer_serializer.data,
                status=status.HTTP_200_OK)

        except Exception as ex:

            return Response(
                {'message': str(ex)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

    def post(self, request):

        beer = BeerModel.objects.create(
            name=request.data.get('name'),
            beer_type=request.data.get('beer_type'),
            description=request.data.get('description'))

        beer.save()
        if beer:
            return Response({'message':'OK'}, status=status.HTTP_200_OK)

        return Response({'message': 'An error occured'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
