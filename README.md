<h1 align="center">Luxury Car</h1>

![My Landing Page](https://github.com/ayaelsaid/laxory-Car-Re.github.io/blob/main/Screenshot%202024-06-08%20013654.png)

-----------------------------------------------------------------------------------------------------------------------------------------------------------
## Author: Aya El Sayed

# Sections

1. [**Introduction && Inspiration &&  Motivation**](#introduction): A brief overview of the project with links to the deployed site, blog article, and author's LinkedIn.
2. [**Installation**](#Installation): Detailed steps to install and run the project locally.
3. [**Challenges and Struggles**](#Challenges-and-Struggles)
4. [**Architecture**](#Architecture)
5. [**snippets**](#snippets)
6. [**Usage**](#Usage): Instructions on how to use the project and a brief description of its features.
7. [**Contributing**](#Contributing): Guidelines for contributing to the project.
8. [**Related projects**](#Related-projects): Links to other related projects.
9. [**Licensing**](#Licensing): Information about the project's license

------------------------------------------------------------------------------------------------------------------------------------------------------------ 

# Introduction
Luxury Car Rental is a website designed to simplify the process of reserving a car from a variety of options, complete with detailed descriptions, and seamless online payment options.

# Inspiration
This project is deeply inspired by my father, who has spent a significant portion of his life working with cars. Growing up around his passion for automobiles, I witnessed firsthand the importance of convenience and reliability in the car rental industry.

# Motivation
My motivation for creating Luxury Car Rental stemmed from the observation that in many countries, renting a car has become a preferred choice over purchasing one outright. This could be due to factors such as flexibility, affordability, and the avoidance of long-term commitments associated with car ownership.

**By building Luxury Car Rental, I aimed to bridge the gap between car rental companies and customers, providing a user-friendly platform that simplifies the process of finding, booking, and paying for rental cars.**

- **Deployed site**: **[visit me](https://ayaelsaid.github.io/laxory-Car-Re.github.io/)**&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; - **Blog**: **[blog](https://app.hackernoon.com/mobile/V6BE6TO89ju8w3WMT0rM)**&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; - **linkedIn**: **[Aya Elsayed](https://www.linkedin.com/in/aya-elsayed-601228285/recent-activity/all/)**


![GIF](https://github.com/ayaelsaid/laxory-Car-Re.github.io/blob/main/Untitled.gif)

-------------------------------------------------------------------------------------------------------------------------------------------------------------

## Installation


| Package              | Installation Command                                                                                                                   | 
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| clone repository     | `git clone https://github.com/ayaelsaid/laxory-Car-Re.github.io/.git && cd laxory-Car-Re.github.io`                                    |   
| anaconda3            | [Install Anaconda](https://www.anaconda.com/download)                                                                                  |
| python3              | Install Python 3.11                                                                                                                    |
| Flask                | `pip3 install flask`                                                                                                                   |
| Flask_login          | `pip3 install flask_login`                                                                                                             |
| sqlalchemy           | `pip3 install flask_sqlalchemy`                                                                                                        |
| flask_bcrypt         | `pip3 install flask_bcrypt`                                                                                                            |
| werkzeug.security    | `pip3 install werkzeug.security`                                                                                                       |
| Bootstrap CSS        | [Bootstrap 4.4.1 CSS](https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css)                                                          |
| Popper.js            | [Popper.js 1.12.9](https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js)                                          |
| Bootstrap JavaScript | [Bootstrap 4.0.0 JS](https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js)                                              |

-------------------------------------------------------------------------------------------------------------------------------------------------------------

## Challenges and Struggles
Building Luxury Car Rental presented numerous challenges and learning opportunities, especially considering my limited knowledge in both front-end and back-end development. As a solo developer, I encountered various hurdles throughout the development process:

1. **Design and Branding**: Creating visually appealing styles and choosing suitable colors for the website proved to be a daunting task. Additionally, designing a logo that accurately represents the brand was a challenge, especially considering my lack of expertise in the automotive industry.
2. **Framework Selection**: Choosing the Right Framework: Selecting the appropriate framework for the project was crucial yet challenging due to my limited understanding of the available options and their suitability for a car rental website.
3. **Page Redirection**: Navigating between pages and ensuring correct redirection was occasionally problematic, leading to errors when linking to incorrect pages within the website.
4. **Database Management**: Altering database tables to accommodate changes in the project's requirements was a significant challenge, particularly as I had to navigate through unfamiliar database management systems.
5. **Data Planning and Modeling**: Insufficient planning for data storage and modeling led to challenges in defining the necessary data structures for each model. This lack of foresight resulted in difficulties when modifying database tables and accommodating new ideas during the development phase.


Despite these obstacles, each challenge served as an opportunity for growth and learning. Overcoming these struggles not only enhanced my technical skills but also reinforced my determination to build a fully functional car rental website from scratch.

------------------------------------------------------------------------------------------------------------------------------------------------------------

# Architecture
![500 ERROR TO ACCESS IT IS SO EASY](https://github.com/ayaelsaid/laxory-Car-Re.github.io/blob/main/Screenshot%202024-06-08%20034132.png)

### Frontend

|       Component         |                                                     Description                                                                                                   |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HTML, CSS, JavaScript   | Fundamental technologies for building the frontend. HTML provides structure, CSS adds styling, and JavaScript adds interactivity.                                 |
| Jinja2 Templating Engine| Used with Flask to generate dynamic HTML content by embedding Python code within HTML templates. Enables dynamic rendering of content based on server-side data.  |
### Backend

|    Component                           |           Description                                                                                                                                               |
|----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Flask Framework                        | Lightweight and flexible Python web framework for building web applications. Provides tools and libraries for handling requests, routing, and integrating with other|
|                                        |components.                                                                                                                                                          |
| Flask-Login                            | Flask extension for user session management, authentication, and authorization. Simplifies the implementation of user authentication and access control.            |
| bcrypt                                 | Password hashing library used for securely storing user passwords in the database. Provides cryptographic hashing functions to protect user passwords from          |
|                                        |unauthorized access.                                                                                                                                                |
| User Authentication and Authorization  | Algorithms and logic for user authentication (login/logout) and authorization (access control). Involves verifying user credentials, managing user sessions, and    |
|                                        |enforcing access control policies based on user roles and permissions.                                                                                               |

### Databases

| Component        | Description                                                                                                                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SQLAlchemy       | Powerful ORM (Object-Relational Mapping) library for Python. Provides a high-level interface for interacting with relational databases. Simplifies database operations by abstracting away|
|                  |low-level SQL queries and allowing developers to work with Python objects.                                                                                                                 |
| SQLFile Database | Presumably, a SQLite database file (*.sqlite or similar) managed by SQLAlchemy. Database models (such as User, Car, Reservation, etc.) are defined using SQLAlchemy ORM,                  |
|                  |which automatically maps Python classes to database tables.                                                                                                                                |

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![tech](https://github.com/ayaelsaid/laxory-Car-Re.github.io/blob/main/Screenshot%202024-06-08%20043151.png)

 ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# snippets 

**auth of log in:**

![tech](https://github.com/ayaelsaid/laxory-Car-Re.github.io/blob/main/Screenshot%202024-06-08%20045842.png)


**auth of logout**

![tech](https://github.com/ayaelsaid/laxory-Car-Re.github.io/blob/main/Screenshot%202024-06-08%20045926.png)

**view file**

![tech](https://github.com/ayaelsaid/laxory-Car-Re.github.io/blob/main/Screenshot%202024-06-08%20050027.png)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Usage

- **HomePage:** Landing page for the site with information and features.

- **Sign Up:**
     Users can sign up to create an account on the site.

- **Login:**
     Users can log in to the site to reserve a car.

- **Logout:**
     To log out of the site.

- **Delete Account:**
     Users can delete their account by clicking on "Delete Account."

- **Settings:**
     Users can change their information.

- **Note:**
     Users can write reviews or any notes to help themselves and us make our service better.

- **Reservation:**
     Users can reserve a car from this page, upload their requirements, fill forms, and pay online.

- **My Reservation:**
     Stores every reservation process of the user.

- **Car:**
     Shows the cars with price, ID, color, and description.

  ![tech](https://github.com/ayaelsaid/laxory-Car-Re.github.io/blob/main/Screenshot%202024-06-08%20044804.png)

--------------------------------------------------------------------------------------------------------------------------------------
## Contributing

Everyone has ideas to make the site better, and you are encouraged to share yours! Your advice is valuable, and I am still learning, so thank you for your help in making my site better.

- **Fork the Project**
- **Create your Feature Branch**
- **Commit your Changes**
- **Push to the Branch**
- **Open a Pull Request**
-----------------------------------------------------------------------------------------------------------------------------------------
## Related projects

- **[avis](https://www.avis.com/en/locations/eg)**

- **[enterprise](https://www.enterprise.com/en/home.html)**

------------------------------------------------------------------------------------------------------------------------------------------
## Licensing

MIT License 
