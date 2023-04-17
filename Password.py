import hashlib


def motDePasse(mdp, *call, mini=8, maxi=12):
    verification = [*call]
    if mini <= len(mdp) <= maxi:
        for lettre in mdp:
            for fct in verification:
                if fct(lettre):
                    verification.remove(fct)
            if not verification:
                return True
        return False
    else:
        return False


if __name__ == "__main__":
    mini = 8
    maxi = 12
    controle = True
    while controle:
        mdp = input("Mot de passe: ")
        if not motDePasse(mdp, str.islower, str.isupper, str.isdigit, lambda x: not x.isalnum(), mini=mini, maxi=maxi):
            print("""{} à {} caractères dont:
            . 1 minuscule
            . 1 majuscule
            . 1 chiffre
            . 1 caractère spécial""".format(mini, maxi))
            continue

        # Confirmation du mot de passe
        for i in range(2):
            confirm_mdp = input("Retapez le mot de passe: ")
            if mdp == confirm_mdp:
                # Hashage du mot de passe
                hashed_mdp = hashlib.sha256(mdp.encode()).hexdigest()
                controle = False
                print("Mot de passe validé et hashé: ", hashed_mdp)
                break
            else:
                print("Les mots de passe ne correspondent pas. Veuillez réessayer.")
        else:
            print("Recommencez intégralement la procédure")
