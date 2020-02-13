'''
A script for checking lotto numbers after sorting the original CSV file
and extracted the columns that will be used for the number generator 
'''
import csv
from pprint import pprint

def example_data_structure():
       data = {}
       with open('newNumbers.csv') as new_number_file:
           csv_reader = csv.DictReader(new_number_file, delimiter =',')
           for row in csv_reader:
                  if row['Draw Date'] != "":
                         data.update(row)
       return data

def add_data_to_list():
       data = {}
       datas = []
       with open('newNumbers.csv') as new_number_file:
           csv_reader = csv.DictReader(new_number_file, delimiter =',')
           for row in csv_reader:
                  if row['Draw Date'] != "":
                         datas.append(row)
       return datas

def create_machine_list():
       line_count = 0                  
       machine_list = []
       datas = add_data_to_list()
       for x in datas:
           i = x.get("Draw Machine")
           if i != " " :
                  if i not in machine_list:
                         machine_list.append(i)    
           line_count += 1
       return machine_list

def create_ball_set_list():
       line_count = 0                  
       ball_set_list = []
       datas = add_data_to_list()
       for x in datas:
           y = x.get("Ball Set")
           if y != " " :    
                  if y not in ball_set_list:
                         ball_set_list.append(y)
           line_count += 1
       return ball_set_list

def stringlist_to_intlist(ball_set_list):
       #Convert strings in ball_set_list to integers
       for i in range(len(ball_set_list)):
              ball_set_list[i] = int(ball_set_list[i])
       return(ball_set_list)

def find_missing_numbers(ballset_num):
       line_count = 0
       key_count = 0
       ball_set_list = []
       keys = ["Ball 1","Ball 2","Ball 3","Ball 4","Ball 5","Ball 6"]
       datas = add_data_to_list()
       for x in datas:
              y = x.get("Ball Set")
              if y == ballset_num:
                     for i in range(len(keys)):
                            if datas[line_count][keys[i]] not in ball_set_list:
                                   ball_set_list.append(datas[line_count][keys[i]])
              line_count += 1      
       return ball_set_list

def find_missing_bonus_numbers(ballset_num):
       line_count = 0
       key_count = 0
       ball_set_list = []
       keys = ["Bonus Ball"]
       datas = add_data_to_list()
       for x in datas:
              y = x.get("Ball Set")
              if y == ballset_num:
                     for i in range(len(keys)):
                            if datas[line_count][keys[i]] not in ball_set_list:
                                   ball_set_list.append(datas[line_count][keys[i]])
              line_count += 1      
       return ball_set_list

x = find_missing_bonus_numbers("30")
stringlist_to_intlist(x)
x.sort()
print(x)
x = find_missing_bonus_numbers("25")
stringlist_to_intlist(x)
x.sort()
print(x)
x = find_missing_bonus_numbers("1")
stringlist_to_intlist(x)
x.sort()
print(x)

'''
structure = example_data_structure()
machine_list = create_machine_list()
ball_set_list = create_ball_set_list()
stringlist_to_intlist(ball_set_list)
ball_set_list.sort()
pprint(structure)
pprint(machine_list)
print(ball_set_list)

'''





