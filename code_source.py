from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/traiter_donnees', methods=['POST'])
def ma_fonction_backend():
    # 1. Récupérer les données envoyées par la page appelante
    donnees = request.get_json()
    nom = donnees.get('nom', 'Inconnu')
    
    # 2. Exécuter votre logique Python
    message_retour = f"Bonjour {nom}, j'ai bien reçu vos données !"
    
    # 3. Renvoyer la réponse au format JSON
    return jsonify({"reponse": message_retour, "statut": "succès"})

if __name__ == '__main__':
    app.run(debug=True)
