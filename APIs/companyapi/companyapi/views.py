from django.http import HttpResponse, JsonResponse
def homepage(request):
  print("Homepage requested")
  l = [
    'Python',
    'Java',
    'c++',
    'JavaScript'
  ]
  return JsonResponse(l,safe=False)