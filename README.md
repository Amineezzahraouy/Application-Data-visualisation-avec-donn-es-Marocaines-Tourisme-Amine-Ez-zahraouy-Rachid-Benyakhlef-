## Dashboard de Données Touristiques

Ce projet consiste en la création d'un tableau de bord interactif de données touristiques utilisant la bibliothèque Bokeh en Python. Le tableau de bord présente diverses visualisations basées sur des données touristiques marocaines, telles que les nuitées réalisées, la capacité hôtelière, les nationalités des touristes, et bien plus encore.

### Table des matières

- [Aperçu](#aperçu)
- [Données](#données)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Visualisations](#visualisations)
- [Contributeurs](#contributeurs)

### Aperçu

Le tableau de bord permet aux utilisateurs de visualiser différentes facettes du tourisme au Maroc. Les visualisations incluent des graphiques à barres, des diagrammes circulaires, et des cartes interactives, offrant une vue d'ensemble complète et détaillée des tendances touristiques.

### Données

Les données utilisées pour ce projet proviennent de plusieurs fichiers Excel contenant des statistiques sur le tourisme au Maroc. Ces fichiers incluent des informations sur les nuitées réalisées, la capacité hôtelière, les nationalités des touristes, les arrivées de touristes par ville, les recettes en devises, les guides touristiques, et les agences de voyages.

### Installation

Pour exécuter ce projet localement, veuillez suivre les étapes suivantes :

1. Clonez le dépôt :
    ```bash
    git clone https://github.com/votre-utilisateur/votre-repo.git
    cd votre-repo
    ```

2. Créez et activez un environnement virtuel (facultatif mais recommandé) :
    ```bash
    python -m venv venv
    source venv/bin/activate # Sur Windows, utilisez venv\Scripts\activate
    ```

3. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

4. Assurez-vous que les fichiers de données sont placés dans le répertoire `data`.

### Utilisation

Pour lancer le tableau de bord, exécutez le script Python principal :
```bash
python dashboard.py
 ```

### Visualisations


## Nombre de Guides Touristiques par Langue

Ce graphe joue un rôle crucial dans notre application de données. Il offre une représentation visuelle claire de la diversité linguistique des guides touristiques au Maroc. Voici pourquoi ce graphique est important :

- **Visualisation de la diversité linguistique** : En un coup d'œil, les utilisateurs peuvent voir quelles langues sont les plus représentées parmi les guides touristiques. Cela aide à comprendre la capacité du pays à accueillir des touristes de différentes régions du monde, en offrant des services dans leur langue maternelle.

- **Informations stratégiques pour le tourisme** : Pour les autorités touristiques, ce graphique fournit des informations précieuses pour élaborer des stratégies de promotion et d'accueil. Par exemple, s'il y a une forte demande de guides parlant une langue spécifique, il pourrait être avantageux d'investir dans la formation de guides supplémentaires dans cette langue.

- **Prise de décision éclairée** : Les entreprises du secteur du tourisme peuvent utiliser ces données pour prendre des décisions éclairées sur la façon de mieux servir leur clientèle internationale. Par exemple, un hôtel peut décider d'offrir des services de conciergerie dans les langues les plus courantes parmi les guides touristiques, afin d'améliorer l'expérience des clients étrangers.

En résumé, ce graphique offre une vue d'ensemble essentielle de la diversité linguistique parmi les guides touristiques au Maroc, ce qui aide les acteurs du secteur du tourisme à mieux comprendre et répondre aux besoins des voyageurs internationaux.

## Nombre d'Agences de Voyages par Ville

Ce graphique revêt une importance capitale dans notre application de données pour plusieurs raisons :

- **Identification des centres touristiques** : En observant la répartition du nombre d'agences de voyages par ville, les utilisateurs peuvent rapidement identifier les principales destinations touristiques au Maroc. Les villes avec un grand nombre d'agences sont souvent des points d'entrée et des hubs pour les voyageurs.

- **Planification de voyages** : Pour les touristes en train de planifier leur voyage au Maroc, ce graphique offre des informations cruciales. Ils peuvent voir quelles villes offrent une infrastructure touristique plus développée, ce qui peut influencer leur itinéraire et leurs choix d'hébergement.

- **Analyse de marché pour les entreprises touristiques** : Les entreprises du secteur du tourisme peuvent utiliser ces données pour évaluer la concurrence et identifier les opportunités de marché. Par exemple, une compagnie aérienne pourrait décider d'ajouter des vols vers des villes avec un nombre d'agences de voyages plus élevé pour répondre à la demande.

- **Prise de décision pour les investissements touristiques** : Les autorités touristiques et les investisseurs peuvent utiliser ces données pour prendre des décisions éclairées sur l'allocation des ressources et des investissements. Par exemple, s'il y a une sous-représentation d'agences de voyages dans certaines régions potentiellement attractives, cela pourrait indiquer un besoin d'infrastructures touristiques supplémentaires.

En combinant la visualisation intuitive des données avec l'interactivité permettant d'afficher le nombre d'agences de voyages et le nom de la ville au survol, ce graphique devient un outil puissant pour comprendre et exploiter le paysage touristique du Maroc. Il fournit des informations stratégiques essentielles pour les touristes individuels, les entreprises du secteur et les décideurs politiques.

## Nuitées Réalisées par Destination

Ce graphique est d'une importance capitale pour notre application de données touristiques pour plusieurs raisons :

- **Analyse des tendances touristiques** : En affichant l'évolution des nuitées réalisées dans différentes destinations au fil des ans, ce graphique permet aux utilisateurs de comprendre les tendances touristiques globales. Ils peuvent observer quels endroits ont gagné en popularité au fil du temps et ceux qui ont peut-être vu une baisse de fréquentation.

- **Prévision et planification stratégique** : Les entreprises du secteur touristique peuvent utiliser ces données pour prévoir la demande future et planifier leurs opérations en conséquence. Par exemple, si une destination voit une tendance à la hausse des nuitées, les hôtels et les agences de voyages peuvent investir davantage dans cette région pour répondre à la demande croissante.

- **Évaluation de la performance** : Les destinations touristiques et les autorités locales peuvent évaluer l'efficacité de leurs initiatives de promotion et de développement touristique en examinant l'évolution des nuitées au fil du temps. Cela leur permet de prendre des décisions éclairées sur l'allocation des ressources et d'ajuster leurs stratégies si nécessaire.

- **Comparaison entre les destinations** : La possibilité de sélectionner différentes destinations dans la légende permet aux utilisateurs de comparer facilement l'évolution des nuitées entre différentes régions. Cela peut être utile pour les touristes qui cherchent à choisir leur prochaine destination de voyage ou pour les entreprises qui cherchent à identifier les marchés les plus prometteurs.

- **Identification des opportunités d'investissement** : Les investisseurs du secteur touristique peuvent utiliser ces données pour identifier les destinations en plein essor et les opportunités d'investissement potentielles. Par exemple, si une destination voit une augmentation constante des nuitées, cela pourrait indiquer un potentiel de croissance pour les entreprises touristiques locales.

En fournissant une vue d'ensemble claire et détaillée de l'évolution des nuitées dans différentes destinations au Maroc, ce graphique offre des informations précieuses pour les touristes, les entreprises du secteur touristique et les décideurs politiques. Il constitue un outil essentiel pour comprendre le paysage touristique du pays et prendre des décisions éclairées en matière de planification, de développement et d'investissement.

## Capacité Hôtelière par Catégorie

Ce diagramme circulaire revêt une grande importance dans notre application de données touristiques, d'autant plus qu'il est accompagné d'un filtre par année de 2012 à 2020. Voici pourquoi :

- **Analyse de la capacité hôtelière** : En fournissant une vue d'ensemble de la capacité hôtelière par catégorie d'hôtel, ce graphique permet aux utilisateurs de comprendre la répartition des lits disponibles, offrant ainsi un aperçu précieux de l'infrastructure touristique au fil du temps.

- **Suivi des tendances dans le temps** : Grâce au filtre par année, les utilisateurs peuvent observer comment la capacité hôtelière a évolué d'année en année. Cela leur permet de détecter des tendances à long terme, telles que l'expansion ou la réduction de la capacité dans certaines catégories d'hôtels, ce qui peut être indicatif des changements dans la demande touristique ou des stratégies de développement régional.

- **Identification des besoins et des opportunités** : En comprenant la répartition actuelle de la capacité hôtelière, les entreprises du secteur touristique, les décideurs politiques et les planificateurs urbains peuvent identifier les besoins non satisfaits ou les opportunités d'investissement. Par exemple, une forte demande dans une catégorie particulière d'hôtels peut signaler un potentiel d'expansion ou de développement dans ce segment de marché.

- **Planification stratégique** : En combinant ces données avec d'autres indicateurs économiques et touristiques, les utilisateurs peuvent élaborer des stratégies de développement touristique plus efficaces. Par exemple, une région où la capacité hôtelière dans la catégorie haut de gamme augmente rapidement peut décider d'orienter ses efforts de marketing vers les voyageurs à haut pouvoir d'achat.

- **Adaptation aux tendances du marché** : En suivant de près l'évolution de la capacité hôtelière dans différentes catégories, les acteurs du secteur peuvent s'adapter rapidement aux changements de comportement des voyageurs. Par exemple, une augmentation de la demande pour des hébergements de luxe peut inciter les investisseurs à développer de nouveaux complexes hôteliers haut de gamme.

En résumé, ce diagramme circulaire constitue un outil essentiel pour comprendre la dynamique de l'offre hôtelière dans différentes régions au fil du temps. En combinant une visualisation claire de la répartition actuelle de la capacité hôtelière avec la possibilité de suivre les tendances historiques, il permet aux utilisateurs de prendre des décisions éclairées en matière de développement touristique et d'investissement.

## Nationalité des Touristes

Ce graphique à barres montre la répartition des touristes par nationalité. Les utilisateurs peuvent voir quelles nationalités sont les plus représentées parmi les visiteurs du Maroc.

- **Analyse des Marchés Sources** : Le graphique permet d'identifier les principaux marchés sources de touristes. Cela aide à comprendre d'où viennent la majorité des visiteurs, ce qui est crucial pour le marketing ciblé et les initiatives de promotion touristique.

- **Stratégies de Marketing** : En sachant quelles nationalités sont les plus représentées, les agences touristiques peuvent adapter leurs campagnes publicitaires pour attirer encore plus de visiteurs de ces pays. Cela optimise les dépenses en marketing et améliore le retour sur investissement.

- **Planification des Services** : Les informations sur les nationalités aident les gestionnaires d'hôtels et d'autres services touristiques à adapter leurs offres. Par exemple, ils peuvent proposer des services linguistiques spécifiques ou des cuisines nationales populaires auprès de ces visiteurs.

- **Suivi des Tendances** : Ce graphique permet de suivre l'évolution des nationalités des touristes au fil du temps. Les variations peuvent indiquer des changements dans les préférences de voyage, l'impact des relations internationales ou des fluctuations économiques.

- **Diversification du Marché** : Identifier les nationalités moins représentées mais en croissance peut aider à diversifier les marchés touristiques. Cela réduit la dépendance à quelques pays et augmente la résilience du secteur touristique face aux chocs économiques ou politiques dans certains pays.

En somme, le graphique de la **Nationalité des Touristes** est un outil essentiel pour comprendre la composition démographique des visiteurs, orienter les stratégies de marketing, améliorer la planification des services et suivre les tendances du tourisme international au Maroc.

## Recettes en Devises

Le cadrant des **Recettes en Devises** affiche la somme totale des recettes touristiques en dirhams pour une période donnée.

- **Analyse des Tendances Économiques** : Le cadrant permet aux utilisateurs d'identifier les tendances économiques sur plusieurs années. En visualisant les recettes annuelles, les décideurs peuvent détecter des périodes de croissance ou de déclin et analyser les causes sous-jacentes.

- **Évaluation des Politiques Touristiques** : Les recettes en devises sont un indicateur clé de l'efficacité des politiques et des initiatives touristiques. En comparant les recettes annuelles, les responsables peuvent évaluer l'impact des stratégies mises en place pour attirer les touristes et augmenter les revenus.

- **Planification Stratégique** : La visualisation des recettes sur plusieurs années aide à la planification stratégique future. Les données historiques peuvent guider les projections financières, les investissements dans les infrastructures et les campagnes de marketing pour maximiser les revenus futurs.

- **Rapidité de l'Information** : En affichant les recettes de manière concise et claire, le cadrant offre une information rapide et facilement interprétable. Cela est crucial pour les présentations aux parties prenantes et pour la prise de décision rapide.

- **Transparence et Communication** : Le cadrant contribue à la transparence en fournissant des données économiques claires et accessibles. Il facilite la communication avec les investisseurs, les partenaires et le public, renforçant la confiance dans le secteur touristique.

En conclusion, le cadrant des **Recettes en Devises**, avec son filtre par année, est un outil essentiel pour l'analyse et la gestion des performances économiques du secteur touristique. Il permet une compréhension approfondie des tendances financières, soutient la prise de décisions stratégiques et améliore la transparence et la communication des résultats financiers.

## Contributeurs ##

**Amine Ez-zahraouy**
**Rachid Benyakhlef** 
