## CAB-NOW		https://cab-now.herokuapp.com/

### Current issues with design 
	- [How to make client and server communicate so that client listens for changes in DB continuously]
	- How will the driver know when the user has requested a ride in his location
	- How will the user know when the driver nearby has accepted his ride
	- Live tracking the driver in user app


### Android app progress [Git-link](https://github.com/Zentario/CabNowAndroidApp)	
- Sign in for user
- Login for user
- Current location
- Test users [phone_no : password] Currently 2 users
	- 123456789 : 123
	- 987654321 : 123
	
### User requirements
	- Able to select destination on map
	- Gets fare and ETA estimate before booking
	- [Optional] Optimize so that nearest drivers are shown in map on user side
	  [nearest drivers can be chosen by ETA or Euclidean distance]
	- Book the ride
	- Route the path to driver
	- Able to cancel ride
	- Emergency contact option
	- Receives notification when ride arrives
	- Route path to destination
	- Ride completes and receives bill receipt as notification
	- Payment interface GooglePay

### Driver requirements
	- Receives notification to accept ride or not
	- When accepted route the path to user
	- After reaching route path to destination
	- Show bill amount after ride

- [Optional] Optimize so that route from driver to user, user to destination, bill, ETA is calculated
   for both user and driver ONLY ONCE


## API server side
- Running Gunicorn with Flask hosted on Heroku [Heroku identifies code push to git and deploys auto]
- Use https://cab-now.herokuapp.com/ as BASE_URL [end points vary on functionality]
### Database
	- [New db design is yet to be made] Use two json files for user and driver
	- All the files in the git repo are hosted on the server in the same directory.

- Detailed HTTP status codes documentation [here](https://www.restapitutorial.com/httpstatuscodes.html)
### Api end points in FLASK 
	- Header ["Content-Type: application/json"]

	- /adduser
		- Request  {"phone_no" : "", "name" : "", "email" : "", "password" : ""}
		- Response {"error" : true/false, "message" : "", user_obj_that_got_created}
		- 201, 202, 405
	
	- /login
		- Request  {"phone_no" : "", "password" : ""}
		- Response {"error" : true/false, "message" : "", user_obj_that_logged_in}
		- 200, 202, 405
