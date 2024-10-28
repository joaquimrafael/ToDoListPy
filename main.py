from collections import deque
# By Joaquim Prieto 2024
if __name__ == "__main__":
    
    chores = deque()
    cond = True
    choice = 0
    current_task = "<none>"
    
    while(cond):
        
        print("\n---ToDO List---")
        print("1 - Start next task")
        print("2 - Insert a task")
        print("3 - Verify next task todo")
        print("4 - Show how many tasks remaining")
        print("5 - Remove all tasks")
        print("6 - Leave")
        print("Current task: " + current_task)
        choice = int(input("\nChose your option: ").strip())
        print()
        
        if choice == 1:
            if len(chores) == 0:
                print("Add tasks first!")
            else:
                current_task = chores.popleft()
                print("Starting {}".format(current_task))
            continue
        
        elif choice == 2:
            new_task = input("Type your new task: ").strip()
            chores.append(new_task)
            print("Task successfully added\n")
            continue
        
        elif choice == 3:
            if len(chores) == 0:
                print("Add tasks first!")
            else:
                print(chores[0])
            continue
        
        elif choice == 4:
            print(f"{len(chores)} task(s) remaining")
            continue
        
        elif choice == 5:
            if len(chores) == 0:
                print("Nothing to clear")
            else:
                chores.clear()
                print("Cleared.")
            continue
        
        elif choice == 6:
            print("Closing...")
            cond = False
            break
        
        else:
            print("Invalid Option")
            continue
            
#TODO: Implement an UI
