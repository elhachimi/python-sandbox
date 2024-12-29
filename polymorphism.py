class GenZ:
    def tell_state(self):
        return "Sekhfan 😴"


class Millennial:
    def tell_state(self):
        return "Baghi izendeg 🛌"


def state_of(person):
    return person.tell_state()


yasser = GenZ()
anas = Millennial()

print(f"daba yasser {state_of(yasser)} ou Anas {state_of(anas)}")
