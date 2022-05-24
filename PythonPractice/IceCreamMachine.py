class IceCreamMachine:

    #constructor
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings
        #ingredient_toppings is a tuple because it is a comma seperate collection
        self.ingredient_toppings = ingredients[0],toppings[0] 

    def scoops(self):
        #return alternation of 1st ingredient and 1st topping 
        list_output = []
            
        for ing in self.ingredients:
            for top in self.toppings:
                list_output.append([ing, top])
        return list_output
        


if __name__ == "__main__":
    machine = IceCreamMachine(["vanilla","chocolate"],["chocolate sauce"])
    print(machine.scoops())
