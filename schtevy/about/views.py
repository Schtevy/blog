from django.http import HttpResponse

def index(request):
    return HttpResponse("this will a short CV about me...maybe in future the 'about' will be more a collective")