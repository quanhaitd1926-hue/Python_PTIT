from datetime import datetime

class Invoice2:
    def __init__(self, id, name, roomNumber, dateCheckIn, dateCheckOut, serviceFee):
        self.id = "KH" + f"{id:02d}"
        self.name = name
        self.roomNumber = roomNumber
        self.dateCheckIn = dateCheckIn
        self.dateCheckOut = dateCheckOut
        self.serviceFee = serviceFee
        self.days = self.dayNumber()
        self.totalPrice = self.calculateTotalPrice()

    def dayNumber(self):
        dateCheckIn = datetime.strptime(self.dateCheckIn, "%d/%m/%Y")
        dateCheckOut = datetime.strptime(self.dateCheckOut, "%d/%m/%Y")
        return (dateCheckOut - dateCheckIn).days + 1

    def calculateTotalPrice(self):
        price = {
            "1": 25,
            "2": 34,
            "3": 50,
            "4": 80
        }
        return self.days * price[self.roomNumber[0]] + self.serviceFee

    def toString(self):
        return "{} {} {} {} {}".format(
            self.id,
            self.name,
            self.roomNumber,
            self.days,
            self.totalPrice
        )

if __name__ == "__main__":
    n = int(input())
    listInvoice = []

    for i in range(n):
        name = input().strip()
        roomNumber = input().strip()
        dateCheckIn = input().strip()
        dateCheckOut = input().strip()
        serviceFee = int(input().strip())
        listInvoice.append(Invoice2(i + 1, name, roomNumber, dateCheckIn, dateCheckOut, serviceFee))

    listInvoice.sort(key=lambda invoice: invoice.totalPrice, reverse=True)

    for invoice in listInvoice:
        print(invoice.toString())