from django.shortcuts import render

# Create your views here.

def home(request):
	import json
	import requests

	api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=10014&distance=25&API_KEY=29CB3F57-4FAE-4ED5-A7B2-0ACB63DC67B2")
	
	try:
		api = json.loads(api_request.content)

	except Exception as e:
		api = "Error..."


	if api[0]['AQI'] <= 50:
		weather_suggestion = "Air Quality is considered satisfactory, and air pollution poses little or no risk."
	elif api[0]['AQI'] <= 100:
		weather_suggestion = "Air Quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution"
	elif api[0]['AQI'] <= 100:
		weather_suggestion = "Although general public is not likely to be affected at this AQI range, people with lung diseasem older adults and children are at greater risk from the presence at particles in the air."
	elif api[0]['AQI'] <= 200:
		weather_suggestion = "Everyone may begin to experience health effects, members of sensitive groups may experience more serious health effects."
	elif api[0]['AQI'] <= 300:
		weather_suggestion = "Health Alert: everyone may experience more serious health effects."
	elif api[0]['AQI'] <= 500:
		weather_suggestion = "Health warning for emergency conditions."	

	return render(request, 'home.html', {
		'api' : api, 
		'weather_suggestion' : weather_suggestion,
		})

def about(request):
	return render(request, 'about.html', {})

