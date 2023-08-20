# FestiveFun
[link to project](https://festivefun.herokuapp.com/)

![am i responsive](https://github.com/damidaramola/festivefun/assets/110638513/e7bfbfc9-9030-486c-b901-e02459b0af93)


## About FestiveFun
FestiveFun is a blog which provides readers with exposure to some of the top music and transformative events from around the world, as well as helpful festival tips and plenty of festival fashion ideas and advice. This blog caters to young people who enjoy going on festival excursions, dancing to live music, meeting new people and expressing themselves through stylish clothing.


## Table of Contents
- About 
- Project Goals
- User Stories 
- Design of Website
 - color scheme
 - WireFrames
- Features
- Technologies I used 
 - Frameworks , Libraries and dependencies 
 - Languages 
- Future Features
- Testing
 - Manual Testing of User Stories
- Bugs
- Deployment
- Credits


## Project Goals

## User Stories 

- As a Blog Reader I can register my email so that I can gain access to adding comments and likes under posts
- As a Registered blog reader I can **log in ** so that I can add and like  blog posts also also comment
- As a logged in  Blog reader I can delete my comments 
- As a logged in Site Blog reader I can create a comment under each post
- A registered User is shown  success messages when user completes an action
- As a logged in Blog reader I can like/unlike so that show that I enjoyed a blog post and I can also change my mind
- As a Blog reader I can view the number of likes on each post so that I can read the blog posts people enjoy
- As a Blog reader I can open each post so that I can read all of the content of the blog
- As a Registered Blog reader I can **log out ** so that I can make sure no one can access my account online
- As an admin user I can create posts in the backend
- As an admin user , I can approve the comments of users to prevent inappropriate comments

## Design of Website
 ### color scheme

 - The colour scheme consists of primarily dark purple to black. There are also secondary colours which represents the colourful nature of many festivals.

![colour scheme](https://github.com/damidaramola/festivefun/assets/110638513/36effce5-5871-4d93-b4b9-c90da877ac6d)

 ### WireFrames

- These wireframes cover the user interfaces of the main posts including the blog post page, landing page and the sign in and sign up pages'

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

- when users are logged out, thy must sign up/signin in order to like posts or comment

![likes logged out comments](https://github.com/damidaramola/festivefun/assets/110638513/3844f198-57ab-4a93-ba46-db116465ad31)

![write a comment](https://github.com/damidaramola/festivefun/assets/110638513/8ef1efdc-d22d-460a-8e7c-317e59e75669)


## Technologies I used 



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

- A registered User is shown  success messages when user completes an action

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



## Deployment



## Credits



