# **Wanderlust**
Waderlust is your online travel diary app, where you can post anekdotes about your travel adventures! Both for yourself to remember, to share with family and friends as well as to inspire other fellow wanderlusters around the globe. The travel diary aims to be a platform for inspiration, discussions and sharing about all thiings travel related. The user can search for other  users posts to get information and inspiration for coming trips, as well as to share and communicate with there friends and family about the trip they are undertaken orprieviously been came home from. The travel diary site targets various kinds of people whom are interested in knowing more about a specific travel location, travel in general or to just socialize with likeminded Wanderlusters!

**Wanderlust** 

Let me introduce you further to [**Wanderlust**]()!
<br>
<br>

![Home]
<br>


## **Content**
1. [**Strategy**](#strategy)
    - [UX](#ux)

2. [**Scope**](#scope)
    - [User Stories](#user-stories)
    - [Entity Relationship Diagram](#entity-relationship-diagram)
    - [Wireframes](#wireframes)    

3. [**Structure**](#structure)
    - [Home page](#home-page)
    - [Navigation](#navigation)
    - [Add post](#add-post)
    - [Edit & delete post](#edit-&-delete-post)
    - [Like post](#like-post)
    - [Comments](#comments)
    - [Profile page](#profile-page)
    - [Follow profile](#follow-profile)
    - [Search function](#search-function)
    - [Future feature](#future-feature)
   
4. [**Skeleton**](#skeleton)
    - [Technologies](#technologies)

5. [**Surface**](#surface)
    - [Design](#design) 

6. [**Testing**](#testing)
    
7. [**Deployment**](#deployment)
    - [Deployment](#deployment)
    - [Clone](#clone)
    - [Forking](#forking)

8. [**Credits**](#credits)
    - [Content](#content)
    - [Acknowledgement](#acknowledgement)

[Back to top](#wanderlust)

<br>

## Strategy

---


### **UX** 

<br>

With the UX principles in mind I started with the Strategy phace, thinking about the target audience and what features would benefit them. 

The target audience are:
- people in various age groups, mostly adults, that like to travel
- people that like to search for inspiration for their next travel
- people that like to share about their travels
- people that like to follow others travel adventures
- people searching for a specific destination or topic

What the user will be looking for:

- Images and posts about someones travel in diary form
- Inspiration for their next travel
- Information about someones trip
- Information about a location they like to travel to
- Information about the others users of the site
- Interaction with other people interested in traveling


[Back to top](#wanderlust)

<br>

## Scope 

---


### **User Stories**

<br>

**Epic: Account Management**
- As a Site User I can sign up for an account so that I can use all the features reserved for members
- As a Site User I can log in to the site so that I can use all the features of the site
- As a Site User I can easily log out from the site so that my account and its content remains secure
- As a Site User I can create a personal profile so that I can control my content
- As a Site User I can edit my personal profile so that I can keep it up to date and safe

**Epic: Forum View**
- As a Site User I can read posts and comments in detail so that I can get information and inspiration
- As a Site User I can see the latest post at the home page so that I get the newest input directly
- As a Site User I can use a search function so that I can find the right post or user that interests me
- As a Site User I can easily and intuitively navigate the site so that I can find what I am looking for
- As a Site User I can see the date a post was created and updated so that I know how accurate it is

**Epic: Forum Interactions**
- As a logged in Site User I can create new post so that I can update my travel diary
- As a logged in Site User I can comment on posts so that I can interact with the other users
- As a logged in Site User I can edit or delete my posts and comment so that I display controll my input on the site
- As a logged in Site User I can like posts so that others can see if a post is popular and so I can find it easily again
- As a logged in Site User I can follow profiles so that I can find it easily again

<br>

To follow an agile approch, a project board (kanban-board) was set up using GitHub Projects: [Kanban](https://github.com/Monika-81/wanderlust-p5/projects/1)

<br>

### Entity Relationship Diagram

<br>

The planing of the database models, aka the Entity Relationship Diagram, is illustrated below:

<br>

![ERD]()

<br>
<br>

### Wireframes

The wireframes for the project is very basic to get the feeling where I wanted the project to go, but over all the choices of the design grew with the development.

<br>

![Mobile]()
![Desktop]()

<br>

<br>

[Back to top](#wanderlust)

<br>

### **Features**

<br>

#### **Home page**
<details>


<br>
<br>

![Home page desktop]()
![Home page mobile]()

<br>
</details>

#### **Navigation**
<details>


<br>
<br>

![Navbar desktop]()
![Navbar desktop dropdown]()

<br>
<br> 

![Navbar mobile expanded dropdown]()
![Navbar mobile expanded]()
![Navbar mobile collapsed]()

<br>
</details>

#### **Add Post**
<details>


<br>
<br>

![Add post button]()
![Add post dropdown]()

<br>
<br> 

![Add form]()
![Add choices]()
![Add error]()
![Add success]()

<br>
</details>


#### **Edit & Delete Post**
<details>


<br>
<br> 

![Edit button]()
![Edit post]()
![Edit play]()
![Delete button]()
![Delete modal]()

<br>
</details>

#### **Comments**
<details>


<br>
<br> 

![Comment not logged in]()
![Comment]()
![Edit comment]()
![Delete comment]()

<br>
</details>

#### **Like Post**
<details>


<br>
<br> 

![Likes list]()
![Likes post]()
![Toggled like]()

<br>
</details>

#### **Profile Page**
<details>

<br>
<br> 

![Profile page]()
![Update email]()

<br>
</details>

#### **Follow profile**
<details>


<br>
<br> 

![Likes list]()
![Likes post]()
![Toggled like]()

<br>
</details>

#### **Search Function**
<details>


<br>
<br> 

![Search bar]()
![Search fail]()
![Search success]()

<br>
</details>


#### **Future Feature**
<details>


<br>
</details>

[Back to top](#wanderlust)

<br>

## **Surface**

### The Design

The design choice for the Wanderlust site aims to get the user to think about a travel diary. With a decorative image .... the image is instead set at the top to welcome the user.

#### Color scheme

The goal of the design is to keep a clean and consistent user experience throughout the pages. With a light background/dark text set up and one accent color .... The color was picked ... Chrome DevTools color dropper tool, then slightly adjusted so the text would still be readable against the background if the image won't load. A color palette was created with the help of Colormind to work as a design foundation during the project...........

![Color Scheme]()

<br>

A contrast grid was used to see how well the colors worked together and to maximaze the visibility on the site.

![Color grid]()


[Back to top](#wanderlust)


## Skeleton

### Technologies
---

#### **Languages**

- **React JS**
<br> The main language for building the User interface for the front end of this full stack application is the JavaScript Library React. React allows for creating reusable UI components that can update separately making the site interactive and user friendly.


- **Django REST Framework**
<br> For this full stack project the Python based framework Django is the development language for the back end API. I used PostgreSQL database, psycopg2 as the adapter and a gunicorn server implementation using WSGI standard. I installed a battery of extra libraries to help run everything smoothly:

    * Pillow (Python Imaging Library)
    * Cloudinary (to host static files)
    * Bootstrap 4 (to style the content and make it resposive)
    * Multiple Django rest libraries (authentication, filters, jwt-tokens, django database url)

- **HTML5**
<br> I used HTML to create the base structure of the project. I started with a basic boilerplate set up and created the first crude structure of the page out of the original design. 

- **CSS3**
<br> The CSS was used to apply the custom styles where I didn't use bootstrap. 

- **Javascript**
<br> A small amount of javascript was used in this application, no separate script was needed and the code is located in the base template.

<br>

#### **Tools**

- [Heroku](https://www.heroku.com/)
    -  I used Heroku to deploy the application. 

- [Balsamiq](https://balsamiq.com/)
    - I used Balsamiq to make the basic wireframes for this project.

- [Colormind](http://www.colormind.io)
    - I used Colormind to create a color palette for my color scheme.

- [Cloudinary](https://cloudinary.com/)
    - I used to create the API's that connects the application to the spreadsheet at Google Sheet. 

- [DevTools](https://developer.chrome.com/docs/devtools/)
    -  I used DevTools to test both changes in my code and the responsivity of the site.  

- [EightShapes](http://eightshapes.com/)
    - I used Eight Shapes color grid to check the color schemes visibility in diffrent combinations.

- [Lucid Chart](https://www.lucidchart.com/pages/)
    - I used Lucid Chart to design the data model and list mock up for the project.

- [GitPod](https://www.gitpod.io/)
    - I used GitPod as the code editor as well as to display to test out changes in my code.

- [GitHub](https://github.com/)
    - I used GitHub to create a repository for my project.

- [Responsive Design Checker](https://responsivedesignchecker.com)
    - I tried using the website on the finally deployed project but the site wouldn't connect to heroku.

- [WAVE](https://wave.webaim.org/)
    - I used WAVE to test the accessibility of the site.

- [W3Schools](https://www.w3schools.com/) 
    - I used W3C to test and validate my code throughout the project. 


[Back to top](#wanderlust)

---

## **Testing**

For more information about the testing performed during the development, go to the separate [testing](/TESTING.md) page.
<br>
<br>

[Back to top](#wanderlust)

---

## **Deployment**

### **Deployment**

The project was deployed to **Heroku** from **GitPod**:
- After creating an account or logging in to an existing one on Heroku, click the "New" button on the right hand side of the 'Personal' menu.
- Choose the option 'Create new app' and then choose a unique name for your application and the right region. Then click 'Create New App'.
- Next you need to add buildpacks and create config vars, this is utterly **important** to have done before you deploy your app!

    - Then add config vars by clicking 'Reveal Config Vars'. I used _Config Var_ called `PORT`, set to `8000`.
    - If you have credentials for your project, you need to add these as well. Create another _Config Var_ called `CREDS` and paste the copy of the requeriments code inside your credentials file into the value field.
    - If you need additional config vars, for example 'secret key', 'database urls' etc they need to be set here as well.

- Now it's time to deploy the app. Go back to the top of the page and click "Deploy".
- Choose a deployment method, I used GitHub since my repository is located on GitHub.
- Scroll down to 'Connect to GitHub' and search for your project. Make sure you are connected to the right GitHub account. Click 'Connect'.
- Keep scrolling downwards, now you can choose between Automatic Deployment or Manual Deployment. I choose Manual first, until the app was properly deployed and a link to the app was visual. Then I choose to enable automatic deployment for smoother testing. 

The live app can be found here: https://padelpals.herokuapp.com/
<br>

<br>
<br>


A copy of this GitHub Repository can be made by either making a copy on your local machine or by forking the GitHub content. By using a copy of the repository changes can be made to the copy without affecting the original code. To make a copy of the repository, follow these steps:

### **Clone**
- Locate the repository at **GitHub**.
- At the top of the file's menu, click the green *code* button to the right.
- The first option in the drop-down menu is clone, where you get three choices of how to clone the repository.
- To clone a copy of the python project, click the 'copy' icon on the right-hand side of **Clone with HTTPS**.
- Choose your code editor, open GitBash and change the working directory to where you want the cloned directory to be made saved.
- In the terminal you write git clone and then paste the copied URL. Like this: '$ git clone https://github.com/Monika-81/padel-pals.git' 
- Press enter and then install the dependencies you like to use for the project.
<br>

### **Forking**
- Locate the repository at **GitHub**.
- At the top right-hand side is a button called *fork*, click on the button to create a copy of the original repository in your GitHub Account.
<br>
<br>


[Back to top](#wanderlust)

---

## **Credits**

### **Content**

For most of the development and bug fixes I went back to the Code Institute LMS (over and over again) and the learning material for this section of the andvanced front end course. While setting up the API the provided Cheat Sheets in the Django section was heavily relied on. Most of the API code is based on the moments project but adjusted to fir this project.

Some of the other sites media I frequently **consulted** was :
<br>
- Code credit to Code Institute's lesson project 



<br>

### **Media**


<br>
<br>

### **Acknowledgement**

- My mentor **Sammy Dartnall** at Code Institute for valuable input, support and encouragement.
- The Slack community for being such an open, warm and sharing place. 
- **Viet Hoang** for letting me run the app by him and for getting user experience input before, during and at the final stage of the project.


[Back to top](#wanderlust)

---