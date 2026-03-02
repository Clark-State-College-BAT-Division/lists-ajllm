#Create two seperate lists for player one and player two. 
#Each one should contain 10 random numbers between 1 and 50.
#Again, your lists should be random numbers
#Do NOT sort the lists.
#Compare the lists in order. Whichever list has the higher number wins.
#Keep track of how many times each list wins.
#Find the highest number in each list and it's index. If the number occers multiple times take the first instsance.
#Find the lowest number in each list and it's index. If the number occers multiple times take the first instsance.
#A tie is not record as a win for either player
#Display the lists
#Report to the user how many times each player won and the information from lines 6 and 7.
#For the example output I am limiting the range to 1 to 9 to keep it more readable.

#Player One = 5,7,2,9,1,1,3,8,6,9
#Player Two = 3,8,5,5,8,1,4,7,4,7
#Player one won 5 times
#Player two won 4 times
#Player one's highest number is 9 at index 3
#Player two's highest number is 8 at index 1
#Player one's lowest number is 1 at index 4
#Player two's lowest number is 1 at index 5

import random

player1 = []
player2 = []

for i in range (10):
    player1.append(int(random.randint(1,50)))
    
for i in range (10):
    player2.append(int(random.randint(1,50)))

print("Player 1s Numbers Were: " +  str(player1))
print("Player 2s Numbers Were: " +  str(player2))

player1Wins = 0
player2Wins = 0

for i in range(len(player1)):
     if player1[i] > player2 [i]:
        player1Wins += 1
     elif player2[i] > player1[i]:
         player2Wins += 1
     else:
         print("Tie...")


print(f"Player 1 Won {player1Wins} Times!")
print(f"Player 2 Won {player2Wins} Times!")

p1Highest = max(player1)
p1HIndex = player1.index(p1Highest)
p2Highest = max(player2)
p2HIndex = player2.index(p2Highest)

print(f"Player 1s highest number was {p1Highest} at index {p1HIndex}")
print(f"Player 2s highest number was {p2Highest} at index {p2HIndex}")

p1Lowest = min(player1)
p1LIndex = player1.index(p1Lowest)
p2Lowest = min(player2)
p2LIndex = player2.index(p2Lowest)

print(f"Player 1s lowest number was {p1Lowest} at index {p1LIndex}")
print(f"Player 2s lowest number was {p2Lowest} at index {p2LIndex}")