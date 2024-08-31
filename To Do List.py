# To Do List using CSV as a permanent memory
# With visual effect
'''

How data is handled

To store
Data --> dataframe --> csv

To read
csv  --> dataframe --> read data

To manipulate
csv --> dataframe --> change values in datframe --> save to csv

'''


'''

Logic for adding new tasks
=================================

Required table = empty table + table with current record (iter - 1)

(rest iter)

Required table = updated required table + table with current record


So logic should be

initialise
required table = empty

Loop:
    Required table = Required table + table with current record


'''

# Visual effect
def visual_effect(number_of_dots):
    for i in range(number_of_dots):
        print('.',end=' ',flush=True)
        time.sleep(1)
    print() #for readability


import pandas as pd
import os
import time


# Creating and empty dataframe
empty_df = pd.DataFrame(columns=['Tasks','Status'])

# Initializing required table be empty

if not os.path.isfile('my_tasks.csv'):
    open('my_tasks.csv','x')
    
    # task is assigned for first time
    combined_df = empty_df

else:
    try:
        # csv --> dataframe
        combined_df = pd.read_csv('my_tasks.csv')
    except:
        # task assigned for first time
        combined_df = empty_df
        



# To view Tasks
def view_tasks():
    try:
        print('Loading data')
        visual_effect(3)
        
        # Load the dataset
        dataset = pd.read_csv('my_tasks.csv')
        # if dataframe is not empty then this block will run
        if dataset.empty == False:
            print(dataset)
        # otherwise dataframe is empty , so task must be added
        else:
            print('No Data !!!,Try Adding some tasks')
    # will try to read csv and if its empty then this block will run
    except:
        print("No tasks added")


# To add a new task
def create_tasks(tasks = None,status = 'Incomplete'):
    
    # Visual effect
    print('Adding task to todo')
    visual_effect(3)
    
    global combined_df
    current_df = pd.DataFrame([[tasks,status]],columns=['Tasks','Status'])
    
    combined_df = pd.concat([combined_df,current_df],ignore_index= True )
    print(combined_df)
    
    combined_df.to_csv('my_tasks.csv', index=False)
    
    print() #for readability
    print('Task added to todo')
    





# To mark a task as complete
def mark_as_complete(index_of_task):
    
    # Visual effect
    print('Marking selected task')
    visual_effect(3)
    print('Task Marked as Completed')
    
    # read the csv to dataframe
    df  = pd.read_csv('my_tasks.csv')
    
    # manipulate the value
    df.loc[index_of_task, 'Status'] = 'Completed'
    
    # store the dataframe to csv 
    df.to_csv('my_tasks.csv', index=False)
    




# To remove a task
def remove_a_task(index_of_task):
    
    # Visual effect
    print('Removing selected task')
    visual_effect(3)
    print('Task removed from the list')
    
    # read the csv to dataframe
    df  = pd.read_csv('my_tasks.csv')
    
    # manipulate the value
    df.drop(index=index_of_task,inplace=True)
    
    
    # store the dataframe to csv 
    df.to_csv('my_tasks.csv',index=False)
    
    # Clearing the temporary table , so after deleting a data , new data should not contain the old data
    global combined_df
    global empty_df
    combined_df = empty_df
    





# To remove all tasks
def remove_all_tasks():
    
    # Visual effect of deletion
    print("Deleting all tasks")
    
    visual_effect(5)
    print("All Task has been deleted")
    
    df  = pd.read_csv('my_tasks.csv')
    df.drop(df.index,inplace=True)

    df.to_csv('my_tasks.csv',index=False)
    
    # Clearing the temporary table , so after deleting a data , new data should not contain the old data
    global combined_df
    global empty_df
    combined_df = empty_df
    


#User choice
while True:


    print("\n=== Available Choices ===")
    print("1. View Tasks")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Reset : Remove all Task")
    print("5. Mark a task as Complete")
    print("6. Exit")
    
    try:
        choice = int(input("Enter your choice: "))
    except:
        print('Use only numbers to navigate')
        continue
      

    if choice == 1:
        view_tasks()
        
    elif choice == 2:
        task = input("Enter task : ")
        create_tasks(task)
        
    elif choice == 3:
        index_of_task = int(input('Enter index of task to remove it : '))
        remove_a_task(index_of_task)

    elif choice == 4:
        remove_all_tasks()
    
    elif choice == 5:
        
        index_of_task = int(input("Enter index of that task you have completed: "))
        mark_as_complete(index_of_task)

    elif choice == 6:
        exit()
        
    else:
        print("Enter a valid option.")


# All Rights Reserved