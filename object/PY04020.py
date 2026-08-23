class Invoice3:
    def __init__(self, id, name, quantity, unitPrice, discountAmount, totalPrice):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.unitPrice = unitPrice
        self.discountAmount = discountAmount
        self.totalPrice = totalPrice

    def toString(self):
        return "{} {} {} {} {} {}".format(self.id, self.name, self.quantity,
            self.unitPrice, self.discountAmount, self.totalPrice)

def calculatorTotalPrice(quantity, unitPrice, discountAmount):
    return quantity * unitPrice - discountAmount

if __name__ == "__main__":
    n = int(input())
    listInvoice = []
    for i in range(n):
        id = input()
        name = input()
        quantity = int(input())
        unitPrice = int(input())
        discountAmount = int(input())
        totalPrice = calculatorTotalPrice(quantity, unitPrice, discountAmount)
        listInvoice.append(Invoice3(id, name, quantity, unitPrice, discountAmount, totalPrice))
    listInvoice.sort(key=lambda invoice: -invoice.totalPrice)
    for invoice in listInvoice:
        print(invoice.toString())