#! python
"""
File: geocode_addresses.py
Description:
    This script pulls a list of locations which need lat/lng added,
    uses an api to retrieve them from google maps, 
    then updates the database records.
"""

#Import python modules used below
import http.client
import mysql.connector
from mysql.connector import errorcode
import pandas as pd
import json

#Setup api details here
api_conn = http.client.HTTPSConnection("google-maps-geocoding.p.rapidapi.com")
headers = {
    'x-rapidapi-host': "google-maps-geocoding.p.rapidapi.com",
    'x-rapidapi-key': "AIzaSyCchpg7d5NjPxB7NB5yZhY-qrYVEABz67M"
    }

#Connect to the local database
try:
    cnx = mysql.connector.connect(user='xxxxxx', password='xxxxxxx',
                              host='localhost',
                              database='xxxxxxxxxx')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

#Function to get json response from google api
def get_geocode_response(this_address):
    api_conn.request("GET", "/geocode/json?language=en&address="+this_address, headers=headers)
    res = api_conn.getresponse()
    data = res.read().decode("utf-8")
    thejson = json.loads(data)
    return thejson

#STEP 1: Query the database to pull a list of location records needing latitude or longitude
sql = ("select * from hotdog_stand_locations where isNull(latitude) or isNull(longitude)")
cursor = cnx.cursor()
try:
    number_of_rows = cursor.execute(sql)
    table_rows = cursor.fetchall()
except mysql.connector.DataError as e:
    print("DataError")
    print(e)
except mysql.connector.InternalError as e:
    print("InternalError")
    print(e)
except mysql.connector.IntegrityError as e:
    print("IntegrityError")
    print(e)
except mysql.connector.OperationalError as e:
    print("OperationalError")
    print(e)
except mysql.connector.NotSupportedError as e:
    print("NotSupportedError")
    print(e)
except mysql.connector.ProgrammingError as e:
    print("ProgrammingError")
    print(e)
except :
    print("Unknown error occurred")

if len(table_rows)>0:
    mydf = pd.DataFrame(table_rows, columns=cursor.column_names)
    
    #STEP 2: For each location record, construct an api call using the address
    for index, row in mydf.iterrows():
        #Setup address string to send to google maps api.  It is ok to have some blank inputs but spaces have to be encoded as %20
        this_address = str(row['location_name'])+' '+str(row['city'])+' '+str(row['state'])+' '+str(row['postal_code'])+' '+str(row['country'])
        this_address = this_address.replace(' ','%20') 

        #STEP 3: Call the google maps geocode api (defined in a function above).
        #   Then parse the results to pull out latitude and longitude
        #print("about to get api response for this_address "+str(this_address))
        api_response = get_geocode_response(this_address)
        this_lat = api_response['results'][0]['geometry']['location']['lat']
        this_lng = api_response['results'][0]['geometry']['location']['lng']
        #print("lat is "+str(this_lat)+" from api_response")

        #STEP 4: Update the database record to include the latitude and longitude
        sql = ("update hotdog_stand_locations set latitude='"+str(this_lat)+"', longitude='"+str(this_lng)+"' "
                "where hotdog_stand_location_id='"+str(row['hotdog_stand_location_id'])+"'")
        try:
            cursor.execute(sql)
            cnx.commit()
        except mysql.connector.DataError as e:
            print("DataError")
            print(e)
        except mysql.connector.InternalError as e:
            print("InternalError")
            print(e)
        except mysql.connector.IntegrityError as e:
            print("IntegrityError")
            print(e)
        except mysql.connector.OperationalError as e:
            print("OperationalError")
            print(e)
        except mysql.connector.NotSupportedError as e:
            print("NotSupportedError")
            print(e)
        except mysql.connector.ProgrammingError as e:
            print("ProgrammingError")
            print(e)
        except :
            print("Unknown error occurred from query: "+sql)

else:
    print("All coordinates are already in place!")
