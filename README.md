# Memory-Box
Capstone Project: photo-feed app to store user memories and simulate the tactile experience of a physical memory box






# Capstone Proposal

## Project Name: Memory Box
### Overview
Memory Box is a personal photo-feed app that helps users handle and let go of physical objects, souveniers, or trinkets, but always keep the memories. 

### User Story
I have always been a nostalgic person, collecting small reminders (or "treasures") of important memories or times in my life. Ticket stubs, matchbooks, small rocks and seaglass, postcards, notes from loved ones. 

![alt text](https://hips.hearstapps.com/hbu.h-cdn.co/assets/cm/15/04/54bf4339ea191_-_1-sendus-0509-xlg.jpg?fill=320:250&resize=480:*)

In short, I have a hard time letting go of physical things. I first started photographing sentimental items before "letting them go" as a teen moving out for the first time. Since then, it's a practice I've kept to for large but sentimental objects in order to try and preserve the memories and feelings attached to an object without keeping it as clutter or junk. However, I've never had a way to organize those photos in a meaningful way and don't feel the experience is the same: so "treasure boxes" full of things still pile up in my life in sock drawers and under my bed. 

As a nostalgic collector but also someone hoping to organize and minimize the "stuff" in my life, I want a way to organize these tactile touchpoints of important times in my life in a way that feels personal, natural, and human. 

I want Memory Box to be a place where instead of stashing physical mementos away and then dealing with the eventual frustration of organizing or throwing them out, they can be easily photographed, commented on, and revisted.

### Basic Features
- [ ] users can create accounts and log in to a personalized page. 
- [ ] the user can upload and store images on their page with a brief description of the memory and a year or specific date associated with it. 
Other info to add could be: 
* people associated with the memory
* feelings associated with the memory
* zip code, state, or address the object/memory is from 

### Better Features
- [ ] user can organize different "boxes" for the memories and open each one 
* boxes display on their index page and users can select each box to see inside. 

### "Stretch" Features (_fun but not fundamental_)
- [ ] "random" memory search to allow user to 'pull' a random memory from any "box" or all "boxes"
- [ ] Display headlines or events, maybe weather or temperature(if the memory has a place), from the year associated with each Memory or "box" 
Possible APIS(need further research into their documentation): 
* [New York Times Archive API](https://developer.nytimes.com/docs/archive-product/1/overview)
* [Open Weather Map's historical weather API](https://openweathermap.org/history)

### Color Scheme:

![alt text](https://www.schemecolor.com/wp-content/themes/colorsite/include/cc6.php?color0=272324&color1=83b799&color2=e2cd6d&color3=c2b28f&color4=e4d8b4&color5=e86f68&pn=Retro)

### Schedule: 
* Pre-project: basic HTML Framework for site to understand layout and templates. 
* First week: create Django project, begin set-up for user logins.
* Second week: set up database for storing user photos and displaying them on the page
    _MVP: Users can log in and upload photos that will display on a main page_
* Third week: added functionality-- add features to allow users to search memories, implement "Better Features" listed above
    _MVP: Site provides visual organization of photos for the user based on: "boxes" or date._
* Fourth week: nit-pick visuals, fix bugs, if on-track, add "Stretch" Features. 
    _MVP: Site provides more context for memories, using an API database to give historical context to memories based on provided date._ 