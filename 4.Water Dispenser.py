from collections import deque
queue = deque()
litters = int(input())
command = input()
while command != 'Start':
    queue.append(command)
    command = input()
command = input().split()
while command[0] != 'End':
    if command[0] == 'refill': # if command.startswith('refill')
        litters += int(command[1])# liiters += int(command.split()[-1])
    elif int(command[0]) <= litters:
        name = queue.popleft()
        print(f'{name} got water')
        litters -= int(command[0])
    else:
        name = queue.popleft()
        print(f'{name} must wait')
    command = input().split()
print(f'{litters} liters left')



'''
Write a program that reads on the first line the starting quantity of water in a dispenser. Then on the next few lines you will be given the names of some people that want to get water (each on separate line) until you receive the command "Start". Add those people in a queue. Finally, you will receive some commands until the command "End":
-	{liters} - Litters that the current person in the queue wants to get. Check if there is enough water in the dispenser for that person.
o	If there is enough water, print "{person_name} got water" and remove him/her from the queue.
o	Otherwise, print "{person} must wait" and remove the person from the queue without reducing the water in the dispenser
-	refill {liters} - add the given litters in the dispenser.
At the end print how many litters of water are left in the format: "{left_liters} liters left"
Examples
Input	Output	Comment
2
Peter
Amy
Start
2
refill 1
1
End	Peter got water
Amy got water
0 liters left	We create a queue with Peter and Amy. After the start command we see that Peter wants 2 liters of water (and he gets them). Water dispenser is left with 0 liters. After refulling, there is 1 liter in the dispenser. So when Amy wants 1 liter, she gets it and there are 0 liters left in the dispenser
10
Peter
George
Amy
Alice
Start
2
3
3
3
End	Peter got water
George got water
Amy got water
Alice must wait
2 liters left

'''