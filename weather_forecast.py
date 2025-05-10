import tkinter as tk
from tkinter import *
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz
import requests
from PIL import Image, ImageTk  #For support image in formate of jpg or png   (default tk doesnt support)


def getWeather():
    city=textfield.get()
    geolocator=Nominatim(user_agent='geopiExercises')
    location=geolocator.geocode(city)
    obj=TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M:%p")
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER")

    #weather
    api = f"https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&appid=e0867875e1e77b40d02cc16d928910ba"

    json_data=requests.get(api).json()





    condition=json_data['weather'][0]['main']
    description=json_data['weather'][0]['description']
    temp=int(json_data['main']['temp']-273.15)
    pressure=json_data['main']['pressure']
    humidity=json_data['main']['humidity']
    wind=json_data['wind']['speed']

    t.config(text=(temp,"°"))
    c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))

    w.config(text=wind)
    h.config(text=humidity)
    d.config(text=description)
    p.config(text=pressure)




root=Tk()
root.title("Weather Application")
root.geometry("900x500+300+200")
root.resizable(False,False)

#-----------------------------SEARCH BOX-------------------------------------
image=Image.open("search_bar.png")

search_img=ImageTk.PhotoImage(image)
search_i=Label(root,image=search_img)
search_i.place(x=20,y=20)

textfield=Entry(root,justify="center",width=17,font=("poppins",25,'bold'),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()


search_icon=PhotoImage(file="search_icon.png")
icon_button=Button(root,image=search_icon,borderwidth=0,bg="#404040",cursor='hand2',command=getWeather)
icon_button.place(x=400,y=34)


#---------------------------------LOGO-----------------------------

logo=PhotoImage(file="logo.png")
Logo_i=Label(root,image=logo)
Logo_i.place(x=150,y=110)




#------------------------------BOTTOM----------------------------

frame_box=PhotoImage(file="box.png")
frame_myimage=Label(root,image=frame_box)
frame_myimage.place(x=50,y=350)




#----------------------------------TIME---------------------------
name=Label(root,font=('arial',15,'bold'))
name.place(x=30,y=100)

clock=Label(root,font=('helvetica',20))
clock.place(x=30,y=130)


#--------------------------------LABELS----------------------------
l1=Label(root,text='WIND',font=('Helvetica',15,'bold'),fg='white',bg='#1ab5ef')
l1.place(x=105,y=370)


l2=Label(root,text='HUMIDITY',font=('Helvetica',15,'bold'),fg='white',bg='#1ab5ef')
l2.place(x=240,y=370)

l3=Label(root,text='DESCRIPTION',font=('Helvetica',15,'bold'),fg='white',bg='#1ab5ef')
l3.place(x=420,y=370)

l4=Label(root,text='PRESSURE',font=('Helvetica',15,'bold'),fg='white',bg='#1ab5ef')
l4.place(x=650,y=370)



t=Label(root,font=('arial',70,'bold'),fg='#ee666d')
t.place(x=400,y=150)
c=Label(root,font=('arial',15,'bold'))
c.place(x=400,y=250)

w=Label(root,text='.....',font=('arial',20,'bold'),bg='#1ab5ef')
w.place(x=105,y=400)

h=Label(root,text='.....',font=('arial',20,'bold'),bg='#1ab5ef')
h.place(x=255,y=400)

d=Label(root,text='.....',font=('arial',20,'bold'),bg='#1ab5ef')
d.place(x=430,y=400)

p=Label(root,text='.....',font=('arial',20,'bold'),bg='#1ab5ef')
p.place(x=680,y=400)




root.mainloop()


