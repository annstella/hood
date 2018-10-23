# NEIGHBOURHOODWATCH.

 a web application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts.

## Getting Started.

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

* $ git clone https://github.com/annstella/hood/
* $ cd awards
* $ source virtual/bin/activate

Install all the necessary requirements by running pip install -r requirements.txt (Python 3.6).
* $ configure your prefered database provider in the settings.
* $ ./manager.py check
* $ ./manager.py makemigrations Task
* $ ./manager.py migrate
* $./manager.py runserver

### As a user of the application I should be able to:

* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.




#### Things you need to install to the software.
* Django==1.11
* django-bootstrap3==11.0.0
* Pillow==5.2.0
* psycopg2==2.7.5
* pytz==2018.5

##### Deployment

Link to a live site:https://majirani10.herokuapp.com/



#### Known bugs
* Searching for the neighbourhood and business

#### Authors

Annstella Kagai

#### License

MIT LICENSE (c) 2018,Annstella kagai

#### Acknowledgments
Inspiration