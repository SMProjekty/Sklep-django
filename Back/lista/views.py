from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from lista.models import User, Shop, Product

from lista.serializers import UserSerializer, UserIdSerializer, ShopSerializer, ProductSerializer

#Rejestracja użytkownika
@csrf_exempt
def registerApi(request, id=0):
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        register_serializer = UserSerializer(data = user_data)
        if register_serializer.is_valid():
            register_serializer.save()
            user = User.objects.filter(Email = user_data['Email'], Pass = user_data['Pass'])
            userid_serializer = UserIdSerializer(user, many = True)
            return JsonResponse("Success to Add", safe = False)
        return JsonResponse("Failed to Add", safe = False)

@csrf_exempt
def userIdApi(request, id=0):
    if request.method == 'GET':
        user = User.objects.all()
        user_serializer = UserSerializer(user, many = True)
        return JsonResponse(user_serializer.data, safe=False)


#Logowanie
@csrf_exempt
def loginApi(request, id=0):
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        if (user_data['Email'] != "" or user_data['Pass'] != ""):
            if(User.objects.filter(Email = user_data['Email'], Pass = user_data['Pass'])):
                user = User.objects.filter(Email = user_data['Email'], Pass = user_data['Pass'])
                user_serializer = UserIdSerializer(user,  many = True)
                return JsonResponse(user_serializer.data, safe = False)
    return JsonResponse("Failed to Add", safe = False)


#Lista produktów
@csrf_exempt
def shopApi(request, id=0):
    if request.method == 'GET':
        shop = Shop.objects.filter(UserId=id)
        shop_serializer = ShopSerializer(shop, many = True)
        return JsonResponse(shop_serializer.data, safe = False)

    elif request.method=='DELETE':
        shop = Shop.objects.get(ShopId=id)
        shop.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

    elif request.method == 'POST':
        shop_data = JSONParser().parse(request)
        shop_serializer = ShopSerializer(data = shop_data)
        if shop_serializer.is_valid():
            shop_serializer.save()
            return JsonResponse("Shop Added Successfully", safe = False)
        return JsonResponse("Failed to Add", safe = False)

    return JsonResponse("Failed to Add", safe = False)

#Produkty (dizałanie podczas działania na listach)
@csrf_exempt
def productApiShop(request, id=0):
    if request.method == 'GET':
        product = Product.objects.filter(ShopId=id)
        product_serializer = ProductSerializer(product, many = True)
        return JsonResponse(product_serializer.data, safe = False)

    elif request.method=='DELETE':
        # product = Product.objects.get(ShopId=id)
        product = Product.objects.filter(ShopId=id).delete()
        # product.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

    elif request.method == 'POST':
        product_data = JSONParser().parse(request)
        product_serializer = ProductSerializer(data = product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse("Shop Added Successfully", safe = False)
        return JsonResponse("Failed to Add", safe = False)

    return JsonResponse("Failed to Add", safe = False)

#Akcje związane z produktami
@csrf_exempt
def productApi(request, id=0):
    if request.method == 'GET':
        product = Product.objects.filter(ShopId=id)
        product_serializer = ProductSerializer(product, many = True)
        return JsonResponse(product_serializer.data, safe = False)

    elif request.method=='DELETE':
        # product = Product.objects.get(ShopId=id)
        product = Product.objects.filter(ProductId=id).delete()
        # product.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

    return JsonResponse("Failed to Add", safe = False)