import pandas

df = pandas.read_csv("hotels.csv",dtype={"id":str})
df_cards = pandas.read_csv("cards.csv",dtype=str).to_dict(orient="records")

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

class CreditCard:
    def __init__(self,number):
        self.number = number
        pass

    def validate(self,expiration,holder, cvc):
        card_data = {"number":self.number,"expiration":expiration,
                     "holder":holder,"cvc":cvc}
        if card_data in df_cards:
            return True
        


id = input("Enter hotel id: ")
hotel = Hotel(id)
if hotel.available():
    credit_card = CreditCard(number = "1234")
    if credit_card.validate(expiration="12/26",holder = "JOHN SMITH", cvc="123"):
        hotel.book()
        name = input("Enter your name: ")
        reservation_ticket = ReservationTicket(name,hotel)
        print(reservation_ticket.generate())
    else:
        print("Bad credit card")
else:
    print("Hotel not available")