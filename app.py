from fastapi import FastAPI

app = FastAPI()

# Liste des engins par catégorie


@app.get("/category/{category}")
def get_vehicles_by_category(category: str):
    # Implémentation pour récupérer les engins de la catégorie spécifiée
    vehicles = []  # Liste vide pour l'exemple

    return vehicles

# Liste des engins par propriétaire


@app.get("/owner/{owner}")
def get_vehicles_by_owner(owner: str):
    # Implémentation pour récupérer les engins du propriétaire spécifié
    vehicles = []  # Liste vide pour l'exemple

    return vehicles

# Facture imputée à un propriétaire


@app.get("/bills/{owner}")
def generate_bill(owner: str):
    # Implémentation pour générer la facture pour le propriétaire spécifié
    immatriculations = []  # Liste vide pour l'exemple
    cotation = 0.0
    majoration = 0.0
    total_amount = 0.0

    bill = Bill(immatriculations=immatriculations, cotation=cotation,
                majoration=majoration, total_amount=total_amount)
    return bill
