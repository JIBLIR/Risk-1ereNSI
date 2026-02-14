# Risk
Jeu du risk par Descendre Violette ; Sueur Zélie ; Jefferski Clément ; Irdel Jean-Baptiste en Première NSI


<img width="1914" height="1076" alt="image" src="https://github.com/user-attachments/assets/1a8289ce-1171-4774-a853-09a0b9eb730a" />




## Cahier des charges 

### À realiser : 

Rendre l affichage plus intuitif en mettant sur le pays son nom le nombre de troupes et des images de troupes 

Rendre des bordures entre les pays pour differencier 

Rendu different si on possede un continent  

Faire un lien entre Bouton attaquer et la fonction attaquer 

Curseur de troupes quand on déploie et on attaque 

Faire un lien entre la liste qui contient le nom des joueurs et la couleur des boutons 

Réaliser une fonction avec une liste où il y a le nombre de cartes pour chaque joueur et aussi faire le lien avec un bouton 

Faire une liste avec tous les boutons pour modifier les couleurs facilement 

### Plusieurs fichiers : 

Fichier jeu / Fichier fonctions phases / Fichier images 

### Règles 

Obj : éliminer votre adversaire en capturant tous ses territoires ou en réalisant votre mission. 

Placer des fantassins sur les territoires stratégiquement 

Tour :  1. recevoir des régiments selon le nombre de territoires occupés (11 territoires = 3 nouveaux régiments ; 14 t = 4 nr ; 17 t = 5 nr) == fonction déploiement 

2. Attaquer : vous pouvez attaquer un territoire avec lequel vous partagez une frontière (terrestre ou maritime). L’attaque se fait que depuis un territoire. Si vous gagnez l’attaque, vous pouvez recommencer jusqu’à obtenir le territoire ou en attaquez un autre. Vous ne pouvez attaquer avec plus de 3 régiments et le territoire duquel vous attaquez ne peut être laissé sans au moins un régiment ! == fonction attaque 

3. Le défenseur choisit un ou deux régiments pour défendre son territoire pas plus. Contrairement à l’attaquant le défenseur peut utiliser tous les régiments présents sur son territoire, personne n’est contraint de monter la garde. == fonction défense 

Remarque : que vous soyez attaquant ou défenseur, plus vous lancer de dés plus vous avez de chance de gagner la bataille mais aussi de perdre des régiments. 

4. Lorsque les deux partis ont fait leur choix, les lancers de dés commencent simultanément. Un dé rouge pour chaque régiment attaquant et un dé bleu pour chaque régiment défenseur. 

5. Celui qui détient résultat de dé le plus élevé gagne. 

Si le dé de l’attaquant est supérieur, le défenseur perd un régiment sur le territoire attaqué. Si le dé du défenseur est supérieur, l’attaquant perd un régiment venant sur territoire attaquant. Si vous avez lancé un nombre différent de dés, les résultats les plus bas sont ignorés. En cas d’égalité, le défenseur l’emporte. L'attaquant ne peut pas perdre plus de deux régiments par jet de dés. Si le défenseur a encore au moins un régiment sur le territoire après l’attaque, les régiments attaquants survivants reviennent sur le territoire depuis lequel ils ont attaqué. Cependant l’attaquant peut attaquer de nouveau s’il le souhaite comme dit précédemment. La comparaison des dés se fait par pair :  

Un territoire est capturé lorsqu’il n’y a plus aucun régiment adverse dessus. 

Vous pouvez attaquer autant de fois que vous le voulez au cours d’un tour même si votre première attaque a échoué. 

Réfléchir si on attaque et défend avec plusieurs régiments 

6. Après avoir attaqué, vous pouvez déplacer des régiments stratégiquement pour défendre une zone ou attaquer. Ce n’est pas obligatoire. == fonction déplacement_strat 

### Carte du monde, système de tableau 

ex : on code les joueurs par un nombre joueur 1 : 1 etc... 

|1||2||3||2||1||3||1||2| 

|1||2||2||2||1||2||3||2| 

On fait des listes dans des listes : 

[[joueur1,19 troupes],[joueur2,15 troupes]] 

 

(Rappel : l’Alaska et le Kamchatka sont frontaliers !) 

 

Fonction carte_risk: 

Instancie les territoires de façon aléatoire et équilibré avec une liste pour chaque territoire dans lequel on instancie le numéro du joueur ainsi que le nombre de troupes équitablement 

 

