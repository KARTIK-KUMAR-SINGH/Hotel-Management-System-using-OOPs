from models.room import Room
from models.customer import Customer
from models.booking import Booking
class Hotel :
    def __init__ (self) :
        self.rooms = []
        self.customers = []
        self.bookings = []

    def add_room(self , room) :
        self.rooms.append(room)

    def add_customer(self , customer) :
        self.customers.append(customer)

    def book_room(self , customer_id , room_number , number_of_nights):
        customer = None
        booking_id = len(self.bookings) + 1
        for i in self.customers :
            if(i.customer_id == customer_id) :
                customer = i
                break

        room = None

        for i in self.rooms :
            if(i.room_number == room_number):
                room = i
                break

        if customer is None :
            print("Customer not found")
            return

        if room is None :
            print("Room not found")
            return

        if not room.is_available :
            print("The room is not avaliable")
            return
        
        else:
            booking = Booking(booking_id , customer, room , number_of_nights)

            self.bookings.append(booking)

            room.is_available = False
            print("Room Booked Sucessfully")

    def cancel_booking(self , booking_id):
        booking = None 
        for i in self.bookings :
            if i.booking_id == booking_id:
                booking = i
                break
            else :
                print("Booking id was not found cancel unsuccessful")

        booking.room.is_avaliable = True
        self.bookings.remove(booking)

        print("Booking canceled Sucessfully")

    def generate_bill(self , booking_id) :
        booking = None
        for i in self.bookings :
            booking = i
            break
        else :
            print("Booking id not fount bill not generated")
            return

        total = booking.room.price * booking.number_of_nights

        print(f"Room price per night :- {booking.room.price}")
        print(f"Number of Nights :- {booking.number_of_nights}")
        print(f"Total Price :- {total}")