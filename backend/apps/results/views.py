from django.http import JsonResponse

def dummy_view(request):
    return JsonResponse({"message": "Result app is working"})
