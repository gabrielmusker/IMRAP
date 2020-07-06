

Hi! Thanks for opening this readme file. Below are some helpful guides on how to use this program.




HOW TO RUN THE PROGRAM:

1) Presumably you've already unzipped this folder into a suitable directory, but if not, do it.

2) Install the latest version (or at least 3.4) of Python if you don't already have it.

3) Open the command line and navigate into the top level of the directory you unzipped.

4) Activate the virtual environment by typing (ignoring the quotation marks) either
	
	- "venv\Scripts\activate" (for windows cmd), or
	- "source venv/bin/activate" (for linux/mac).

5) Install Flask by typing "pip install flask".

6) Install the required packages by typing the following command:

	- "pip install python-dotenv flask-wtf flask-sqlalchemy flask-migrate requests datetime"
		
7) Run the program by typing "flask run".

8) Open a web browser and navigate to http://localhost:5000/

9) Explore the site at your leisure!






HOW TO USE THE SITE:

The site comes pre-populated with some sites randomly imported from IMDb, but if you want to start from 
scratch, you can always navigate to the "remove all films" page and delete them. If you'd like to add your
own films to the database, you can use the "add film" tab and fill in the required fields, or you can go 
to the "import films" section, where you can populate the database with data taken from the omdbapi. You
can also remove specific films from the database by typing their name into the "remove film" form.






POTENTIAL BUGS & FIXES:

Importing the films will take a few seconds, but if it causes an error it may be because the api key I used
was no longer valid. This can be fixed by going to http://www.omdbapi.com, where you can request a new key
which they will email to you. You can then copy this key into the file called "apikey.txt" at the top level 
of the program file, and this should fix the issue.


