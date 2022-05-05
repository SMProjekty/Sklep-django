from rest_framework import serializers
from lista.models import User, Shop, Product

#Tworzenie usera
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('UserId', 'Email','Pass')

#Rejestracja klienta (pobranie id usera)
class UserIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('UserId', 'Email')


#Tworzenie Listy
class ShopSerializer(serializers.ModelSerializer):

    class Meta:
       model = Shop
       fields = ('ShopId', 'UserId', 'NameShop')

#Tworzenie produktów
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
       model = Product
       fields = ('ProductId', 'ShopId', 'NameProduct')


