import easygui
import tkinter

#Locaton Chart
location_name = input("Location name: ")
location_climate = input("Type of climate: ")
location_nature = input("Type of nature: ")
location_landarea = input("Land area size: ")

#History
location_history = input("Brief history of the location: ")
location_pride = input("Location proud milestones: ")
location_trauma = input("Location historical trauma: ")

#Demographics
location_pop = input("Location population: ")
location_ethnic = input("Location ethnic groups: ")
location_medianage = input("Location median age: ")
location_religions = input("Location religions: ")
location_language = input("Location languages: ")

#Culture
location_arts = input("Location arts & music: ")
location_cuisine = input("Location cuisine: ")
location_recreation = input("Location popular recreation: ")
location_media = input("Location media outlets: ")

#Politics
location_politics = input("Location governance style: ")
location_foreignrelations = input("Location foreign relations: ")

#Economy
location_economy = input("Location economic status: ")
location_currency = input("Location currency: ")
location_industries = input("Location main industries: ")
location_employment = input("Location employment status: ")

#Infrastructure
location_infrastatus = input("Location infrastructure status: ")
location_landtransport = input("Location types of land transport: ")
location_seatransport = input("Location types of sea transport: ")
location_airtransport = input("Location types of air transport: ")
location_water = input("Location water availability: ")
location_education = input("Location education level: ")
location_healthcare = input("Location healthcare level: ")


easygui.msgbox(f"Location Chart \nLocation name: {location_name} \nType of climate: {location_climate} \nType of nature: {location_nature} \nLand area size: {location_landarea} \
\n\nHistory \nBrief history of the location: {location_history} \nLocation proud milestones: {location_pride} \nLocation historical trauma: {location_trauma} \
\n\nDemographics \nLocation population: {location_pop} \nLocation ethnic groups: {location_ethnic} \nLocation median age: {location_medianage} \nLocation religions: {location_religions} \nLocation languages: {location_language} \
\n\nCulture \nLocation arts & music: {location_arts} \nLocation cuisine: {location_cuisine} \nLocation popular recreation: {location_recreation} \nLocation media outlets: {location_media} \
\n\nPolitics \nLocation governance style: {location_politics} \nLocation foreign relations: {location_foreignrelations} \
\n\nEconomy \nLocation economic status: {location_economy} \nLocation currency: {location_currency} \nLocation main industries: {location_industries} \nLocation employment status: {location_employment} \
\n\nInfrastructure \nLocation infrastructure status: {location_infrastatus} \nLocation types of land transport: {location_landtransport} \nLocation types of sea transport: {location_seatransport} \nLocation types of air transport: {location_airtransport} \nLocation water availability: {location_water} \nLocation education level: {location_education} \nLocation healthcare level: {location_healthcare}", title="Location Sheet")