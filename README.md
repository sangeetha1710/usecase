# usecase
This repository will contain use cases using python

Online House Renting Portal

The Online House Renting Portal allows to rent a house. The system consists of Users, Approver, Admin. It allows the Users to rent a house. It also has an Admin to control the system.

Mock data

Locality	    Kodambakkam	   Goripalayam	          Anna Nagar
City	        Chennai      	 Madurai	              Chennai
Square Feet	  798	           560	                  1200
Type	        2BHK	         1BHK	                   3BHK
Rent	        Rs. 6000 / Month	Rs. 5500 / Month	Rs. 15000 / Month
Owner Id	    1	             1	                     2

Basic Cases:
User:
•	Owner - Can create a request to post / remove their house for rental.
•	Can view the list of houses available for rent.
•	Tenant - Can create request to rent a house (Owner confirmation is required).
•	Owner - Can View / Approve / Decline the created request.

Approver:
•	Can view all the requests from User (Owner).
•	Can Approve / Decline the request.

System:
•	Should display Advertisement (for User only).

Admin:
	Can view the report
Can manage the advertisement(content and timing) 

Bonus Capabilities:
•	User can view their history of rentals.
•	System should show suggestions according to the previous search history (Location, Rental Amount)
