# README
## Application Desc:
This application has been designed to provide users with a platform to sign up and post images that can be tagged with categories in a fun and safe space (uncomfortable content can be reported for removal).
These are posts and are displayed on the feed page with a filter option to show only images with a matching tag.
Users can vote on these posts and the top 5 will be displayed in order on the home page.
From the home page, users can also select their preferred background colour for the site with a colour selector on the left of the page.
Feed and Post can only be accessed by logged-in users and will otherwise be redirected to the login page. If users havn't registered they can sign up by clicking the sign up button on the login page.  

## Group Members:
| UWA ID    | Names              | Github Users |
| --------  | -------            | -------      |
| 23086965  | Rondelyn Hanson    | Rondelyn     |
| 23374376  | Lisa Cantu         | lcan2        |
| 23048519  | Georgia Mackiewicz | mackwiezy    |
| 22964393  |  Aya Bilal         | ayabilal     |


## Instructions for use:
Please install the following installs:
alembic==1.13.1
bcrypt==4.1.3
blinker==1.8.0
click==8.1.7
colorama==0.4.6
distlib==0.3.8
filelock==3.14.0
Flask==3.0.3
Flask-Bcrypt==1.0.1
Flask-Login==0.6.3
Flask-Migrate==4.0.7
Flask-SQLAlchemy==3.1.1
Flask-Uploads==0.2.1
Flask-WTF==1.2.1
greenlet==3.0.3
itsdangerous==2.2.0
Jinja2==3.1.3
Mako==1.3.3
MarkupSafe==2.1.5
platformdirs==4.2.1
SQLAlchemy==2.0.29
typing_extensions==4.11.0

Make a virtual enviroment and then install requirements.txt (using pip install -r requirements.txt) 
When running flask run if it doesnt run if you use the command python -m flask run
To run it successfully you need to type: flask --app YOUR_WORKING_DIRECTRY_TO_PROJECTIFY.PY run. To do this right click on the projectify.py file and click copy path, use this path in the command in the termainal.  

## Instructions for tests:
To run the tests run the command in the terminal: python -m unittest tests/unit.py. This will run the unit tests automatically using a data base created in the memory. 
