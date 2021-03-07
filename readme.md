# MySQL_db_project
I finished this personal project while I was on a data engineering bootcamp, I made a CLI application built in Python for an online retailer.Built a MySQL database for the retailer to store its data and allowed the users to perform CRUD operations on their data. 
</br>
</br>
## To use this program
you need [Python](https://www.python.org/downloads/) 3.8 + and [Docker](https://docs.docker.com/get-docker/) installed
 
 
After you got that follow instructions below
</br>
</br>
 
This program uses a MySQL database for data persistence and searching engine. You need a docker container running MySQL image.
</br>
</br>
### To connect to MySQL this program uses a environment file which contain sensitive info
</br>
 
#### Add .env file to run with the following details
- ##### MYSQL_HOST (address to MySQL server)
- ##### MYSQL_PORT (port to MySQL Server; 3306 default)
- ##### MYSQL_PASSWORD
- ##### MYSQL_USER
- ##### DB (Database name you would like to use for app
 
 
On root of the project folder run it is required to install requirements.txt, best to do it in a virtual environment and then compose a docker container with my MySQL
* python -m venv .venv
* python -m pip install -r .\requirements.txt
* docker-compose up -d
* If you have done all of the above you should only need to run the app file from the src folder to use this program.
</br>
</br>

### Future plans

I will come back to this to add more stuff as soon as i get some free time from my current projects.
 
Things I want to add are an option to search an order with a name so all orders with that name come up and the user can select one.

As well as a new table to sql db for inventory to check stock level and compare whats going out and what's coming in per week.
