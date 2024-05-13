from abc import ABC, abstractmethod
from datetime import datetime

class Room(ABC):
    def __init__(self, roomnumber, price):
        self.roomnumber = roomnumber
        self.price = price
        self.booked_dates = []

    def info(self):
        pass

    def book(self, date):
        if self.check_date(date):
            if self.if_booked(date):
                print(f"On {date} in this date the {self.roomnumber} room was unavaible.")
            else:
                self.booked_dates.append(date)
                print(f"Room #{self.roomnumber} booked for the next date: {date}")

    def resign(self, date):
        if date in self.booked_dates:
            self.booked_dates.remove(date)
            print(f"Room #{self.roomnumber} booking resign for the next date: {date}")
        else:
            print(f"Dont have a booking for the next date and room {date} #3{self.roomnumber}")


    def check_date(self,date):
        if datetime.strptime(date, "%Y-%m-%d").date() < datetime.now().date():
            print("Cant book for the past.")
            return False
        return True

    def if_booked(self, date):
        return date in self.booked_dates

    def info(self):
        return f"Room#{self.roomnumber}, price: {self.price}, booked dates: {self.booked_dates}"

class Standardroom(Room):
    def __init__(self, roomnumber):
        super().__init__(roomnumber, 98000)

    def info(self):
        return f"Onebed room #{self.roomnumber}, price: {self.price}"

class Deluxeroom(Room):
    def __init__(self, roomnumber):
        super().__init__(roomnumber, 250000)

    def info(self):
        return f"Twobed room #{self.roomnumber}, price: {self.price}"

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def new_room(self, room):
        self.rooms.append(room)

    def room_booking(self, roomnumber, date):
        for room in self.rooms:
            if room.roomnumber == roomnumber:
                if room.check_date(date) and date not in room.booked_dates:
                    room.book(date)
                    return room.price
                else:
                    return None
        print(f"Dont have that room #{roomnumber} in this hotel")
        return None


    def book_resign(self, roomnumber, date):
        for room in self.rooms:
            if room.roomnumber == roomnumber:
                room.resign(date)
                return
            print(f"Dont have that #{roomnumber} room in this hotel.")


    def all_booked_room(self):
        booked_rooms = [ room for room in self.rooms if room.booked_dates]
        if booked_rooms:
            print("All booked rooms:")
            for room in booked_rooms:
                print(f"Room #{room.roomnumber}: {room.booked_dates}, {room.price} - for each room")
        else:
            print("Dont have booked room in this hotel.")


class Booking:
    def __init__(self, room, date):
        self.room = room
        self.date = date

    def __str__(self):
        return f"Booking for a {self.room.info()} room, date: {self.date}"


def main():
    hotel = Hotel("London hotel")
    for i in range(100, 199):
        hotel.new_room(Standardroom(i))
    for i in range(200, 299):
        hotel.new_room(Deluxeroom(i))


    hotel.room_booking(100, "2024-05-10")
    hotel.room_booking(101, "2024-05-11")
    hotel.room_booking(102, "2024-05-12")
    hotel.room_booking(201, "2024-05-13")
    hotel.room_booking(202, "2024-05-14")

    while True:
        print("\nChoose an option:")
        print("1. Room booking")
        print("2. Booking resign")
        print("3. All booked rooms")
        print("4. Exit")

        option = input("Choose a number: ")

        if option == "1":
            roomnumber = int(input("Standard rooms 100-199, Deluxe rooms 200-299:"))
            date = input("What date are you looking for (pl. 2024-05-10): ")
            hotel.room_booking(roomnumber, date)

        elif option == "2":
            roomnumber = int(input("What room are you wanna resign?: "))
            date = input("What date?  (pl. 2024-05-10): ")
            hotel.book_resign(roomnumber, date)
        elif option == "3":
            hotel.all_booked_room()
        elif option == "4":
            print("Exit...")
            break
        else:
            print("Wrong option. Please pick a correct option.")

if __name__ == "__main__":
    main()



