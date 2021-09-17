import csv
from os import write
import pandas as pd

data=[]
with open("gr.csv","r")as f:
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

gravity = []

for index,r in enumerate(stardata):
  pg = (float(mass[index])*6.67e-11)/(float(radius[index])*float(radius[index]))
  gravity.append(pg)


df = pd.DataFrame(list(zip(name , dist , mass , radius , gravity)) , columns = ["name","distance","mass","radius","gravity"] )
df.to_csv('final.csv',index=False)

