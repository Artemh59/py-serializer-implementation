from io import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    return JSONRenderer().render(CarSerializer(car).data)


def deserialize_car_object(json_data: bytes) -> Car:
    serializer = CarSerializer(data=JSONParser().parse(BytesIO(json_data)))
    serializer.is_valid(raise_exception=True)
    return serializer.save()
