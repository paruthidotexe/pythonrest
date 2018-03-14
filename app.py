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

def PonsPrint(printType, printVal):
    if(printType == True):
        print(printVal)
    else:
        outputFilePath = "RecipeList.txt"
        outputFile = open(outputFilePath, "a")
        outputFile.write("\n")
        outputFile.write(printVal)
        outputFile.close()


def GetRecipeDetails(urlpath):
    PonsPrint (False, urlpath)
    
    htmlFile = urlopen(urlpath)

    htmlContent = htmlFile.read()

    soup = BeautifulSoup(htmlContent, "html.parser")

    ingredients = soup.find("div", class_="heading")
    PonsPrint(False,ingredients.h2.text)

    recipeDetails = soup.find("div", class_="recipe-detail-rating-block")
    cuisine = recipeDetails.find("ul", class_="pre-tags")
    PonsPrint(False,cuisine.text)
    # print(cuisine.span.text)

    ingredients = soup.find_all("div", class_="ingredients")
    PonsPrint(False, ingredients[0].h3.text)
    for curingredients in ingredients:
        if curingredients.ul:
            ingredientsList = curingredients.ul.find_all("li")
            if(ingredientsList):
                for li in ingredientsList:
                    PonsPrint(False,li.text)

    ingredients = soup.find_all("div", class_="ingredients")
    PonsPrint(False, "\n" + ingredients[1].h3.text)
    cookwareList = ingredients[1].find_all("a")
    for curCookware in cookwareList:
        PonsPrint(False,curCookware.attrs['href'])

    #ingredients = soup.find_all("div", class_="recipe-steps")
    recipeSteps = soup.find_all("div", class_="step-detail")
    PonsPrint(False,"\nStep by step")
    recipeSteps = recipeSteps[0].find_all("p")
    for curRecipeStep in recipeSteps:
        PonsPrint(False, curRecipeStep.text)

    PonsPrint (False, "\n----------------------------End of Recipe--------------------------------------\n")


if __name__ == '__main__':
    recipePaths = [
        'http://www.prestigesmartchef.com/recipe/view/italian-pasta-penne-allaarrabiata',
          "http://www.prestigesmartchef.com/recipe/view/chicken-tikka",
          "http://www.prestigesmartchef.com/recipe/view/shammi-kebab",
          "http://www.prestigesmartchef.com/recipe/view/hariyali-chicken-kadahi"
          
    ]
    
    outputFilePath = "RecipeList.txt"
    outputFile = open(outputFilePath, "w")
    outputFile.write ("\n----------------------------Automation START--------------------------------------\n")
    outputFile.close()

    for index in recipePaths:
        GetRecipeDetails(index)

    outputFile = open(outputFilePath, "a")
    outputFile.write ("\n-----------------------------Automation END---------------------------------------\n")
    outputFile.close()


