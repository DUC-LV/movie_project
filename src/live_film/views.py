from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import LiveFilm
from .serializers import LiveFilmSerializer


# Create your views here.
@csrf_exempt
def live_film_list(request):
    if request.method == 'GET':
        content = LiveFilm.objects.all()
        data = {
            "errorCode": 200,
            "message": "Successful.",
            "name": "HBO GO",
            "data": list(
                content.values('created', '_id', 'coverImage', 'coverImageH', 'description', 'slug', 'type', 'link'))
        }
        return JsonResponse(data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LiveFilmSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def live_film_detail(request, slug):
    content = LiveFilm.objects.filter(slug=slug)
    if not content.exist():
        return HttpResponse(status=404)
    content = content[0]
    if request.method == 'GET':
        serializer = LiveFilmSerializer(content)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LiveFilmSerializer(content, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        content.delete()
        return HttpResponse(status=204)


def test_search(request):
    print(request.GET.get("search_text"))
    return HttpResponse(200)
