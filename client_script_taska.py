from person import Person




p1 = Person("Nina", "Jolly", "Female", [1980, 12, 12])
print(p1.full_name())
p1.change_of_name("Batt")
print(p1.full_name())
# why are there None's after each print