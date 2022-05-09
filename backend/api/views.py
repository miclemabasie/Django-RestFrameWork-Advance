from django.http import JsonResponse

def api_home(request, *args, **kwargs):

    return JsonResponse({"message": "hi there, this is your django api response"})