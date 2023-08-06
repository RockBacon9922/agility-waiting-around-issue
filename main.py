# I do alot of dog agility and I am sick and tired of the waiting around for my next class to start. They always seem to be at each end of the day.
# so I am going to create a random show with random dogs and i want to create an algorithm that will work out the best way to schedule the classes
# so that there is minimal waiting around for the handlers and dogs.

# %%
from faker import Faker
from faker.providers import DynamicProvider
import random
fake = Faker()

eventType = DynamicProvider(provider_name='eventType', elements=["Jumping", "Agility", "Swap", "Pairs"])
fake.add_provider(eventType)

# %%
# Dog and Runner Creation
class Dog:
    def __init__(self, name: str):
        self.name = name

class Runner:
    def __init__(self, name: str, dogs: list[Dog]):
        self.name = name
        self.dogs = dogs

def createDog() -> Dog:
    """Create a dog"""
    name = fake.first_name()
    return Dog(name)

def createRunners(numberOfRunners: int, maxDogs: int) -> list:
    """Create a list of runners with dogs"""
    return [Runner(fake.first_name(), [createDog() for i in range(0, random.randint(1, maxDogs))]) for i in range(0, numberOfRunners)]

# %%
class Class:
    def __init__(self, name: str, dogs: list[Dog]):
        self.name = name
        self.dogs = dogs

def createClass (name: str, dogs: list[Dog]) -> Class:
    # create a random number between 3 and the number of dogs
    dogList = [dogs[i] for i in range(random.randint(3, len(dogs)))]

    return Class(name, dogList)

# %%
class Ring:
    def __init__(self, id: int, classes: list[Class]):
        self.id = id
        self.classes = classes

def createRing(classes: list[Class], id: int) -> Ring:
    return Ring(id, classes)

# %%
class Show:
    def __init__(self, name: str, rings: list[Ring]):
        self.name = name
        self.rings = rings

def createShow(name: str, rings: list[Ring]):
    return Show(name, rings)

# %%
numRunners = 300
maxDogs = 3
numRings = 6
classesPerRing = 4

# %%
# Created our runners
runners = createRunners(numRunners, maxDogs)

# %%
# create our classes

# get all the dogs from every runner and put them in a list
dogs = [dog for runner in runners for dog in runner.dogs]

rings = [createRing(id=i, classes=[createClass(name=fake.eventType(), dogs=dogs)]) for i in range(numRings)]

# %%
# use the rings to create a show
show = createShow(name=fake.company(), rings=rings)

# %%
# create a list of all the dogs in the show
allDogs = [dog for ring in show.rings for class_ in ring.classes for dog in class_.dogs]

# %%
# create a list of all the classes in the show
allClasses = [class_ for ring in show.rings for class_ in ring.classes]

# %%
# create a list of all the runners in the show
allRunners = [runner for runner in runners]

# %%
# create a list of all the rings in the show
allRings = [ring for ring in show.rings]

# %%
# create an algorithm to work out the best way to schedule the classes
# so that there is minimal waiting around for the handlers and dogs.
# aprox 2 mins per dog per class plus 10 mins between classes

# %%
def calculateTime(class_: Class) -> int:
    return len(class_.dogs) * 2 + 10

calculateTime()

# %%
def calculateRingTime(ring: Ring) -> int:
    return sum([calculateTime(class_) for class_ in ring.classes])

calculateRingTime()

# %%
def calculateShowTime(show: Show) -> int:
    return sum([calculateRingTime(ring) for ring in show.rings])


# %%
