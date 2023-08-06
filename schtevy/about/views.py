from django.http import HttpResponse

def index(request):
    return HttpResponse("this will a short CV about me")