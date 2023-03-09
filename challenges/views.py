from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


# Create your views here.
def index(request):
    list_items =""
    months = list(monthly_challenges.keys())
    
    return render(request, 'challenges/index.htm', {"months":months})
    
    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
        
    # respone_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(respone_data)


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
    "december": None
    
}

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    
    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    #try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.htm", {"challenge_text": challenge_text,
                                                            "month_name": month.capitalize()})
        #response_data = render_to_string("challenges/challenge.htm",)
       # return HttpResponse(response_data)
    #except:
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