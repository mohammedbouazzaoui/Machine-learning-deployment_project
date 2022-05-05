virtualenv venv
pip install Flask
pip install gunicorn

pip freeze

click==8.1.2
colorama==0.4.4
Flask==2.1.1
gunicorn==20.1.0
importlib-metadata==4.11.3
itsdangerous==2.1.2
Jinja2==3.1.1
MarkupSafe==2.1.1
Werkzeug==2.1.1
zipp==3.8.0



# API deployment

- Repository: `challenge-machine-learning-api-deployment`
- Type of Challenge: `Learning`
- Duration: `6 days`
- Deadline: `05/04/2022 04:30 PM` **(code)**
- Presentation: `05/05/2022 1:30 PM`
- Team challenge : Solo project

## Mission objectives

- Be able to deploy a machine learning model.
- Be able to create a Flask API that can handle a machine learning model.
- Deploy an API to Heroku.

## The Mission

The real estate company "ImmoEliza" is really happy about your data collection using web scrapping. Whenever a new property comes on the market, the question of how it should be priced naturally arises.

Now, the company asks you to create a machine learning model to predict prices on Belgium's real estate sales. "ImmoEliza" has hired you to build a tool that enables the company to predict property prices using linear regression.  

Take the dataset that was previously **scraped** and preprocess the data to be used with machine learning. 

In addition, they would like you to create an API to let their web-developers create a website around it.

Ideally, your API would ask a user to provide with information about a property (features) and return the estimated price using your model.


## Preparation

In any API use case the first thing to decide _(for each route)_, is the **input** and the **output** you want.
Your very first step will be to decide that.

### Input

The input of your API is:

*(Can be modified depending on your model's need.)*

```json
{
  "data": {
    "area": int,
    "property-type": "APARTMENT" | "HOUSE" | "OTHERS",
    "rooms-number": int,
    "zip-code": int,
    "land-area": Optional[int],
    "garden": Optional[bool],
    "garden-area": Optional[int],
    "equipped-kitchen": Optional[bool],
    "full-address": Optional[str],
    "swimming-pool": Optional[bool],
    "furnished": Optional[bool],
    "open-fire": Optional[bool],
    "terrace": Optional[bool],
    "terrace-area": Optional[int],
    "facades-number": Optional[int],
    "building-state": Optional[
      "NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"
    ]
  }
}
```

Don't forget to specify which parameters will be required or not.

The JSON input data must be acquired through a HTML form that you will create in Flask. Think to add a "validate" button that will generate the JSON.

### Output

Your JSON output should look something like that:
**(This is an example, you will need to decide the format of the prediction (float or string))**

```json
{
  "prediction": Optional[float],
  "error": Optional[str]
}
```

The output must be displayed in a pretty way in your interface.

Don't forget to provide an error if something went wrong (in this case, you can also provide an HTTP status code. For more information about that, check the [Flask documentation](https://flask.palletsprojects.com/en/2.0.x/errorhandling/#returning-api-errors-as-json) and the [status' code list](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status).)


### Must-have features

#### Step 1: Project preparation

- Create a folder to handle your project.
- Create a file `app.py` that will contain the code for your API.
- Create a folder `preprocessing/` that will contain all the code to preprocess your data.
- Create a folder `model/` that will contain your model.
- Create a folder `predict/` that will contain all the code to predict the price.

#### Step 2: Preprocessing pipeline

This python module will contain all the code to preprocess your data. Make sure to think about what will be the format of your data to fit the model.
Also, be sure to know which information HAVE to be there and which one can be empty (NAN).

In the `preprocessing/` folder:

- Create the `cleaning_data.py` file that will contain all the code that will be used to preprocess the data you will receive to predict a new price. (fill the NaN values, handle text data, etc...).
- This file should contain a function called `preprocess()` that will take a new house's data as input and return those data preprocessed as output.
- If your data doesn't contain the required information, you should return an error to the user.

#### Step 3: Fit your data

Fit your data to your model.

In the `predict/` folder:

- Create the `prediction.py` file that will contain all the code used to predict a new house's price.
- Your file should contain a function `train()` that will create and store the model and a function `predict()` that will take your preprocessed data as an input and return a price as output using your stored model.

#### Step 4: Create your API

In your `app.py` file, create a Flask API that contains:

- A route at `/` that accept:
  - `GET` request and return `"alive"` if the server is alive.
- A route at `/predict` that accept:
  - `POST` request that receives the data of a house in JSON format.
  - `GET` request returning a string to explain what the `POST` expect (data and format).

#### Step 5: Deploy your app on Heroku
Deploy your web app on Heroku using the requirements.txt file. You can use the following tutorial as a reference: [Deploying a Flask Application to Heroku](https://stackabuse.com/deploying-a-flask-application-to-heroku/) 

## Nice-to- have's:

- Try other regression models for your prediction. 
- Deploy your application using a docker image to Heroku. To deploy your API, using Docker:

  - Create a Dockerfile that creates an image with:
    - Ubuntu
    - Python 3.8
    - Flask
    - All the other dependencies you will need.
    - All the files of your project in an `/app` folder that you will previously create.
  - Create a `requirements.txt` file. 
  - Run your `app.py` file with Python.
  - Heroku will allow you to push your docker container on their server and start it.


## Deliverables

1. Pimp up the README file:
   - Description
   - Installation
   - Usage
   - (Visuals)
   - (Contributors)
   - (Timeline)
   - (Personal situation)
2. Your API is able to predict the price and is deployed on Heroku.
3. Pitch your project in 3 minutes. (NO SLIDES! DEMO ONLY!)

## Evaluation criteria

| Criteria       | Indicator                                                | Yes/No |
| -------------- | -------------------------------------------------------- | ------ |
| 1. Is complete | Your API works.                                          | [ ]    |
|                | The API is clear and the presentation is understandable. | [ ]    |
|                | README is pimped.                                        | [ ]    |
|                | Your model is trained and can predict a result.          | [ ]    |
|                | Your API is deployed on Heroku.              | [ ]    |
| 2. Is good     | The repo doesn't contain unnecessary files.              | [ ]    |
|                | You used typing.                                         | [ ]    |
|                | The presentation is clean.                               | [ ]    |


![You've got this!](https://media.giphy.com/media/YSTLV9MkR248Qvxjz3/giphy.gif)










#############################################################################


INPUT DATA IS COMING FROM THE immowebscraper app:


# Immo_Eliza_scraping

Immo_Eliza_scraping is a project intended to gather as much readable data as possible for the pseudo realestate company called ImmoEliza. With this project, we were tasked to gather field attributes from as many (~10000) houses in Belgium. Field attributes include information like locality, type of property, price, area, no. of rooms, no. of bathrooms etc.

The python file included here is written to scrap a website for such information/field attributes, convert them into a json object for each individual house and append it to a .CSV file.
Once we have a .CSV file the data is cleaned and converted to a readable dataset.

This data is exclusive to houses within Belgium, but can be changed given you have a source from which a list of links can be created for your needs.

## Installation

In order to run this program, make sure you have the python packages: Pandas, selenium and BeautifulSoup, json installed. If you do not wish to run this programme and simply want it to understand how the data was arrived at then these packages will not be necessary.


## Usage

This program is used to scrap for data regarding an online accessible server; primarily regarding housing but could be altered to work for similar purposes.
Once the Data is scrapped, a dataset is created in the form of a readable .CSV file.


## Contributors
This project was performed by Mohammed Bouazzaoui, Anzeem Arief and Mousumi Sen. You are welcome to append and make changes to the source code with intentions of making it more efficient or so for it to suit your needs. Please do create a branch and request for approvals before you make changes!
