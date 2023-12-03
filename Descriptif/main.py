from forex_python.converter import CurrencyRates
import datetime

def convertisseur_de_devise():
    historique = []

    try:
        montant = float(input("Entrez le montant à convertir : "))
        devise_source = input("Entrez la devise source (par exemple, USD) : ").upper()
        devise_cible = input("Entrez la devise cible (par exemple, EUR) : ").upper()

        c = CurrencyRates()

        taux_de_change = c.get_rate(devise_source, devise_cible)
        resultat = montant * taux_de_change

        print(f"{montant} {devise_source} équivaut à {resultat:.2f} {devise_cible}")

        # Sauvegarder l'historique
        date_conversion = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conversion = f"{date_conversion} : {montant} {devise_source} -> {resultat:.2f} {devise_cible}"
        historique.append(conversion)

        # Demander à l'utilisateur s'il souhaite voir l'historique
        voir_historique = input("Voulez-vous voir l'historique des conversions? (o/n): ").lower()
        if voir_historique == "o":
            print("Historique des conversions:")
            for i, conversion in enumerate(historique, start=1):
                print(f"{i}. {conversion}")

    except ValueError:
        print("Erreur : Veuillez entrer un montant valide.")
    except Exception as e:
        print(f"Erreur : Une erreur inattendue s'est produite - {e}")

# Appeler la fonction convertisseur_de_devise
convertisseur_de_devise()
