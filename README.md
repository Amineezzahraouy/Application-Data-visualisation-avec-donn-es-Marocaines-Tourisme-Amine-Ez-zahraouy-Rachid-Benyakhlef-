Dashboard de Données Touristiques

Ce projet consiste en la création d'un tableau de bord interactif de données touristiques utilisant la bibliothèque Bokeh en Python. Le tableau de bord présente diverses visualisations basées sur des données touristiques marocaines, telles que les nuitées réalisées, la capacité hôtelière, les nationalités des touristes, et bien plus encore.

Table des matières

Aperçu

Données

Installation

Utilisation

Visualisations

Contributeurs

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

1. Ce graphe joue un rôle crucial dans notre application de données. Il offre une représentation visuelle claire de la diversité linguistique des guides touristiques au Maroc. Voici pourquoi ce graphique est important :

2. Visualisation de la diversité linguistique : En un coup d'œil, les utilisateurs peuvent voir quelles langues sont les plus représentées parmi les guides touristiques. Cela aide à comprendre la capacité du pays à accueillir des touristes de différentes régions du monde, en offrant des services dans leur langue maternelle.

3. Informations stratégiques pour le tourisme : Pour les autorités touristiques, ce graphique fournit des informations précieuses pour élaborer des stratégies de promotion et d'accueil. Par exemple, s'il y a une forte demande de guides parlant une langue spécifique, il pourrait être avantageux d'investir dans la formation de guides supplémentaires dans cette langue.

4. Prise de décision éclairée : Les entreprises du secteur du tourisme peuvent utiliser ces données pour prendre des décisions éclairées sur la façon de mieux servir leur clientèle internationale. Par exemple, un hôtel peut décider d'offrir des services de conciergerie dans les langues les plus courantes parmi les guides touristiques, afin d'améliorer l'expérience des clients étrangers.

En résumé, ce graphique offre une vue d'ensemble essentielle de la diversité linguistique parmi les guides touristiques au Maroc, ce qui aide les acteurs du secteur du tourisme à mieux comprendre et répondre aux besoins des voyageurs internationaux.


Nombre d'Agences de Voyages par Ville

Ce graphique revêt une importance capitale dans notre application de données pour plusieurs raisons :

1. Identification des centres touristiques : En observant la répartition du nombre d'agences de voyages par ville, les utilisateurs peuvent rapidement identifier les principales destinations touristiques au Maroc. Les villes avec un grand nombre d'agences sont souvent des points d'entrée et des hubs pour les voyageurs.

2. Planification de voyages : Pour les touristes en train de planifier leur voyage au Maroc, ce graphique offre des informations cruciales. Ils peuvent voir quelles villes offrent une infrastructure touristique plus développée, ce qui peut influencer leur itinéraire et leurs choix d'hébergement.

3. Analyse de marché pour les entreprises touristiques : Les entreprises du secteur du tourisme peuvent utiliser ces données pour évaluer la concurrence et identifier les opportunités de marché. Par exemple, une compagnie aérienne pourrait décider d'ajouter des vols vers des villes avec un nombre d'agences de voyages plus élevé pour répondre à la demande.

4. Prise de décision pour les investissements touristiques : Les autorités touristiques et les investisseurs peuvent utiliser ces données pour prendre des décisions éclairées sur l'allocation des ressources et des investissements. Par exemple, s'il y a une sous-représentation d'agences de voyages dans certaines régions potentiellement attractives, cela pourrait indiquer un besoin d'infrastructures touristiques supplémentaires.

En combinant la visualisation intuitive des données avec l'interactivité permettant d'afficher le nombre d'agences de voyages et le nom de la ville au survol, ce graphique devient un outil puissant pour comprendre et exploiter le paysage touristique du Maroc. Il fournit des informations stratégiques essentielles pour les touristes individuels, les entreprises du secteur et les décideurs politiques.

Nuitées Réalisées par Destination

Cette série de graphiques montre l'évolution des nuitées réalisées dans différentes destinations touristiques au Maroc au fil des ans. Les utilisateurs peuvent sélectionner différentes destinations et années pour voir les tendances spécifiques.

Capacité Hôtelière par Catégorie

Ce diagramme circulaire illustre la capacité hôtelière classée par catégorie d'hôtel. Les utilisateurs peuvent voir la répartition des lits disponibles dans différentes catégories d'hôtels.

Nationalité des Touristes

Ce graphique à barres montre la répartition des touristes par nationalité. Les utilisateurs peuvent voir quelles nationalités sont les plus représentées parmi les visiteurs du Maroc.

Contributeurs

Amine Ez-zahraouy  

Rachid Benyakhlef
