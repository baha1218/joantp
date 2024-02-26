import subprocess

def main():
    # URL du dépôt Git à cloner
    git_repo_url = "https://github.com/baha1218/joantp.git"

    # Cloner le dépôt Git
    subprocess.run(["git", "clone", git_repo_url])

    # Exécuter le script test.py
    subprocess.run(["python", "votre_depot/app.py"])

if __name__ == "__main__":
    main()