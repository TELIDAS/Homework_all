class Animals:
    def __init__(self, name, quantity, dangerous,
                 cages_size, employers, ticket_cost, food, zone, energy_consumption):
        self.name = name
        if isinstance(quantity, int):
            self.quantity = quantity
        else:
            raise ValueError("Quantity is not integer")
        self.dangerous = dangerous
        self.cages_size = cages_size
        if isinstance(employers, int):
            self.employers = employers
        else:
            raise ValueError("Employers is not integer")
        if isinstance(ticket_cost, int):
            self.ticket_cost = ticket_cost
        else:
            raise ValueError("Ticket Cost is not integer")
        self.food = food
        self.zone = zone
        if isinstance(energy_consumption, int):
            self.energy_consumption = energy_consumption
        else:
            raise ValueError("Energy Consumption is not integer")

    def __str__(self):
        return f"{self.name, self.quantity}" + \
               f"{self.dangerous, self.cages_size}" + \
               f"{self.employers, self.ticket_cost, self.food, self.zone}" + \
               f"{self.energy_consumption}"


class Zoo:
    def __init__(self, species, animals, cages_size,
                 employers, ticket_cost, food, zone,
                 energy_consumption):
        self.species = species
        self.animals = animals
        self.cages_size = cages_size
        self.employers = employers
        self.ticket_cost = ticket_cost
        self.food = food
        self.zone = zone
        self.energy_consumption = energy_consumption

    def __str__(self):
        return f"{self.species}, {self.animals}, {self.cages_size}, {self.employers}, " \
               f"{self.ticket_cost}, {self.food}, {self.zone}, {self.energy_consumption}"


def show_began():
    return "Show Began"


class Zoo_Show(Zoo):
    def __init__(self, species, animals, cages_size,
                 employers, ticket_cost, food, zone,
                 energy_consumption, elephant_shows):
        super(Zoo_Show, self).__init__(species, animals, cages_size,
                                       employers, ticket_cost, food, zone,
                                       energy_consumption)
        if isinstance(elephant_shows, int):
            self.elephant_shows = elephant_shows
        else:
            raise ValueError("elephant_shows is not integer")

    def __str__(self):
        return f"{super(Zoo_Show, self).__str__()}, {self.elephant_shows}"

    def __add__(self, other):
        return f"${self.ticket_cost + other.ticket_cost}"



snake = Animals("King Cobra", 10, "Of Course",
                "medium", 3, 10, "bird or smaller snakes", "zone of snakes", 30)
print(snake)

snake2 = Animals("Python", 100, "Of course, r u kidding me?",
                 "Large", 15, 10, "frog or smaller snakes", "zone of snakes", 30)
print(snake2)

snake3 = Animals("Anaconda", 3, "say good bye to ur life",
                 "small", 1, 10, "owl or smaller snakes", "zone of snakes", 30)
print(snake3)

snake4 = Animals("Black Mamba", 4, "there is no word such a safe",
                 "small", 1, 10, "meat or smaller snakes", "zone of snakes", 30)
print(snake4)

kitty = Animals("Lions", 4, "yup",
                "Big", 2, 100, "just meat", "zone of kitty", 5)
print(kitty)

monkey = Animals("Chimpanzee", 30, "more safe than dangerous",
                 "wide", 8, 10, "fruits such a banana", "zone of monkey", 15)
print(monkey)

monkey2 = Animals("Orangutan", 12, "enough dangerous outside",
                  "medium", 2, 10, "fruits", "zone of monkey", 15)
print(monkey2)

doggy = Animals("Wolf", 20, "dangerous",
                "medium", 4, 10, "meat", "zone of doggy", 8)
print(doggy)

bishop = Animals("Elephant", 8, "safe",
                 "large", 1, 10, "plants and fruits", "zone of doggy", 8)
print(bishop)

show1 = Zoo_Show("Elephant", 8, "safe",
                 "large", 1, 10, "plants and fruits", "zone of doggy", 8)
show2 = Zoo_Show("Elephant", 8, "safe",
                 "large", 1, 10, "plants and fruits", "zone of doggy", 8)


total_ticket_cost = show1 + show2
print(total_ticket_cost)
