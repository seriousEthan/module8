# Module8
# Ethan Martin

# import modules
import copy
import itertools

# Make some data, in this case a list of the Packer Quarterbacks that I have seen play a significant amount of time.
PackerQB1 = [["Don", "Majkowski", 7], ["Brett", "Favre", 4], ["Aaron", "Rodgers", 12]]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def mod8():

    print("")
    print("This is the Module 8 assignment that was completed by Ethan Martin.")
    # Make and display a shallow copy
    sc()
    # Make and display a deep copy
    dc()
    # infinite iteration
    iter_infinite()
    # zip function
    iter_zip()
    # repeat function
    iter_repeat()
    # cycle function
    iter_cycle()



def sc():
    print("")
    print("This is how shallow copy works.")
    print(f"The original data (a list of Packer QBs) is : {PackerQB1}")
    print("")
    PackerQB2 = copy.copy(PackerQB1)
    print(f"A shallow copy was made using copy.copy, and it looks like this : {PackerQB2}")
    PackerQB2 [2] [2] = 7
    print(f"What if Aaron Rodgers wanted to honor Don Majkowski and change his number to 7? It would look like this : {PackerQB2}")
    print("")
    print(f"When we print the original list we find that it has also changed : {PackerQB1}")
    PackerQB2.append(["Ethan", "Martin", 22])
    print("If I add myself to the list it does not change the first list : ")
    print(f"{PackerQB1} !=")
    print(PackerQB2)
    print("This is because I added a new object instead of modifying one of the existing objects.")
    PackerQB3 = copy.copy(PackerQB2)
    print("")
    print("If I then make a shallow copy of that list and modify the new copy it changes both nested lists, just like the first example:")
    PackerQB3 [3] [0] = "BadAss"
    print(f"{PackerQB2} ==")
    print(PackerQB3)
    print("")
    print("This is because shallow copy does not create a copy of nested objects, it just copies the reference number of the object. As we will see this is solved")
    print("by making a deep copy of the nested objects.  This will copy the object itself and populate that object with objects with a new refrence id.")

def dc():
    print("")
    print("This is how deep copy works.")
    print(f"The original data (a list of Packer QBs) is : {PackerQB1}")
    print("")
    PackerQB2 = copy.deepcopy(PackerQB1)
    print(f"A deep copy was made using copy.deepcopy, and it looks like this : {PackerQB2}")
    PackerQB2[2][2] = 12
    print(f"What if Aaron Rodgers decided he disliked Don Majkowski and changed his number back to 12? It would look like this : {PackerQB2}")
    print("")
    print(f"When we print the original list we find that it has not changed this time : {PackerQB1}")
    print(f"This is because deep copy recursively copied the nested items as well as the non-nested items.")



def iter_infinite():
    print("This is a function that prints an infinite string of numbers. I passed it a starting place of 1 and")
    print("a step of negative .5, I also added a break when the number gets to -5.  If I hadn't the counter would")
    print("have kept going infinitely.  I proved this by forgetting the negative sign the first time.")
    print("")
    for i in itertools.count(1, -0.5):

        if i == -5:
            break
        print(str(i))



sales = [200, 300, 250, 350, 600, 500, 350]

def iter_zip():
    counter = itertools.count(1)
    print("")
    print("Another useful function is zip. This will pair two iterable objects into a single object. If you wrap")
    print("that in a list function it is easy to print out the result.")
    print("In this case I will pair a fictional list of daily sales with a counter I created using the intertools.count function.")
    daily_sales = list(zip(counter, sales))
    print(daily_sales)
    print("")
    print("You could also use the range function to do this as you can see below :")
    daily_sales2 = list(zip(range(1, 10), sales))
    print(daily_sales2)
    print("")
    print("Both of these methods will only go as long as the shortest object.  Both of the counters I used could have gone")
    print("longer, infinite counters are good for this when you don't know how much data you have or if the amount of data changes frequently.")
    print("")
    print("If you use the intertools.zip_longest function the pairing continues until the longest object is done. In this case I specified that")
    print("it stop before it equals ten. When there is no data to pair the function replaces the missing values with None, which is a NULL value.")
    print("")
    daily_sales3 = list(itertools.zip_longest(range(1, 10), sales))
    print(daily_sales3)



def iter_repeat():
    print("")
    print("I will use the itertools.repeat function to repeat the weeks worth of sales data I used earlier four times")
    print(f"in order to generate a months worth of sales data. The original version : {sales}")
    monthly_sales = list(itertools.repeat(sales, 4))
    print(f"The new month long version with 4 nested weeks : {monthly_sales}")



def iter_cycle():
    print("")
    print("Now I am going to use the itertool.cycle function.  This will repeat a iterable object infinitely. In this")
    print("case I am going to use it to repeat the days of the week twice.")
    print("")
    cntr = 0
    for i in itertools.cycle(days):
        cntr += 1
        if cntr == 15:
            break
        print (i)

mod8()
