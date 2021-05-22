from collections import deque
queue = deque()
while True:
    command = input()
    if command == "Paid":
        while len(queue):
            print(queue.popleft())
    elif command == "End":
        print(f"{len(queue)} people remaining.")
        break
    else:
        queue.append(command)

'''
Write a program that reads an input consisting of a name and adds it to a queue until "End" is received. If you receive "Paid", print every customer name and empty the queue, otherwise we receive a client and we must add him to the queue. When we receive "End", we must print the count of the remaining people in the queue in the format: "{count} people remaining."
 
Examples
Input	Output
George
Peter
William
Paid
Michael
Oscar
Olivia
Linda
End	

George
Peter
William
4 people remaining.
Anna
Emma
Alexander
End	3 people remaining.

'''