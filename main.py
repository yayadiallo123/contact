
import sqlite3 

class Contacts:
    
    def __init__(self):
        self.db_nom = 'contact.db'
        self.db_connecter()
        self.curseur.execute(''' 
                             CREATE TABLE IF NOT EXISTS Contacts
                             (id INTEGER PRIMARY KEY AUTOINCREMENT ,
                             nom TEXT NOT NULL UNIQUE , prenom TEXT UNIQUE,email varchar(200),numero INT(9), addresse TEXT)
                             
                             ''')
        self.db_fermer()
        
        
        
    def db_connecter(self):
            self.connection = sqlite3.connect(self.db_nom)
            self.curseur = self.connection.cursor()
        
    def db_fermer(self):
            self.connection.close()
            

    def ajouterContact(self,nom,prenom,email,numero,addresse):
        requette= f"INSERT INTO Contacts(nom,prenom,email,numero,addresse) VALUES('{nom}','{prenom}','{email}','{numero}','{addresse}')"
        #print(requette)
        self.curseur.execute(requette)
        self.connection.commit()
        
    def rechercher(self,nom):
        
        requette = f"SELECT * FROM Contacts WHERE nom = '{nom}' "
         
        resultat = self.curseur.execute(requette).fetchone()
        for r in resultat:
             print(r)
         
        return True if resultat else False
    
    def modifier(self,nom,numero):
         if self.rechercher(nom):
             
             requette = f"UPDATE Contacts SET numero = '{numero}' WHERE nom = '{nom}'"
             self.curseur.execute(requette)
             self.connection.commit()
             print(f" Le Nouveau numero : {numero} ")
         else:
             print("Erreur le Contact  n'existe pas")
             
             
    def afficher(self):
        requette=f" SELECT * FROM Contacts "
        contacts = self.curseur.execute(requette).fetchall()
        for c in contacts:
            print(f"{c[0]} -- {c[1]}-- {c[2]} -- {c[3]} -- {c[4]} -- {c[5]}")
        
    def supprimer(self,nom):
        if self.rechercher(nom):
            requette = f"DELETE FROM Contacts WHERE nom = '{nom}' "
            #print(requette)
            self.curseur.execute(requette)
            self.connection.commit()
        else:
            print("Erreur le contact n'existe pas")
              
        
        
        
        

contacts = Contacts()

try: 
    
    contacts.db_connecter()
    
    
    
    while True:
        cmd = input("Entrer une commande (+: Ajouter, r: Rechercher, m: Modifier, s: Supprimer, a: Afficher , q: Quitter) : ")
        print()
        if cmd == "+":
            nom= input("Entrer le contact : ")
            prenom=input(" le Prenom : ")
            email=input("le email :")
            numero=int(input(" le numero : "))
            addresse= input(" L' adresse : ")
            contacts.ajouterContact(nom,prenom,email,numero,addresse)
        
        elif cmd =="s":
            nom=input("Nom du contact a supprime : ")
            contacts.supprimer(nom)
        elif cmd == "a":
            contacts.afficher()
        elif cmd == "r":
            nom=input("Donner le nom: ")
            
            contacts.rechercher(nom)
            
                
            
            
        elif cmd == "m":
            nom = input(" Donner le nom : ")
            
            numero=int(input("Donner le nouveau numero : "))
            contacts.modifier(nom,numero)
            
            
        elif cmd == "q":
            break
        else:
            print("Commande invalide")
            
    
    #contacts.ajouterContact(nom="diallo",prenom="mamadou",email="mamadou@gmail.com",numero=778376970,addresse="Mbour")
    # contacts.ajouterContact(nom="diop",prenom="ousseynou",email="ouseynou@gmail.com",numero=778456567,addresse="Dakar")
    # contacts.ajouterContact(nom="fall",prenom="oumy",email="oumy@gmail.com",numero=55555555,addresse="thies")
   
    #contacts.afficher()
    #contacts.supprimer('diallo')
    #contacts.afficher()
    #contacts.modifier(77455667,"yaya")
    
    
except Exception as e:
    print("ERRREUR ", e)
finally:
    contacts.db_fermer()
   

