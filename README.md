# Marco Cook

Deployed app: https://marcocookwebsite.herokuapp.com/

## UX

This app has two primary parties involved – users who want to add recipes to the site for storage purposes/future reference/to share with others, and users who want to search for recipes. The user stories for these parties are as follows:

#### Users adding recipes: 
* We want to easily add recipes to the site's database.
* We want to access these recipes in future easily.
#### Users searching for recipes:
* We want to be able to easily access recipes based on the recipe title.
* We want the recipe to be clear and concisely presented, in an easily understandable format.


## Code Validation Testing

To initially test the website I used the following validators:

[W3C Markup Validation](https://validator.w3.org/) Service for HTML I inserted the code into the validator via direct input. I consistently checked used this throughut previous checks, where any errors/warnings were addressed directly and documented in commits. Upon a final check no erros/warnings were present.

[W3C CSS Validation](https://jigsaw.w3.org/css-validator/) Service for CSS I inserted the code into the validator via direct input. No errors were were found upon final check.

[JSHint](https://jshint.com/) for Javascript I inserted the code into the validator via direct input. 

## User Stories 

1- Users adding recipes:

Easily add recipes to the app's database:
* Go to the add recipe page (either through the navbar link or by the add recipe card on home page).

* Insert random values into the form elements and click the "Add Recipe" button at the bottom of the page.

* Users will see that they have added a recipe with a thank you message and link back to the site's home page.

* Search for the recipe using one of the categories to see if it was added.

* Can visually confirm that this works. As the site developer, I can see that this has been added to the database on MongoDB Atlas.

2- Users searching for recipes:

* Easily access recipes based on recipe title

* Users will be presented with a card for each recipe matching their search criteria. Initially, these just have the title and an image (if provided - if not, they are given a default image stating no image exists for the recipe). On clicking the card, they will then receive a more detailed description of the recipe. This graduated release of information allows users to more easily filter through recipes, only getting more information on recipes which appeal to them.

### Wireframes

These wireframes were created using [Balsamiq](https://balsamiq.com/) during the Scope Plane part of the design and planning process for this project.

[View the wireframes here](https://github.com/marcomoreschi/milestone-3/tree/master/wireframes)

## Features

#### Existing Features

* Parallax: Parallax is an effect where the background content or image in this case, is moved at a different speed than the foreground content while scrolling. Here, it is used for the hero image on the home page.
* Cards: A convenient means of displaying content composed of different types of objects. Here, these are used to section off content in a visually pleasing manner.
* Dropdown: Used for the "Add a recipe" in the section "Choose Cuisine/type" and part of the navbar, to allow users to select which category they would like to use to search in mobile version.
* Buttons: Used for specific actions for user interaction.
* Forms: Used as front-end methods to add and edit recipes on the site.
* Card Reveal: Used to reveal the recipe description of search results, and also the link to the recipe itself once users have decided that is the recipe they wish to view.

#### Features Left to Implement

* Delete Modal: When users hit the delete button on the recipe page, a modal pops up asking if users are sure they wish to delete the recipe. This allows for a "second chance" in case of accidental clicks of the delete button.
* For adding a recipe, I have provided users 9 ingredient slots (which I felt was a sufficient number for the purposes of the project). In future, I would like to incorporate a means of allowing users to add additional ingredient slots to the form so as not to restrict them in this way.

## Technologies Used

#### HTML

The project uses [HTML](https://en.wikipedia.org/wiki/HTML) to structure the site.

#### CSS

The project uses [CSS](https://it.wikipedia.org/wiki/CSS) to style the site.

#### Javascript

The project uses [Javascript](https://en.wikipedia.org/wiki/JavaScript), in particular JQuery, for interactive elements on various pages.

#### Materialize

The project uses [Materialize](https://materializecss.com/) to aid in both the styling (Materialize CSS, Components and Javascript) and structure (Grid System) of the site, as well as aiding to create a responsive design (also through the Grid System).

#### FontAwesome

The project uses [FontAwesome icons](https://fontawesome.com/v4.7.0/) on various pages of the app.

#### Python

The project uses [Python](https://www.python.org/) for logic elements of the project.

#### Flask

The project uses the [Flask Framework](https://en.wikipedia.org/wiki/Flask_(web_framework)).

#### MongoDB

The project uses [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) as a non-relational database for the project's data.


## Manual Testing

### Tests taken on Desktop

All steps on desktop were repeated in browsers: Firefox, Chrome and Safari and Microsoft Edge.

1. Hero Header/Landing section on website
* Opened up the page in the browser
* Refreshed the page immediately
* Closed the page and then opened the website again in a new tab and in a new browser window
* Scrolled back up to test if I could still go back up and scrolled down
* Clicked the back button, where it returned me to the landing section view again

2. Information Section
* Hovered back and forth over the information boxes slowly, then quickly to test animate
* Clicked on the buttons to see what would happen
* Scrolled up and down to see how this was working and also to see how quickly I could find the next call to action button and/or scroll down to this next section
* Clicked on the next call to action button, testing again the scroll behaviour and where the button will redirect me


## Deployment

I created a repository on GitHub, linking my project on Cloud9 to it. I committed and pushed content to this repository at various stages of the project (e.g. when I had a section fully structured and styled, or when I had coded a certain function to function in the desired manner).

I then created the app on Heroku, created a requirements.txt file (with the project's required applications) and a Procfile (specifying the app is a Python web app).

I then pushed to Heroku. Having done this, I then specified the IP and PORT.

I pushed to heroku whenever I pushed to Github. This was incredibly useful in testing the site, as outlined above, especially in testing it on various screen sizes.

## Credits

#### Content

* All text in this project was written by the developer.

### Media

#### Images

* The images used for the recipes were obtained from Google Images and are used for educational purposes only. 

#### Recipe

* All recipes were taken from Gino D'Acampo and i have added some changed.

## Acknowledgements

I have taken inspiration from different website that I have found online. My mentor, online student support and Slack were both great help throughout my project.

##### Disclaimer

* The content of this website, including the images used, are for educational purposes only.


