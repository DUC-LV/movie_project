from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Banner
from .serializers import BannerSerializer


# Create your views here.
@csrf_exempt
def banner_list(request):
    if request.method == 'GET':
        content = Banner.objects.all()
        data = {
            "errorCode": 200,
            "message": "Successful.",
            "data": list(
                content.values('created', '_id', 'title', 'message', 'itemId', 'itemType', 'urlImage'))
        }
        return JsonResponse(data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BannerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def banner_detail(request, pk):

    try:
        content = Banner.objects.get(pk=pk)
    except Banner.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BannerSerializer(content)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BannerSerializer(content, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        content.delete()
        return HttpResponse(status=204)