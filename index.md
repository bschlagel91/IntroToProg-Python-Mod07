# Assignment07
*Brandon Schlagel, 8.24.2021*

List of Links:

-GITHUB Repository: https://github.com/bschlagel91/IntroToProg-Python-Mod07

-GITHUB Website: 

-Pickling Resource: https://www.datacamp.com/community/tutorials/pickle-python-tutorial#what

-Structured error proof (try/except): https://www.techbeamers.com/use-try-except-python/

## Introduction
The assignment is to create a script that pickles a document, shows structured error handling, or does both at the same time and demonstrate your skills doing them.  I decided to do both in the same script.   However, when I built the script, I first made sure that the script pickled correctly, then create script that guided the user to use the correct data types that would dump into the binary file.  
If I were to explain pickling to someone, I would say its to convert the data into a useable state for databases, disk drive, or other platforms properly to be used for a later date.  I almost thought that it was like zipping a file, but it is not!  They both change the data, but pickling is a converting data into a different form while zipping is making data smaller.
Structured error proofing is to take an error and make it in a more readable format for a typical user.  A typical user may not know to use an integer or a string or even not know what those data types are.  Error proofing predicts a possible error that may be taken and directs the user with a friendly message with easy to understand directions.
## Assignment 7: Pickling and Structured Error proofing
I started this assignment by first thinking about the inputs that I wanted to pickle.  Inputting an integer and string seemed like a good idea since they are different data types, and you can spot the error quickly.  I created a try/except within a while loop for both inputs.  The integer input is shown below (Figure 1).  What is also show in figure 1 is the try except error proofing.  This is to help the user make sure that an integer is selected.  The format I chose to use was the try-except method.  This was appropriate due to the simplicity of the code written.  If the user does not select an integer in the input, the script will ask the user to use a number instead and loop back to the beginning of the script. 

![figure1](https://user-images.githubusercontent.com/88756940/130708941-e8aa536f-d468-452a-9480-ff30276fb497.png)
#### Figure 1: while loop, try/except for integer, custom error message

Next, I do the same while true loop > try except but this time we want the user to type in a name using letters.  Then we store this information into a list and read the entry in list format using a print statement (Figure 2).

![figure2](https://user-images.githubusercontent.com/88756940/130708967-7da555e0-685e-4ed9-ac5a-b24134d52ef6.png)
#### Figure 2: while loop, try/except for string, custom error message, list

Lastly, I take the data in the list we just created and dump it into a file.  When I look inside the binary file, it looks like gibberish but that means it stored correctly into the file.  Then, we read the first entry in the binary file. (Figure 3)

![figure3](https://user-images.githubusercontent.com/88756940/130709002-25c45394-1cf2-46be-946f-8777ffdb5f06.png) 
#### Figure 3: dump data into binary file and then read the data using load

## Summary
In summary, Pickling a file converts the python object into readable data by a database system or a disk drive.  This way you can pull this information later.  Structured error proofing helps guide a user to use the correct entry if they are to use a script.  A good way to write a structured error proof is to think about common mistakes a user might make and give them a clear readable solution to their mistake.  There are lots of different custom exceptions you can create and stored procedures within Python as well.
