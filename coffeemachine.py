class coffee_machine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 0
        
    def display(self):
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.beans, "of coffee beans")
        print(self.cups, "of disposable cups")
        print("$" + str(self.money), "of money")
        
    def buy(self, coffe_type):
        if coffe_type == "Americano":
            if self.water >= 250 and self.beans >= 16 and self.cups >= 1:
                self.water -= 250
                self.beans -= 16
                self.cups -= 1
                self.money += 4
                print("I have enough resources, making you a coffee!")
            elif self.water < 250:
                print("Sorry, not enough water!")
            elif self.beans < 16:
                print("Sorry, not enough coffee beans!")
            elif self.cups < 1:
                print("Sorry, not enough disposable cups!")
        elif coffe_type == "Espresso":
            if self.water >= 350 and self.beans >= 20 and self.cups >= 1:
                self.water -= 350
                self.beans -= 20
                self.cups -= 1
                self.money += 7
                print("I have enough resources, making you a coffee!")
            elif self.water < 350:
                print("Sorry, not enough water!")
            elif self.beans < 20:
                print("Sorry, not enough coffee beans!")
            elif self.cups < 1:
                print("Sorry, not enough disposable cups!")
        elif coffe_type == "Latte":
            if self.water >= 200 and self.milk >= 100 and self.beans >= 12 and self.cups >= 1:
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.cups -= 1
                self.money += 6
                print("I have enough resources, making you a coffee!")
            elif self.water < 200:
                print("Sorry, not enough water!")
            elif self.milk < 100:
                print("Sorry, not enough milk!")
            elif self.beans < 12:
                print("Sorry, not enough coffee beans!")
            elif self.cups < 1:
                print("Sorry, not enough disposable cups!")
        elif coffe_type == "Cappuccino":
            if self.water >= 250 and self.milk >= 100 and self.beans >= 12 and self.cups >= 1:
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.cups -= 1
                self.money += 6
                print("I have enough resources, making you a coffee!")
            elif self.water < 200:
                print("Sorry, not enough water!")
            elif self.milk < 100:
                print("Sorry, not enough milk!")
            elif self.beans < 12:
                print("Sorry, not enough coffee beans!")
            elif self.cups < 1:
                print("Sorry, not enough disposable cups!")
        else:
            print("Invalid coffee type!")
            
    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add: "))
        self.milk += int(input("Write how many ml of milk do you want to add: "))
        self.beans += int(input("Write how many grams of coffee beans do you want to add: "))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add: "))
    def take(self):
        print("I gave you $" + str(self.money))
        self.money = 0

def main():
    coffee = coffee_machine()
    print("""   ( (
    ) )
  ........
  |      |]
  \      /   
   `----'
 """)
    while True:
        action = input("Write action (buy, fill, take, remaining, exit): ")
        if action == "buy":
            coffee.buy(input("What do you want to buy? 1 - Espresso, 2 - Latte, 3 - Americano, 4 - Cappuccino, back - to main menu: "))
        elif action == "fill":
            coffee.fill()
        elif action == "take":
            coffee.take()
        elif action == "remaining":
            coffee.display()
        elif action == "exit":
            break
        else:
            print("Invalid action!")
            
if __name__ == "__main__":
    main()