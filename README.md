# simple_pipeline

This is my pokemon pipeline for the ETL process.
i kinda liked going back to my old days of statistics for gaming.
yeah. its kinda nice going for DataScience.
its a good try for me to do little things for the moment.
if you see things clearly i like to used print and also pandas as a view.

## API
> The Api that i used is Pokeapi. <br>
https://pokeapi.co/ <br> <br>
The endpoint is: <br>
> https://pokeapi.co/api/v2/pokemon <br>


## Pip Packages. 
1.requests <br>
2.pandas <br>
3.mysql-connector-python <br>

just type this in a command line.

> pip install requests pandas mysql-connector-python

##Note: replace the password with your own personal password. its just an example. 

## extract.py
This thing extracts some data from the API. i know the response is few but its for example purposes.

## createdb.py
This thing creates the database from python file to the mysql server.

## loaddata.py
This thing kinda load the data gathered from the site to your own personal sql server that you made from creatdb.py
