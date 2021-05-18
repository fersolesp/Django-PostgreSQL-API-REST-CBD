from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import json 
from .models import *
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .viewsApiDjangoBase import *
from .viewsApiDjangoRestFramework import *


