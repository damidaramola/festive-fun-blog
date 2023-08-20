# FestiveFun
[link to project](https://festivefun.herokuapp.com/)

![am i responsive](https://github.com/damidaramola/festivefun/assets/110638513/e7bfbfc9-9030-486c-b901-e02459b0af93)


## About FestiveFun
FestiveFun is a blog which provides readers with exposure to some of the top music and transformative events from around the world, as well as helpful festival tips and plenty of festival fashion ideas and advice. This blog caters to young people who enjoy going on festival excursions, dancing to live music, meeting new people and expressing themselves through stylish clothing.


## Table of Contents
- [About](#about-festivefun)
-  [Project Goals](#project-goals)
-  [User Stories](#user-stories)
-  [Design of Website](#design-of-website)
 - [color scheme](#color-scheme)
 - [WireFrames](#wireframes)
- [Features](#features)
- [Technologies I Used](#technologies-i-used)
 - [Frameworks , Libraries and dependencies](#development-frameworks-and-packages-used)
 -  [languages](#languages-used)
- [Testing](#testing)
 -  [Manual Testing of User Stories](#manual-testing-of-user-stories)
-  [Bugs](#bugs)
-  [Deployment](#deployment)
- [credits](#credits)


## Project Goals

Project purpose: In this project, you'll build a Full-Stack site based on business logic used to control a centrally-owned dataset. You will set up an authentication mechanism and provide role-based access to the site's data or other activities based on the dataset - Code Institute

## User Stories 

- As a Blog Reader I can register my email so that I can gain access to adding comments and likes under posts
- As a Registered blog reader I can log in so that I can add and like  blog posts also also comment
- As a logged in  Blog reader I can delete my comments 
- As a logged in Site Blog reader I can create a comment under each post
- A registered User is shown  success messages when user completes an action
- As a logged in Blog reader I can like/unlike so that show that I enjoyed a blog post and I can also change my mind
- As a Blog reader I can view the number of likes on each post so that I can read the blog posts people enjoy
- As a Blog reader I can open each post so that I can read all of the content of the blog
- As a Registered Blog reader I can log out so that I can make sure no one can access my account online
- As an admin user I can create posts in the backend
- As an admin user , I can approve the comments of users to prevent inappropriate comments

## Design of Website
 ### color scheme

 - The colour scheme consists of primarily dark purple to black. There are also secondary colours which represents the vibrant nature of many festivals.

![colour scheme](https://github.com/damidaramola/festivefun/assets/110638513/36effce5-5871-4d93-b4b9-c90da877ac6d)

 ### WireFrames

- These wireframes cover the user interfaces of the main pages including the blog post page, landing page and the sign in and sign up pages'

![blog wireframe](https://github.com/damidaramola/festivefun/assets/110638513/1ef967e4-c04d-412b-94dc-21d57af937ec)
![blog post wireframe](https://github.com/damidaramola/festivefun/assets/110638513/e56e7d65-febd-4694-b481-59cbe7195933)
![sign up page wireframe](https://github.com/damidaramola/festivefun/assets/110638513/c8bbb859-7bfd-4e2c-8cd3-530e89acd346)
![Sign in wireframe](https://github.com/damidaramola/festivefun/assets/110638513/e5f54ede-31ac-4249-8267-6eb5aadf9dba)

## Features

 The home page is the feature you see once you first land on the blog website

![Home Page](https://github.com/damidaramola/festivefun/assets/110638513/cf7d6053-7785-4b9b-adbf-3f7bbc192d57)

- A user can access the About us page using the link through the carousel

![about us](https://github.com/damidaramola/festivefun/assets/110638513/4df6ce0d-819f-43f5-aaa7-20549d8ace9e)

- The user can sign in to be able to comment , like posts and edit posts

![Sign in](https://github.com/damidaramola/festivefun/assets/110638513/4b17ecd5-58f1-4fa4-8d72-1664e20d7f66)

- Here in the blog detail page , we can see The title of the blog, the date it was created on , the category which the blog is in and the blog content

![blog detail](https://github.com/damidaramola/festivefun/assets/110638513/626eb832-7da7-49ed-be11-00e958aff0f8)

- The carousel shows some images for inspiration to festival goers

![Carousel](https://github.com/damidaramola/festivefun/assets/110638513/e1015a18-805b-4124-903f-38d617406a28)

- Once the user comments through the form , the comment is sent to the admin panel from approval

![comment waiting approval](https://github.com/damidaramola/festivefun/assets/110638513/0af8bb64-9af0-4f85-ba4c-44f44fbe49c5)

This user is notified when they are logged in / signed out
![feedback message](https://github.com/damidaramola/festivefun/assets/110638513/bcaf4c0c-b6da-41c3-afe1-e885fa3d5d56)

- when users are logged out, they must sign up/signin in order to like posts or comment

![likes logged out comments](https://github.com/damidaramola/festivefun/assets/110638513/3844f198-57ab-4a93-ba46-db116465ad31)

- Users can edit or delete the comment they have written

![write a comment](https://github.com/damidaramola/festivefun/assets/110638513/8ef1efdc-d22d-460a-8e7c-317e59e75669)


## Technologies I Used 

### Workspace

#### GitPod
[GitPod](https://gitpod.io/) was the IDE workspace I used to build this blog.


### Version Control

#### Git
[Git](https://git-scm.com/) was used for version control by utilizing the Gitpod terminal to add and commit to Git and push to GitHub.

#### GitHub
[GitHub](https://github.com/) is used to store the project.


### Wireframing 

#### Figma
[Figma](https://www.figma.com/) was used to create wireframes during the creative brainstorming/design process.


[Back to top](#festivefun)

### Languages used

#### HTML
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
#### CSS
- [CSS3](https://en.wikipedia.org/wiki/CSS)
#### JavaScript
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
#### Python
- [Python](https://www.python.org/)

#### Font Awesome
[Font Awesome](https://fontawesome.com/) was used on the website to add icons.

#### Bootstrap (4)
[Bootstrap](https://getbootstrap.com/) was imported for responsiveness and styling of the website.

### Development Frameworks and packages used

#### Django
[Django](https://www.djangoproject.com/) was the web framework used to build this project.

- Additional packages/libraries/applications that were used to build this project

- Django Crispy Forms
[Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) was used to style my forms

- Summernote
[Summernote](https://summernote.org/) was used To give the admin more options to customize blog posts in the editor.

## Deployment

### Heroku
[Heroku](https://www.heroku.com/) is where I deployed to the blog.

### Gunicorn
[Gunicorn](https://gunicorn.org/) was use to the project to Heroku.

### Cloudinary
[Cloudinary](https://cloudinary.com/) was used to host static/media files and serve them to Heroku.

### ElephantSQL
[ElephantSQL](https://www.elephantsql.com/) was used to host my database. ElephantSQL is a cloud-based PostgreSQL database hosting service.

[Back to top](#festivefun)

## Testing

### WC3 Validator testing
[WC3 Validator for html](https://validator.w3.org/)

- The HTML code has the Django code incorporated meaning that this naturally leads to errors in the WC3 Validator tests

![Capture](https://github.com/damidaramola/festivefun/assets/110638513/69d59b41-ea53-4094-bce9-935b7c23c8cd)

### Jigsaw CSS testing

- No issues were found with the css file code

![css validation](https://github.com/damidaramola/festivefun/assets/110638513/7d0021d7-924b-4d6a-ae14-6d03584a7665)


### Manual Testing of User Stories

- As a Blog Reader I can register my email so that I can gain access to adding comments and likes under posts

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
 Click 'Sign up' at the top right of Navbar|The user is directed to the sign up page| Works as expected |

- As a Registered blog reader I can **log in ** so that I can add and like  blog posts also also comment

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
  Click 'Log in' at the top right of Navbar|The user is directed to the log in page| Works as expected |

- As a Registered Blog reader I can **log out ** so that I can make sure no one can access my account online

 **Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
 Click 'Log out' at the top right of Navbar|The user is directed to the log out page| Works as expected |

- As a Blog reader I can open each post so that I can read all of the content of the blog

 **Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
 Click on post preview|User is taken to the post with further information about each blog| Works as expected |

- As a blog reader I can view the comments on each post so that I can participate in the conversation

 **Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
 Scroll under the blog post content | User can see comments under each post| Works as expected |

- As a Blog reader I can open each post so that I can read all of the content of the blog

 **Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
 Scroll under the blog post image |User can read Blog Post content| Works as expected |

- As a Blog reader I can view the number of likes on each post so that I can read the blog posts people enjoy

 **Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
 View clapping icon above comment section| User can see clapping icon with 'clap count'| Works as expected |

- As a logged in Blog reader I can like/unlike so that show that I enjoyed a blog post and I can also change my mind

 **Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
 Click on clap icon|Counter increments/decrements by 1| Works as expected |

- A registered User is shown success messages when user completes an action

 **Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
 Log In to your profile|Success message is displayed at the top with a timer| Works as expected |

- As a logged in Site Blog reader I can create a comment under each post

 **Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
 Fill in the comment form under each post|User can delete comments| Works as expected |


- As a logged in  Blog reader I can delete my comments 

 **Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
 Click on red delete icon|The page refreshes and the comment is gone| Works as expected |


- As an admin user , I can approve the comments of users to prevent inappropriate comments

 **Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
 Go to the comment model in the django admin panel|Click accepted under the comment| Works as expected |


- As an admin user I can create posts in the backend

 **Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
 Create a post in the fields of the post model| The post appears on the front end| Works as expected |

## LightHouse Testing 

- The results show that the performance is 55. I think that the images may be slowing down the loading time of the page.

![Light house testing](https://github.com/damidaramola/festivefun/assets/110638513/4f5407de-dc99-4a30-9d50-028d84f1c00b)
 

## Bugs

 I had an issue with data base migrations and while changing the Comment user_name field from an CharField to a ForeignKey. I have learned to check my models properly and migrate them consistently to avoid problems such as that.

[Back to top](#festivefun)

## Deployment

### Step 1:
_Installing Django and supporting libraries_

1. Clone [this repository](https://github.com/Code-Institute-Org/gitpod-full-template)


2. Install Django, supporting libraries and Cloudinary libraries using these commands in the terminal
````
pip3 install 'django<4' gunicorn
pip3 install dj_database_url psycopg2
pip3 install dj3-cloudinary-storage
````

3. Create requirements file using this command in the terminal
`````
pip3 freeze --local > requirements.txt
`````

4. Create project using this command in the terminal
`````
django-admin startproject YOUR_PROJECT_NAME .
`````
_(Don't forget the .)_

5. Create app using this command in the terminal
````
python3 manage.py startapp YOUR_APP_NAME
````

6. Add installed apps to settings.py
`````
NSTALLED_APPS = [
    …
    'YOUR_APP_NAME',
]
`````

7. Migrate Changes using this command in the terminal
````
python3 manage.py migrate
````

8. Run server to test using this command in the terminal
````
python3 manage.py runserver
````

### Step 2:
_Create a new external database_

1. Sign Up/Log In on [ElephantSQL](https://www.elephantsql.com/)

2. Click "Create New Instance"

3. Set up your plan
- Give your plan a name
- Select the Tiny Turtle (Free) plan
- Tags field can be left blank

4. Click "Select Region"
- Select a data center near you

5. Click "Review"
- Check that your details are correct. Then click "Create instance"

6. Go to ElephantSQL dashboard and click on your database project

7. Copy your ElephantSQL database URL

### Step 3:
_Create a Heroku app_

1. Sign Up/Log In on [Heroku](https://www.heroku.com/)

2. From the dashboard click on "New" and create new Heroku App

3. Enter your app name and your location

4. Go to the settings tab

5. Click on "Reveal Config Vars"

6. Add a Config Var called DATABASE_URL
- The value should be the ElephantSQL database URL

### Step 4:
_Attach the database_

1. In GitPod create new file called env.py file on top level directory

2. In the env.py add these lines of code:
- Import os library
````
import os
````
- Set environment variables
````
os.environ["DATABASE_URL"] = "Paste in ElephantSQL database URL"
````
- Add secret key
````
os.environ["SECRET_KEY"] = "Make up your own randomSecretKey"
````

3. Go back to [Heroku](heroku.com)
- Add your secret key to Config Vars - SECRET_KEY, “randomSecretKey”

### Step 5:
_Prepare your environment and settings.py file_

1. In settings.py - reference env.py with this line of code:
````
from pathlib import Path
import os
import dj_database_url

if os.path.isfile("env.py"):
   import env
````

2. Remove the insecure secret key and replace - links to the SECRET_KEY variable on Heroku
````
SECRET_KEY = os.environ.get('SECRET_KEY')
````

3. Comment out the old ````DATABASES```` section.

4. Add a new ````DATABASES```` section _(links to the DATATBASE_URL variable on Heroku)_:
````
DATABASES = {
   'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}
````

5. Save all the files and make migrations in the terminal using this:
````
python3 manage.py migrate
````

### Step 6:
_Get your static and media files stored on [Cloudinary](https://cloudinary.com/):_

1. Sign Up/Log In on [Cloudinary](https://cloudinary.com/) and copy your CLOUDINARY_URL from the Cloudinary dashboard.

2. Add Cloudinary URL to env.py:
````
os.environ["CLOUDINARY_URL"] = "cloudinary://************************"
````

3. Go back to [Heroku](heroku.com) and add Cloudinary URL to Heroku Config Vars
- COUDINARY_URL, cloudinary://************************

4. Add DISABLE_COLLECTSTATIC to Heroku Config Vars:
- DISABLE_COLLECTSTATIC, 1

5. In the settings.py, add Cloudinary libraries to INSTALLED_APPS in this order:
````
INSTALLED_APPS = [
    …,
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    …,
]
````

6. Make Django use Cloudinary to store media and static files:
````
STATIC_URL = '/static/'

STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
````

7. Link file to the templates directory in Heroku
Place this under the BASE_DIR line:
````
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
````

8. Change the templates directory to TEMPLATES_DIR
````
TEMPLATES = [
    {
        …,
        'DIRS': [TEMPLATES_DIR],
       …,
            ],
        },
    },
]
````

9. Add Heroku Hostname to ALLOWED_HOSTS:
````
ALLOWED_HOSTS = ["PROJ_NAME.herokuapp.com", "localhost"]
````

### Step 7:

1. In GitPod create 3 new folders on top level directory called:
- media
- static
- templates

2. Create a file called ````Procfile```` on the top level directory

3. In the Procfile add this code:
````
web: gunicorn PROJ_NAME.wsgi
````

4. In the Terminal Add, commit and push your files:
````
git add .
git commit -m “Deployment Commit”
git push
````

5. In Heroku go to the deploy tab.

6. Chose GitHub as deployment method and chose your repository.

7. At the bottom of the page chose Deploy branch (from the main branch).

## Production

1. In your settings.py file, set DEBUG to False
````
DEBUG = False
````

2. Make sure that X_FRAME_OPTIONS and ALLOWED_HOSTS are added to your settings.py file.
````
X_FRAME_OPTIONS = 'SAMEORIGIN'

ALLOWED_HOSTS = ['your_app_name.herokuapp.com', 'localhost']
````

3. Go to Heroku, in Settings - Reveal Config Vars

4. Remove DISABLE_COLLECTSTATIC

5. On Heroku, go to Deploy tab and scroll to the bottom of the page and chose Deploy(Main branch)

6. Click "View App" when the build is done.

## Credits

This project is inspired by the "I Think Therefore I Blog" walkthrough, produced by Matt Rudge at Code Institute.
photos are from [Pexels.com](https://www.pexels.com/photo/ladies-on-a-concert-10825138/)

## Appreciation
I would like to thank my mentor Jubril for his support throughout

[Back to top](#festivefun)




