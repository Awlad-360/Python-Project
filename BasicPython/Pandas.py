#import Pandas Library
import pandas as pd
#Empty DataFrame Make
df = pd.DataFrame()
df
#DataFrame Information
df.info()
#Make List By Country Name
city = ['Bangladesh','Singapore','America','England']
city
#Convert List to DataFrame
df = pd.DataFrame(city)
df
type(df)
type(city)
#Identify How many row and coll in DataFrame
row, col = df.shape
row
col
#Identify How many row and coll in DataFrame
df.shape
#Collum Name and Row Name Setup of DataFrame
df
#Set Columns Name
df = pd.DataFrame(city, columns=['CountryName'])
df
#Set Columns Name & Row Name
df = pd.DataFrame(city, columns=['CountryName'], index=['C1', 'C2', 'C3','c4'])
df
#How to make 2 file converted in 1 file by zip file & Add columns name 
city2 = ['Dhaka','Rajshahi','Khulna','Sylhet']
df2=pd.DataFrame(zip(city, city2), columns=['city1','city2'])
df2
df2.shape
#Two Dimentional array
city3 = [['Gazipur','Tangail','Ashulia','Savar'],['Munshiganj','Keraniganj','Komolapur','Narayanganj']]
city3
#Two Dimentional array columns name and row name set
df4 = pd.DataFrame(city3, columns=['Stage1','Stage2','Stage3','Stage4'], index=['North','South'])
df4
#List to Dictonary Convert
city
city2
dict1 = {
    'country1':city,
    'country2':city2
}
dict1
#Make DataFrame From Dictionary
df5 = pd.DataFrame(dict1)
df5
type(dict1)
