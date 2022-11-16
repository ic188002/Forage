<h1>Project 3 ReadMe </h1>



<h3>Description</h3>

<p>This was the first application I developed, tested and deployed coding in Python. The final outcome is an images sharing application, that  allows users to add, save and create a playlist of all images that are added to the site.
</p>
<hr>
<h3>
Deployment link</h3><h5>
Follow this link for the deployed version
<strong>https://bit.ly/3DLHTba</strong>
</h5>

<hr>

<h3>
Timeframe & Working Team (Solo/Pair/Group)</h3>

This Project was complete and deployed within our 5 day timeframe, it was a group project and I was working alongside Helene van Besouw and Henry Philpotts.


<hr>
<h3>
Technologies Used</h3>

<h5>
Insert your Technologies Used here:</h5>

<ul>
<li>Python</li>
<li>HTML</li>
<li>CSS</li>
<li>JavaScript</li>
<li>Django</li>
<li>pgAdmin 4</li>
<li>Git</li>
<li>GitHub</li>
<li>Heroku</li>
<li>ProCreate</li>
<li>Figma </li>
<li>Trello</li>
</ul>

<hr>
<h3>
Brief</h3>

Design, build and deploy an active and functional website which needs to fulfil these requirements 

Create the application using at least 2 related models, one of which should be a user
Include all major CRUD functions for at least one of your models
Add authentication AND authorization (page protection) to restrict access to appropriate users
User must be able to sign up or login
Signed in user must be able to change password and logout
change password and logout must only be available to logged in users
Give feedback to the user after each action, and after form submissions with success/failure.
Clear forms after submission failure.
Manage team contributions and collaboration using a standard Git flow on Github
Layout and style your front-end with clean & well-formatted CSS, with or without a framework. Put effort into your design!
Deploy your application online so it's publicly accessible.
Allow users to change website themes, Dark mode etc.
Allow users to upload image files.

<hr>


<h3>
Planning</h3>

In our first meeting we broke down the project requirements and what we and a group would like to accomplish within our time frame, it was here that I pitched the idea of building a image sharing application and after we all agreed we create our first ERD as seen below, this highlight the relationships that we need to build into the applications, were one user can create an account, add information such as phone number, email address, password, profile image and then add images that are added to the image database for all other users to access. By using an ERD we could refer to all aspects of the database and easily pull the information. 
We also mapped out our plans on Trello adding cards for each aspect of the project allowing us to track our progress. We communicated as a team on Zoom every hour to inform our group of our progress and ask any questions.

<img src="/p3photos/12.png" width="100%">
<img src="/p3photos/1.png" width="100%">

The next step I undertook was the create on the wireframes, the first was a rough drawing depicting how i imagined user to interact with the site, after which I went back to the team for final confirmation on the desired layout, from there I completed a more accurate wire frame showcasing features such as the light and dark mode that we wanted to incorporate into the application. 

<img src="/p3photos/2.png" width="100%">
<img src="/p3photos/3.png" width="100%">






The next step we undertook was to find out everyone's preferred skills so that we could develop a full application in the short timeframe. <hr>

<h3>
Build/Code Process</h3>



After deciding on our project path, our group came together to set up what files are needed in this application; consulting our ERD and knowing we were following the software design pattern MVT (Model View Template) we could set up the boiler plate of the site.


We decided to extend the built-in Django User model by adding a User Profile model linked one to one. We added the model in `models.py` then registered the model in `admin.py` so that we could use them with Django’s admin interface. 

<img src="/p3photos/4.png" width="100%">

After which we created a database on pgAdmin4 and successfully migrated checked using GUI (Graphical User Interface)





In `views.py` i started writing the request and responses, in the instance below I was able to  render the image index page. The image_Index function sets the variable “images” calling upon the Image models and render the `image/index.html`

<img src="/p3photos/5.png" width="100%">
Then In our `urls.py` I added the desired path the image_Index would follow.
<img src="/p3photos/6.png" width="100%">
By doing this I was able to easily add links to the index page by wrapping the path name ‘image_Index’ in backend code {% url ’image_Index’ %}. 


Below is our `images/index.html` we add the {% extends ‘base.html’  %}  and
{ % block content % } in order to keep the same layout of the navigation bar and keep the applications consistent. Inside the block content I added a title and started building how I was going to display all the images recorded in our database. This being my first function I had created in an HTML document with python it did take some trial and error; by creating a for loop around the image tag it renders all the images in the database on the page. Furthermore by adding the anchor tag in backend code if the user selects on an image they are taken to the image detail page due to the fact we added the image ID to the href. 

<img src="/p3photos/7.png" width="100%">



The function below while small toggles the CSS of the web site creating a Night Mode that was one of the desired deliverables. 
<img src="/p3photos/8.png" width="100%">
<hr>
<h3>
Challenges</h3>

<img src="/p3photos/9.png" width="100%">

This Profile detail function was a security concern with a potential lack of protection allowing other users to manually enter other user urls and edit their information, by passing the @login_required function that we imported from the Django framework. To solve this issue we run an if statement to compare whether the url user.id is not equal to the current user.id and if that statement if true it will redirect them back to the home page, when it is a match the function can carry one and run a POST to get the user profile page. The reason this was challenging as it did not expect to run into this issue, as this was our first application we built using Python and Django I believed that the built in Django auth verification function would be sufficient, but after a daily stand-up this weakness was pointed out. As a team we talked about how we might solve this issue and decided that a basic if-else statement to verify the current user was a simple and efficient solution to this issue.    
<hr><h3>
Wins</h3>

This for me was our greatest win combining back end Python with HTML to render a hero board that displays the current users photo board images providing a showreel of all the images saved.
<img src="/p3photos/10.png" width="100%">
For this we used a for-loop to go through and render all the boards associated with that user id, while providing an anchor tag that provides access to the full board. We also place a if statement that controls the amount of images, setting the count at 4 rendering 5 images of the hero board. The reason this was a big win for me and our team is because it highlights the key elements behind our site and incorporates all the functionality that we have learned, using a mix of backend code in a HTML page to render a professional looking page. 

<img src="/p3photos/11.png" width="100%">

<hr><h3>
Key Learnings</h3>

As this was my first application built using Python and Django I can say that my understanding of them both has increased a vast amount. I can see the great benefits that building an application with Django provides, with the built in functionality of this framework you can quickly build a functional site. Working as a team is becoming far easier with GitHub becoming a alot smoother with less merge conflicts, this is the result of clear planning on our shared Trello page as we can see which file each other is working on and know to stay clear of their programming path. 


<hr><h3>
Bugs</h3>
Currently, links to other users’ profiles are redirecting you back to your own profile. (No way of seeing other users’ boards) 
<li>The board index page renders when a board is deleted</li>
<li>Heroku file storage means that images will only display on the application for a limited amount of time. Within 24hrs the images will be cleared</li>
<li>Dark Mode clears when the page is refreshed</li>




<hr><h3>
Future Improvements
</h3>
<ul>
<li>Make the site responsive</li>
<li>Improve user flow through the site</li>
<li>Enhance the CSS for a cleaner finish</li>
<li>Filter available images to add to the board by themes associated with the ‘subject’ of the board</li>
</ul>




