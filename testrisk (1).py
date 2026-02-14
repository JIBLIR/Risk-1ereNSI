import pygame
import sys
import random
from svgpathtools import svg2paths
from pathlib import Path

from tkinter import *
from pygame import mixer

# Dossier contenant le script et les ressources
DOSSIER_RESSOURCES = Path(__file__).parent

pygame.init()
mixer.init()

mixer.music.load(str(DOSSIER_RESSOURCES / "musique.mp3"))
mixer.music.play(loops=-1)


charger = False

def debut():

    def command2():
        cine = Tk()
        cine.title("Contextualisation")
        cine.geometry("1250x800")
        cine["bg"]="gray"

        canvas = Canvas(cine, width=1250, height=1100)
        canvas.configure(bg="gray")
        canvas.pack()

        canvas_t = canvas.create_text(10,10,text='',anchor=NW, font=("Arial",30))
        leTexte = "Bienvenue soldat,"
        delta = 75
        delay = 0

        for x in range(len(leTexte)+1):
            s = leTexte[:x]
            nv_text = lambda s=s: canvas.itemconfigure(canvas_t,text=s)
            canvas.after(delay,nv_text)
            delay += delta

        canvas_t2 = canvas.create_text(10,60,text='',anchor=NW, font=("Arial",30))
        Texte2 = "Vous le savez, le contexte géopolitique actuel est très complexe/tendu."

        for x in range(len(Texte2)+1):
            s = Texte2[:x]
            nv_text = lambda s=s: canvas.itemconfigure(canvas_t2,text=s)
            canvas.after(delay,nv_text)
            delay += delta

        canvas_t3 = canvas.create_text(10,110,text='',anchor=NW, font=("Arial",30))
        Texte3 = "Raison pour laquelle nous vous demandons d'accepter de prendre "


        for x in range(len(Texte3)+1):
            s = Texte3[:x]
            nv_text = lambda s=s: canvas.itemconfigure(canvas_t3,text=s)
            canvas.after(delay,nv_text)
            delay += delta

        canvas_t4 = canvas.create_text(10,160,text='',anchor=NW, font=("Arial",30))
        Texte4 = "part à ce conflit : nous vous nommons chef de l'ensemble des troupes."


        for x in range(len(Texte4)+1):
            s = Texte4[:x]
            nv_text = lambda s=s: canvas.itemconfigure(canvas_t4,text=s)
            canvas.after(delay,nv_text)
            delay += delta

        def command3():
            cc = 1
            if cc == 0:
                carte_simple(t, j)
            elif cc == 1:
                map_detaillee(t, j)
            return

        def accepter():
            print("hello")
            Texte5 = "Bien, c'est parti, revenez après victoire !!"
            label = Label(cine, text = Texte5, font=("Arial",36), bg="gray")
            label.pack()
            label.place(x=10,y=425)
            label.after(3000,command3) # + ouverture programme pygame
        


        ok = Button(cine, text="Accepter", font=("Arial",40),bg="gray",command=accepter)
        ok.pack()
        ok.place(x=450,y=240)


        cine.mainloop()

    def command1():
        f.destroy()
        command2()


    def para():
        p = Toplevel()
        p.title("Parametres")
        p.geometry("800x500")
        p.configure(bg="lightblue")

        troupe = Label(p,text="Nombre de troupes : ", font="Arial, 40", bg="lightblue")
        troupe.place(x=10,y=20)

        v1 = DoubleVar()
        s1 = Scale(p,variable=v1,from_=20,to=100,orient=HORIZONTAL,bg="#FFC90E")
        s1.pack()
        s1.place(x=600,y=35)

        nb_joueur = Label(p,text="Nombre de joueurs : ", font="Arial, 40", bg="lightblue")
        nb_joueur.place(x=10,y=120)

        v2 = DoubleVar()
        s2 = Scale(p,variable=v2,from_=2,to=4,orient=HORIZONTAL,bg="#FFC90E")
        s2.pack()
        s2.place(x=600,y=135)

        carte = Label(p,text="Choix de carte : ", font="Arial, 40", bg="lightblue")
        carte.place(x=10,y=220)

        choix = Listbox(p,width=17,height=2,bg="#FFC90E")
        choix.pack()
        choix.place(x=600,y=232)
        choix.insert(1,"carte facile")
        choix.insert(2,"carte détaillée")
        choix.selection_set(0)
        choix.activate(0)


        def my_upd():
            global t, j, cc
            t = s1.get()
            j = s2.get()
            c = choix.curselection()
            cc = c[0]
        my_upd()
            

        val = Button(p,text="Sauvegarder", font="Arial, 40", bg="#FFC90E",border=1, command=lambda:my_upd())
        val.pack()
        val.place(x=240,y=350)

    f = Tk()
    f.attributes("-fullscreen", True)
    f.title("Jouer")


    bg = PhotoImage(file=str(DOSSIER_RESSOURCES / "paysage.png"))
    label = Label(f,image = bg, cursor="tcross")
    label.place(x=-10,y=-10)

    bouton = Button(
        f, 
        text="Quitter", 
        font="Arial, 20",
        width=6,
        height=1,
        bg="#FFC90E",
        border=0,
        activebackground="yellow",
        cursor="plus",
        command=quit
        )
    bouton.pack()
    bouton.place(x=1810,y=15)

    bouton_jouer = Button(
        f, 
        text="Jouer", 
        font="Arial, 40",
        width=26,
        height=2,
        bg="#FFC90E",
        border=0,
        activebackground="yellow",
        cursor="cross",
        command = lambda: command2(),
        )
    bouton_jouer.pack()
    bouton_jouer.place(x=550,y=300)

    bouton_parametres = Button(
        f, 
        text="Parametres", 
        font="Arial, 40",
        width = 26,
        height = 2,
        bg="#FFC90E",
        border=0,
        activebackground="yellow",
        cursor="cross",
        command = para
        )
    bouton_parametres.pack()
    bouton_parametres.place(x=550,y=590)
    para()

    def enregistrement():
        global charger,init_map
        save = Tk()
        save.title("Charger une partie")
        save.geometry("800x300")
        save["bg"]="gray"

        fichier = open(str(DOSSIER_RESSOURCES / "sauvegarde_carte.txt"), "r")
        elements = []
        for ligne in fichier:
            elements.append(ligne)
        fichier.close()

        print(elements)
        j = int(elements[1][0])
        t = int(elements[2][0])

        s = elements[0].strip('[]')
        elements = s.split('], [')
        init_map = []
        for e in elements:
            nums = [int(x) for x in e.replace('[', '').replace(']', '').split(', ')]
            init_map.append(nums)
        print(type(init_map))
        print(init_map)
        charger = True

        bouton_save = Button(save,width=25,height=2,text="Repprendre la partie en cours",font=("Arial",40),border=0,bg="#FFC90E", command=lambda: command2())
        bouton_save.pack()
        bouton_save.place(x=10,y=75)

        save.mainloop()

    bouton_parties = Button(
        f, 
        text="Enregistrement", 
        font="Arial, 40",
        width = 13,
        bg="#FFC90E",
        border=0,
        activebackground="yellow",
        cursor="cross",
        command = enregistrement       
        )
    bouton_parties.pack()
    bouton_parties.place(x=950,y=475)

    def regles():
        regle = Tk()
        regle.title("Enregistrement")
        regle.geometry("1400x600")
        regle["bg"]="gray"

        TEXTE1 = "Trop Riské est un logiciel inspiré du jeu de société le Risk. Afin d’espérer gagner la partie, le joueur doit soit éliminer son adversaire en capturant tous ses territoires,"
        TEXTE2 = "soit en réalisant sa mission. Les deux joueurs peuvent voir leur mission l’un l’autre. Pour tenter de remporter la victoire, ils doivent donc faire preuve de stratégie afin" 
        TEXTE3 = "de gagner des territoires, mener à bien leur mission et empêcher leur adversaire de remplir la leur. Les joueurs ont 5 possibilités lorsqu’il s’agit de leur tour :"
        texte1 = Label(regle,text=TEXTE1,font=("Arial",14),bg="gray")
        texte1.pack()
        texte1.place(x=5,y=5)
        texte2 = Label(regle,text=TEXTE2,font=("Arial",14),bg="gray")
        texte2.pack()
        texte2.place(x=5,y=35)
        texte3 = Label(regle,text=TEXTE3,font=("Arial",14),bg="gray")
        texte3.pack()
        texte3.place(x=5,y=65)
        TEXTE4 = "- Vous pouvez piocher un possible bonus au cours de la partie. Lorsque vous possédez trois cartes d’un même territoire, vous obtenez des troupes supplémentaires."
        TEXTE5 = "- Vous pouvez déployer des troupes. Au début de chaque tour des troupes vous sont attribuées. Vous pouvez les disposer sur un ou plusieurs de votre territoires."
        TEXTE6 = "- Vous pouvez attaquer autant de fois que vous souhaitez. Lorsque la phase est sélectionnée, il faut choisir le pays attaquant puis le pays attaqué. Ensuite des dés"
        TEXTE7 = "  sont lancés et celui qui à le plus petit nombre perd des troupes à l’inverse de l’autre. Lorsqu’il n’y a plus de troupe sur un territoire, le territoire attaquant le possède."
        TEXTE8 = "- Vous pouvez choisir de renforcer votre positions en déplaçant des troupes dans le but d’attaquer ou de défendre stratégiquement leurs territoires."
        TEXTE9 = "- Vous pouvez passer votre tour en faisant défiler toutes les phases de jeu, le tour de jeu passe directement celui de l’adversaire."
        TEXTE10 = "Le jeu est terminé lorsque le message de victoire pour une équipe est affiché."
        texte4 = Label(regle,text=TEXTE4,font=("Arial",14),bg="gray")
        texte4.pack()
        texte4.place(x=5,y=95)
        texte5 = Label(regle,text=TEXTE5,font=("Arial",14),bg="gray")
        texte5.pack()
        texte5.place(x=5,y=125)
        texte6 = Label(regle,text=TEXTE6,font=("Arial",14),bg="gray")
        texte6.pack()
        texte6.place(x=5,y=155)  
        texte7 = Label(regle,text=TEXTE7,font=("Arial",14),bg="gray")
        texte7.pack()
        texte7.place(x=5,y=185)
        texte8 = Label(regle,text=TEXTE8,font=("Arial",14),bg="gray")
        texte8.pack()
        texte8.place(x=5,y=215)
        texte9 = Label(regle,text=TEXTE9,font=("Arial",14),bg="gray")
        texte9.pack()
        texte9.place(x=5,y=245) 
        texte10 = Label(regle,text=TEXTE10,font=("Arial",14),bg="gray")
        texte10.pack()
        texte10.place(x=5,y=275)       

        def fin():
            regle.destroy()

        bouton_regle = Button(regle,height=1,text="Revenir au menu",font=("Arial",40),border=0,bg="#FFC90E",command=fin)
        bouton_regle.pack()
        bouton_regle.place(x=450,y=400)

        regle.mainloop()       

    bouton_regles = Button(
        f, 
        text="Règles", 
        font="Arial, 40",
        width = 12,
        bg="#FFC90E",
        border=0,
        activebackground="yellow",
        cursor="cross",
        command = regles
        )
    bouton_regles.pack()
    bouton_regles.place(x=550,y=475)

    f.mainloop()

