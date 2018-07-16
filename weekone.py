#Week one, Day one exercises

#Hours in a year

year = (365*24)

leap = (366*24)

print ("There are " + str(year) + " hours in a year, or " + str(leap) + " hours in a leap year")


#Minutes in a decade

minindecade = (10*365*24*60)

print ("There are " + str(minindecade) + " minutes in a decade")


#Age in seconds

#Assume time = 3:40pm on 16th July 2018

#Birthdate and time approx 10:30am on 29th August 1989

seconds = ((365*28) + (1*7) + (31+30+31+30+31+31+28+31+30+31+17)) *24*60*60 + (5*60*60) + (10*60)

print ("I am " + str(seconds) + " seconds old")


#Andrea is 48618000 seconds old

seconds = 48618000
minutes = (seconds // 60)	
seconds = (seconds % 60)
hours = (minutes // 60)
minutes = (minutes % 60)
days = (hours // 24)
hours = (hours % 24)
years = (days // 365)
days = (days % 365)

print (str(years) + " years, " + str(days) + " days, " + str(hours) + " hours, " + str(minutes) + " minutes, " + str(seconds) + " seconds.")




#32 bit system

seconds = (2**31)-1

print ("sec ", seconds)

minutes = (seconds // 60)
seconds = (seconds % 60)
hours = (minutes // 60)
minutes = (minutes % 60)
days = (hours // 24)
hours = (hours % 24)
years = (days // 365)
days = (days % 365)

print (str(years) + " years, " + str(days) + " days, " + str(hours) + " hours, " + str(minutes) + " minutes, " + str(seconds) + " seconds until timeout in a 32-bit system")



#64 bit system

seconds = (2**63)-1

print ("sec ", seconds)

minutes = (seconds // 60)
seconds = (seconds % 60)
hours = (minutes // 60)
minutes = (minutes % 60)
days = (hours // 24)
hours = (hours % 24)
years = (days // 365)
days = (days % 365)

print (str(years) + " years, " + str(days) + " days, " + str(hours) + " hours, " + str(minutes) + " minutes, " + str(seconds) + " seconds until timeout in a 64-bit system.")



#Exact age

import datetime

birthday = datetime.date(1989,8,29)
print ("I was born on ", birthday)
print ("Current date and time is ", datetime.datetime.now())

a = datetime.datetime.now()
b = datetime.datetime(1989, 8, 29, 10, 30, 0)
time_difference = a-b

print ("I am exactly ", time_difference, " seconds old.")
