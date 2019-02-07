from math import radians, cos, sin, asin, sqrt
def haversine(lat1, lon1, lat2, lon2):
    R = 3959.87433 # this is in miles.  For Earth radius in kilometers use 6372.8 km

    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
    c = 2*asin(sqrt(a))

    return R * c;

import requests;
meteorites = requests.get('https://data.nasa.gov/resource/y77d-th95.json')
if(meteorites.status_code == 200):
    data = meteorites.json()

print('*****************************Meteorite Landings************************************** \n ')
print('This function will tell you all the meteorite landings near a specific area.')
while True:
    try:
        mypoint = (float(input("enter location lattitude in radians \n ")),float(input("enter location longitude in radians \n ")))
        break;
    except ValueError:
        print("Sorry, value you entered is not valid. Try again")
    except NameError:
        print("something went wrong")
    except:
        print("No idea what went wrong")
        raise

print("\n\n Metorite Landings have taken place at the folloiwng locations \n\n")

for site in data:
         try:
             if('reclat' not in site.keys() or 'reclong' not in site.keys()):
                 continue
             if haversine(mypoint[0],mypoint[1],float(site['reclat']),float(site['reclong'])) < 300:
                 print(" A Meteorite landed at", site['name'], "in", site['year'][:4])
             else:
                 continue
         except:
             raise
