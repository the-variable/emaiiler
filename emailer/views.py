from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token

from django.core.mail import EmailMessage

import json

def csrf_token_view(request):
    return JsonResponse({'csrfToken': get_token(request)})

@csrf_exempt
def send(request):
    data = json.loads(request.body)
    print(data)
    email = EmailMessage(
        subject=f"{data['name']} wants to connect with you!",
        body=data['message'],
        to=['prajincmakam0802@gmail.com'],
        reply_to=[data['email']]
        
    )
    email.send()
    return HttpResponse('Done')
