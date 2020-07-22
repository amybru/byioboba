# BYOBoba
Welcome to BYOBoba! Where you can find and create your favorite boba tea drinks! This application serves as an online recipe book to help you (the user) to try out and remember awesome drinks!

I have created this app for the Data Centric Development Milestone project of Code Institute's Full Stack Software Development course. The scope of this project was to create an application using Python and MongoDB, using CRUD (create, read, update, delete) operations to allow users to interract with the website.
Click here to see the deployed website:

## Table of contents
* [UX](#ux)
* [Features](#features)
* [Technologies](#technologies)
* [Testing](#testing)
* [Deployment](#deployment)
* [Acknowledgement](#acknowledgement)
* [Content Credits](#content-credits)

# UX
This website have been designed to give any visitors easy access to all of it's content without needing to signup. Each user is able to contribute with their favorite drink recipe that the other fellow users can view. 
### User Stories
> As a consumer, I want to browse a variety of interesting drink combinations to make purchasing a drink at a cafe easier.

> As a consumer, I want to experiment with combinations at home and share what I enjoy with others.

> As a barista in a cafe and owner of a small business, I want to see what new drinks and popular ingredients my customers enjoy. This way I can make recommendations to them.

##### Site Owner Goals
> Collect user information to see what is currently popular
>
> Generate interest in trying these new drinks
>
> Attract brands to feature on website, allowing for networking and affiliate programs


### Styling
The design of this website follows a very minimalistic approach, only displaying valuable content to the user.
BYOBoba uses very bright and clean colors. Inspiration was found from this photo on Unsplash of a teacup. Colors were pulled from this photo to give a colorpalate used throughout the site. As teas are usually greens, yellows, and creams, this photo seemed very appropriate. Inspiration was taken from a local tea shop called Utepia.
I chose to use the font Ubuntu from Google Fonts as it is a very clean and easy to read font. The Siracha font was also used to add some interest to the headers and forms.
![Color Scheme](/wireframes/colors.jpg "colors")

### Wireframes
I drew my wireframes for this website using Procreate on the iPad. I have made two wireframes for each page to show considration to a mobile-first responsive app. The links to the files are below:
* [Home Page](/wireframes/wf_home.jpg "Home Page")
* [Home Page- Mobile View](/wireframes/wf_mobile_home.jpg "Home Page Mobile")
* [Drinks Page](/wireframes/wf_drinks.jpg "View all Drinks Page")
* [Drinks Page- Mobile View](/wireframes/wf_mobile_drink.jpg "View all Drinks Page- Mobile")
* [Add/Edit Drink Page](/wireframes/wf_add.jpg "Add Drinks Page")
* [Add/Edit Drink Page- Mobile View](/wireframes/wf_mobile_add.jpg "Add Drinks Page- Mobile")
* [View One Drink Page](/wireframes/wf_view.jpg "View Drink")
* [View One Drink Page- Mobile View](/wireframes/wf_mobile_view.jpg "View drink-mobile")

 
There are some differences between my wireframes and my final website. This was due to visual preferences and other users who tested my website. 

### Data Architecture
Before building my project, I discussed what kind of data structure would be good for this project with the tutors. They all gave some valuable advice. Below are what the collections look like from the database.

* In the [Boba Collection](/wireframes/database/boba-collection.png) , data is collected from the add drink form and stored in the boba collection. 
The following collections contain predetermined data to populate the fields in the forms and provide options for the user to choose from.

* [Drinks Collection](/wireframes/database/drink-collection.png)

* [Teas Collection](/wireframes/database/teas-collection.png)

* [Decaf Collection](/wireframes/database/decaf-collection.png)

* [Toppings Collection](/wireframes/database/toppings-collection.png)

* [Ice Collection](/wireframes/database/ice-collection.png)

* [Sweet Collection](/wireframes/database/sweet-collection.png)

# Features
All of the CRUD (Create, Read, Update and Delete) operations have been fully deployed in the app.

### Existing Features
* Navigation bar
All pages feature a navigation bar at the top of the page to make each CRUD function accessible.
The business name, BYOBoba is located in the middle of the bar and acts as a button to return to the home page.
On small and medium screens, the navbar reduces to show just the business name and a collapsable button.
On large screens, the user will see a link on the left side named "Browse Drinks". Clicking on this link will take the user to the page to view all drinks currently in the database.
On the right side, there is a button with a plus sign, referring to the "Add" function of this website. This will take the user directly to the add drink form.

* View all drinks
This page features all of the user entered data in the database. A rounded shape will give us one entry that we can click on to view more information on this specific drink. 
Clicking on it will give us the option to edit the drink or to view all ingredients in this drink.

* Add Drink & Edit Drink Forms
Two major features of the site are the add and edit functions that allow the user to interract with the site. The user must fill in each of the fields in the form to properly create or edit the drink.
The forms are formatted in exactly the same way, the only difference being the edit drink function is populated with data already inputted to the database. 
The form includes a textarea, two selects, one switch, and three radios.

* Delete drink modal
Located in the edit drink page, the delete modal can be found by clicking a button that reads "Delete Bubble Tea". 
The modal appears with a prompt that asks if the user is sure they want to delete. Clicking a confirm will call the delete function, deleting the drink from the database.

### Features Left to Implement
* In the add drink and edit drink forms, I would like for the user to be able to add their own drink to the database. 

* I would love to implement a rating stystem so that users can let others know how good or bad they are. This will also help small buisnesses to see what kinds of combinations their customers enjoy, so as to make better recomendations and drink offerings in their stores.

* I would also like to add authentication as it would ensure data that is added is authentic and less inclined to be spam. Also, users would not be allowed to delete drinks from the database. This is something only the administrator would be able to do. It would allow any user to view, but a user must be logged in to create or update.

* I would like to add a place for the user to send us suggestions of new ingredients to add to our database to allow for more combonations to be created.

* It would also be interesting to develop a favorites page so the user can save their favorite drinks in a list separate from the rest of the drinks.

* For business practices, I would like to add in an ordering feature to be used at a cafe. This would help the administrator to make a profit using affiliate links. An alternative idea would to be to have a place where the user can click on links to purchase ingredients to make the drink at their home.

# Technologies
A [Flask](https://en.wikipedia.org/wiki/Flask_(web_framework)) Application, written in [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

[HTML](https://en.wikipedia.org/wiki/HTML)
HTML5 was employed for markup text.


[CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
CSS3 was used to style each of the pages on the website.

[Javascript](https://en.wikipedia.org/wiki/JavaScript)
Javascript was added to improve the functionality of the website. Most Javascript on this site is required by Materialize. 


[Jinja](https://jinja.palletsprojects.com/en/2.10.x/)
A templating language used with python to retrieve data from the database to display on the website.


[Materialize](https://materializecss.com/)
Materialize 1.0.0 was used for its design framework. The grid system is used throughout the website.


[MongoDB](https://en.wikipedia.org/wiki/MongoDB)
The database used to organize data from the users.


[Pymongo](https://pymongo.readthedocs.io/en/stable/)
The project uses PyMongo as the Python API for MongoDB. This API enables linking the data from the back-end database to the front-end app.

Git & [GitHub](https://en.wikipedia.org/wiki/GitHub)
Git and Git Hub were used for version control. 


[Heroku](https://devcenter.heroku.com/)
Used to deploy the final website

Final website link:  



# Testing
### Code Validators
The follow validators were used to check the code developed from this project:

HTML [Validator](https://validator.w3.org/#validate_by_input)

HTML Validator was used to validate the HTML code. However, the validator is not able to recognise the Jinja templating syntax so some errors were recorded. All code other than the jinja syntax was successfully validated.

CSS [Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)

CSS Validator was used to validate CSS code. The CSS successfully passed this check with no errors.

### Browser testing 
This website was tested on multiple devices with varying screen sizes and in multiple browsers. All devices and web browsers passed testing.

Web Browsers

- Google Chrome
- Safari
- Firefox

Devices
- Macbook
- iPad Pro
- iPad Air
- iPhone x
- iPhone 11


The primary method of testing the application was to ask several users to visit the website using these different devices and web browsers. Each user was asked to create a drink, view it, edit it, and delete it. The feedback recieved allowed me to make any necessary changes to the code or design.

### User Stories Testing
I have tested my user stories and documented each of the steps that each user would need to accomplish what they have stated.


> A consumer wants to browse a variety of interesting drink combinations to make purchasing a drink at a cafe easier.

1. User loads app and is directed to the home page (index.html). The user is able to see a brief introduction to what boba tea is. They are also able to see a large button to browse drinks available in the database. At the bottom of the page, the user can also see a button to add a new drink. These buttons are also available in the navbar at the top of the page.

2. A user clicks on the browse drinks button in either the navbar or on the home page, taking them to a page to view all availible drinks (drinks.html).

3. The user is able to scroll down the page to see previews of each drink with the top three inputs. Clicking on any of these entries will lead the user to a page (drinkCard.html) where they can see more information about the drink. 


> A consumer wants to experiment with combinations at home and share what they enjoy with others.

1. User loads app and is directed to the home page (index.html). The user is able to see a brief introduction to what boba tea is. They are also able to see a large button to browse drinks available in the database. At the bottom of the page, the user can also see a button to add a new drink. These buttons are also available in the navbar at the top of the page.

2. The user clicks on the plus button in the navbar, or the add drinks button located on the bottom of the page to navigate to the add drinks form (addDrink.html).

3. The user fills out each of the fields in the form, customizing it to their unique drink.

4. The user clicks submit at the bottom of the page to save the data to the database.

5. The user is then redirected to the main View All drinks page (drinks.html).


> A barista in a cafe/owner of a small business wants to see what new drinks and popular ingredients their customers enjoy. 



### Manual Testing


### Bugs

Bug: Data was coming through eight times on the drinkCard.html page

* Fix: I had a for loop in my code, looping through the boba collection. This collection has eight items, so every entry was repeating eight times. This for loop was removed.

* Verdict: Data is displayed only once on the drink card page, as expected.


Bug: Navbar hamburger not opening on small screens

* Fix: It was found, with help from the Code Institute Tutors and the slack community that keeping the Javascript required for this project in a separate file, causes this element not to work as expected. Therefore, the Javascript was moved into a script tag in the base.html file.

* Verdict: On medium and small screens, the hamburger icon is able to open and function as expected.


Bug : Select not appearing on add drink or edit drink form

* Fix: Initially a css class was applied with the class !important. Later it was found that the Materialize Javascript required, did not work in a separate javascript file. Javascript was added by means of a script tag in the base.html file. 

* Verdict: The select now works as Materialize expects it to.


Bug: Delete modal not opening when the delete button is clicked

* Fix: It was found in connection with the previous two bugs, that the javascript was moved into the base.html file. However, the modal was still not opening. After comparing my code with the Materialize docs, it was found that the button to open the modal contained an outdated class. This was changed.

* Verdict: Delete modal is now able to open when the button on the editDrink.html page is clicked. 


Bug: Issues with connecting to MongoDB database

* Fix: It was realized that the login for the mongodb website was used in the connection string, instead of the password for my database. These passwords were reset and environment variable was set up.

* Verdict: Data is able to be posted to and retrieved from the database.


# Deployment 
This app is currently deployed on Heroku. The code deployed is stored on the master branch of this project here on GitHub. Heroku requires the followung steps to deploy this project.

1. Register/sign in for Heroku.

2. Once signed in, click the "new" button on the dashbord to create a new application.

3. Name the App and choose the region you are currently in.

4. Create a requirements.txt file to allow Heroku to install the dependencies required by the application.
    ```
    pip3 freeze --local > requirements.txt
    ```

5. Create a procfile to tell Heroku what type of application will be deployed.
    ```
    echo web: python run.py > Procfile
    ```

6. On the deployment page of the Heroku project, choose Heroku GIT for deploying.

7. In the CLI of your environment, input the following code:
    ```
    $ heroku login
    $ heroku git:remote -a <byoboba>
    $ git push heroku master
    ```

8. In Heroku settings, chose "Real Config Vars" to set the proper environmental variables
```
* IP:    0.0.0.0
* Port:    5000
* MONGO_URI mongodb+srv://<username>:<password>@<cluster_name>.mongodb.net/<database>?retryWrites=true&w=majority
* SECRET_KEY:   <your_value>
```

9. Click the "Open App" button to view the final deployed app.

# Acknowledgement
I would like to thank and credit the following sources for their assistance and contribution to this project.

- My mentor with Code Institue, Gerard McBride, for helping me to brainstorm and coaching me through this project 

- The tutoring Team at Code Institute for helping me fix several bugs and understand why these errors were happening

- A big thanks to my sister and the rest of my family for helping me test the site extensively, to make sure each feature worked as expected on various devices.


# Content Credits
Content found in each drink entry was created by myself as beverages I enjoy. 

The images (bkgrnd.jpg, boba.jpg, and tapioca.jpg) were found on unsplash.com

Cartoon-like images (logo.jpg & anatomy.jpg) were drawn by myself using the Procreate app on ipad.

All fonts are from [Google Fonts](https://fonts.google.com).

