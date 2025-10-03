import requests
import matplotlib.pyplot as plt

API_KEY = "3eb524422a4b094348c1a85e143f6c41"
cities = ["Chennai", "Delhi", "Mumbai", "Kolkata", "Bengaluru"]
temps = []

for city in cities:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    data = requests.get(url).json()
    temps.append(data["main"]["temp"])

plt.bar(cities, temps, color="orange")
plt.xlabel("Cities")
plt.ylabel("Temperature (°C)")
plt.title("Current Temperature in Indian Cities")
plt.show()