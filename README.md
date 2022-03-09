# Week6 Working with Classes

We have been split into 3 teams. Stushbush and I are Team 1, NameUser5 and DannyDorestant are Team 2, and Juniorxy and Evelynb92 Team 3. 

### Team 1 will build an airline booking system. Starting with classes of Passenger, Flight, Destination. 

Passenger class must have the following instance attributes, * are required:

`first_name*, last_name*, Birthday, nationality*, frequent_flyer_number, frequent_flyer_miles, miles_expiration_date, home_city*, seating_preference, phone_number*, email`

Flight class should have the following instance attributes:

`origination_city*, destination_city*, plane_model*, total_seats, available_seats, occupide_seats, layover_city, departure_time*, arrival_time*, cost*`

Destination class should have: 

`city_name, state, country, logitude, latitude, language, max_inbound_flights, max_outbound_flights, inbound_flights, outbound_flights`


### Team 2 will build an online retail business. Starting with Classes of Sku, Channel, Vendor.

Sku class should have the following instance attributes:

`part_number*, manufacturer*, model*, condition, color, weight*, dimension*, quantity*, warehouse_location*, vendor, cost, selling_price`

Channel class should have the following instance attributes:

`name*, account_manager*, marketplace_fee_percentage, transaction_fees, type*, refund_policy, warranty_policy, content_manager`

Vendor class should have the following instance attributes:

`name*, sales_contact*, street_adress, city*, state, zip, account_number*, payment_terms, bank_number, routing_number`


### Team 3 will build a university platform. Starting with Classes of Student, Course, Professor. 

Student class should have the following instance attributes:

`first_name*, last_name*, nationality*, student_id*, gpa, classification*, advisor, major, second_major, minor, courses_taken, courses_enrolled`

Course class should have the following instance attributes:

`course_id*, course_name*, instructor*, max_seats, enrolled_students, classroom*, start_time, end_time, course_days, hybrid`

Professor class should have the following instance attributes:

`first_name*, last_name*, specialty*, courses_taught, office_location*, office_hours_start, office_hours_stop, office_hour_days, salary*, tenure*`


## Tasks (split the work so everyone get practice, I advise sharing a replit with your partner)
1. Create each classs on a seperate file (name the file the same as the class name). For example, class Animal would be on a file calle animal.py
2. Find out how to import your class to your main file.
3. In your main file, create 20 Passengers, 20 Skus, 20 Students (depending on your respective team). Place them all into a list.
4. In your main file, create 5 Flights, 5 Channels, 5 Courses (depending on your respective team). Place them all into a list. 
5. In your main file, create 10 Destinations, 10 Vendors, 10  Professors (depending on your respective team). Place them all into a list.
6. What is the average age of your passengers, price of your Sku, or professor salary?
7. list the full name of each passenger, make and model of each Sku, or full name of every students. 
8. randomly print out the name of 5 passengers, 5 sku or 5 students.
9. Check-in Time - Book a time to show me your progress (remote replit share is good)
