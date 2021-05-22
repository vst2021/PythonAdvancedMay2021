from collections import deque

children = deque(input().split())
count = int(input())

while len(children) > 1:
    children.rotate(-count)
    print(f'Removed {children.pop()}')
print(f'Last is {children.popleft()}')

'''
Hot potato is a game in which children form a circle and start passing a hot potato. The counting starts with the first kid. Every nth toss the child left with the potato leaves the game. When a kid leaves the game, it passes the potato along. This continues until there is only one kid left.
Create a program that simulates the game of Hot Potato. Print every kid that is removed from the circle. In the end, print the kid that is left last.
Examples
Input	Output
Tracy Emily Daniel
2	Removed Emily
Removed Tracy
Last is Daniel
George Peter Michael William Thomas
10	Removed Thomas
Removed Peter
Removed Michael
Removed George
Last is William
George Peter Michael William Thomas
1	Removed George
Removed Peter
Removed Michael
Removed William
Last is Thomas



'''