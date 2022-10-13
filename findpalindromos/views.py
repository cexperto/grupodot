from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
# Create your views here.
from findpalindromos.palindrome import find_palindromes

def index(request):
    return HttpResponse('welcome to palindrome API')


class Palindrome(APIView):    
    def post(self, request):
        data = request.data
        if 'text' in request.data:            
            return JsonResponse({'the palindrome most long the text: ': find_palindromes(data['text'])})
        return JsonResponse({'error: ': "the key in not valide, 'text' is a valide key"})