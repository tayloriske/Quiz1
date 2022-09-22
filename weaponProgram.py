import weaponClass as w
import csv


'''
- Craete a program that will read the contents of the file 'weapons.txt'. Each record in the file represents the specs to a weapon.
- Create an instance of the weapon object for each record. 
- Create a dictionary that will contain the name of the weapon as the key and the number of bullets as the value. 
- Print out details of each weapon using the object's methods only (as per comments below). 
- Fire all bullets of the weapon and print a countdown of bullets remaining (run exe file to visualize, HINT: use end='\r' in your print statement).
- Print out the name of the weapon and the number of bullets from the dictionary.

HINT: Follow the comments for each line to help with the logic of the problem.
'''


# create a file object to open the file in read mode

with open("weapons.txt", "rb") as infile, open("weapons.csv", "wb") as outfile:
    next(infile)
    outfile.write(infile.read())

#create an empty dictionary named 'weapons_dict'

weapons_dict = {}

#use a for loop to iterate through every row of the csv file

    #use variables for name,speed and range (optional)
    

    # create an instance of the weapon object using the 
    # specs from the csv file (name,speed and range) 
    

    # append the name and bullet count to 'weapons_dict'
    
def main():
    name = input("Name:")
    speed = input("Speed:")
    range = input("Range:")

    weapon = w.Weapon(name, speed, range)
    bullets = weapon.get_bullets()
    # print out the name of the weapon using the appropriate method of the object 
    print("Weapon Name:", weapon.get_name())
    # print out the speed of the weapon using the appropriate method of the object
    print("Speed:", weapon.get_speed())
    # print out the range of the weapon using the appropriate method of the object
    print("Range:", weapon.get_range())
    # print out the number of bullets of the weapon using the appropriate method of the object
    print("Number of Bullets:", bullets)

    #use an input statement to halt the program and wait for the user - 
    
    
    
    # use an appropriate loop to keep firing the weapon until all bullets run out
    while bullets>0:
        input("Press any key to fire the weapon")
        weapon.fire_bullet()
        print(weapon.get_bullets())
        # call the appropriate method to fire a bullet
       
        # print out the bullet count every time the weapon is fired
main()     

    


#using a loop print out the name and number of bullets from the dictionary
#I RAN OUT OF TIME!