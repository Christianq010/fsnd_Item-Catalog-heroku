# Item Catalog
==============================================

URL - https://fsnd-item-catalog-app.herokuapp.com/catalog/

## Description

> This repository contains instructions to setting up a Web application that queries a database and then dynamically generates complete web pages and API endpoints on the Heroku Service.
> Explore the original repo this project was cloned from [here](https://github.com/Christianq010/fsnd_Item-Catalog).

### About Our Project

#### *Item Catalog*
* We use an Object-Relational Mapping (ORM) layer - SQLAlchemy to interact with our database.
* `GET` and `POST` requests that translate to CRUD operations.
* Using the Flask framework for development of our application.

We need to be able to successfully run the virtual machine in order to view our projects.

The VM is a Linux server system that runs on top of your own computer.
* We can share files easily between our computer and the VM.
* We'll be running a web service inside the VM which we'll be able to access from our regular browser locally.

We're using tools called Vagrant and VirtualBox to install and manage the VM. You'll need to install these to run the applications.

## Prerequisites -
* Create an account on Heroku.
* Create a new app. In my case the app called `fsnd-item-catalog-app`.

## Instructions
* On your local machine
  * Run your vagrant machine (`vagrant up`, `vagrant ssh`, `cd /vagrant/yourproject-folder`)
  * Run these following commands within vagrant:
  ``` 
  sudo apt-get install git
  sudo apt-get install ruby-full
  wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh | sh
  sudo gem install foreman
  ```
  * Create a file called `Procfile` with `vi Procfile` and open it in the editor and add following line and save it
  ```
  web: gunicorn project:app
  ```
  * To save and exit, hit `ESC`, then `:x`.
  * Continue by running these commands within vagrant 
  ```
  sudo apt-get install libpq-dev python-dev
  sudo pip install gunicorn
  pip freeze >requirements.txt
  sudo pip install -r requirements.txt --allow-all-external
  ```

* On Heroku
  * Go back to your Heroku account, create a free Dev version PostgreSQL database
  * Copy the URL of the database
  * Paste the Heroku database URL in these python files in your projects. (These edit can be done using any   text editor)
  * This new URL will replace the existing `sqlite:///catalogitems.db` in `database_setup.py`, `data.py` and `project.py`

* On local machine
  * Go to `project.py` and comment out the following lines and remove indents of the middle two lines.
  ```python
  if name == 'main':" and "app.run(host = '0.0.0.0', port = 5000)
  ```
  * Add following line in `database_setup.py` under class `Restaurant`. (Ref: Step 5 in https://www.udacity.com/wiki/ud330/deploy6)
  ```python
  menuItems = relationship("MenuItem", cascade = "all, delete-orphan")
  ```
  * On our vagrant machine, run the following files - `python database_setup.py`, `python data.py`.
  _If both of these files run without error, the app is ready to be run locally_,

* Run our app on http://localhost:5000 with vagrant using `foreman start web` .
  _If it runs successfully, now its ready for deployment in Heroku._

## Deployment on Heroku
* On local machine, in the VM
* Log in to Heroku with `heroku login`, enter your email and password.
* Use the Heroku dashboard to connect heroku app to the github repo and automate deployments with the master branch
 * git init
 * `heroku git:remote -a your-heroku-app-name`
 * It should display the following `set git remote heroku to https://git.heroku.com/fsnd-item-catalog-app.git`.
 * Check git remote status with `git remote -v`
 * Make a commit and push (notice there is a dot after git add)
  ```git
  git add . 
  git commit -am "First Commit"
  git push heroku master 
  ```

### Troubleshooting
* Add () to print statements in `project.py`, error noted in heroku dyno error logs during deployment.

### Create Google Client ID & Secret
* Create and then Go to your app's page in the Google APIs Console — https://console.developers.google.com/apis
* You can then set the authorized JavaScript origins to `http://localhost:5000`.

### Create Facebook Client and Secret
* Go to your app's page in the Facebook Developers Console — https://developers.facebook.com/apps/
* Configure Client OAuth Settings and Valid OAuth redirect URIs (http://localhost:5000, https://fsnd-item-catalog-app.herokuapp.com/catalog/) etc and save changes.

### API Endpoints
* Show all Catalog names in JSON - `/catalog/JSON`.
* Show Items in Specific Catalog Page in JSON - `/catalog/<int:category_id>/items/JSON`
* Show individual Items in the URL in JSON - `/catalog/<int:category_id>/items/<int:menu_id>/JSON`


### Resources
* Udacity Forum post of Heroku Deployment - https://discussions.udacity.com/t/steps-to-deploy-your-app-in-heroku-for-free/46351
* Refactor Code to Python PEP 8 style guide
  * http://pep8online.com/checkresult
  * https://stackoverflow.com/questions/10739843/how-should-i-format-a-long-url-in-a-python-comment-and-still-be-pep8-compliant
  * https://stackoverflow.com/questions/1874592/how-to-write-very-long-string-that-conforms-with-pep8-and-prevent-e501
  * https://stackoverflow.com/questions/40003378/pep8-error-in-import-line-e501-line-too-long
