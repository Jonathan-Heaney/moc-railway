# Map of Contemporaries

## Table of contents

- [Overview](#overview)
  - [Screenshot](#screenshot)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learned](#what-i-learned)
  - [Continued development](#continued-development)
  - [Useful resources](#useful-resources)

## Overview

### Screenshot

![](./screenshot.jpg)

### Links

- Live Site URL: [Add live site URL here](https://your-live-site-url.com)

## My process

### Built with

- Python/Django
- HTML/Django Templating Language
- CSS
- Minimal JavaScript

### What I learned

- Had some trouble connecting to the RDS database when I first made migrations. It was because the default db_name is 'postgres'
- Ran into a bunch of problems adding data to the new database. Ended up using pgAdmin to connect to Amazon RDS database, and then importing the data with a CSV file
  - Also explored a pg_dump/psql tool, which didn't work in this case because of pg_dump version compatibility issues
- Make sure to call load_dotenv() - I didn't at first, I just had load_dotenv, and my database connection didn't work
- It's possible to nest 'includes' template snippets
- Not all HTML files need to extend from a base, and they also don't need the HTML skeleton
- Had a lot of trouble refreshing the page and getting to an actual reset, without generating a new random person. What worked in the end was using @require.POST to set a generation flag, and removing the flag every time the page is rendered with data
- Use .get() to just get one specific value from the database. .filter() gets a QuerySet which can have multiple values
- It's possible to include JavaScript in your Django templates
- Sessions are a really helpful way of storing values across page reloads/state changes
- Setting 'window.location.href' in JavaScript is a way to set the URL of the current page. So going to that URL triggers a Django view function associated with that URL - that's how my search function works
- Always do hard refreshes to make sure old JS files aren't being cached
- Don't link to script files from a child template that gets used multiple times in other templates - all the variables will get duplicated, causing lots of console errors
- Whitenoise was really helpful for managing my static files, I'll use that with Django going forward

### Continued development

- Work to make data searching more efficient - the people and lists load very slowly right now
- Come up with a more elegant solution for creating the occupation colors - the JS function that waits for the DOM content to load is a little hacky
- Fix the CSS so that the overlap list cards don't spread out across the page
- "Load more" button
- More explanations for how the site works and what everything is doing
- Ability to filter by occupation, to show only people within the same profession or other specific professions

### Useful resources
