This is my understanding of the AirBnB Console Project. It is the first of my attempts towards the building of a mini but full version of the AirBnB website. A house sharing and rental web application.

The Console, is the back-enders paradise. This is the place where we build the logic that allows our web page to function. Specifically, this is the command line interpreter that allows for us to create, display, update and delete the users of pur website. If properly constructed the console is ideal for development, testing and debugging.

Firstly, using the cmd module I will build a command line interface that works like a shell or the interatcfive REPL of python. It will take commands to create, destroy, update and display users data. It is initialised by running the file and will take commands to terminate at developers command.

i.e 
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit

it will also work in non-interative mode:
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

In order for the console to work I will build a Base Class, to which all classes will inherit and subsequent classes relevant to a website such as these, for instances classes such as user, place, city, state and ammenities. The clone will interact with these classes in order to dynamically create user data.

There will also be a file storage mechanism that ensures all the data that is created is persistent(stored and available for future manipulation post the end of the termination of the program)

Finally, there must be test mechanism to ensure the methods and code base are interacting as expected. This too will be implemented.

For further details hit up my github, thanks for watching!
