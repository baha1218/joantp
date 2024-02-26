import subprocess

# Liste des scripts à cloner et exécuter
scripts = [
    "https://github.com/votre_nom/util_script_1.git",
    "https://github.com/votre_nom/util_script_2.git",
    # Ajoutez autant de scripts que vous le souhaitez
]

def main():
    # Pour chaque script dans la liste, clonez-le et exécutez-le
    for script in scripts:
        # Cloner le dépôt
        subprocess.run(["git", "clone", script])

        # Extraire le nom du script du lien GitHub
        script_name = script.split("/")[-1].split(".git")[0]

        # Exécuter le script cloné
        subprocess.run(["python", f"{script_name}/nom_du_script.py"])

if __name__ == "__main__":
    main()
