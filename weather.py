from tkinter import *
from tkinter import ttk
import requests

# Fetch data from API
def data_get():
    city = city_name.get()
    try:
        data = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=2c295a3684a7eca84e2c9deab0817a9b").json()
        if 'weather' in data:
            weather_climate_lable1.config(text=data['weather'][0]['main'])
            weather_discription_lable1.config(text=data['weather'][0]['description'])

            temperature = int(data['main']['temp']) - 273
            weather_temp_lable1.config(text=f'Temperature: {temperature}°C')

            humidity = data['main']['humidity']
            weather_humidity_lable1.config(text=f'Humidity: {humidity}%')
        else:
            # Handle case where 'weather' key is not present
            weather_climate_lable1.config(text="N/A")
            weather_discription_lable1.config(text="N/A")
            weather_temp_lable1.config(text="N/A")
            weather_humidity_lable1.config(text="N/A")
    except Exception as e:
        print(f"Error: {e}")

# App frame
app = Tk()
app.title("Weather App")
app.geometry("400x650")

# Set background color
app.configure(bg="lightblue")

# Weather App label
name_label = Label(app, text="Weather App", font=("Serif", 35), foreground='black', bg='lightblue', padx=10, relief="solid")
name_label.place(x=20, y=50, height=50, width=360)







# Weather App label
name_label = Label(app, text="Weather App", font=("Serif", 35), foreground='black', bg='lightblue', padx=10,relief="solid")
name_label.place(x=20, y=50, height=50, width=360)


city_name_label = Label(app, text="Enter City Name", font=("Serif", 20),bg="lightblue")
city_name_label.place(x=80, y=160, height=50, width=260)

# Combobox
list_name = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
             "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra",
             "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu",
             "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands",
             "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep", "Delhi", "Puducherry"]
city_name = StringVar()
com = ttk.Combobox(app, font=("Serif", 20), values=list_name, textvariable=city_name)
com.place(x=20, y=200, height=50, width=360)

# Adding the Submit Button
submit_button = Button(app, text="Get Weather", command=data_get, font=("Serif", 15), background="green", foreground="white")
submit_button.place(x=140, y=280, height=40, width=120)

# Display climate
weather_climate_label = Label(app, text="Climate", font=("Serif", 15))
weather_climate_label.place(x=10, y=410, height=30, width=150)
weather_climate_lable1 = Label(app, text="", font=("Serif", 15))
weather_climate_lable1.place(x=180, y=410, height=30, width=150)

# Weather description
weather_description_label = Label(app, text="Description", font=("Serif", 15))
weather_description_label.place(x=10, y=450, height=30, width=150)
weather_discription_lable1 = Label(app, text="", font=("Serif", 15))
weather_discription_lable1.place(x=180, y=450, height=30, width=150)

# Weather temperature
weather_temp_label = Label(app, text="Temperature", font=("Serif", 15))
weather_temp_label.place(x=10, y=490, height=30, width=150)
weather_temp_lable1 = Label(app, text="", font=("Serif", 15))
weather_temp_lable1.place(x=180, y=490, height=30, width=200)

# Humidity
weather_humidity_label = Label(app, text="Humidity", font=("Serif", 15))
weather_humidity_label.place(x=10, y=530, height=30, width=150)
weather_humidity_lable1 = Label(app, text="", font=("Serif", 15))
weather_humidity_lable1.place(x=180, y=530, height=30, width=150)

# Exit button
quit_button = Button(app, text="Quit", command=app.destroy, font=("Serif", 15), background="red", foreground="white")
quit_button.place(x=140, y=570, height=40, width=120)

# Rest of your code...
app.mainloop()
