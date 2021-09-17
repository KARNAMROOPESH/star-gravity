import csv
from os import write
import pandas as pd


data=[]
with open("ms.csv","r")as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row)

headers = data[0]
stardata = data[1:]

star = list(stardata)

radius = []
mass = []
name = []
dist = []

for star in stardata:
    radius.append(star[3])


for star in stardata:
    mass.append(star[2])

for star in stardata:
    name.append(star[0])

for star in stardata:
    dist.append(star[1])


massc=[]
radiusc=[]

for index,m in enumerate(mass):
  p = (float(mass[index])*1.989e+30)
  massc.append(p)

for index,r in enumerate(radius):
  pr = (float(radius[index])*6.957e+8)
  radiusc.append(pr)

df = pd.DataFrame(list(zip(name , dist , massc , radiusc ,)) , columns = ["name","distance","mass","radius"] )
df.to_csv('gr.csv',index=False)


