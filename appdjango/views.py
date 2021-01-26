from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from django.http import JsonResponse
from .managerSolutions import problemPadelLeague

# Create your views here.
@api_view(["POST"])
def liga_padel(data):
    try:
        response = problemPadelLeague(data.body)
        return JsonResponse(response,safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)