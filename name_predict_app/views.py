#!/usr/bin/env python3

from flask import Flask, render_template, url_for,	 request
import os
import pandas as pd
import numpy as np

def get_enriched_description(character):
    character_enriched = []
    for i in range(0,len(character)):
        character_enriched

    return character_enriched

def get_jaccard_sim(str1, str2):
    a = set(str1.replace(",","").split())
    b = set(str2.replace(",","").split())
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))


def name_predict_model(is_boy, is_girl, characters):
    df = pd.read_csv("name_predict_app/data/names_database_clean_v1.csv")


    if (is_boy == False) & (is_girl == True):
        df = df.loc[df.gender == 'girl']
    if (is_boy == True) & (is_girl == False):
        df = df.loc[df.gender == 'boy']

    df_traits = pd.read_csv("name_predict_app/data/traits_database_v1.csv")

    user_input = ''
    for trait_id in characters:
        user_input = user_input + df_traits["traits_enriched_stemmed"].iloc[trait_id] + " "

    result = pd.DataFrame(df[["name", "meaning", "bullshit_reduced"]],
                          columns=["name", "meaning", "bullshit_reduced", "jaccard_similarity"])
    result["jaccard_similarity"] = df["adj_and_nouns_enriched_stemmed"].apply(lambda x: get_jaccard_sim(x, user_input))
    result = result.sort_values(by=["jaccard_similarity"], ascending=False)[:15]
    result = result.reset_index()

    random_result_index = []
    while len(random_result_index) < 3:
        r = np.random.randint(0, 15)
        if r not in random_result_index: random_result_index.append(r)

    result = result.iloc[random_result_index]
    result = result.reset_index()

    return result


os.environ["APP_SETTINGS"] = "config.ProductionConfig"

app = Flask(__name__)

app.config.from_object(os.environ["APP_SETTINGS"])
app.secret_key = 'development key' # Flask_WTform CSFR protection

from .templates.includes.forms import Choose_Character_Form

@app.route("/", methods=('GET', 'POST'))
def index():
    form = Choose_Character_Form()

    if request.method == "POST":
        keylist = [("trait" + str(x)) for x in range(0, 5)]
        characters = [int(form.data[x]) for x in keylist]
        is_boy = form.data["boy"]
        is_girl = form.data["girl"]
        #print(characters)
        #print(is_boy)
        #print(is_girl)
        names = name_predict_model(is_boy, is_girl, characters)
        print(names)
        return render_template("name_prediction.html", predictions = names)

    return render_template("index.html", form = form)

@app.route("/essai")
def index2():
    form = Choose_Character_Form()

    if request.method == "POST":
        keylist = [("trait" + str(x)) for x in range(0,5)]
        characters = [int(form.data[x]) for x in keylist]
        is_boy = form.data["boy"]
        is_girl = form.data["girl"]
        print(int(form.data[trait4]))
        print(type(int(form.data[trait4])))
        print(characters)

        print(is_boy)
        print(is_girl)
        return render_template("index.html", form = form)

    return render_template("index.html", form = form)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/test1", methods=('GET', 'POST'))
def test1():
    form = AnswerForms()

    if request.method == "POST":
        keylist = [("word" + str(x)) for x in range(1,15)]
        student_answers = [form.data[x] for x in keylist]

        result = SaveTest(
            nom=str(dict(request.form)["nom"]),
            prenom=str(dict(request.form)["prenom"]),
            groupe=str(dict(request.form)["groupe"]),
            answer=[form.data[x] for x in keylist],
            exercice = 'Synthese 2A'
        )

        db.session.add(result)
        db.session.commit()
        app.logger.info(result.id)

        return render_template("answer1.html", prop = student_answers)

    else :
        return render_template("test1.html", form = form)

