# jovian_careers_web
A careers website for Jovian

# Web Development With Python

Code: https://github.com/aakashns/jovian-careers-website

There are several tools to deploy your web application but in this notebook, we are focussing on building and deploying a website using the tools provided by python. 

![](https://res.cloudinary.com/practicaldev/image/fetch/s--Y19O2Ab3--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/pfftroqy6k915lu968u9.JPG)



### Objective
 
- Create a “Jovian Careers” website listing job openings at Jovian
- Use a modern HTML & CSS framework for layout and styling
- Deploy the website to the cloud and attach a custom domain



### Objective 

+ Explore web development and deployment with Python
+ Create a Jovian Careers" website listing job openings at Jovian
+ Use a modern HTML and CSS framework for layout and styling
+ Deploy the website to the cloud and attach a custom domain

Topics covered are:
* GitHub
* Replit
* Flask
* HTML
* CSS
* Bootstrap
* Deployment (render.com)
* Domains & DNS

## Prerequisites

To make the best use of this tutorial make sure to go through the following tutorials/lessons prior to this one:

- Python - https://jovian.ai/aakashns/first-steps-with-python 
- Git - https://jovian.ai/aakashns/python-local-development-git 
- HTML tutorial: https://htmldog.com/guides/ , https://www.w3schools.com/html/
- CSS tutorial: https://htmldog.com/guides/css/ , https://www.w3schools.com/css/
- Basic HTML, CSS templates : https://www.squarespace.com/blog/what-is-a-website-template 

Let's get started,


### Open up the Project on Replit:

Replit is a free online collaborative in browser IDE that allows us to create projects and write code in many supported languages. 
Replit allows us to **integrate our code on GitHub** i.e we can make edits on the cloud and the code will directly be synced on the cloud. 

- To get started, you will first need to head at https://replit.com/ and **SIGN UP** to create your replit account if you haven't done that already. 

- Once you've created your account, you will be able to view your replit dashboard. You can directly create new projects from here but ideally you should you github to keep a track of your prpjects. You can do this by connecting to GitHub: 
<p float="left">
  <img src="https://i.imgur.com/GzfLI1F.png" width="700" /></p>

- After this step, you will be able to see a **GithubRepos** section on your dashboard. You can always disable this integration incase it doesn't work and then re-enable it to start from scratch.  

- You can select your repo and import it: 
<p float='left'>
<img src='https://i.imgur.com/InqNqMY.png' width='700'></p>
Which is now going to show all the repo files on replit. 

- Now that you have your project open, you will be asked to configure a run command which will be executed everytime we click on the run button. 
<p float='left'>
<img src='https://i.imgur.com/Ob0SeQF.png' width='500'></p>

- Head to the files tab and add a new file called `app.py`. 


### Running a Flask Web Server 
For building web application in python we use a framework called flask. 
### Flask

Flask is one of the most popular web frameworks in python. It is lightweight and provides useful tools that make creation of web applications in python easier. 


### Installation

If you're using flask locally, you can install it according to your operating system using this tutorial: https://phoenixnap.com/kb/install-flask


Because we are already using a cloud enviroment, we can directly install flask using the following command on our shell:

`pip install Flask` 


**Please Note:**
Sometimes, GitHub integration does not allow this command to function properly. If it works for you, great, you can go ahead. But for those of you who are facing an issue of Flask installation, try to create a fresh repl on replit without integrating github and continue working. Later, you can connect your github with the version control option in the left sidebar. 

<p float='left'>
<img src='https://i.imgur.com/CQxHQwF.png' width='200'></p>


### Creating a Simple Flask Application 

1. We begin with **importing the Flask class** from the flask module. 

`from flask import Flask `
  
  - Even though these are both called flask, inside the **module flask** there is a class called **Flask** who's instance will be our WSGI application(Web Server Gateway Interface).  


**WSGI:** A Web Server Gateway Interface describes how a web server communicates with web applications. 
![](https://www.fullstackpython.com/img/visuals/wsgi-interface.png)

You can read more about WSGI: https://www.fullstackpython.com/wsgi-servers.html




2. **Creating an object of Flask** called `app`. To this we provide a pre-defined variable in python `__name__`, which evaluates to the name of the currect module. This helps Flask to locate resources and templates used in making a website. 

`app = Flask(__name__)`


3. Next, we need to **register a ROUTE**. `Route` is simply a part of the URL that comes after the domain name. This tells our flask application what should be returned when a certain URL is requested. 

`app.route('/') `

- We do this with the help of a decorator `@` and provide the path we want our app to match. For now, we will provide an empty route with an upward slash`('/')` which is usually the home page of any website. 

4. To **run our flask application**, we will use the flask command `app.run` and pass the host name = '0.0.0.0', to run it locally. 

`if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)`

- We will also pass in an additional argument `debug=True` which simply tells flask that we are currently developing and reflects all the changes we make immediately. 
 
- Upon clicking the run button, replit will open up a browser within our browser which we can also view in a new tab. 

<p><img src = 'https://i.imgur.com/hWxLogj.png'> </p>

### References

- GitHub tutorial: https://docs.github.com/en/get-started/quickstart/hello-world
- Replit tutorial: https://docs.replit.com/tutorials/overview
- Flask tutorial: https://flask.palletsprojects.com/en/2.1.x/quickstart/




Creating Wireframes: 

To have a gist of what we are creating we will create a rough outline of our website using a whiteboard or a notebook. We are using a virtual whiteboard https://excalidraw.com/ to create our wireframes.  
 
It is important to have a clear picture of what our website should look like, otherwise writing code can get tricky. 

<p float='left'>
<img src='https://i.imgur.com/adj3lqZ.png' width='500'></p>

This is what our wireframe/outline looks like. So now we get straight to adding the right tags in our website. 

#### Adding an Image to our Website: 

**Static assets** are a term for objects we render in our website that when sent to the server remains unchanged like an **image**. 

For this purpose we will head over to the files section and create another folder - `static`. So if we upload a file inside this, we can access it using the url of the server where we are rendering the `route('/')`, by adding `/ static/ image_name`. 

![Imgur](https://i.imgur.com/IzmQuu4.png)

You can add this link directly to the source of the image in the `img` tag in your html. 

### Styling the page using CSS 



**CSS - Cascading Style Sheets**,
is used for styling your web pages. CSS usually functions around a few major concepts: 
- [Selectors:](https://web.dev/learn/css/selectors/) `Id` and `Class`
- [The Box Model](https://web.dev/learn/css/box-model/) 
  <p float="left">
  <img src="data:image/png;base64,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" width="380" /></p>


- You can search through the whole list of features as per your need. The best way to add CSS is to do a quick CSS tutorial, you can refer to https://web.dev/learn/css/.  


All code for CSS can be added to the `<style>` tag of your html document. For eg, we are using the code below to add styling to our website as per our wireframe. 


```
<DOCTYPE html>
<html>
  <head>
    <style>
      h1{
        font-family: Roboto;
        text-align: center;
        color: rgb(180, 180, 100)
      }
      h2{
        font-family: Roboto;
        color: rgb(180, 180, 100)
        text-align: center;
      }
      .bodytext {
        font-family: rosybrown; 
        text-align: center; 
        color: rgb(80,90,90)
      }

      #container{
        max-width: 720px;
        margin: 0 auto 0 auto;
      }
    </style>
  </head>
  <body>
  </body>
</html>
```

You can fiddle around and experiment with CSS to understand it better. 

### Using Bootstrap for faster Development 

Instead of typing whole CSS manually for every website, you can use a pre existing set of styles that have been created by some good designers.  

You can head to Bootstrap's quickstart guide: https://getbootstrap.com/docs/5.2/getting-started/introduction/, 
and follow the steps below to add some extra tags within the `<head>` tag to ensure the proper working of bootstrap: 

- Add the follwing meta tags: 

```
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
```

- For CSS add a link tag: 

```
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
```

  This contains some pre-existing styles that immediately get applied to our page. You can reload and see the changes straight away.  So now, all we need to do is add appropriate classes to style our website according to preexisting styles by bootstrap developers. 



Let's look at a few classes we will add to make our website look more presentable and ready. 

- For Centre Aligning your text: `class = "text-center"`

- Margin Top: `mt-margin_size`
- Margin Bottom: `mb-margin_size`

For any feature you want, you can always look up into the bootstrap documentation. 

### Dynamic Data 

Now, as you can imagine, it is not a good idea to list all the jobs in HTML file format, because everytime we have to add a new job, we might have to go to the html file and make changes. So data is stored somewhere like a database where administrators can directly make changes, then information is fetched from their to display on the website. 
We will not connect to a database today but stimulate the process. 


- We will create a dictionary of jobs that we want to pass into our website. 

  <p float='left'>
<img src='https://i.imgur.com/fMxjwEP.png' width='500'></p>

- Then we will add an argument in the `render_template` as `jobs` and then we can head to html to add add this with the help of a special template called **Jinja Template**. 

```
def hello_jovian():
  return render_template('home.html', jobs=JOBS)
```


#### Jinja Template 

It is a text-based template language and thus can be used to generate any markup as well as source code. 

We can use jinja template to customize html tags. That is exactly what we are going to do here. 
Here's a cheatsheet on using Jinja Template to add fields into your flask app: https://www.codecademy.com/learn/learn-flask/modules/flask-templates-and-forms/cheatsheet

- We will head over to `home.html`, to where we want to insert these jobs and add: `{{jobs}}`. You'll notice that whatever information we put inside our `jobs` dictionary will appear as a string:

  ![Imgur](https://i.imgur.com/izM10Z4.png)

We can also use this to pass other variables like `company_name = 'Jovian'` and use jinja template to render the company name wherever within the `home.html`. 


#### For Loop Inside Template

These templates support a special syntax to select particular information from python datastructure. 

We can access the elements within a dictionary just how we would in python. So let's get the `title` from the `jobs` dictionary.  

Syntax:
```
{% for job in jobs %}
  <div>{{job['title']}}</div>
{% endfor %}
```
This is what the above piece of code will result to: 
<p float='left'>
<img src='https://i.imgur.com/7DxKLkz.png' width='500'></p>

To make it appear like we want, we can add html accordingly. 

This is what our final code and output looks like with jinja template:

<p float='left'>
<img src='https://i.imgur.com/21Novy8.png' width='800'></p>

Another thing we can do here is, to add all the jinja template code to another file called `jobitem.html`, and add `{% include 'jobitem.html' %}` instead,  which should look something like this: 

![Imgur](https://i.imgur.com/bFe6jgU.png)


This is how we can structure our templates and extract reusable components from our code. 

Again, we can use BootStrap to add the Apply button and make our website look presentable. We can directly google or search in the bootstrap documentation for any functionality we want to add. 


### Adding API Route to Return JSON 



Another way to represent dynamic data is using API - Application Programming Interface. For this, instead of rendering a tempplate, we can simply call a JSON file. JSON is simply **JavaScript Objects**.  

For returning a JSON string, we will use the function `jsonify`, and instead of routing `('/')`, we will route `('/jobs')` and return our json string. We can do this with the help of a function. 

<img src='https://i.imgur.com/9hJM2fN.png' width='350'>

Now we have added another URL to our website, so if we go ahead and add extend /jobs on our home url we will be able to see: 

<img src='https://i.imgur.com/TFHPcCh.png' width='400'>

This is exactly what Rest API or JSON API stand for. i.e our webpage is not just returning html but the same information is accesible with JSON. 


We generally use the route: <img src='https://i.imgur.com/ZW7EqiT.png' width='200'> to differentiate this from html pages. 



### Deploying Project 

To put your website into production you need to figure out some cloud platform to deploy your website. We will be using https://render.com/ for deploying our websites. There are more platforms like AWS, Heroku, Google Cloud etc... but Render is very easy to work with. 

The first step is to head to the **Version Control** tab in the left sidebar to commit your work to GitHub. Like we saw earlier, we will simply write down the changes we made, and press Commit&Push.
  
<img src='https://i.imgur.com/c2zzVy0.png' width='300'>


**Note:** 
For those who weren't able to integrate and work with Flask earlier, now is the time to connect to github and integrate your changes. 

- We can head to https://render.com/ and create an account. Render provides a free plan to get started. 

- Once you have created an account you will be able to access a dashboard. Go ahead and press New+>WebService:
  <img src='https://i.imgur.com/p3MjzHM.png' width ='500'>

- Again, we need to connect to github. We need to allow render to pull our code fom github by clicking on 'Connect Account'. 
  <img src='https://i.imgur.com/rRayuos.png' width ='500'> 

- We will click on 'Connect' and now, we have to configure our code which is present on GitHub. For this, we need to provide the following details: 

**Name:** You can name it anything, its for internal reference.

**Enviroment:** python3

**Region:** It reflects where in the world the server is going to be. You might want to choose a place with less earthquakes😆. 

**Built Command:** The build command is an important piece of code/command that needs to run to keep track of the libraries that need to be installed to run your project. For this we create a `requirement.txt` file and add `Flask` to it.

  <img src='https://i.imgur.com/yhrJ9mr.png' width='500'>

  This is an accepted standard in the python ecosystem wherein we put our requirements in a `requirement.txt` file for our python project to run. 

  Another library we will add to our `requirement.txt` file is `gunicorn`. `gunicorn` is a helper library for Flask for production with python, you can look up for it. And then we can commint the changes. 

  So for our **build command** we can write: `pip install -r requirements.txt`


**Start Command:** For starting the server we will call `gunicorn`, the name of the file we want to be executed i.e `app:`, and then the name of the Flask app <img src='https://i.imgur.com/MQbRBZC.png' width='180'>which in our case is `app` itself. 


<img src='https://i.imgur.com/LNkbigl.png'>

This deployment process differs for each site. You can always look into the documention of the website you want to deploy your website in.

### Conecting a Domain 

To add a custom domain, you will need to buy a domain.


### References

- Render.com deployment docs: https://render.com/docs/deploy-flask
- Google Domains: https://domains.google.com/
- Heroku flask deployment: https://devcenter.heroku.com/articles/getting-started-with-python

### Important Links

- Wireframes: https://app.excalidraw.com/s/2NiSy9956hc/8ihFsZTCbBo
- Finished site: https://joviancareers.xyz

## Step 4 - Functional & Aesthetic Improvements

- Add a Navbar and Footer from Bootstrap
- Add `mailto:` links for the buttons
- Make the website mobile-friendly (responsive)
- Refactor templates into reusable components


You can go ahead and try the above steps with the help of bootstrap documentation. 

### References

- Bootstrap examples: https://getbootstrap.com/docs/5.2/examples/
- Mailto Link Generator: https://mailtolink.me/
- Mailto Link tutorial: https://www.freecodecamp.org/news/mailto-link-how-to-make-an-html-email-link-example-code/
- Bootstrap docs: https://getbootstrap.com/docs/5.2/getting-started/introduction/

- Replit Account: https://www.freecodecamp.org/news/how-to-use-replit/


## Future Work

- Create a page to show the details about the job (requirements etc.)
- Create a page to submit an application (instead of sending an email)
- Store information about jobs and applications in a cloud database
- Send email confirmation to candidate & Jovian admin after application
- Create an admin login interface to check submitted applications


jovian.commit(project='aakashns/web-development-with-python') 



jovian.commit(project='aakashns/web-development-with-python') 

