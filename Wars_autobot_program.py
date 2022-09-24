from random import shuffle
from time import sleep



#Crea una baraja
class Cards:
    numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', "Jack", "Queen", "King", 'Ace']
    suits = ['spades', 'hearts', 'diamonds', 'clubs']
    deck = []

    def __init__(self):
        for s in self.suits:
            for n in self.numbers:
                self.deck.append((f'{n} of {s}'))

#Crea a los jugadores (nombre, sus cartas y puntos)
class Players():
    players = []
    
    def __init__(self):
        self.name = input(f"Input player {str(len(self.players) + 1)}: ").upper()
        self.players.append(self.name)
        self.cards = []
        self.points = 0

#Asigna jugadores avariables y distribuye cartas
class Game(Cards):
    player_1 = Players()
    player_2 = Players()
    Cards()

    def __init__(self):
        self.card_dist()

    def card_dist(self):
        shuffle(self.deck)
        # sleep(1)
        print("Shuffling cards")
        # sleep(1)
        print("Dealing cards")

        while len(self.deck) >= 1:
            self.player_1.cards.append(self.deck[-1])
            self.deck.pop()
            self.player_2.cards.append(self.deck[-1])
            self.deck.pop()
        
        print("Cards dealed")
        print(f"Player 1: {len(self.player_1.cards)} cards")
        print(f"Player 2: {len(self.player_2.cards)} cards")

#Crea y aplica las mecánicas, cuenta puntos y decide ganadores
class Play(Game):

    def __init__(self):
        # sleep(2)
        Game()
        self.round = 1
        while self.player_1.cards or self.player_2.cards:
            print(f"Round {self.round}")
            sleep(2)
            self.play_cards()
            print("Playing cards")
            self.mechanics(self.card_1, self.card_2)
            self.round += 1
        self.end()

    def play_cards(self):
        self.card_1 = self.player_1.cards[-1]
        self.player_1.cards.pop()
        self.card_2 = self.player_2.cards[-1]
        self.player_2.cards.pop()
        print(self.card_1)
        # sleep(1)
        print(self.card_2)
    
    def mechanics(self, card_1, card_2):
        val_1 = Cards.numbers.index(card_1.split(" ")[0])
        val_2 = Cards.numbers.index(card_2.split(" ")[0])
        
        if val_1 == val_2:
            val_1 = Cards.suits.index(card_1.split(" ")[-1])
            val_2 = Cards.suits.index(card_2.split(" ")[-1])

        if val_1 > val_2:
            self.player_1.points += 1
            print(f"Point for {Game.player_1.name}")
        elif val_1 < val_2:
            self.player_2.points += 1
            print(f"Point for {Game.player_2.name}")

    def end(self):
        print(f"{self.player_1.points} vs {self.player_2.points}")
        if self.player_1.points > self.player_2.points:
            print(f"{Game.player_1.name} winss!!")
        elif self.player_1.points < self.player_2.points:
            print(f"{Game.player_2.name} winss!!")
        elif self.player_1.points == self.player_2.points:
            print("Is a draww!!")

   
        

    
    
#Cards: Crear baraja
#Players: Crear jugadores, repartir baraja
# Game: Mecanicas con la baraja, decir ganador


Play()