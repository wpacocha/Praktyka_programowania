# Produkt - obiekt, który budujemy
class Pizza:
    def __init__(self):
        self.cheese = False
        self.sauce = None
        self.meat = None
        self.veggies = []

    def __str__(self):
        return f"Pizza(cheese={self.cheese}, sauce={self.sauce}, meat={self.meat}, veggies={self.veggies})"


# builder - interfejs utawiajacy czesci obiektu
class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def add_cheese(self):
        self.pizza.cheese = True
        return self

    def add_sauce(self, sauce_type):
        self.pizza.sauce = sauce_type
        return self

    def add_meat(self, meat_type):
        self.pizza.meat = meat_type
        return self

    def add_veggies(self, *veggies):
        self.pizza.veggies.extend(veggies)
        return self

    def build(self):
        return self.pizza


# director - opcjonalny, zarzadza procesem budowy
class PizzaDiretor:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def build_pepperoni_pizza(self):
        return (
            self.builder.add_cheese()
            .add_sauce("tomato")
            .add_meat("pepperoni")
            .add_veggies("olives", "peppers")
            .build()
        )

    def build_veggie_pizza(self):
        return (
            self.builder.add_cheese()
            .add_sauce("pesto")
            .add_veggies("mushrooms", "spinach", "onions")
            .build()
        )


# uzycie
builder = PizzaBuilder()
director = PizzaDiretor(builder)

pizza1 = director.build_pepperoni_pizza()
print(pizza1)

pizza2 = director.build_veggie_pizza()
print(pizza2)

# mozna recznie
custom_pizza = (
    PizzaBuilder()
    .add_cheese()
    .add_sauce("bbq")
    .add_meat("chicken")
    .add_veggies("onion")
    .build()
)
print(custom_pizza)
