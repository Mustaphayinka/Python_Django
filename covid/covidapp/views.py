from django.shortcuts import render
import requests
from django.http import JsonResponse
# import jsonlib
import jsons
import json

url = "https://covid-193.p.rapidapi.com/history"

# querystring = {"country":"All","day":"2020-06-02"}
querystring = {"country":"nigeria","day":"2020-06-02"}


headers = {
	"X-RapidAPI-Key": "3ed6d9880dmshb30522d4c60cf50p1b1f9bjsn13e0e856a185",
	"X-RapidAPI-Host": "covid-193.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring).json()
print(response)


def helloworldview(request):
    if request.method == 'POST':
        print('coming...')
        # selected_country = request.POST['selectedcountry']
    #     print("This is the selected country", selected_country)
    #     noofresults = int(response['results'])
    #     for x in range(0, noofresults):
    #         if selected_country==response['response'][x]['country']:
    #             print(response['response'][x]['cases'])
    # # print(response['response'][0])
    # # print(response['response'][1])
    data = response['response']
    d = data[0]
    context = {
        'all':d['cases']['total'],
        'recovered':d['cases']['recovered'],
        'deaths': d['deaths']['total'],
        'new': d['cases']['new'],
        'critical': d['cases']['critical'],
        'population': d['population'],
    }

    return render(request, 'helloworld.html', context)
