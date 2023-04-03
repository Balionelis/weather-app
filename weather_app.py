# Made by github.com/Balionelis

import requests
from tkinter import *
from PIL import ImageTk, Image
import io

api_key = '2beedc5bb7499d437250644781ea653a'

root = Tk()
root.title("Weather App")
root.geometry("900x80")

root.configure(bg='#F5F5F5')

frame1 = Frame(root, bg='#F5F5F5')
frame2 = Frame(root, bg='#F5F5F5')
frame1.pack(pady=20)
frame2.pack(pady=10)

city_label = Label(frame1, text="City: ", font=('Arial', 14), bg='#F5F5F5', fg='#333')
city_label.pack(side=LEFT, padx=10)
temp_label = Label(frame1, text="Temperature: ", font=('Arial', 14), bg='#F5F5F5', fg='#333')
temp_label.pack(side=LEFT, padx=10)

city_entry = Entry(frame1, font=('Arial', 14), width=20)
city_entry.pack(side=LEFT, padx=10)

city_entry.bind('<Return>', lambda event=None: get_weather())

image_label = Label(frame2)
image_label.pack()

def get_weather():
    city = city_entry.get()
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    temp = data['main']['temp']
    temp_label.config(text=f"Temperature: {temp}°C")

    icon_url = f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}.png"
    icon_response = requests.get(icon_url, stream=True)
    icon_data = icon_response.content

    img = ImageTk.PhotoImage(Image.open(io.BytesIO(icon_data)))
    image_label.config(image=img)
    image_label.image = img

button = Button(frame1, text="Get Weather", font=('Arial', 14), bg='#4CAF50', fg='white', command=get_weather)
button.pack(side=LEFT, padx=10)

frame1.pack()
frame2.pack()

root.mainloop()
