from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import ListFilmSerializers, TopicFilmSerializers
from .models import *


# Create your views here.


@csrf_exempt
def list_film_list(request):
    if request.method == 'GET':
        content1 = TopicFilm.objects.all()
        data = []
        for item1 in content1:
            content2 = item1.listfilm_set.all()
            item1_data = {
                'name': item1.name,
                'description': item1.description,
                'slug': item1.slug,
                'type': item1.type,
                'itemType': item1.itemType
            }
            list_film = []
            for item2 in content2:
                list_film.append(
                    {
                        'name': item2.name,
                        'coverImage': item2.coverImage,
                        'coverImageH': item2.coverImageH,
                        'type': item2.type,
                        'description': item2.description,
                        'slug': item2.slug,
                        'link': item2.link,
                    }
                )
            item1_data['contents'] = list_film
            data.append(item1_data)

        return JsonResponse(data, safe=False)

    # elif request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     serializer = ListFilmSerializers(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=400)
