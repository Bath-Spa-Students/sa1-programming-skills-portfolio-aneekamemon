# Control Structures

'''

Imagine an alien was just shot down in a game. Create a variable called alien_color and
assign it a value of 'green', 'yellow', or 'red'.

•Write an if statement to test whether the alien’s color is green. If it is, print a message
that the player just earned 5 points.

•Write one version of this program that passes the if test and another that fails. (The
version that fails will have no output.)

# This has been copied from the bonus exercise sheet.

'''
alien_colors = ["green", "yellow", "red"]   # Dictionary with different alien colors

user_input = input("\nEnter the color of the alien: ").lower() # .lower() allows for the colors to be typed in lowercased. 

points_gained = 0       # The starting amounts of points.


if user_input == alien_colors[0]:   # for Green colored alien

    points_gained =+ 5      # 5 points gained if an green alien is killed


    print (f"\nYOU HAVE GAINED {points_gained} POINTS")


elif user_input == alien_colors[1]: # for yellow colored alien

    points_gained =+ 3      # 3 points gained if an yellow alien is killed


    print (f"\nYOU HAVE GAINED {points_gained} POINTS")


elif user_input == alien_colors[2]:     ## for red colored alien

    points_gained =+ 1      # 1 point gained if an red alien is killed


    print (f"\nYOU HAVE GAINED {points_gained} POINT")


else:
    print ("You haven't gained any points so far.")     # If a color is that isnt in the dictionary is typed in, then no points are to be given...


