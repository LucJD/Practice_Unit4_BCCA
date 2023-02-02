from django.test import TestCase
from app import models

# Create your tests here.


class Test_Taxi(TestCase):
    def test_can_create_taxi(self):
        taxi = models.create_taxi(3, 2, 1.5, "van")

        self.assertEqual(taxi.passengers, 2)
        self.assertEqual(taxi.occupied, True)
        self.assertEqual(taxi.taxi_number, 111)
        self.assertTrue(taxi.occupied)

        taxi2 = models.create_taxi(6, 0, 1.0, "car", "wait before loading")

        self.assertEqual(taxi2.taxi_number, 122)
        self.assertEqual(taxi2.notes, "wait before loading")
        taxi3 = models.create_taxi(5, 0, 1.4, "van")
        self.assertEqual(taxi3.taxi_number, 133)

    def test_can_update_taxi(self):

        taxi = models.create_taxi(3, 0, 1.5, "van")

        taxi2 = models.create_taxi(5, 3, 2, "car")

        self.assertFalse(taxi.occupied)

        taxi = models.send_taxi(taxi.taxi_number, 3)

        self.assertEqual(taxi.passengers, 3)
        self.assertTrue(taxi.occupied)

        # too many passengers
        with self.assertRaises(ValueError):
            models.send_taxi(taxi.taxi_number, 5)

        # taxi does not exist
        with self.assertRaises(ValueError):
            models.send_taxi(165, 4)
        # taxi is already occupied
        with self.assertRaises(ValueError):
            models.send_taxi(taxi2.taxi_number, 3)

    def test_can_end_fare(self):
        taxi = models.create_taxi(3, 0, 1.5, "van")

        taxi2 = models.create_taxi(5, 3, 2, "car")

        taxi3 = models.create_taxi(5, 0, 1.4, "van")

        self.assertEqual(models.end_fare(taxi2.taxi_number, 4.5), 9)

        # taxi not occupied
        with self.assertRaises(ValueError):
            models.end_fare(taxi.taxi_number, 3)
        # taxi does not exist
        with self.assertRaises(ValueError):
            models.end_fare(166, 3)

        # check updates occupied
        models.send_taxi(taxi.taxi_number, 3)
        self.assertEqual(models.get_taxi(taxi.taxi_number).occupied, True)
        self.assertEqual(models.get_taxi(taxi.taxi_number).passengers, 3)
        models.end_fare(taxi.taxi_number, 5.0)
        self.assertEqual(models.get_taxi(taxi.taxi_number).occupied, False)
        self.assertEqual(models.get_taxi(taxi.taxi_number).passengers, 0)

    def test_can_remove(self):
        taxi = models.create_taxi(3, 0, 1.5, "van")

        taxi2 = models.create_taxi(5, 3, 2, "car")

        taxi3 = models.create_taxi(5, 0, 1.4, "van")

        models.remove_taxi(taxi3.taxi_number)

        taxi_list = models.Taxi.objects.all()

        # check remove
        self.assertEqual(len(taxi_list), 2)

        # check that new taxi has correct number after remove
        taxi4 = models.create_taxi(1, 0, 1, "car")
        self.assertEqual(taxi4.taxi_number, 133)

    def test_can_filter(self):
        taxi = models.create_taxi(3, 0, 1.5, "van")

        taxi2 = models.create_taxi(5, 3, 2, "car")

        taxi3 = models.create_taxi(5, 0, 1.4, "van")

        free_taxis = models.find_available_taxis()
        self.assertEqual(len(free_taxis), 2)

        free_taxis_with_capacity = models.find_available_taxis(4)
        self.assertEqual(len(free_taxis_with_capacity), 1)
