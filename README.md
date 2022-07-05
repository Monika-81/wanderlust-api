# **Wanderlust**

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
    - [Edit post](#edit-post)
    - [Delete post](#delete-post)
    - [Like post](#like-post)
    - [Comments](#comments)
    - [Profile page](#profile-page)
    - [Contact form](#contect-form)
    - [Search function](#search-function)
    - [Admin](#admin)

   
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

What the user will be looking for:

[Back to top](#wanderlust)

<br>

## Scope 

---


### **User Stories**

<br>

**Epic: Admin**


**Epic: Account Management**


<br>

To follow an agile approch, a project board (kanban-board) was set up using GitHub Projects: [Kanban]()

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


#### **Edit Post**
<details>


<br>
<br> 

![Edit button]()
![Edit post]()
![Edit play]()

<br>
</details>

#### **Delete Post**
<details>

<br>
<br> 

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

#### **Contact Form**
<details>


<br>
<br> 

![Contact form]()
![Confirmation]()

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

#### **Admin**
<details>


![Search bar]()

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

#### Color scheme


![Color Scheme]()

<br>

A contrast grid was used to see how well the colors worked together and to maximaze the visibility on the site.

![Color grid]()


[Back to top](#wanderlust)


## Skeleton

### Technologies
---

#### **Languages**

- **Django**
<br> For this full stack project the Python based framework Django is the development language for the application. I used PostgreSQL database, psycopg2 as the adapter and a gunicorn server. I installed a battery of extra libraries to help run everything smoothly:

    * Cloudinary (to host static files)
    * Bootstrap 4 (to style the content and make it resposive)

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

For most of the development and bug fixes I went back to the Code Institute LMS (over and over again) and the learning material for this section of the course.

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