import random

class Cards:
    def __init__(self):
        """
        Initialize a deck of cards.
        """
        self.deck = []
        for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for value in range(1, 14):
                self.deck.append((value, suit))

    def shuffle(self):
        """
        Shuffle the deck of cards.
        """
        random.shuffle(self.deck)

    def deal(self):
        """
        Deal a card from the deck.
        """
        return self.deck.pop(0)
    
class Blackjack:
    def __init__(self):
        """
        Initialize the Blackjack game.
        """
        self.cards = Cards()
        self.cards.shuffle()
        self.player_hand = []
        self.dealer_hand = []
        self.player_score = 0
        self.dealer_score = 0

    def deal_initial(self):
        """
        Deal the initial cards to the player and the dealer.
        """
        for _ in range(2):
            self.player_hand.append(self.cards.deal())
            self.dealer_hand.append(self.cards.deal())
        self.calculate_score()

    def calculate_score(self):
        """
        Calculate the score of the player and the dealer.
        """
        self.player_score = 0
        self.dealer_score = 0
        for card in self.player_hand:
            self.player_score += min(card[0], 10)  # Face cards have a value of 10
        for card in self.dealer_hand:
            self.dealer_score += min(card[0], 10)

    def hit(self, hand):
        """
        Add a card to the specified hand.
        """
        hand.append(self.cards.deal())
        self.calculate_score()

    def check_blackjack(self):
        """
        Check if either the player or the dealer has a blackjack.
        """
        if self.player_score == 21:
            print("You got a blackjack! You win!")
            return True
        elif self.dealer_score == 21:
            print("Dealer got a blackjack! You lose!")
            return True
        return False

    def check_bust(self):
        """
        Check if either the player or the dealer has busted.
        """
        if self.player_score > 21:
            print("You busted! You lose!")
            return True
        elif self.dealer_score > 21:
            print("Dealer busted! You win!")
            return True
        return False

    def check_win(self):
        """
        Check who wins the game.
        """
        if self.player_score > self.dealer_score:
            print("You win!")
        elif self.player_score < self.dealer_score:
            print("You lose!")
        else:
            print("It's a tie!")

    def display_hands(self, show_dealer_hand=False):
        """
        Display the player's and the dealer's hands.
        """
        print("Your hand:", self.player_hand)
        if show_dealer_hand:
            print("Dealer's hand:", self.dealer_hand)
        else:
            print("Dealer's hand:", [self.dealer_hand[0], "X"])

    def main(self):
        """
        Main function to run the Blackjack game.
        """
        self.deal_initial()
        if self.check_blackjack():
            return
        while True:
            self.display_hands()
            action = input("Do you want to hit or stand? ").lower()
            if action == "hit":
                self.hit(self.player_hand)
                self.display_hands()
                if self.check_bust():
                    break
            elif action == "stand":
                break
            else:
                print("Invalid action. Please enter hit or stand.")
        if self.check_bust():
            return
        while self.dealer_score < 17:
            self.hit(self.dealer_hand)
        self.display_hands(show_dealer_hand=True)
        self.check_win()

if __name__ == "__main__":
    game = Blackjack()
    game.main()