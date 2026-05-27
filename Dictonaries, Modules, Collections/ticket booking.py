##Code logic is incomplete so don't fucking give dumbass inputs please I've been drained working on code logic
import random

#setting up lists for trains for each route
routes = {
    "Chennai": ["Chennai express 1", "Chennai express 2", "Chennai express 3", "Chennai express 4", "Chennai express 5", "Chennai express 6"],
    "Madurai": ["Madurai express 1", "Madurai express 2", "Madurai express 3", "Madurai express 4", "Madurai express 5", "Madurai express 6"],
    "Trichy": ["Trichy express 1", "Trichy express 2", "Trichy express 3", "Trichy express 4", "Trichy express 5", "Trichy express 6"],
    "Tenkasi": ["Tenkasi express 1", "Tenkasi express 2", "Tenkasi express 3", "Tenkasi express 4", "Tenkasi express 5", "Tenkasi express 6"],
    "Tutricon": ["Tutricon express 1", "Tutricon express 2", "Tutricon express 3", "Tutricon express 4", "Tutricon express 5", "Tutricon express 6"],
    "Nagercoil": ["Nagercoil express 1", "Nagercoil express 2", "Nagercoil express 3", "Nagercoil express 4", "Nagercoil express 5", "Nagercoil express 6"]
}

#global values 
max_tickets = 5
tamt = 500
available_tickets = {}
t_time = "7:45 PM"
if_running = True

#to keep track of booked tickets
for trains in routes.values():
    for train in trains:
        available_tickets[train] = 0

booked_tickets = []

#function to initate the process of booking tickets
def book_ticket():
   
   print("Welcome to ticket booking!")
   p_name = input("Enter Your Name:")
   p_id = random.randint(10000,10000000)
   p_aadh = int(input("Enter Your Aadhar Number:"))
   p_age = int(input("Enter Your Age:"))
   boarding_point = input("Enter Boarding Point:")
   #if boarding or dropping points not in routes
   if boarding_point not in routes:
       print("Station not recognized. Transaction cancelled.")
       return
   
   dropping_point = input("Enter Dropping Point:")
   
   if dropping_point not in routes:
       print("Destination not recognized. Transaction cancelled.")
       return
   
   print(f"The available trains for your route are: {routes[dropping_point]}")
   p_train = input("Enter the Train name:")
   #if non existent train chosen
   if p_train not in available_tickets:
       print("Train not found")
       return
   #I know there's a module called datetime or stuff but I need to type extra try and catch codelines too lazy and annoyed for that so I'll skip it
   p_date = input("Enter the date (DD:MM:YYYY):")
   p_count = int(input("Enter No Of Passengers:"))

# to check if the tickets are avilable
   if available_tickets[p_train] + p_count > max_tickets:
       print("Tickets are unavailable. Choose another train!")
       return
# yes payment logic is trash I'm just learning. feel free to pinpoint the errors and give solutions too
   else:
        tot_amt = p_count * tamt
        print(f"Pay Your Amount: {tot_amt}")
        paid = int(input("Enter Your Amount:"))

        while tot_amt > paid:
            ramt = tot_amt - paid
            print(f"Kindly pay the full amount. Balance amount to be paid: {ramt}")
            rpaid = int(input("Enter The Amount:"))
            paid += rpaid

        if paid > tot_amt:
            print("Remaining amount is sent back to your account!")

        print("The Transaction is Done")

# update the available tickets
        available_tickets[p_train] += p_count

   ticket_details = {
       "Passenger Name" : p_name,
       "Passenger id" : p_id,
       "Passenger Aadhar" : p_aadh,
       "Passenger Age" : p_age,
       "Boarding Point" :boarding_point,
       "Dropping Point" : dropping_point,
       "Passenger Count" : p_count,
       "Booked Train" : p_train,
       "Booked Date" : p_date, 
       "Train Time" : t_time}
        

   booked_tickets.append(ticket_details)
   print(f"Ticket No. {p_id} is confirmed on {p_date} at {t_time}")

#function to initiate the process of cancelling tickets
def cancel_ticket():
   book_ticket.remove(booked_tickets)

#function to check booked tickets
def check_ticket():
   print (f"The Ticket Details are: {booked_tickets}")

while if_running:
    
    choice = input("Enter Your Choice: 1. Book Tickets 2. Cancel Tickets 3. Check Ticket Status 4. Exit")
    
    if choice == "1":
        book_ticket()
    
    elif choice == "2":
        cancel_ticket()

    elif choice == "3":
        check_ticket()
    
    elif choice == "4":
        if_running = False
    
    else:
        print("Kindly choose within the options Mr.Out Of Box")

