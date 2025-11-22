from django.http import JsonResponse

def dummy_view(request):
    return JsonResponse({"message": "Exams app is working"})
