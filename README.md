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

Easily access recipes based on recipe title

* Users will be presented with a card for each recipe matching their search criteria. Initially, these just have the title and an image (if provided - if not, they are given a default image stating no image exists for the recipe). On clicking the card, they will then receive a more detailed description of the recipe. This graduated release of information allows users to more easily filter through recipes, only getting more information on recipes which appeal to them.

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
* Hovered over the tooltip on the underlined piece of text
* Clicked on tooltip to see what would happen
* Scrolled up and down to see how this was working and also to see how quickly I could find the next call to action button and/or scroll down to this next section
* Clicked on the next call to action button, testing again the scroll behaviour and where the button will redirect me
* Scrolled back up to test that this was working