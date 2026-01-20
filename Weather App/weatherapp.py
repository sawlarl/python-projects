import tkinter as tk
import requests
from tkinter import messagebox

API_KEY = "d9c0cd457f9e741d2685098200b5868f"

def get_weather():
    city = city_entry.get()
    if city == "":
        messagebox.showerror("Error", "Please enter a city name")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            messagebox.showerror("Error", "City not found")
            return

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]

        result_label.config(
            text=f"🌡 Temperature: {temp}°C\n"
                 f"☁ Condition: {condition}\n"
                 f"💧 Humidity: {humidity}%"
        )

    except:
        messagebox.showerror("Error", "Failed to fetch data")

root = tk.Tk()
root.title("Weather App")
root.geometry("350x300")
root.resizable(False, False)

tk.Label(root, text="Weather App", font=("Arial", 16)).pack(pady=10)

tk.Label(root, text="Enter your city:", font=("Arial", 14)).pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 14), justify="center")
city_entry.pack(pady=10)

tk.Button(root, text="Get Weather", width=20, command=get_weather).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
