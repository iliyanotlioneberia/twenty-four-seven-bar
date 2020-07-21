from django.test import TestCase
from rest_framework import status
from beer.models import BeerModel
    
class PostBeerTestCase(TestCase):
    def test_post(self):

        data = {"name" : "Test Beer",
                "beer_type" : "AL",
                "description" : "Test description" }
        response = self.client.post("/api/beer/", data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(BeerModel.objects.count(), 1)
        self.assertEqual(BeerModel.objects.get().name, "Test Beer")
        self.assertEqual(BeerModel.objects.get().beer_type, 'AL')
        self.assertEqual(BeerModel.objects.get().description, "Test description")


class GetOneBeerTestCase(TestCase):

        def setUp(self):
                BeerModel.objects.create(
                        name = "Test Beer 0",
                        beer_type = 'AL',
                        description = "Test description 0"
                )

                BeerModel.objects.create(
                        name = "Test Beer 1",
                        beer_type = 'LA',
                        description = "Test description 1"
                )

                BeerModel.objects.create(
                        name = "Test Beer 2",
                        beer_type = 'ST',
                        description = "Test description 2"
                )

        def test_get_single(self):

                beer = BeerModel.objects.all() 

                self.assertEqual(beer[0].name, "Test Beer 0")
                self.assertEqual(beer[0].beer_type, 'AL')
                self.assertEqual(beer[0].description, "Test description 0")
        
                response = self.client.get("/api/beer/1/")
                self.assertEqual(response.status_code, status.HTTP_200_OK)


        def test_get_multiple(self):

                beers = BeerModel.objects.all()

                for i in range(3):
                        response = self.client.get(f"/api/beer/{i+1}/")
                        self.assertEqual(response.status_code, status.HTTP_200_OK)

                        self.assertEqual(beers[i].name, "Test Beer " + str(i))
                        self.assertEqual(beers[i].description, "Test description " + str(i))
                        
                        if i == 0:
                                self.assertEqual(beers[i].beer_type, 'AL')
                        elif i == 1:
                                self.assertEqual(beers[i].beer_type, 'LA')
                        elif i == 2:
                                self.assertEqual(beers[i].beer_type, 'ST')
