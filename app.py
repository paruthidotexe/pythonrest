from flask import Flask, render_template, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
import urllib
import urllib.parse
from urllib.request import urlopen
import json
from bs4 import BeautifulSoup

app = Flask(__name__)

## html pages
@app.route("/")
def home():
    return "Start Page"


def GetRecipeDetails(urlpath):
    print (urlpath)
    
    htmlFile = urlopen(urlpath)

    htmlContent = htmlFile.read()

    soup = BeautifulSoup(htmlContent, "html.parser")

    ingredients = soup.find("div", class_="heading")
    print(ingredients.h2.text)

    recipeDetails = soup.find("div", class_="recipe-detail-rating-block")
    cuisine = recipeDetails.find("ul", class_="pre-tags")
    print(cuisine.text)
    # print(cuisine.span.text)

    ingredients = soup.find_all("div", class_="ingredients")
    print (ingredients[0].h3.text)
    for curingredients in ingredients:
        if curingredients.ul:
            ingredientsList = curingredients.ul.find_all("li")
            if(ingredientsList):
                for li in ingredientsList:
                    print(li.text)

    ingredients = soup.find_all("div", class_="ingredients")
    print ("\n" + ingredients[1].h3.text)
    cookwareList = ingredients[1].find_all("a")
    for curCookware in cookwareList:
        print(curCookware.attrs['href'])

    #ingredients = soup.find_all("div", class_="recipe-steps")
    recipeSteps = soup.find_all("div", class_="step-detail")
    print ("\nStep by step")
    recipeSteps = recipeSteps[0].find_all("p")
    for curRecipeStep in recipeSteps:
        print(curRecipeStep.text)


if __name__ == '__main__':
    recipePaths = [
        'http://www.prestigesmartchef.com/recipe/view/italian-pasta-penne-allaarrabiata',
          "http://www.prestigesmartchef.com/recipe/view/chicken-tikka"
    ]
    for index in recipePaths:
        print ("----------------------------------------------------------------------------")
        GetRecipeDetails(index)
        print ("----------------------------------------------------------------------------")




