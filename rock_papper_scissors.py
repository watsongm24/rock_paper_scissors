import random

def play():
    user = input("What's your Choice? 'r' for rock, 'p' for papper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return "It's a tie"
    
    if is_win(user, computer):
        return "You won!"
    
    return " You lost!"


# r > s, s > p, p >r
def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p >r 
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True
    
print(play())