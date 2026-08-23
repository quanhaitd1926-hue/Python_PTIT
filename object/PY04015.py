class Invoice1:
    def __init__(self, id, name, oldIndex, newIndex):
        self.id = "KH" + f"{id:02d}"
        self.name = name
        self.oldIndex = oldIndex
        self.newIndex = newIndex
        self.money = self.calculateMoney()

    def calculateMoney(self):
        index = self.newIndex - self.oldIndex
        if index <= 50:
            total = index * 100
            return total + total * 0.02
        elif index <= 100:
            total = 50 * 100 + (index - 50) * 150
            return total + total * 0.03
        else:
            total = 50 * 100 + 50 * 150 + (index - 100) * 200
            return total + total * 0.05

    def toString(self):
        return self.id + " " + self.name + " " + f"{self.money:.0f}"

if __name__ == "__main__":
    n = int(input())
    listInvoice = []
    for i in range(1, n + 1):
        name = input()
        oldIndex = int(input())
        newIndex = int(input())
        listInvoice.append(Invoice1(i, name, oldIndex, newIndex))
    listInvoice.sort(key=lambda invoice: (-invoice.money, invoice.id))
    for invoice in listInvoice:
        print(invoice.toString())