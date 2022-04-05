from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from super_types.models import SuperType
from super_types.serializers import SuperTypeSerializer
from .serializers import SuperSerializer
from .models import Super, Power

# Create your views here.

@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':
        type_param = request.query_params.get('type')
        custom_response_dict = {}
        supers = SuperType.objects.all()
        if type_param:
            supers = Super.objects.filter(super_type__type=type_param)
            serializer = SuperSerializer(supers, many=True)
            return Response(serializer.data)
        for each in supers:
            sup_response = Super.objects.filter(super_type__type=each.type)
            super_serializer = SuperSerializer(sup_response, many=True)
            custom_response_dict[each.type] = super_serializer.data
        return Response(custom_response_dict)
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk):
    name = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(name)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperSerializer(name, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        name.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PATCH'])
def supers_power(request, pk, id):
    name = get_object_or_404(Super, pk=pk)
    power = get_object_or_404(Power, id=id)
    if request.method == 'PATCH':
        name.powers.add(power)
        serializer = SuperSerializer(name, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

@api_view(['GET'])
def supers_battle(request, super_name1, super_name2):
# find correct superheros/villains
    super_1 = get_object_or_404(Super, name=super_name1)
    super_2 = get_object_or_404(Super, name=super_name2)
# find length of their powers
    power_lvl1 = len(super_1.powers.all())
    power_lvl2 = len(super_2.powers.all())
# compare numbers
    if power_lvl1 > power_lvl2:
        winner = super_1
        loser = super_2
    elif power_lvl2 > power_lvl1:
        winner = super_2
        loser = super_1
    else:
        return Response(f'A victor could not be decided between f{super_1} and f{super_2}!!')
# give output
    custom_response_dict = {}
    win_serializer = SuperSerializer(winner)
    los_serializer = SuperSerializer(loser)
    custom_response_dict["Winner"] = win_serializer.data
    custom_response_dict["Loser :("] = los_serializer.data
    return Response(custom_response_dict)