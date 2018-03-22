from flask import Flask, render_template, request, jsonify, make_response
from flask import send_file
from flask_sqlalchemy import SQLAlchemy
import urllib
import urllib.parse
from urllib.request import urlopen
import json
from bs4 import BeautifulSoup

app = Flask(__name__)

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
    PonsPrint (False, urlpath + "\n")
    
    htmlFile = urlopen(urlpath)

    htmlContent = htmlFile.read()

    soup = BeautifulSoup(htmlContent, "html.parser")

    ingredients = soup.find("div", class_="heading")
    recipeName = ingredients.h2.text
    PonsPrint(False,"Recipe : " + recipeName)

    recipeDetails = soup.find("div", class_="recipe-detail-rating-block")
    cuisine = recipeDetails.find("ul", class_="pre-tags")
    PonsPrint(False,cuisine.text)
    # print(cuisine.span.text)

    ingredients = soup.find_all("div", class_="ingredients")
    PonsPrint(False, ingredients[0].h3.text)
    curingredients = ingredients[0]
    if curingredients.ul:
        ingredientsList = curingredients.ul.find_all("li")
        if(ingredientsList):
            for li in ingredientsList:
                PonsPrint(False,li.get_text().strip())
    elif curingredients.ol:
        ingredientsList = curingredients.ol.find_all("li")
        if(ingredientsList):
            for li in ingredientsList:
                PonsPrint(False, li.get_text().strip())
    elif curingredients:
        ingredientsList = curingredients.find_all("div")
        if(ingredientsList):
            for li in ingredientsList:
                PonsPrint(False, li.get_text().strip())
        else:
            ingredientsListNew = curingredients.find_all("p")
            if(ingredientsListNew):
                for li in ingredientsListNew:
                    PonsPrint(False, li.get_text().strip())

    ingredients = soup.find_all("div", class_="ingredients")
    PonsPrint(False, "\n" + ingredients[1].h3.text)
    cookwareList = ingredients[1].find_all("a")
    if cookwareList:
        for curCookware in cookwareList:
            PonsPrint(False,curCookware.attrs['href'])
    else:
        cookwareListNew = ingredients[1].find_all("p")
        for curCookware in cookwareListNew:
            PonsPrint(False,curCookware.get_text().strip())

    #ingredients = soup.find_all("div", class_="recipe-steps")
    recipeSteps = soup.find_all("div", class_="step-detail")
    PonsPrint(False,"\nStep by step")
    recipeSteps = recipeSteps[0].find_all("p")
    for curRecipeStep in recipeSteps:
        PonsPrint(False, curRecipeStep.text.strip())

    recipeSteps = soup.find_all("div", class_="detail", id="chef-recips-title")
    for curRecipeStep in recipeSteps:
        PonsPrint(False, "\nChef : " + curRecipeStep.h4.get_text())

    recipeSteps = soup.find_all("div", id="divImage")
    for curRecipeStep in recipeSteps:
        imgTags = curRecipeStep.find_all("img", id="imgRecipe")
        for imgTag in imgTags:
            relativePath = imgTag["src"]
            fileExt = relativePath.rsplit(".")[-1:]
            if fileExt[0]:
                imgPath = urllib.parse.urljoin(urlpath, relativePath)
                urllib.request.urlretrieve(imgPath, recipeName + "." + fileExt[0])

    PonsPrint (False, "\n----------------------------End of Recipe--------------------------------------\n")


## html pages
@app.route("/")
def home():
    return "Start Page"

@app.route('/<path:filename>', methods=['GET', 'POST'])
def download(filename):    
    return send_file(filename)

if __name__ == '__main__':
    # recipePaths = [
    #     'http://www.prestigesmartchef.com/recipe/view/italian-pasta-penne-allaarrabiata',
    #       "http://www.prestigesmartchef.com/recipe/view/chicken-tikka",
    #       "http://www.prestigesmartchef.com/recipe/view/brownie-cake",
    #       "http://www.prestigesmartchef.com/recipe/view/veg-hakka-noodle",
    #       "http://www.prestigesmartchef.com/recipe/view/indian-cottage-cheese-with-fenugreek-paneer-methi",
    #       "http://www.prestigesmartchef.com/recipe/view/dum-aloo",
    #       "http://www.prestigesmartchef.com/recipe/view/shammi-kebab",
    #       "http://www.prestigesmartchef.com/recipe/view/hariyali-chicken-kadahi",
    #       "http://www.prestigesmartchef.com/recipe/view/reshmi-paneer-seekh",
    #       "http://www.prestigesmartchef.com/recipe/view/indian-cottage-cheese-with-fenugreek-paneer-methi",
    #       "http://www.prestigesmartchef.com/recipe/view/paneer-tikka"          
    # ]

    # recipePaths = [
    #       "http://www.prestigesmartchef.com/recipe/view/coconut-chicken-curry",
    # ]
    
    # outputFilePath = "RecipeList.txt"
    # outputFile = open(outputFilePath, "w")
    # outputFile.write ("\n----------------------------Automation START--------------------------------------\n")
    # outputFile.close()

    # for index in recipePaths:
    #     GetRecipeDetails(index)

    # outputFile = open(outputFilePath, "a")
    # outputFile.write ("\n-----------------------------Automation END---------------------------------------\n")
    # outputFile.close()

    app.run(debug=True, port=7777)

