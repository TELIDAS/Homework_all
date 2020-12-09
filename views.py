from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def get_posts(request):
    method_post = request.method
    if method_post == 'POST':
        return HttpResponse('Post on my profile')
    if method_post == 'PUT':
        return HttpResponse('Put the information to my profile')
    if method_post == 'GET':
        return HttpResponse('Get the information from my profile')
    if method_post == 'DELETE':
        return HttpResponse('Delete my profile')
    if method_post == 'PATCH':
        return HttpResponse('New postff patch is available')
    # print(vars(HttpResponse))
    return HttpResponse('Hi master, i\'m working!')

@csrf_exempt
def get_profile(request):
    method_profile = request.method
    print(method_profile)
    if method_profile == 'POST':
        return HttpResponse('Post on my profile')
    if method_profile == 'PUT':
        return HttpResponse('Put the information to my profile')
    if method_profile == 'GET':
        return HttpResponse('Get the information from my profile')
    if method_profile == 'DELETE':
        return HttpResponse('Delete my profile')
    if method_profile == 'PATCH':
        return HttpResponse('New profile patch is available')
    return HttpResponse('My profile')
