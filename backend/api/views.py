from django.http import JsonResponse


def api_home(request):
    return JsonResponse({'massage':'Hello and welcome to out API django app'})