### Système de continent, Récompense 

 

3 troupes par défaut 

Si case1 == joueur et case9 == joueur etc... : (exemple tt les cases d'Océanie) 

On récompense par plus de troupes 

 

### Fonction attaque : 

Entrer le numéro du territoire dont on attaque. 

Entrer le numéro du territoire que l’on attaque.  

Si le territoire n’est pas frontalier reposer la question. 

Lancers de dés. 

Changement du nombre de régiment selon si le défenseur perd ou gagne. 

Menu pour attaquer à nouveau ou changer les régiments de place donner le tour à l’autre joueur. 

 

### Système de dé  

 

Dé : fait en exo 

Carte fantassins / cavaliers / arti 

Fantassin = 1 régiment ; cavalier = 5 régiments ; artillerie = 10 régiments 

Fonction déploiement (troupe en plus) (JB) : 

Pour la fonction déploiement, il faut parcourir tout la liste map pour vérifier si le joueur possède tt les territoires du continent  

il faut ajouter des troupes en fonction des territoires occupés par le joueur (3 par défaut) 

Fonction attribution des territoires : 

Attribuer de façon croissante un territoire à chaque joueur : [[1],[2],[3],[4]] 

Puis mélanger la liste et attribuer équitablement des troupes : [[2,10],[1,10],[4,10],[3,10]] 

 

On pioche des cartes aléatoires en utilisant la méthode append pour entrer dans une liste ex : [1,] le joueur a un cavalier il pioche un arti, [1,3] ensuite il faut enlever les cartes quand le joueur les utilise (bonus et faire des bonus en fonction des territoires présents sur les cartes) 

 

### Système tour par tour 

 

- il y aura un bouton pour passer le tour (bonus : chaque joueur à sa couleur et l'interface change aussi en fonction)  

Bonus 

- régiments neutres au départ ou pas ? 

- je propose un système de fortification entre les territoires et si on attaque on a plus de probabilité de perdre des troupes ainsi on met l'accent sur la stratégie (contourner les lignes de fortifications) 

- IA par renforcement qui prend en input les données de la map et retourne en output le territoire à attaquer et depuis où il attaque ou alors des boucles si. 

- une seule carte (terre) mais en 3D (=relief montagne et tout = trop beau) 

- plusieurs dés 

 

## Démarche de projet :  

### Emergence de l’idée  

Que faut il résoudre  ?  

Le manque de stimulation intellectuel logique et l’élaboration de stratégies plus complexes pour réussir dans le monde tant professionnel que scolaire. 

A quels besoins faut il répondre ?  

Divertissement de l’utilisateur 

Développement d’un esprit logique et de stratégie 

Interactions avec la société 

 

Quelle production attendre ?  

Jeu de stratégie virtuel = programme pour simuler des attaques sur une carte selon les territoires occupés 

Quel public ? 

Des enfants aux adultes = 6 ans et + 

Outils et démarches : réflexion en groupe sur les centres d’intérêts, souhaits/envies de chacun qui a mené à la reprise d’un jeu de stratégie. Réunion élève-professeur. Recherche d’informations quant à la procédure à suivre afin de créer le jeu : rédiger un cahier des charges et une démarche de projet afin de clarifier et organiser nos idées. 

 

### Analyse de la situation  

Quel objectif atteindre :  

Réaliser un jeu et assurer son bon fonctionnement afin qu’il soit fluide et que l’utilisateur puisse décider de chacune de ses actions. 

Quelles ressources employer ?  

Tkinter 

Simulateur de code python (Geany) 

Quelles contraintes prendre en compte ?  

Difficulté concernant la partie interface graphique et la création de la carte. 

L’organisation des fonctions du jeu afin d’obtenir un programme fluide. 

Détermination des territoires frontaliers à celui sélectionné 

Quelles stratégies/pistes envisager ? 

Utilisation de fonctions imbriquées (une fonction qui appelle à la fin à une autre fonction) 

Programmation des territoires frontaliers manuellement (pas de fonction) 

Envisager d’utiliser une carte de fond à la place de l’interface graphique 

Utilisation de liste imbriquées pour l’attribution et la numérotation des territoires de la carte 

 

### Choix d’une stratégie 

Quel plan d’action adopter ? :  

Apprendre à créer une interface graphique pour pouvoir écrire l’algorithme en fonction de la carte de fond.  

S’accorde-t-il avec l’objectif ? 

Oui  

Est-il réaliste ? 

Oui  

Quel cahier des charges établir ? 

 

Quel contrat établir avec les élèves ? 

Outils et démarches : cahier des charges, contrat, fiche d’appréciation collective du projet  

### Montage et planification du projet 

Quelles sont les étapes (activités, productions attendues) ? 

Décider du format de la carte au brouillon pour que l’équipe puisse travailler en même temps sur l’interface graphique et l’algorithme. 

Réaliser la fonction carte et écrire l’algorithme des territoires frontaliers. 

Écrire les fonctions déploiement, attaque, menu en prenant en compte le fonctionnement de la fonction carte. 

Comment les organiser : acteurs (rôle, responsabilités), volume horaire pour chaque discipline ? 

Clément : programmeur de l’interface graphique – apprendre et réaliser l’interface graphique dans sa totalité (carte et affichage des menus) à 10 et plus 

JB : programmeur de l’algo et secrétaire - écrire les fonctions carte, déploiement, attaque, renforcement + écrire le document descriptif du projet à 10h ou plus 

Violette : programmeuse de l’algo et secrétaire – écrire la fonction menu et défense + l’algo sur la répartition des territoires frontaliers avec Zélie + aide pour interface graphique, rédiger la démarche de projet à 10h ou plus 

Zélie : programmeuse de l’algo et secrétaire – fonction disposition des fantassins + écrire l’algo sur la répartition des territoires frontaliers et le contrat de l’équipe et fiche d’appréciation collective du projet à 10h ou plus 

Comment les hiérarchiser ? 

Organisation du plus important au moins important : 

Cahier des charges 

Fonction carte et interface 

Fonction attaque et algo territoires frontaliers 

Fonction disposition des fantassins 

Fonction menu et défense 

Fiche contrat, document descriptif, fiche d’appréciation collective du projet 

Quelle évaluation prévoir ? 

Respecter de la répartition des tâches 

Entraide des élèves si la demande est formulée 

 

 

### Mise en œuvre du projet 

Comment suivre le projet ? 

Rédiger les documents administratifs puis suivre l’ordre des étapes pour la rédaction du jeu. 

Quels indicateurs de réussite choisir ? 

Objectif du projet réalisé 

 

Quelle régulation, quels ajustements apporter ? 

Comment garantir la cohérence entre la mise en œuvre et les objectifs ? 

Quelle aide individualisée apporter en terminale BEP ? 

 

### Bilan 

Comment évaluer le projet ? 

Comment évaluer les compétences développées par les élèves ? 

Comment rendre compte du projet : déroulement, résultats… ? 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

## Description algorithmique du code : 

Le jeu du risk est divisé en 4 phases, la phase de l’instanciation de la carte, le déploiement, l’attaque et le renforcement, notre but est d’établir 4 fonctions. 

  ### - Carte risk 

But : attribuer aléatoirement les territoires aux joueurs ainsi que leurs troupes en fonction du nombre de territoires et de nombre de troupe par joueur. Le but est que cette répartition se fasse de la façon équitable possible 

Définition des variables : 

La liste “map” est clé dans cette fonction, elle est représentée comme ceci, map = [[numéro du joueur possédant le territoire , nombre de troupes sur le territoire],	[...] ,	[numéro du joueur possédant le territoire, nombre de troupes sur le territoire] 

La liste “troupes” représente liste de troupes totales restantes au joueurs, elle est représentée comme ceci, troupes = [troupes totales restantes pour le joueur 1, ... ,troupes totales restantes pour le joueur n] 

1ère étape instanciation des territoires aléatoirement 

Nous utilisons d’abord une boucle pour attribuant dans un ordre croissant les territoires aux joueurs, qui sont ajoutés à la liste “map” puis nous mélangeons celle-ci à l’aide de random.suffle().  

2ème étape instanciation des troupes aléatoiremnet 

Nous utilisons une boucle tant que qui vérifie que tant qu’un élément de la liste “troupes” est supérieur à 0, une boucle pour se réalise ajoutant aléatoirement une troupe ou non à “l’élément nombre de troupes sur le territoire”  du joueur sélectionné et soustrayant de facto le résultat aléatoire à l’élément correspondant au joueur dans la liste “troupes”. 

Enfin on renvoi la liste “map”. 

### - Déploiement 

But : distribuer le nombre de troupes en fonctions du nombre de territoire et des continents occupés  

Définition des variables :  

La liste “map” 

La variable troupes qui correspond au nombre de troupes 

La variable “territoire_joueur” correspondant au nombre de territoires du joueur 

La variable “joueur” qui correspond au numéro du joueur 

1ère étape calcul du nombre de territoire 

On utilise une boucle qui parcoure tout les territoires de la carte et compte les territoires correspondant au joueur 

2ème étape calcul du nombre de territoire 

On accorde un bonus de 4 si le joueur occupe tout les territoires du continent pour cela on vérifie avec une boucle si, si tout les territoires allant de 1 à 4 sont occupés par le joueur avec la fonction all et une boucle pour 

On accorde un nombre de troupe général de 3, si le joueur à plus de 13 troupes, on lui accorde les troupes en utilisant la formule (troupes = nombre de territoire – 2) // 3 

A la fin on retourne la variable troupes.   

### - Attaque 

But : prend en entrée les territoires en combat et retourne les résultats 

Définition des variables :  

Territoire_attaque : correspond au numéro du territoire attaqué 

Territoire_attaquant : correspond au numéro du territoire attaquant 

troupe_attaquant : correspond au nombre de troupes du territoire attaquant 

troupe_attaque : correspond au nombre de troupes du territoire attaquée 

De_attaquant 1,2 et 3 : correspond au dé qui attaquent 

De_attaquant : liste qui prend tout les variables de_attaquant 1,2 et 3 

De_attaque  1 et 2  : correspond au dé qui sont attaqués 

De_attaque : liste qui prend tout les variables de_attaque 1 et 2 

Map : liste “map” 

De_max_attaque : le dé le plus grand attaqué 

De_max_attaquant : le dé le plus grand attaquant 

 

1ère étape instanciation des dés 

En fonction du nombre de troupes présents sur le territoire, le programme va choisir combien de dé sera utilisé on apparaît tout les dés dans des listes 

2ème étape combat 

En faisant une boucle pour parcourant plusieurs étapes, on prend le maximum des 2 listes, on enlève les éléments et on vérifie si le dé attaque et plus grand ou égal au dé attaquant, les troupes attaquant perdent 1 troupes et inversement. 

Aussi, si il n’y a plus de troupe	pour défendre, le programme donne le territoire au joueur attaquant 

3 ème application dans la liste map 

On change les résultats dans la liste map et on la retourne avec les résultats 

(il faudrait que le joueur puisse choisir le nombre de troupes à introduire si le territoire est gagné) 

 

### - Retranchement 

But : déplace une troupe d'un point a à b 

Définition des variables :  

Liste “map” 

Troupe retranche : correspond au nombre de troupes qui vont se déplacer 

Territoire a : correspond au territoire retranchant  

Territoire b : correspond au territoire retranche 

 

1 ère étape boucle si 

On fait une boucle si pour vérifier si l’on peut faire le retranchement, puis on ajoute la variable “troupe_retranche” au territoire b et on le soustrait au territoire a 

Enfin, on retourne la liste ”map” 

 

 

 

### - Fonction attaque : 

Entrer le numéro du territoire dont on attaque. 

Entrer le numéro du territoire que l’on attaque.  

Si le territoire n’est pas frontalier reposer la question. 

Lancers de dés. 

Changement du nombre de régiment selon si le défenseur perd ou gagne. 

Menu pour attaquer à nouveau ou changer les régiments de place donner le tour à l’autre joueur. 

 

Id attaque de vio : = plus simple mais voir si fonctionne aussi  

Quels sont les territoires frontaliers : affiche les territoires frontaliers asso à un nombre. L’utilisateur choisi un num 

Si le nul n’est pas dans la liste donne alors il faut reposer la question 

Si la liste dans la liste est pleine du même joueur alors on ajoute des régiments. 

 

Une image contenant carte, texte, atlas

Le contenu généré par l’IA peut être incorrect. 

 

 

 

 

 

 

 

 

 

 

 

Tableau de bord : 

Février :  

1 ère semaine  : brainstorming, sélection des idées, choix du Risk 

2 ème semaine : programmation des 2 premières phases 

3 eme semaine : programmation des 2 dernières phases 

4 eme semaine : amélioration des 4 phases 

 
