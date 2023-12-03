from forex_python.converter import CurrencyRates
import datetime

def convertisseur_de_devise():
    historique = []
    devises_personnalisees = {}

    try:
        while True:
            print("\n1. Convertir une somme")
            print("2. Ajouter une devise personnalisée")
            print("3. Voir l'historique")
            print("4. Quitter")
            
            choix = input("Choisissez une option (1/2/3/4) : ")

            if choix == "1":
                montant = float(input("Entrez le montant à convertir : "))
                devise_source = input("Entrez la devise source (par exemple, USD) : ").upper()
                devise_cible = input("Entrez la devise cible (par exemple, EUR) : ").upper()

                c = CurrencyRates()

                if devise_source in devises_personnalisees:
                    taux_de_change_source = devises_personnalisees[devise_source]
                else:
                    taux_de_change_source = c.get_rate(devise_source, "USD")

                if devise_cible in devises_personnalisees:
                    taux_de_change_cible = devises_personnalisees[devise_cible]
                else:
                    taux_de_change_cible = c.get_rate(devise_cible, "USD")

                resultat = montant * (taux_de_change_cible / taux_de_change_source)

                print(f"{montant} {devise_source} équivaut à {resultat:.2f} {devise_cible}")

                date_conversion = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                conversion = f"{date_conversion} : {montant} {devise_source} -> {resultat:.2f} {devise_cible}"
                historique.append(conversion)

            elif choix == "2":
                devise = input("Entrez le code de la nouvelle devise (par exemple, USD) : ").upper()
                taux = float(input(f"Entrez le taux de conversion pour {devise} par rapport à USD : "))
                devises_personnalisees[devise] = taux
                print(f"Devise {devise} ajoutée avec succès!")

            elif choix == "3":
                print("\nHistorique des conversions:")
                for i, conversion in enumerate(historique, start=1):
                    print(f"{i}. {conversion}")

            elif choix == "4":
                print("Au revoir!")
                break

            else:
                print("Choix non valide. Veuillez choisir une option valide.")

    except ValueError:
        print("Erreur : Veuillez entrer un montant valide.")
    except Exception as e:
        print(f"Erreur : Une erreur inattendue s'est produite - {e}")

convertisseur_de_devise()