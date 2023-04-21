from django.shortcuts import render, redirect
from .models import Contestants, Season
from .forms import SeasonForm


def home(request):
    if request.method == 'POST':
        form = SeasonForm(request.POST)
        if form.is_valid():
            season = form.cleaned_data['season']
            shuffle = form.cleaned_data['shuffle']
            return redirect('/results/{0}/{1}/'.format(season, shuffle),
                            {'season':season, 'shuffle':shuffle})
    else:
        form = SeasonForm(request.POST)
        return render(request, 'website/home.html', {'form':form})

def results(request, season, shuffle):
    return render(request, 'website/results.html')
