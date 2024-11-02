import pandas

df = pandas.read_csv("hotels.csv",dtype={"id":str})

class Hotel:
    def __init__(self,id):
        self.hotel_id = id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()
    
    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv",index=False)

    def available(self):
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

class ReservationTicket:
    def __init__(self, customer_name, hotel):
        self.customer_name = customer_name
        self.hotel = hotel

    def generate(self):
        content=f"""
            Thanks for booking
            Booking Data:
            Name: {self.customer_name}
            Hotel: {self.hotel.name}
        """
        return content

id = input("Enter id")
hotel = Hotel(id)
if hotel.available():
    hotel.book()
    name = input("Enter ur name")
    reservation_ticket = ReservationTicket(name,hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel not available")