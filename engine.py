import tkinter as tk
import requests
import time


def getWeather(canvas):
    city = textField.get()
    textfield= ("Enter City Name")
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=514dfb44dc2f1748b699f5e29bc55d50"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = condition + "\n" + str(temp) + "°C" 
    final_data = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text = final_info)
    label2.config(text = final_data)


canvas = tk.Tk()
canvas.geometry("400x550")
canvas.title("Rahul's Weather App")
f = ("Times", 20,"bold")
t = ("Times", 30, "bold")
k = ("poppins" , 10,"bold")

textField = tk.Entry(canvas, justify='center', width = 18, font = f)
textField.pack(pady = 30)
textField.focus()
textField.bind('<Return>', getWeather)

label1=tk.Label(canvas,text="Enter City", font=f)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()
label3 = tk.Label(canvas, font=t)
label3.pack()
label4 = tk.Label(canvas, justify='right',text="Copyright for Rahul (201CS259)",font=k)
label4.pack()
canvas.mainloop() 
