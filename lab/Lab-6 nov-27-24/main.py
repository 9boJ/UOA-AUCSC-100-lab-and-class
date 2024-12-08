import requests 

city_name = "Toronto"
your_api_key = "a7ee35e986660cd26ad86ae6316c09b5"



url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={your_api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    place = data["name"]
    temp = data["main"]["temp"]
    sky = data["weather"][0]
    sky2 = sky["main"]
    print("Place: ",place)
    print("Tems: ",temp)
    print("Sky: ",sky2)
else:
    print("Failed to fetch data. Status code:", response.status_code)