class Hands:
    def __init__(self, type):
        self.type = type
        if isinstance(self.type, Person):
            self.fingers_count = 5
            self.hands_count = 2
        elif isinstance(self.type, Dog):
            self.fingers_count = 4
            self.hands_count = 0


class Foots:
    def __init__(self, type_):
        self.fingers_count = 0
        self.foot_count = 0

    def total_foot_finger_count(self):
        if isinstance(type, Person):
            self.fingers_count = 5
            self.hands_count = 2
        elif isinstance(type, Dog):
            self.fingers_count = 4
            self.hands_count = 0
        return self.fingers_count * self.hands_count


class Head():
    def __init__(self):
        self.eyes = 2
        self.mouth = 1

    def head_info(self):
        return f"{self.eyes} eyes and {self.mouth} mouth"


class Voice:

    @staticmethod
    def bark():
        return "haf, haf"

    @staticmethod
    def speak():
        return 'hello there'


class Mamals:

    def __init__(self, age):
        self.age = age


class Person(Mamals):
    v = Voice()
    person_voice = v.speak()
    person_finger = Hands()
    person_head = Head.head_info()

    def __init__(self, age, name):
        super().__init__(age, name)
        self.name = name
        self.hands = Hands()


class Dog(Mamals):
    dv = Voice()
    dog_voice = dv.bark()
    dog_finger = Hands.total_hand_finger_count()
    dog_head = Head.head_info()

    def __init__(self, age):
        super().__init__(age)


harut = Person("harut", 48)
print(harut.person_voice)
