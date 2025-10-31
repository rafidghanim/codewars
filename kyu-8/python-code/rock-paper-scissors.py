def rps(p1, p2):
    #your code here
    return "Draw!" if p1 == p2 else "Player 1 won!" if (p1, p2) in [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")] else "Player 2 won!"

#     if p1 == p2:
#         return "Draw!"
#     elif (p1, p2) in [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")]:
#         return "Player 1 won!"
#     else:
#         return "Player 2 won!"

#     if p1==p2:
#         return "Draw!"
#     elif p1=="rock" and p2=="scissors":
#         return "Player 1 won!"
#     elif p1=="scissors" and p2=="rock":
#         return "Player 2 won!"
#     elif p1=="paper" and p2=="scissors":
#         return "Player 2 won!"
#     elif p1=="scissors" and p2=="paper":
#         return "Player 1 won!"
#     elif p1=="paper" and p2=="rock":
#         return "Player 1 won!"
#     elif p1=="rock" and p2=="paper":
#         return "Player 2 won!"
