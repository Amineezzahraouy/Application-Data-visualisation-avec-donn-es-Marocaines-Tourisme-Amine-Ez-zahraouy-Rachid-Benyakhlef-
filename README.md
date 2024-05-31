Dashboard de Données Touristiques
Ce projet consiste en la création d'un tableau de bord interactif de données touristiques utilisant la bibliothèque Bokeh en Python. Le tableau de bord présente diverses visualisations basées sur des données touristiques marocaines, telles que les nuitées réalisées, la capacité hôtelière, les nationalités des touristes, et bien plus encore.

Table des matières
Aperçu
Données
Installation
Utilisation
Visualisations
Contributeurs
Licence
Aperçu
Le tableau de bord permet aux utilisateurs de visualiser différentes facettes du tourisme au Maroc. Les visualisations incluent des graphiques à barres, des diagrammes circulaires, et des cartes interactives, offrant une vue d'ensemble complète et détaillée des tendances touristiques.

Données
Les données utilisées pour ce projet proviennent de plusieurs fichiers Excel contenant des statistiques sur le tourisme au Maroc. Ces fichiers incluent des informations sur les nuitées réalisées, la capacité hôtelière, les nationalités des touristes, les arrivées de touristes par ville, les recettes en devises, les guides touristiques, et les agences de voyages.

Installation
Pour exécuter ce projet localement, veuillez suivre les étapes suivantes :

Clonez le dépôt :
git clone https://github.com/votre-utilisateur/votre-repo.git
cd votre-repo

Créez et activez un environnement virtuel (facultatif mais recommandé) :
python -m venv venv
source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`

Installez les dépendances :
pip install -r requirements.txt

Assurez-vous que les fichiers de données sont placés dans le répertoire data.

Utilisation
Pour lancer le tableau de bord, exécutez le script Python principal :
python dashboard.py

Le tableau de bord sera généré et ouvert dans votre navigateur par défaut.

Visualisations
Nombre de Guides Touristiques par Langue
Ce graphique à barres montre le nombre de guides touristiques par langue maîtrisée. Les langues sont listées sur l'axe des x et le nombre de guides sur l'axe des y. Les utilisateurs peuvent survoler les barres pour voir les valeurs exactes.

Nombre d'Agences de Voyages par Ville
Ce graphique à barres présente le nombre d'agences de voyages dans différentes villes du Maroc. Les villes sont listées sur l'axe des x et le nombre d'agences sur l'axe des y. Les utilisateurs peuvent interagir avec le graphique pour zoomer et explorer les données plus en détail.

Nuitées Réalisées par Destination
Cette série de graphiques montre l'évolution des nuitées réalisées dans différentes destinations touristiques au Maroc au fil des ans. Les utilisateurs peuvent sélectionner différentes destinations et années pour voir les tendances spécifiques.

Capacité Hôtelière par Catégorie
Ce diagramme circulaire illustre la capacité hôtelière classée par catégorie d'hôtel. Les utilisateurs peuvent voir la répartition des lits disponibles dans différentes catégories d'hôtels.

Nationalité des Touristes
Ce graphique à barres montre la répartition des touristes par nationalité. Les utilisateurs peuvent voir quelles nationalités sont les plus représentées parmi les visiteurs du Maroc.

Contributeurs
Amine Ez-zahraouy  
Rachid Benyakhlef
