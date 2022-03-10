class Team:
    def __init__(self,name,id,boss,drivers,car):
        self.name= name
        self.id= id
        self.boss= boss
        self.drivers= drivers
        self.car= car

Mercedes= Team(
    name= "Mercedes-AMG Petronas F1 Team",
    id= 1,
    boss= "Toto Wolff",
    drivers= ("Lewis Hamilton","George Russell"),
    car= "W13"
)

RedBull= Team(
    name= "Oracle Red Bull Racing",
    id= 2,
    boss= "Christian Horner",
    drivers= ("Max Verstappen","Sergio Perez"),
    car= "RB18"
)

Ferrari= Team(
    name= "Scuderia Ferrari",
    id= 3,
    boss= "Mattia Binotto",
    drivers= ("Charles Leclerc","Carlos Sainz"),
    car= "F1-75"
)

McLaren= Team(
    name= "McLaren F1 Team",
    id= 4,
    boss= "Andreas Seidl",
    drivers= ("Daniel Ricciardo","Lando Norris"),
    car= "MCL36"
)

Alpine= Team(
    name= "BWT Alpine F1 Team",
    id= 5,
    boss= "Otmar Szafnauer",
    drivers= ("Fernando Alonso","Esteban Ocon"),
    car= "A522"
)

AlphaTauri= Team(
    name= "Scuderia AlphaTauri",
    id= 6,
    boss= "Franz Tost",
    drivers= ("Pierre Gasly","Yuki Tsunoda"),
    car= "AT03"
)

AstonMartin= Team(
    name= "Aston Martin Aramco Cognizant F1 Team",
    id= 7,
    boss= "Mike Krack",
    drivers= ("Sebastian Vettel","Lance Stroll"),
    car= "AMR22"
)

Williams= Team(
    name= "Williams Racing",
    id= 8,
    boss= "Jost Capito",
    drivers= ("Nicholas Latifi","Alexander Albon"),
    car= "FW44"
)

AlfaRomeo= Team(
    name= "Alfa Romeo F1 Team ORLEN",
    id= 9,
    boss= "Frederic Vasseur",
    drivers= ("Valtteri Bottas","Zhou Guanyu"),
    car= "C42"
)

Haas= Team(
    name= "Haas F1 Team",
    id= 10,
    boss= "Guenther Steiner",
    drivers= ("Mick Schumacher","Kevin Magnussen"),
    car= "VF-22"
)

team_list= [Mercedes,RedBull,Ferrari,McLaren,Alpine,AlphaTauri,AstonMartin,Williams,AlfaRomeo,Haas]