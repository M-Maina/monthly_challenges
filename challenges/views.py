from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
#def index(request):
 #   return HttpResponse('<h1>Welcome to january</h1>')


#def feb(request):
 #   return HttpResponse('<h1>Walk atleast 20 minutes a day!</h1>')


#def march(request):
  #  return HttpResponse('<h1>Learn django for atleast 30 minutes a day!</h1>')
monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for atleast 20 minutes every day!",
    "march": "Learn Django",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for atleast 20 minutes every day!",
    "june": "Learn Django",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for atleast 20 minutes every day!",
    "september": "Learn Django",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for atleast 20 minutes every day!",
    "december": "Learn Django",
    
}

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    
    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Not support Month")
    # if month == "january":
    #     challenge_text = "Eat no meat for the entire month!"
    # elif month == "february":
    #     challenge_text = "Walk for atleast 20 minutes every day!"
    # elif month == "march":
    #     challenge_text = "Learn Django"
    # else:
    #     return HttpResponseNotFound("Not support Month")
    #return HttpResponse(challenge_text)