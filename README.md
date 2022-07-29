# Fever Tracker
#### Video Demo:  [Fever Tracker](https://youtu.be/f4VQJMfVPt0)
#### Description:

For this final project I have decided to create a program for keep track of a patient's fever. It is called Fever Tracker, and it has two versions, a CLI version and a GUI version.

This is a simple program that attempts to help the user minimize the sometimes overwhelming task of checking a family member's fever. 
It does that task by saving the data to a csv file and giving the user the option to create a pdf file with the formatted data.

In the CLI version of the program, we initially have to choose between 5 options: create a fever log, add temperature to an existing log, check an existing log, convert a csv file log to a pdf file, or exit the program.

When we want to open an existing record, the program asks us to choose between the files that are saved in the csv file folder. Then, in the CLI version of the program, the data is displayed in a formatted table style directly in the terminal shell. 

This program works with the csv, pdf and tabulate modules of Python. The csv files act as a database and keep track of all the records. The pdf files help the user to get a better way to store and share the results. The tabulate module helps us to display the data to the user in the formatted table style in an elegant way.

The GUI version of the program does exactly the same thing, but in a more user-friendly way. 

Among the libraries and frameworks available in the Python universe, I chose PyQt because it seems like a very popular tool for making GUIs in various industries. Maybe it's a good technology to learn.

PyQt has a fairly intuitive object-oriented API that, once you understand how it works, lets you get the job done without too much headache. The fact that you can style your app using CSS syntax is great. However, I didn't waste too much effort on the look and feel of the GUI. All in all, I have really enjoyed the experience of working with PyQt

It has been a good challenge in which I have learned a lot and that will allow me to continue learning.

There are some bugs creating the pdf file or validating input data, but since the goal is to continue learning, I can't spend much more time on it.

#### Fever Traker GUI repo:  [Fever Tracker GUI](https://github.com/joan-kii/fever-tracker-gui)