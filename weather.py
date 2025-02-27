from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
import datetime
import requests
import pytz


root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getWeather():
    try:
        city=textfield.get()

        geolocator= Nominatim(user_agent="geopiExercises")
        location= geolocator.geocode(city)
        obj= TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)

        home=pytz.timezone(result)
        local_time=datetime.datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")
        place.config(text=city)

        #weather
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=646824f2b7b86caffec1d0b16ea77f79"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
        
    except Exception as e:
      messagebox.showerror("Weather App","Invaild Entry!!")

#search box
Search_image=PhotoImage(file="search.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center",width=17,font=("Rockwell",23,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()

Search_icon=PhotoImage(file="search_icon.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=400,y=34)

#logo
Logo_image=PhotoImage(file="logo.png")
logo=Label(image=Logo_image)
logo.place(x=150,y=100)


#Bottom box
Frame_image=PhotoImage(file="box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font=("Times New Roman",16,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Times New Roman",20))
clock.place(x=30,y=130)

#place name
place = Label(root, font=("Times New Roman", 18,"bold"), fg="blue")
place.place(x=410,y=120)

#label
label1=Label(root,text="WIND",font=("Times New Roman",17,"bold"),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)

label1=Label(root,text="HUMIDITY",font=("Times New Roman",17,"bold"),fg="white",bg="#1ab5ef")
label1.place(x=250,y=400)

label1=Label(root,text="DESCRIPTION",font=("Times New Roman",17,"bold"),fg="white",bg="#1ab5ef")
label1.place(x=430,y=400)

label1=Label(root,text="PRESSURE",font=("Times New Roman",17,"bold"),fg="white",bg="#1ab5ef")
label1.place(x=650,y=400)

t=Label(font=("Times New Roman",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("Times New Roman",15,'bold'))
c.place(x=400,y=250)

w=Label(text="...",font=("Times New Roman",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)
h=Label(text="...",font=("Times New Roman",20,"bold"),bg="#1ab5ef")
h.place(x=280,y=430)
d=Label(text="...",font=("Times New Roman",20,"bold"),bg="#1ab5ef")
d.place(x=430,y=430)
p=Label(text="...",font=("Times New Roman",20,"bold"),bg="#1ab5ef")
p.place(x=690,y=430)



root.mainloop()
