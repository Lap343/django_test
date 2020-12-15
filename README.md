# Garage Api Test

Welcome to the garage api test. In a nutshel it saves a logged in user's cars, trucks, and boats.

If you are not registered on this website here are the steps to get your information stored.

#Registration
Register your account at this endpoint
/rest-auth/registration/
and enter username, email and password1 and password2 in JSON format with a POST request. Password1 and password2 need to match.
{
    "username": "",
    "email": "",
    "password1": "",
    "password2": ""
}

#Login
you should be logged in automatically but if you ever get logged out and want to log back in
/rest-auth/login/
is the endpoint where you want to go. 
To log in submit a POST request with this JSON formatted code.
{
    "username": "",
    "email": "",
    "password": ""
}
email and username have to be unique.

#Logout
To logout of te site send a POST request to this endpoint
/rest-auth/logout/

#All Cars
After a sucessful login the /cars/ endpoint has two main uses. 
A GET request will get a JSON formatted list of all the cars you have in the database. 
If none are saved then an empty list will be returned.

A POST request with this JSON information
{
    "make": "",
    "model": "",
    "year": null,
    "seats": null,
    "color": "",
    "vin": "",
    "current_mileage": null,
    "service_interval": "",
    "next_service": null
}
with the value paires propperly filled out as so.
{
    "make": "Toyota",
    "model": "Corolla",
    "year": 2018,
    "seats": 5,
    "color": "Black",
    "vin": "3f34f3424fgtg",
    "current_mileage": 12000,
    "service_interval": "30-60-90",
    "next_service": "2020-12-30"
}
Please remember that the date for next_service is in "year-month-date" number format.

#A Specific Car
To see/edit/delete a single car the endpoint should be /cars/(the id of the car placed here).
If you need to find the id of a car send a GET request on /cars/ and the id will show up.

The /cars/(id) endpoint with a GET request gets a json formatted response with this information.
{
    "id": 1,
    "owner": 1,
    "make": "Toyota",
    "model": "Corolla",
    "year": 2018,
    "seats": 5,
    "color": "Black",
    "vin": "3f34f3424fgtg",
    "current_mileage": 12000,
    "service_interval": "30-60-90",
    "next_service": "2020-12-30"
}

to edit a value, send a PATCH request to /cars/(id) with JSON formatted data in this format
{
  "(key you want to edit)":"(new value)"
}

to delete a car a DELETE request must be sent to cars/(id)

#All Trucks
After a sucessful login the /trucks/ endpoint has the same two main uses as cars. 
A GET request will get a JSON formatted list of all the trucks you have in the database. 
If none are saved then an empty list will be returned.

A POST request with this JSON information
{
    "make": "",
    "model": "",
    "year": null,
    "seats": null,
    "bed_length": "",
    "color": "",
    "vin": "",
    "current_mileage": null,
    "service_interval": "",
    "next_service": null
}
with the value paires propperly filled out as so.
{
    "make": "Ford",
    "model": "F-150",
    "year": 2019,
    "seats": 4,
    "bed_length": "6tf",
    "color": "Black",
    "vin": "f34fvtvg5f4fvevfv3",
    "current_mileage": 15000,
    "service_interval": "30-30-30-",
    "next_service": "2021-03-10"
}
Please remember that the date for next_service is in "year-month-date" number format.

#A Specific Truck
To see/edit/delete a single truck the endpoint should be /trucks/(the id of the truck placed here).
If you need to find the id of a truck send a GET request on /trucks/ and the id will show up.

The /truckss/(id) endpoint with a GET request gets a json formatted response with this information.
{
    "id": 1,
    "owner": 1,
    "make": "Ford",
    "model": "F-150",
    "year": 2019,
    "seats": 4,
    "bed_length": "6tf",
    "color": "Black",
    "vin": "f34fvtvg5f4fvevfv3",
    "current_mileage": 15000,
    "service_interval": "30-30-30-",
    "next_service": "2021-03-10"
}

to edit a value, send a PATCH request to /trucks/(id) with JSON formatted data in this format
{
  "(key you want to edit)":"(new value)"
}

to delete a truck a DELETE request must be sent to trucks/(id)

#All Boats
After a sucessful login the /boats/ endpoint has two main uses. 
A GET request will get a JSON formatted list of all the trucks you have in the database. 
If none are saved then an empty list will be returned.

A POST request with this JSON information
{
    "make": "",
    "model": "",
    "year": null,
    "length": "",
    "width": "",
    "hin": "",
    "current_hours": null,
    "service_interval": "",
    "next_service": null
}
with the value paires propperly filled out as so.
{
    "make": "Yamaha",
    "model": "Outboard",
    "year": 2020,
    "length": "12ft",
    "width": "7ft",
    "hin": "ABC67689B606",
    "current_hours": 12,
    "service_interval": "30-30-30",
    "next_service": "2020-12-26"
}
Please remember that the date for next_service is in "year-month-date" number format.

#A Specific Boat
To see/edit/delete a single car the endpoint should be /boats/(the id of the boat placed here).
If you need to find the id of a boat send a GET request on /boats/ and the id will show up.

The /boats/(id) endpoint with a GET request gets a json formatted response with this information.
{
    "id": 1,
    "owner": 1,
    "make": "Yamaha",
    "model": "Outboard",
    "year": 2020,
    "length": "12ft",
    "width": "7ft",
    "hin": "ABC67689B606",
    "current_hours": 12,
    "service_interval": "30-30-30",
    "next_service": "2020-12-26"
}

to edit a value, send a PATCH request to /boats/(id) with JSON formatted data in this format
{
  "(key you want to edit)":"(new value)"
}

to delete a boat a DELETE request must be sent to cars/(id)
