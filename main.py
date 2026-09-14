from models.customer import Customer
from models.room import Room
from models.hotel import Hotel
from models.booking import Booking
hotel = Hotel()

while True :
    print("==== Hotel Booking System ====")

    print("1. Add Room")
    print("2. Register Customer")
    print("3. View Available Rooms")
    print("4. Book Room")
    print("5. View Bookings")
    print("6. Cancel Booking")
    print("7. Generate Bill")
    print("8. Exit")

    choice = int(input("Enter your choice :-"))

    if (choice == 1) :
        #print("Add room")
        room_number = int(input("Enter the room number :- "))
        type = input("Enter the type :- ")
        price = int(input("Enter the price :- "))
        room = Room(room_number , type , price)
        hotel.add_room(room)
        # for i in hotel.rooms :
        #     print(i.room_number , i.type , i.price)

    elif(choice == 2):
        #print("Register Customer")
        name = input("Enter the customer name :- ")
        customer_id = int(input("Enter the customer id :- "))
        phone_no = int(input("Enter the phone number :- "))
        customer = Customer(name , customer_id , phone_no)
        hotel.add_customer(customer)

        # for i in hotel.customers :
        #     print(i.name , i.customer_id , i.phone_number)

    elif(choice == 3):
        #print("View Available Rooms")
        for i in hotel.rooms :
            print(f"room number :- {i.room_number} || room type :- {i.type} || room price :- {i.price}")

    elif(choice == 4):
        #print("Book Room")
        customer_id = int(input("Enter your customer id :- "))
        room_number = int(input("Enter the room number you want to book :- "))
        number_of_nights = int(input("Enter the number of nights you want to stay :- "))
        hotel.book_room(customer_id , room_number , number_of_nights)

    elif(choice == 5):
        #print("View Bookings")
        for i in hotel.bookings :
            print(f"The customer name is {i.customer.name} his room number is {i.room.room_number} and his number of nights stay is {i.number_of_nights} and his booking id is :- {i.booking_id}")

    elif(choice == 6):
        #print("Cancel Booking")
        booking_id = int(input("Enter the booking id to cancel :- "))
        hotel.cancel_booking(booking_id)

    elif(choice == 7):
        #print("Generate Bill")
        booking_id = int(input("Enter the booking id to generate the bill :- "))
        hotel.generate_bill(booking_id)

    else:
        print("Thank you for using the hotel bookng system")
        print("Exit")
        break