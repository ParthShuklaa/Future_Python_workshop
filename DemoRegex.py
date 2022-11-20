#Step 1: importing the package ie re
import re
myTxt = "The Quick Brown Fox Jumps over the Lazy Dog"
myTxt1 = "My Very Educated Mother Just Show Us Nine Planets"
#Step2: Checking if the strings from "My" and ends with Planets
counting_The = re.search("^My.*Planets$",myTxt1)
if counting_The:
    print("Congratulations, we have a Match")
else:
    print("No match !!")
#Step3: Showing Output
counting_planets = re.search(".Planets$",myTxt1)
if counting_planets:
    print(" Congratulations, planet word is there at the end of string")
else:
    print("Planets word not found")

