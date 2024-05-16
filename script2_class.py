
# from flask import Flask
# import requests

# app = Flask(__name__)

# @app.route("/bonjour/<prenom>")
# def hello_world(prenom):
#     return "hi " + prenom

# app.run(debug =True)




# @app.route("/pokemon existe/<nom>")
# def search_pokemon(nom)
# v=requests.get()
# json=v.json()
# p_name=json["name"]


# from flask import Flask, Response
# import requests
# import json

# app = Flask(__name__)

# @app.route("/pokemon_existe/<nom>")
# def search_pokemon(nom):
#     try:
#         url = f"https://pokeapi.co/api/v2/pokemon/{nom}"
#         response = requests.get(url)
#         response.raise_for_status()
#         data = response.json()
#         result = {"name": data["name"]}
#         return Response(json.dumps(result), mimetype='application/json')
#     except requests.exceptions.HTTPError:
#         error_message = {"error": "y a pas ce pok"}
#         return Response(json.dumps(error_message), status=404, mimetype='application/json')

# app.run(debug=True)



# @app.route('/Find/<univers>/<id>')
# def find(univers,id):
#     try:
#         if(univers == 'sw'):
#             try:
#                 donnees = requests.get('https://swapi.dev/api/people/'+id)
#                 json = donnees.json()
#                 name = json['name'];
#                 return name;
#             except:
#                 return 'Star Wars Id not found'
#         elif (univers == 'pk'):
#             try:
#                 donnees = requests.get('https://pokeapi.co/api/v2/pokemon/'+id);
#                 json = donnees.json();
#                 name = json['name'];
#                 return name;
#             except:
#                 return 'Pokemon Id not found'
#     except:
#         return 'Univers not found'
# app.run(debug = True)




class Voiture:
    def __init__(self, marque, modele, couleur):
        self.marque = marque
        self.modele = modele
        self.couleur = couleur

    def démarrer(self):
        print(f"La {self.marque} {self.modele} {self.couleur} démarre.")

    def freiner(self):
        print(f"La {self.marque} {self.modele} {self.couleur}freine.")




ma_voiture = Voiture("Toyota", "Corolla", "rouge")


ma_voiture.démarrer()
        