def map_detaillee(t,j):
    global charger, init_map
    # Charger le fichier SVG
    paths, attributes = svg2paths(str(DOSSIER_RESSOURCES / "risk5.svg"))

    SCALE_FACTOR = 1.7  # Ajustez ce facteur pour agrandir ou réduire la carte
    OFFSET_X = -400  # Décalage horizontal (négatif pour aller à gauche)
    OFFSET_Y = -200 

    def extract_polygon_points(path):
        points = []
        for segment in path:
            x = segment.start.real * SCALE_FACTOR + OFFSET_X
            y = segment.start.imag * SCALE_FACTOR + OFFSET_Y
            points.append((x, y))
        return points

    # Initialiser Pygame
    pygame.init()
    info = pygame.display.Info()
    screen_width = info.current_w
    screen_height = info.current_h

    screen = pygame.display.set_mode((screen_width, screen_height))# Exemple de dimensions plus grandes
    pygame.display.set_caption("Carte Risk")
    clock = pygame.time.Clock()

    # Couleurs des joueurs
    dico_couleurs = {
        1: (0, 0, 255),  # Bleu
        2: (255, 0, 0),  # Rouge
        3: (0, 100, 0),  # Vert
        4: (184,184,20),  # Jaune
    }

    dico_couleurs_sombre = {
        1: (25,25,112),  # Bleu
        2: (112,25,25),  # Rouge
        3: (7,62,24),  # Vert
        4: (128,128,0),  # Jaune
    }

    dico_couleurs_texte = {
        1: "Bleu",  # Bleu
        2: "Rouge",  # Rouge
        3: "Vert",  # Vert
        4: "Jaune",  # Jaune
    }

    couleur_texte = (255, 255, 255)  # Couleur du texte

    COULEUR_FOND = (0, 0, 0)
    screen.fill(COULEUR_FOND)

    # Paramètres du jeu
    nombre_de_joueur = j
    nombre_de_territoire = len(paths)
    nombre_troupe_debut = t

    # Liste des noms des pays (adaptée à 10 territoires comme dans le deuxième code)
    territoires_infos = [
        "Australie de l'Est", "Indonésie",
        "Nouvelle-Guinée","Alaska" , "Ontario","Territoires du Nord-Ouest",
        "Venezuela","Madagascar", "Afrique du Nord",
        "Groenland", "Islande" ,
        "Grande-Bretagne" ,"Scandinavie" ,
        "Japon", "Yakoutie","Kamchatka" , "Sibérie", "Oural",
        "Afghanistan", "Moyen-Orient",
        "Inde", "Siam", "Chine","Mongolie", 
        "Irkusk", "Ukraine",
        "Europe du Sud", "Europe de l'Ouest", 
        "Europe du Nord","Égypte" , "Afrique de l'Est", "Congo",
        "Afrique du Sud","Brésil" , "Argentine" ,"Est des États-Unis",
            "Ouest des États-Unis",
    "Québec", "Amérique Centrale","Pérou" ,"Australie de l'Ouest" ,
    "Alberta"
    ]


    voisins = {
        "Australie de l'Est": ["Indonésie", "Nouvelle-Guinée", "Australie de l'Ouest"],
        "Indonésie": ["Australie de l'Est", "Nouvelle-Guinée", "Australie de l'Ouest", "Siam"],
        "Nouvelle-Guinée": ["Australie de l'Est", "Indonésie"],
        "Alaska": ["Territoires du Nord-Ouest", "Alberta", "Kamchatka"],
        "Ontario": ["Territoires du Nord-Ouest", "Alberta", "Québec", "Est des États-Unis", "Ouest des États-Unis"],
        "Territoires du Nord-Ouest": ["Alaska", "Alberta", "Ontario", "Groenland"],
        "Venezuela": ["Brésil", "Pérou", "Amérique Centrale"],
        "Madagascar": ["Afrique de l'Est", "Afrique du Sud"],
        "Afrique du Nord": ["Égypte", "Afrique de l'Est", "Congo", "Brésil", "Europe de l'Ouest"],
        "Groenland": ["Territoires du Nord-Ouest", "Québec", "Islande"],
        "Islande": ["Groenland", "Grande-Bretagne", "Scandinavie"],
        "Grande-Bretagne": ["Islande", "Scandinavie", "Europe de l'Ouest", "Europe du Nord"],
        "Scandinavie": ["Islande", "Grande-Bretagne", "Europe du Nord", "Ukraine"],
        "Japon": ["Kamchatka", "Mongolie"],
        "Yakoutie": ["Kamchatka", "Irkusk", "Sibérie"],
        "Kamchatka": ["Alaska", "Japon", "Yakoutie", "Irkusk", "Mongolie"],
        "Sibérie": ["Yakoutie", "Irkusk", "Mongolie", "Chine", "Oural"],
        "Oural": ["Sibérie", "Chine", "Afghanistan", "Ukraine"],
        "Afghanistan": ["Oural", "Chine", "Inde", "Moyen-Orient", "Ukraine"],
        "Moyen-Orient": ["Afghanistan", "Inde", "Égypte", "Afrique de l'Est", "Europe du Sud", "Ukraine"],
        "Inde": ["Afghanistan", "Moyen-Orient", "Chine", "Siam"],
        "Siam": ["Indonésie", "Inde", "Chine"],
        "Chine": ["Sibérie", "Oural", "Afghanistan", "Inde", "Siam", "Mongolie"],
        "Mongolie": ["Japon", "Kamchatka", "Irkusk", "Sibérie", "Chine"],
        "Irkusk": ["Yakoutie", "Kamchatka", "Sibérie", "Mongolie"],
        "Ukraine": ["Scandinavie", "Oural", "Afghanistan", "Moyen-Orient", "Europe du Sud", "Europe du Nord"],
        "Europe du Sud": ["Moyen-Orient", "Ukraine", "Europe du Nord", "Europe de l'Ouest", "Égypte"],
        "Europe de l'Ouest": ["Grande-Bretagne", "Europe du Nord", "Europe du Sud", "Afrique du Nord"],
        "Europe du Nord": ["Grande-Bretagne", "Scandinavie", "Ukraine", "Europe du Sud", "Europe de l'Ouest"],
        "Égypte": ["Moyen-Orient", "Afrique du Nord", "Afrique de l'Est", "Europe du Sud"],
        "Afrique de l'Est": ["Égypte", "Afrique du Nord", "Congo", "Afrique du Sud", "Madagascar", "Moyen-Orient"],
        "Congo": ["Afrique du Nord", "Afrique de l'Est", "Afrique du Sud"],
        "Afrique du Sud": ["Congo", "Afrique de l'Est", "Madagascar"],
        "Brésil": ["Venezuela", "Pérou", "Argentine", "Afrique du Nord"],
        "Argentine": ["Brésil", "Pérou"],
        "Est des États-Unis": ["Ontario", "Ouest des États-Unis", "Québec", "Amérique Centrale"],
        "Ouest des États-Unis": ["Ontario", "Alberta", "Est des États-Unis", "Amérique Centrale"],
        "Québec": ["Ontario", "Est des États-Unis", "Groenland"],
        "Amérique Centrale": ["Venezuela", "Est des États-Unis", "Ouest des États-Unis"],
        "Pérou": ["Venezuela", "Brésil", "Argentine"],
        "Australie de l'Ouest": ["Australie de l'Est", "Indonésie"],
        "Alberta": ["Alaska", "Territoires du Nord-Ouest", "Ontario", "Ouest des États-Unis"]
    }

    # Police pour le texte
    font = pygame.font.Font(None, 36)
    font_name = pygame.font.Font(None, 1)  # Police pour les noms des pays
    font_number = pygame.font.Font(None, 25)  # Police pour les nombres de troupes

    # Boutons
    afficher_deployer = True
    afficher_attaquer = False
    afficher_renforcer = False
    bouton_deployer = pygame.Rect(500, 50, 160, 80)
    attaquer_bouton = pygame.Rect(500, 50, 160, 80)
    bouton_renforcer = pygame.Rect(500, 50, 160, 80)
    bouton_phase = pygame.Rect(900, 50, 250, 80)
    bouton_enregistrer = pygame.Rect(screen_width - 300, 10, 140, 50)
    curseur1 = pygame.Rect(400, 50, 80, 80)  # Diminuer troupes
    curseur2 = pygame.Rect(700, 50, 80, 80)  # Augmenter troupes

    bouton_quitter = pygame.Rect(screen_width - 150, 10, 140, 50)  # Position en haut à droite

    # Triangles pour curseurs
    triangle1 = [
        (400 + curseur2.width / 2 - 20, 50 + curseur2.height / 2),
        (400 + curseur2.width / 2 + 20, 50 + curseur2.height / 2 + 20),
        (400 + curseur2.width / 2 + 20, 50 + curseur2.height / 2 - 20)
    ]
    triangle2 = [
        (700 + curseur1.width / 2 + 20, 50 + curseur1.height / 2),
        (700 + curseur1.width / 2 - 20, 50 + curseur1.height / 2 + 20),
        (700 + curseur1.width / 2 - 20, 50 + curseur1.height / 2 - 20)
    ]

    # Classe pour gérer la carte et les territoires

    class Map():
        def __init__(self):
            
            self.territories = {}
            self.first_selected = None
            self.second_selected = None
            
        
        def add_territory(self, name, color, dim, font_size):
            self.territories[name] = Territory(self, name, color, dim, font_size)
        
        def draw(self):
            for territory in self.territories.values():
                territory.draw()

        def update_color(self, map):
            for i,territory in enumerate(self.territories.values()):
                new_owner_id = map[i][0]  
                territory.owner_id = new_owner_id  
                territory.update_color_territory(dico_couleurs[new_owner_id])

    # Extrait du code (remplacez uniquement la méthode draw dans la classe Territory)
    class Territory():
        def __init__(self, on_map:Map, name:str, color:tuple, dim:list, font_size:int):
            self.on_map = on_map
            self.name = name
            self.color = color
            self.font_size = font_number
            self.neighbors = voisins.get(name, [])
            self.isattacking = False
            self.isattacked = False
            self.owner_id = 0
            self.troups = 0
            self.index = len(on_map.territories)
            self.polygon_points = extract_polygon_points(paths[self.index])

        def draw(self):
            polygon = self.polygon_points
            if len(polygon) >= 3:
                pygame.draw.polygon(screen, self.color, polygon)
                if self.isattacking:
                    pygame.draw.lines(screen, (255, 0, 0), True, polygon, 5)
                    self.color = dico_couleurs_sombre[self.owner_id]
                
                else:
                    pass
                if self.isattacked:
                    pygame.draw.lines(screen, (255, 255, 255), True, polygon, 5)
                    self.color = dico_couleurs_sombre[self.owner_id]
                    
                else:
                    pass
                    
                pygame.draw.lines(screen, (0, 0, 0), True, polygon, 2)
                # Calculer le centroïde pour centrer le texte
                centroid = (sum(p[0] for p in polygon) / len(polygon), sum(p[1] for p in polygon) / len(polygon))
                # Afficher le nom du pays centré
                """name_text = font_name.render(self.name, True, (0, 0, 0))  # Texte principal en noir
                name_text_contour = font_name.render(self.name, True, (255, 255, 255))  # Contour blanc
                name_rect = name_text.get_rect(center=(centroid[0], centroid[1])) """ # Centré exactement au centroïde
                # Dessiner le contour
                """screen.blit(name_text_contour, name_rect.move(1, 1))
                screen.blit(name_text_contour, name_rect.move(-1, -1))
                screen.blit(name_text_contour, name_rect.move(1, -1))
                screen.blit(name_text_contour, name_rect.move(-1, 1))
                screen.blit(name_text, name_rect)"""
                # Afficher le nombre de troupes juste en dessous
                troupe_text = font_number.render(str(self.troups), True, (255, 255, 255))
                troupe_rect = troupe_text.get_rect(center=(centroid[0], centroid[1]))  # Décalage minimal pour lisibilité
                screen.blit(troupe_text, troupe_rect)
        def init_troups(self, owner_id:int, troups:int):
            self.owner_id = owner_id
            self.troups = troups

        def update_color_territory(self, new_color):
            self.color = new_color

    # Fon
    def carte_risk(nombre_de_joueur:int,nombre_de_territoire:int,nombre_troupe_debut:int)->list[list[int,int]]: 
        """attribue aléatoirement des territoires aux joueurs

        Args:
            nombre_de_joueur (int): nombre de joueurs
            nombre_de_territoire (int): nombre de territoire
            nombre_troupe_debut (int): troupes au départ

        Returns:
            list[list[int,int]]: liste contant les positions de depart des joueurs avec leur troupes
        """ 
        attribution = 0
        troupes = [nombre_troupe_debut] * nombre_de_joueur
        res = []

        for i in range(nombre_de_territoire):
            attribution += 1
            res.append([])
            res[i].append(attribution)
            res[i].append(1)
            troupes[res[i][0]-1] -= 1
            if attribution == nombre_de_joueur:
                attribution = 0
        random.shuffle(res)
                
        while any(troupe > 0 for troupe in troupes):
            for i in range(len(res)):
                if troupes[res[i][0] - 1] > 0:
                    troupe_a_retirer = random.randint(0, 1)
                    res[i][1] += troupe_a_retirer
                    troupes[res[i][0] - 1] -= troupe_a_retirer
        return res

    def deploiement(map,joueur):
        """calcule le nombre de troupes en fonction des territoires """
        territoire_joueur = 0
        troupes = 0
        for i in range(len(map)):
            if map[i][0] == joueur:
                territoire_joueur += 1

        if territoire_joueur > 13:
            troupes += (territoire_joueur-2) // 3
        else:
            troupes += 3
        
        amerique_du_sud = [6, 33, 34, 39] 
        controle_amerique_du_sud = True
        for idx in amerique_du_sud:
            if map[idx][0] != joueur:
                controle_amerique_du_sud = False
                break
        if controle_amerique_du_sud:
            troupes += 2  

    
        australie = [0, 1, 2, 40]
        controle_australie = True
        for idx in australie:
            if map[idx][0] != joueur:
                controle_australie = False
                break
        if controle_australie:
            troupes += 2  

        
        amerique_du_nord = [3, 4, 5, 9, 35, 36, 37, 38, 41]
        controle_amerique_du_nord = True
        for idx in amerique_du_nord:
            if map[idx][0] != joueur:
                controle_amerique_du_nord = False
                break
        if controle_amerique_du_nord:
            troupes += 5  

    
        afrique = [7, 8, 29, 30, 31, 32]
        controle_afrique = True
        for idx in afrique:
            if map[idx][0] != joueur:
                controle_afrique = False
                break
        if controle_afrique:
            troupes += 3 
    
        europe = [10, 11, 12, 25, 26, 27, 28]
        controle_europe = True
        for idx in europe:
            if map[idx][0] != joueur:
                controle_europe = False
                break
        if controle_europe:
            troupes += 5  

        asie = list(range(13, 25))
        controle_asie = True
        for idx in asie:
            if map[idx][0] != joueur:
                controle_asie = False
                break
        if controle_asie:
            troupes += 7  
        return troupes


    def attaquer_risk(map,territoire_attaque, territoire_attaquant, annexation=False):
        """ prend en entree les territoires en combat et retourne leur nombre de troupes respectifs"""
        troupe_attaquant = map[territoire_attaquant-1][1]
        troupe_attaque = map[territoire_attaque-1][1] 

        """print(f"les forces en présences : attaquants : {territoire_attaquant}ème territoire avec {troupe_attaquant} troupes")
        print(f"les forces en présences : attaqués : {territoire_attaque}ème territoire avec {troupe_attaque} troupes")
        """
        de_attaque = []
        if troupe_attaque >= 1 and troupe_attaque < 3:
            de_attaque1 = random.randint(0,6)
            de_attaque.append(de_attaque1)
        elif troupe_attaque >= 3: 
            de_attaque1 = random.randint(0,6)
            de_attaque2 = random.randint(0,6)
            de_attaque.append(de_attaque1)
            de_attaque.append(de_attaque2)
            
        de_attaquant = []
        if troupe_attaquant >= 2 and troupe_attaquant < 3:
            de_attaquant1 = random.randint(0,6)
            de_attaquant.append(de_attaquant1)
        elif troupe_attaquant >= 3 and troupe_attaquant < 4: 
            de_attaquant1 = random.randint(0,6)
            de_attaquant2 = random.randint(0,6)
            de_attaquant.append(de_attaquant1)
            de_attaquant.append(de_attaquant2)
        elif troupe_attaquant >= 4 :
            de_attaquant1 = random.randint(0,6)
            de_attaquant2 = random.randint(0,6)
            de_attaquant3 = random.randint(0,6)
            de_attaquant.append(de_attaquant1)
            de_attaquant.append(de_attaquant2)
            de_attaquant.append(de_attaquant3)
            
        
        
        '''print(f"dés attaquants : {de_attaquant}")
        print(f"dés attaqués : {de_attaque}")'''
        
        for i in range(len(de_attaque)):
            if (len(de_attaquant) > 0) and (troupe_attaquant > 0): 
                de_max_attaque = max(de_attaque)
                de_max_attaquant = max(de_attaquant)
                de_attaque.pop(de_attaque.index(de_max_attaque))
                de_attaquant.pop(de_attaquant.index(de_max_attaquant))
                if de_max_attaque >= de_max_attaquant:
                    troupe_attaquant -= 1
                else:
                    troupe_attaque -= 1
                    
        if troupe_attaque == 0:
                map[territoire_attaque-1][0] = map[territoire_attaquant-1][0]
                #print("le territoire attaqué est tombé")
                annexation = True
                
            
        map[territoire_attaquant-1][1] = troupe_attaquant 
        map[territoire_attaque-1][1] = troupe_attaque

        #print(f"finalement il reste : {troupe_attaquant} attaquants et {troupe_attaque} attaqués ")
        return map, annexation, troupe_attaque, troupe_attaquant

    def one_shot(map,territoire_attaque, territoire_attaquant):
        troupe_attaque = 1
        troupe_attaquant = 2
        while troupe_attaque > 0 and troupe_attaquant > 1:
            #print(troupe_attaquant,troupe_attaque)
            map,annexation, troupe_attaque,troupe_attaquant = attaquer_risk(map,territoire_attaque,territoire_attaquant)
        return map, annexation

    # Initialisation de la carte
    if charger == False:
        init_map = carte_risk(nombre_de_joueur, nombre_de_territoire, nombre_troupe_debut)
    my_map = Map()


    for i in range(nombre_de_territoire):
        nom = territoires_infos[i]
        # Couleur du joueur initialement propriétaire
        print(init_map)
        owner_id, nb_troupes = init_map[i]
        my_map.add_territory(nom, dico_couleurs[owner_id], 50,font_number)
        my_map.territories[nom].init_troups(owner_id, nb_troupes)
        

    # Variables pour gérer les actions
    annexation = False
    deploiement_balise = False
    renforcement = False
    troupe_a_deployer_initiale = 0
    troupe_initial = 0

    joueur = 1

    # Boucle principale
    running = True
    while running:
        screen.fill(COULEUR_FOND)

        # Dessiner la carte
        my_map.draw()

        pygame.draw.rect(screen, (200, 0, 0), bouton_quitter)
        text = pygame.font.Font(None, 36).render("Quitter", True, (255, 255, 255))
        screen.blit(text, text.get_rect(center=bouton_quitter.center))

        # Afficher les boutons selon la phase
        if afficher_deployer:
            pygame.draw.rect(screen, dico_couleurs[joueur], bouton_deployer)
            text = font.render("Déploiement", True, couleur_texte)
            screen.blit(text, text.get_rect(center=bouton_deployer.center))
            texte_a_afficher = font.render(f"Déploiement, vous avez {deploiement(init_map,joueur)} troupes joueur {dico_couleurs_texte[joueur]}", True, (255, 255, 255))
            screen.blit(texte_a_afficher, (0,0))

            texte_a_afficher = font.render(f"{troupe_a_deployer_initiale} troupes", True, (255, 255, 255))
            screen.blit(texte_a_afficher, (0,50))

            
        elif afficher_attaquer:
            pygame.draw.rect(screen, dico_couleurs[joueur], attaquer_bouton)
            text = font.render("Attaquer", True, couleur_texte)
            screen.blit(text, text.get_rect(center=attaquer_bouton.center))
        
        elif afficher_renforcer:
            pygame.draw.rect(screen, dico_couleurs[joueur], bouton_renforcer)
            text = font.render("Renforcer", True, couleur_texte)
            screen.blit(text, text.get_rect(center=bouton_renforcer.center))
            
        #Bouton pour enregistrer la carte 
        pygame.draw.rect(screen, dico_couleurs[joueur], bouton_enregistrer)
        text = font.render("Enregistrer", True, couleur_texte)
        screen.blit(text, text.get_rect(center=bouton_enregistrer.center))

        # Bouton pour changer de phase
        pygame.draw.rect(screen, dico_couleurs[joueur], bouton_phase)
        text = font.render("Changer de phase", True, couleur_texte)
        screen.blit(text, text.get_rect(center=bouton_phase.center))

        # Curseurs
        pygame.draw.rect(screen, (255, 255, 0), curseur1)
        pygame.draw.rect(screen, (255, 255, 0), curseur2)
        pygame.draw.polygon(screen, (0, 0, 0), triangle1)
        pygame.draw.polygon(screen, (0, 0, 0), triangle2)

        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos


                    # Vérifier si le bouton "Quitter" est cliqué
                if bouton_quitter.collidepoint(pos):
                        running = False
                        break  # Sortir immédiatement de la boucle d'événements            
                
                # enregister
                if bouton_enregistrer.collidepoint(pos):
                    print("Enregistrement de la carte...")
                    fichier = open(str(DOSSIER_RESSOURCES / "sauvegarde_carte.txt"), "w")
                    fichier.write(str(init_map))
                    fichier.write(str(nombre_de_joueur))
                    fichier.write(str(nombre_troupe_debut))
                    fichier.close()


                
                # Changer de phase
                if bouton_phase.collidepoint(pos):
                
                    if afficher_deployer:
                        afficher_deployer = False
                        deploiement_balise = False
                        afficher_attaquer = True
                        
                    elif afficher_attaquer:
                        afficher_attaquer = False
                        annexation = False
                        afficher_renforcer = True
                    
                    elif afficher_renforcer:
                        afficher_deployer = True
                        afficher_renforcer = False
                        renforcement = False

                        joueur += 1
                        if joueur > nombre_de_joueur:
                            joueur = 1
                        

                # Sélectionner un territoire
                for i, path in enumerate(paths):
                    polygon = extract_polygon_points(path)
                    if len(polygon) >= 3:
                        mask_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
                        pygame.draw.polygon(mask_surface, (255, 255, 255, 255), polygon)
                        if pos[0] < 0 or pos[1] < 0 or pos[0] >= screen_width or pos[1] >= screen_height:
                            continue  # Ignorer les clics en dehors de l'écran
                        if mask_surface.get_at(pos)[3] != 0:  # Vérifier si le clic est sur un territoire
                            territory = my_map.territories[territoires_infos[i]]
                            if my_map.first_selected == territory.name:
                                my_map.first_selected = None
                                territory.isattacking = False
                            elif my_map.first_selected is None and init_map[territoires_infos.index(territory.name)][0] == joueur:
                                my_map.first_selected = territory.name
                                index_a = territoires_infos.index(my_map.first_selected)
                                territory.isattacking = True
                            else:
                                if my_map.second_selected == territory.name:
                                    my_map.second_selected = None
                                    territory.isattacked = False
                                elif my_map.first_selected is not None:
                                    if (my_map.second_selected is None and ((init_map[territoires_infos.index(territory.name)][0] != joueur and (afficher_renforcer == False)) or ((afficher_renforcer == True) and (init_map[territoires_infos.index(territory.name)][0] == joueur))) and (afficher_deployer == False)) and ((( territory.name in my_map.territories[my_map.first_selected].neighbors) and (afficher_attaquer == True)) or afficher_renforcer == True):
                                        my_map.second_selected = territory.name
                                        index_b = territoires_infos.index(my_map.second_selected)
                                        territory.isattacked = True
                            break
                
                # Actions selon la phase
                if afficher_deployer and attaquer_bouton.collidepoint(pos) and my_map.first_selected:

                    for i, (territory_name) in enumerate(territoires_infos):
                            my_map.territories[territory_name].init_troups(*init_map[i])
                            
                    my_map.update_color(init_map)
                    my_map.first_selected = None
                    my_map.second_selected = None

                    for territory in my_map.territories.values():
                        territory.isattacking = False
                        territory.isattacked = False
                    if not deploiement_balise:
                        troupe_a_deployer_initiale = deploiement(init_map, joueur)
                    troupe_initial = init_map[index_a][1]
                    deploiement_balise = True


                if deploiement_balise and (curseur1.collidepoint(pos) or curseur2.collidepoint(pos)):
                        
                        if curseur1.collidepoint(pos) and init_map[index_a][1] > troupe_initial:
                                init_map[index_a][1] -= 1
                                troupe_a_deployer_initiale += 1
                        if curseur2.collidepoint(pos) and troupe_a_deployer_initiale > 0 :
                                init_map[index_a][1] += 1
                                troupe_a_deployer_initiale -= 1
                                    
                        for i, (territory_name) in enumerate(territoires_infos):
                                my_map.territories[territory_name].init_troups(*init_map[i])

                        my_map.update_color(init_map)






                if afficher_attaquer and my_map.first_selected and my_map.second_selected and init_map[index_a][1]>1:
                    
                    init_map, annexation = one_shot(init_map, index_b + 1, index_a + 1)

                    troupe_a_deployer_initiale_attaque = init_map[index_a][1]

                    if annexation == True:
                        init_map[index_a][1] -= 1
                        init_map[index_b][1] += 1

                    for i, (territory_name) in enumerate(territoires_infos):
                            my_map.territories[territory_name].init_troups(*init_map[i])
                    my_map.update_color(init_map)

                    
                    for territory in my_map.territories.values():
                        territory.isattacking = False
                        territory.isattacked = False

                    my_map.first_selected = None
                    my_map.second_selected = None

                    
                    

                if annexation and (curseur1.collidepoint(pos) or curseur2.collidepoint(pos)):
                    troupe_a_deployer_attaque = init_map[index_a][1]
                    if curseur1.collidepoint(pos) and troupe_a_deployer_attaque < troupe_a_deployer_initiale_attaque - 1:
                        init_map[index_a][1] += 1
                        init_map[index_b][1] -= 1
                    if curseur2.collidepoint(pos) and troupe_a_deployer_attaque > 1:
                        init_map[index_a][1] -= 1
                        init_map[index_b][1] += 1

                    for i, (territory_name) in enumerate(territoires_infos):
                        my_map.territories[territory_name].init_troups(*init_map[i])

                    my_map.update_color(init_map)

                    for territory in my_map.territories.values():
                        territory.isattacking = False
                        territory.isattacked = False

                    my_map.first_selected = None
                    my_map.second_selected = None


                

                if afficher_renforcer and my_map.first_selected and my_map.second_selected:
                    renforcement = True 

                    for territory in my_map.territories.values():
                            territory.isattacking = False
                            territory.isattacked = False


                if renforcement and (curseur1.collidepoint(pos) or curseur2.collidepoint(pos)):
        
                    if curseur2.collidepoint(pos) and init_map[index_a][1] > 1:
                            
                            init_map[index_a][1] -= 1
                            init_map[index_b][1] += 1

                    if curseur1.collidepoint(pos) and init_map[index_b][1] > 1:
                        
                            init_map[index_a][1] += 1
                            init_map[index_b][1] -= 1
                        

                    for i, (territory_name) in enumerate(territoires_infos):
                        my_map.territories[territory_name].init_troups(*init_map[i])
                    
                    my_map.update_color(init_map)

        if all(init_map[i][0]==joueur for i in range(len(init_map))):
            overlay = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))  
            screen.blit(overlay, (0, 0))
            text = font.render('Vous avez gagné !', True, (255,255,255))  # blanc
            text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
            screen.blit(text, text_rect)


        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()
    

debut()
