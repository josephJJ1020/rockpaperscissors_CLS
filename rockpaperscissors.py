import random
import time


class Player:
    def __init__(self):
        self.score = 0
        self.pick = None


class Game:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.options = ["Y", "N"]
        self.running = True

    def run(self):
        if self.running is False:
            exit()

        else:
            print("Rock paper scissors game\nRace to 5\n1 = rock; 2 = paper; 3 = scissors")

            def close():
                play_again = input("Would you like to play again? (Y/N)").upper()
                if play_again not in self.options:
                    print("Invalid input!")
                    close()

                if play_again == self.options[0]:
                    computer.score = 0
                    player.score = 0
                    play()

                if play_again == self.options[1]:
                    print("Thank you for playing!")
                    self.running = False
                    self.run()

            def play():

                if player.score == 5:
                    print("You win!")
                    close()

                elif computer.score == 5:
                    print("You lose!")
                    close()

                else:
                    time.sleep(1)
                    player_input = int(input("Place your pick!"))
                    if player_input > 3 or player_input < 1:
                        print("Invalid input!")
                        play()

                    player.pick = self.choices[player_input-1]
                    computer.pick = random.choice(self.choices)

                    if computer.pick == player.pick:
                        print(f"\n\n\n\n\nYou both picked {computer.pick}! Try again!")
                        print(f"Player {player.score} - {computer.score} Computer\n\n\n\n")
                        play()

                    if computer.pick == self.choices[0]:
                        print(f"\n\n\n\n\nComputer picked {computer.pick}!")
                        time.sleep(1)

                        if player.pick == self.choices[1]:
                            print("You win!")
                            player.score += 1
                            print(f"Player {player.score} - {computer.score} Computer\n\n\n\n")
                            play()

                        if player.pick == self.choices[2]:
                            print("You lose!")
                            computer.score += 1
                            print(f"Player {player.score} - {computer.score} Computer\n\n\n\n")
                            play()

                    if computer.pick == self.choices[1]:
                        print(f"\n\n\n\n\nComputer picked {computer.pick}!")
                        time.sleep(1)

                        if player.pick == self.choices[0]:
                            print("You lose!")
                            computer.score += 1
                            print(f"Player {player.score} - {computer.score} Computer\n\n\n\n")
                            play()

                        if player.pick == self.choices[2]:
                            print("You win!")
                            player.score += 1
                            print(f"Player {player.score} - {computer.score} Computer\n\n\n\n")
                            play()

                    if computer.pick == self.choices[2]:
                        print(f"\n\n\n\n\nComputer picked {computer.pick}!")
                        time.sleep(1)

                        if player.pick == self.choices[0]:
                            print("You win!")
                            player.score += 1
                            print(f"Player {player.score} - {computer.score} Computer\n\n\n\n")
                            play()

                        if player.pick == self.choices[1]:
                            print("You lose!")
                            computer.score += 1
                            print(f"Player {player.score} - {computer.score} Computer\n\n\n\n")
                            play()
            play()


player = Player()
game = Game()
computer = Player()

if __name__ == "__main__":
    game.run()
