import requests
	def weather_info(query):
		api= "acf3e20cc24ca3b0c786b5d5bd4ad252"
		url = "http://api.openweathermap.org/data/2.5/forcast?"
		whole_url = url + "appid=" + api +"&" + query
		res=requests.get(whole_url);
		return response.json();

	def display_info(weather, city):
		print("{}'s temperature: {} C".format(city, weather['main']['temp']))

	def main():
		city=input("Enter the city name or zipcode: ")
		print()

	try:
		query='q='+city;
		w_data=weather_data(query);
		disyplay_info(w_data, city)
		print()
	except:print("City name not found")

	if __name__=='__main__':
		main()

anotherseach = 'yes'
while another_search == 'yes' or another_search == 'y':
	import requests
	def weather_info(query):
		api= "acf3e20cc24ca3b0c786b5d5bd4ad252"
		url = "http://api.openweathermap.org/data/2.5/forcast?"
		whole_url = url + "appid=" + api +"&" + query
		res=requests.get(whole_url);
		return res.json();

	def display_info(weather, city):
		print("{}'s temperature: {} C".format(city, weather['main']['temp']))

	def main():
		city=input("Enter the city name or zipcode: ")
		print()

	try:
		query='q='+city;
		w_data=weather_data(query);
		disyplay_info(w_data, city)
		print()
	except:print("City name not found")

	if __name__=='__main__':
		main()
    
	print('Do you want infomration on a different city? (yes or no)')
	another_search = input()
	if another_search == 'no' or another_search == 'n':
		input("press ENTER to EXIT")
