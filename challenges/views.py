from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def index(request):
 #   return HttpResponse('<h1>Welcome to january</h1>')


#def feb(request):
 #   return HttpResponse('<h1>Walk atleast 20 minutes a day!</h1>')


#def march(request):
  #  return HttpResponse('<h1>Learn django for atleast 30 minutes a day!</h1>')


def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Eat no meat for the entire month!"
    elif month == "february":
        challenge_text = "Walk for atleast 20 minutes every day!"
    elif month == "march":
        challenge_text = "Learn Django"
    else:
        return HttpResponseNotFound("Not support Month")
    return HttpResponse(challenge_text)