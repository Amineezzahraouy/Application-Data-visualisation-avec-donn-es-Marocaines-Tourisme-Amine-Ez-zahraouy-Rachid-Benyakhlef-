import pandas as pd
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, WheelZoomTool, BoxZoomTool, ResetTool
from bokeh.layouts import column
from bokeh.models import HoverTool, Legend
from bokeh.palettes import Category20
from bokeh.transform import factor_cmap
from math import pi
from bokeh.palettes import Category20c
from bokeh.models import CustomJS
from bokeh.transform import cumsum
from bokeh.layouts import column


base_path = "D:/TELECHARGEMENTS/Projet Tourisme/Module python/Module python/Projet Tourisme/"

nuitees_destination = pd.read_excel(base_path + 'evolution-nuitees-realisees-etablissements-hebergement-touristique-par-destination.xlsx')
capacité_hotélière = pd.read_excel(base_path + 'evolution-par-categorie-de-la-capacite-hoteliere-classee-en-lits.xlsx')
capacité_hotélière_destination = pd.read_excel(base_path + 'evolution-par-destination-de-la-capacite-hoteliere-classee-en-lits.xlsx')
nuitees_marché = pd.read_excel(base_path + 'evolution-par-marche-nuitees-realisees-etablissements-hebergement-touristique.xlsx')
touristes_arrivée_natio = pd.read_excel(base_path + 'evolution-par-nationalite-des-arrivees-des-touristes-aux-postes-frontieres.xlsx')
touristes_arrivée_ville = pd.read_excel(base_path + 'evolution-par-point-dentree-des-arrivees-des-touristes-aux-postes-frontieres.xlsx')
indicateurs_sectoriels_tourisme_data = pd.read_excel(base_path + 'indicateurs-sectoriels-tourisme.xlsx')
recettes_en_devises_data = pd.read_excel(base_path + 'recettes-en-devises.xlsx')
guides_data = pd.read_excel(base_path + 'annuaire-des-guides-touristiques-ministere-du-tourisme.xlsx')
agences_data = pd.read_excel(base_path + 'annuaire-des-agences-de-voyages-ministere-du-tourisme.xlsx')
liste_agences = pd.read_excel(base_path + 'liste-agences-de-voyages.xlsx')
liste_etablissements = pd.read_excel(base_path + 'liste-des-etablissements-hebergement-touristique-mt-2010.xlsx')

ND = nuitees_destination
CHC = capacité_hotélière
CHD = capacité_hotélière_destination
NM = nuitees_marché
TAN = touristes_arrivée_natio
TAV = touristes_arrivée_ville
IS = indicateurs_sectoriels_tourisme_data
RD = recettes_en_devises_data
G = guides_data
AGL = agences_data
AGC = liste_agences
E = liste_etablissements

# Nettoyage des données de langues
langues_separees = G['Langue '].str.split(r'[-,\s]+', expand=True).stack().reset_index(level=1, drop=True).rename('Langue')
langues_separees_df = G.drop('Langue ', axis=1).join(langues_separees)
langues_separees_df['Langue'] = langues_separees_df['Langue'].str.upper().str.strip()
langues_separees_df['Langue'].replace({'F': 'FR', 'RUSSE': 'RUS', 'RUSS': 'RUS'}, inplace=True)
langues_separees_df = langues_separees_df[langues_separees_df['Langue'].notna()]
langues_separees_df = langues_separees_df[langues_separees_df['Langue'] != 'TANGER']

# Compter le nombre de guides pour chaque langue
comptage_langues = langues_separees_df['Langue'].value_counts().sort_index()
source_langues = ColumnDataSource(data=dict(langues=comptage_langues.index.tolist(), nombres=comptage_langues.values.tolist()))

# Définir une palette de couleurs
palette = ["#c9d9d3", "#718dbf", "#e84d60", "#ddb7b1", "#e9a3c9", "#a6d854", "#ffd92f", "#66c2a5", "#fc8d62", "#8da0cb", "#e78ac3", "#a6d854"]

# Créer le diagramme à barres pour les langues
p_langues = figure(x_range=comptage_langues.index.tolist(), height=350, title="Nombre de guides touristiques par langue maîtrisée",
                   toolbar_location="above", tools="pan,box_zoom,wheel_zoom,reset", width=1000)

vbars = p_langues.vbar(x='langues', top='nombres', width=0.7, source=source_langues,
                       legend_field="langues", line_color='white', fill_color=factor_cmap('langues', palette=palette, factors=comptage_langues.index.tolist()))

# Ajouter des outils d'interaction
hover = HoverTool()
hover.tooltips = [("Langue", "@langues"), ("Nombre de guides", "@nombres")]
p_langues.add_tools(hover)

# Personnaliser l'apparence du graphique
p_langues.xgrid.grid_line_color = None
p_langues.y_range.start = 0
p_langues.xaxis.axis_label = "Langue"
p_langues.yaxis.axis_label = "Nombre de guides"
p_langues.title.align = "center"

# Configurer la légende
p_langues.legend.title = "Langues"
p_langues.legend.title_text_font_style = "bold"
p_langues.legend.label_text_font_size = '10pt'
p_langues.legend.location = "top_right"
p_langues.legend.orientation = "vertical"
p_langues.legend.click_policy = "hide"

# Activer les outils de zoom et de reset
wheel_zoom_langues = WheelZoomTool()
box_zoom_langues = BoxZoomTool()
p_langues.add_tools(wheel_zoom_langues, box_zoom_langues, ResetTool())
p_langues.toolbar.active_scroll = wheel_zoom_langues


# Créer un DataFrame avec les villes spécifiées
villes_specifiees = ['Casablanca', 'Marrakech', 'Rabat', 'Agadir', 'Tanger', 'Fès', 'Nador', 'Meknès', 'Témara', 'Oujda', 'Tetouan', 'Kénitra', 'Salé', 'Laayoune', 'Ouarzazate', 'El Jadida']
agences_par_ville = AGC[AGC['Nom_province'].isin(villes_specifiees)]
comptage_villes = agences_par_ville['Nom_province'].value_counts()
source_villes = ColumnDataSource(data=dict(villes=comptage_villes.index.tolist(), agences=comptage_villes.values.tolist()))

# Définir une palette de couleurs
palette = ["#c9d9d3", "#718dbf", "#e84d60", "#ddb7b1", "#e9a3c9", "#a6d854", "#ffd92f", "#66c2a5", "#fc8d62", "#8da0cb", "#e78ac3", "#a6d854", "#fdc086", "#beaed4", "#fdc086", "#ffff99"]

# Créer le diagramme à barres pour les villes
p_villes = figure(x_range=villes_specifiees, height=350, title="Nombre d'agences par ville",
                  toolbar_location="above", tools="pan,box_zoom,wheel_zoom,reset", width=1200)

vbars = p_villes.vbar(x='villes', top='agences', width=0.8, source=source_villes,
                      legend_field="villes", line_color='white', fill_color=factor_cmap('villes', palette=palette, factors=villes_specifiees))

# Ajouter des outils d'interaction
hover = HoverTool()
hover.tooltips = [("Ville", "@villes"), ("Nombre d'agences", "@agences")]
p_villes.add_tools(hover)

# Personnaliser l'apparence du graphique
p_villes.xgrid.grid_line_color = None
p_villes.y_range.start = 0
p_villes.y_range.end = max(comptage_villes) + 5
p_villes.xaxis.axis_label = "Ville"
p_villes.yaxis.axis_label = "Nombre d'agences"
p_villes.title.align = "center"

# Configurer la légende
p_villes.legend.title = "Villes"
p_villes.legend.title_text_font_style = "bold"
p_villes.legend.label_text_font_size = '10pt'
p_villes.legend.location = "top_center"
p_villes.legend.orientation = "horizontal"
p_villes.legend.click_policy = "hide"

# Activer les outils de zoom et de reset
wheel_zoom_villes = WheelZoomTool()
box_zoom_villes = BoxZoomTool()
p_villes.add_tools(wheel_zoom_villes, box_zoom_villes, ResetTool())
p_villes.toolbar.active_scroll = wheel_zoom_villes


#ND
# Données fournies sous forme de listes
x = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]

Agadir_Taghazout = [4558091, 5072974, 5137811, 4711215, 4902520, 5452994, 5898754, 6048411, 1861507]
Marrakech = [5821191, 6425896, 6546300, 5991167, 6121224, 7111152, 7873933, 8342980, 1791932]
Casablanca = [1565755, 1745824, 1734166, 1663124, 1806466, 1985841, 2052138, 2155528, 621974]
Tanger_Assilah = [886587, 943934, 953991, 937607, 996075, 1241293, 1352583, 1451707, 414361]
Rabat = [602709, 621367, 639535, 627437, 629910, 714900, 778865, 785490, 336567]
Fes = [643776, 769635, 832367, 724665, 682008, 945102, 1096721, 1117579, 253856]
Essaouira_Mogador = [399449, 473376, 487617, 419958, 413686, 461657, 511161, 556904, 176625]
Oujda_Saidia = [463404, 456099, 344105, 405401, 440102, 503141, 572931, 628424, 163829]
Al_Haouz = [94463, 86937, 181199, 269228, 518800, 625744, 657852, 702204, 112996]
El_Jadida_Mazagan = [309703, 360752, 374701, 378213, 349166, 350324, 352185, 350994, 97603]
Ouarzazate = [300869, 311646, 381217, 275268, 261633, 360967, 388233, 380000, 71629]
Meknes = [200878, 216746, 219062, 209534, 199457, 227197, 243856, 252715, 82908]

# Liste des provinces et leurs données
provinces = [
    ('Agadir-Taghazout', Agadir_Taghazout),
    ('Marrakech', Marrakech),
    ('Casablanca', Casablanca),
    ('Tanger-Assilah', Tanger_Assilah),
    ('Rabat', Rabat),
    ('Fès', Fes),
    ('Essaouira-Mogador', Essaouira_Mogador),
    ('Oujda-Saidia', Oujda_Saidia),
    ('Al Haouz', Al_Haouz),
    ('El Jadida-Mazagan', El_Jadida_Mazagan),
    ('Ouarzazate', Ouarzazate),
    ('Meknès', Meknes)
]

# Palette de couleurs pour les différentes lignes (utilisation de Category20)
colors = Category20[len(provinces)]

# Sortie vers un fichier HTML
output_file("evolution_villes.html")

# Création de la figure Bokeh avec une largeur ajustée
p = figure(title="Évolution des données de chaque ville de 2012 à 2020", 
           x_axis_label='Année', y_axis_label='Nombre de nuitées',
           plot_width=1200, plot_height=600,  # Ajustement de la largeur de la figure
           tools="pan,wheel_zoom,box_zoom,reset,hover,save",
           tooltips="@provinces: @value")

# Ajout de la courbe pour chaque ville, masquée par défaut
for i, (province, data) in enumerate(provinces):
    p.line(x, data, legend_label=province, line_width=2, color=colors[i], visible=False)

# Configuration des éléments du graphique
p.legend.title = 'Villes'
p.legend.location = 'top_left'
p.legend.click_policy = "hide"  # Permet de cliquer pour masquer/afficher les lignes




import pandas as pd
from math import pi
from bokeh.palettes import Category20c
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, HoverTool, Select, CustomJS
from bokeh.transform import cumsum
from bokeh.layouts import column

# Les données fournies
data = {
    'hotels': ['Hôtel 1*', 'Hôtel 2*', 'Hôtel 3*', 'Hôtel 4*', 'Hôtel 5*', 'Luxe', 
               'Résidences Hôtelières', 'Clubs Hôtels', 'Maisons d\'Hôtes', 'Autres*'],
    '2012': [13160, 14382, 28884, 41595, 28273, 4654, 14216, 18970, 20243, 15371],
    '2013': [14908, 14922, 29312, 43249, 28684, 4832, 15188, 19692, 22185, 19443],
    '2014': [15447, 15247, 30391, 44311, 28610, 4832, 17921, 19692, 23625, 22974],
    '2015': [15793, 16456, 30575, 45733, 30554, 5354, 19492, 19647, 26740, 24054],
    '2016': [16101, 16811, 31578, 47952, 32677, 5784, 21413, 20013, 28101, 25146],
    '2017': [16403, 16998, 32288, 49287, 34235, 6052, 22535, 20675, 29721, 26294],
    '2018': [16624, 17350, 33239, 50181, 34909, 6052, 24085, 20930, 30813, 27727],
    '2019': [16713, 17721, 34167, 51031, 36937, 6363, 24873, 20930, 31818, 28887],
    '2020': [16921, 18088, 34898, 51139, 37461, 6363, 25564, 20930, 32848, 30180]
}

df = pd.DataFrame(data)

# Création de la source de données initiale pour l'année 2020
df['angle'] = df['2020'] / df['2020'].sum() * 2 * pi
df['color'] = Category20c[len(df)]
source = ColumnDataSource(data=dict(hotels=df['hotels'], angle=df['angle'], color=df['color'], counts=df['2020']))

# Création du graphique à secteurs
p_hotel = figure(height=350, title="Capacité des hôtels en lits 2020", toolbar_location=None,
           tools="hover", tooltips="@hotels: @counts", x_range=(-0.5, 1.0))

p_hotel.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='hotels', source=source)

# Configuration de la légende et des autres propriétés du graphique
p_hotel.axis.axis_label = None
p_hotel.axis.visible = False
p_hotel.grid.grid_line_color = None

# Création du sélecteur d'années
select = Select(title="Année", value="2020", options=[str(year) for year in range(2012, 2021)])

# Callback JavaScript pour mettre à jour les données
callback = CustomJS(args=dict(source=source, df=df.to_dict('list'), p=p_hotel), code="""
    const data = source.data;
    const year = cb_obj.value;
    const angles = [];
    const counts = df[year];
    const total = counts.reduce((a, b) => a + b, 0);
    for (let i = 0; i < counts.length; i++) {
        angles.push(counts[i] / total * 2 * Math.PI);
    }
    data['angle'] = angles;
    data['counts'] = counts;
    source.change.emit();
    p.title.text = "Capacité en lits des hôtels en " + year;
""")
select.js_on_change('value', callback)

# Disposition des éléments dans la colonne
layout_H= column(select, p_hotel)

# Afficher le graphique en mode autonome
#output_file("hotels_pie_chart.html")

import pandas as pd
from bokeh.plotting import figure, show, output_file
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, HoverTool, Select, CustomJS, WheelZoomTool, PanTool, ResetTool
from bokeh.layouts import column
from bokeh.transform import factor_cmap, factor_mark
from math import pi

# Données fournies
capacite_data = {
    'provinces': ['Marrakech', 'Agadir-Taghazout', 'Casablanca', 'Tanger-Assilah', 'Fès', 'Ifrane', 
                  'Oujda-Saidia', 'Essaouira-Mogador', 'Ouarzazate', 'Rabat', 'Al Haouz', 'Meknès', 'El Jadida-Mazagan'],
    '2012': [56581, 34014, 14472, 8568, 7785, 6663, 7006, 5223, 6384, 5601, 3043, 3633, 2646],
    '2013': [59298, 34762, 14885, 9448, 8156, 8423, 7781, 5354, 6630, 5866, 3149, 3729, 2674],
    '2014': [60517, 37199, 15141, 10176, 9429, 8542, 7901, 5632, 6791, 5982, 3277, 4452, 2672],
    '2015': [64556, 37824, 15959, 10672, 9791, 8974, 7894, 5876, 6863, 5982, 5243, 4563, 2740],
    '2016': [67453, 38603, 18751, 11620, 10094, 9014, 7894, 6090, 6960, 6080, 5277, 4589, 2793],
    '2017': [69486, 38823, 18883, 12176, 10298, 9099, 9052, 6185, 7251, 6458, 5667, 4648, 2793],
    '2018': [71294, 38983, 20416, 12419, 10346, 9149, 9052, 6303, 7251, 6468, 5715, 4670, 2869],
    '2019': [73048, 40136, 21200, 13497, 10346, 9149, 9116, 6481, 7290, 6468, 5995, 4705, 2949],
    '2020': [73175, 40660, 21417, 14060, 10586, 9149, 9116, 8602, 7302, 6654, 5995, 4705, 2949]
}

nuitees_data = {
    'provinces': ['Marrakech', 'Agadir-Taghazout', 'Casablanca', 'Tanger-Assilah', 'Rabat', 'Fès', 
                  'Essaouira-Mogador', 'Oujda-Saidia', 'Al Haouz', 'El Jadida-Mazagan', 'Ouarzazate', 'Meknès'],
    '2012': [5821191, 4558091, 1565755, 886587, 602709, 643776, 399449, 463404, 94463, 309703, 300869, 200878],
    '2013': [6425896, 5072974, 1745824, 943934, 621367, 769635, 473376, 456099, 86937, 360752, 311646, 216746],
    '2014': [6546300, 5137811, 1734166, 953991, 639535, 832367, 487617, 344105, 181199, 374701, 381217, 219062],
    '2015': [5991167, 4711215, 1663124, 937607, 627437, 724665, 419958, 405401, 269228, 378213, 275268, 209534],
    '2016': [6121224, 4902520, 1806466, 996075, 629910, 682008, 413686, 440102, 518800, 349166, 261633, 199457],
    '2017': [7111152, 5452994, 1985841, 1241293, 714900, 945102, 461657, 503141, 625744, 350324, 360967, 227197],
    '2018': [7873933, 5898754, 2052138, 1352583, 778865, 1096721, 511161, 572931, 657852, 352185, 388233, 243856],
    '2019': [8342980, 6048411, 2155528, 1451707, 785490, 1117579, 556904, 628424, 702204, 350994, 380000, 252715],
    '2020': [1791932, 1861507, 621974, 414361, 336567, 253856, 176625, 163829, 112996, 97603, 71629, 82908]
}

capacite_df = pd.DataFrame(capacite_data)
nuitees_df = pd.DataFrame(nuitees_data)

# Mapping for province name corrections
province_corrections = {
    'Agadir+Taghazout': 'Agadir-Taghazout',
    'Essaouira': 'Essaouira-Mogador',
    'El Jadida': 'El Jadida-Mazagan',
    # Add more corrections if needed
}

# Apply corrections
capacite_df['provinces'] = capacite_df['provinces'].replace(province_corrections)
nuitees_df['provinces'] = nuitees_df['provinces'].replace(province_corrections)

# Keep only provinces present in both dataframes
common_provinces = set(capacite_df['provinces']).intersection(set(nuitees_df['provinces']))
capacite_df = capacite_df[capacite_df['provinces'].isin(common_provinces)]
nuitees_df = nuitees_df[nuitees_df['provinces'].isin(common_provinces)]

# Conversion des données pour les barres côte à côte
def get_combined_data(year):
    combined_data = []
    for index, row in capacite_df.iterrows():
        province = row['provinces']
        capacity = row[str(year)]
        nights = nuitees_df[nuitees_df['provinces'] == province][str(year)].values[0]
        rate = capacity / nights if nights != 0 else 0  # Calculate rate
        combined_data.append((province, 'Capacity', capacity, rate))
        combined_data.append((province, 'Nights', nights, rate))
    return combined_data

# Données initiales pour l'année 2020
initial_data = get_combined_data(2020)
source = ColumnDataSource(data=dict(x=[x[0] for x in initial_data],
                                    type=[x[1] for x in initial_data],
                                    counts=[x[2] for x in initial_data],
                                    rate=[x[3] for x in initial_data]))

# Liste des provinces et des types
provinces = list(capacite_df['provinces'])
types = ['Capacity', 'Nights']

# Couleurs pour chaque province
colors = [
    "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", 
    "#e377c2", "#7f7f7f", "#bcbd22", "#17becf", "#9edae5", "#ad494a", "#8c6d31"
]

# Création du graphique à barres côte à côte
p_DC = figure(x_range=provinces, height=600, width=1000, title="Capacité en lits et nuitées par destination en 2020",
           toolbar_location="above", tools="hover,pan,wheel_zoom,box_zoom,reset",
           tooltips=[("Type", "@type"), ("Nombre", "@counts"), ("Taux", "@rate{0.00%}")])

bars = p_DC.vbar(x='x', top='counts', width=0.7, source=source, line_color='white',
              fill_color=factor_cmap('x', palette=colors, factors=provinces))

p_DC .xgrid.grid_line_color = None
p_DC .y_range.start = 0
p_DC .xaxis.major_label_orientation = pi/4
p_DC .xaxis.axis_label = "Province"
p_DC .yaxis.axis_label = "Nombre"
p_DC .legend.title = "Type"
p_DC .legend.label_text_font_size = '10pt'
p_DC .legend.click_policy = "hide"  # Make legend interactive

# Adding Zoom and Pan tools
p_DC .add_tools(WheelZoomTool(), PanTool(), ResetTool())

# Creating JSON-serializable structures from DataFrames
capacite_json = capacite_df.to_dict(orient='list')
nuitees_json = nuitees_df.to_dict(orient='list')

# Création du sélecteur d'années
select_DC = Select(title="Année", value="2020", options=[str(year) for year in range(2012, 2021)])

# Callback JavaScript
callback = CustomJS(args=dict(source=source, capacite_json=capacite_json, nuitees_json=nuitees_json), code="""
    const year = cb_obj.value;
    const data = source.data;
    const capacite = capacite_json[year];
    const nuitees = nuitees_json[year];
    const provinces = capacite_json['provinces'];

    data['x'] = [];
    data['type'] = [];
    data['counts'] = [];
    data['rate'] = [];

    for (let i = 0; i < provinces.length; i++) {
        let province = provinces[i];
        let capacity = capacite[i];
        let nights = nuitees[i];
        let rate = capacity / nights;

        data['x'].push(province);
        data['type'].push('Capacity');
        data['counts'].push(capacity);
        data['rate'].push(rate);

        data['x'].push(province);
        data['type'].push('Nights');
        data['counts'].push(nights);
        data['rate'].push(rate);
    }

    source.change.emit();
""")

# Ajouter le callback au sélecteur
select_DC.js_on_change('value', callback)

# Disposition de l'application
layout_DC = column(select_DC, p_DC)

from math import pi
import pandas as pd
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource, Select, CustomJS, HoverTool
from bokeh.plotting import figure
from bokeh.layouts import column
from bokeh.palettes import Category20c

# Vos données
data = {
    'nationalite': ['France', 'Espagne', 'Royaume-Uni', 'Allemagne', 'Italie', 
                    'Etats Unis', 'Belgique', 'Hollande', 'Maghreb', 'Chine', 'Scandinavie', 'MRE'],
    '2012': [1769710, 730882, 357347, 199349, 196186, 140045, 255290, 204767, 219280, 6899, 67165, 4363427],
    '2013': [1782056, 682834, 403325, 237852, 234912, 160033, 272593, 210859, 270227, 7871, 83999, 4722931],
    '2014': [1798190, 683761, 476550, 255124, 254209, 167267, 267308, 191158, 213675, 9403, 95193, 4845491],
    '2015': [1563568, 626896, 504475, 286328, 227961, 181468, 243815, 183349, 195214, 10515, 83554, 5025058],
    '2016': [1449757, 615720, 458561, 260255, 219334, 197858, 238984, 182379, 209823, 42844, 93009, 5228527],
    '2017': [1614011, 710729, 486262, 331185, 246312, 254531, 259658, 214016, 207885, 107434, 118460, 5484427],
    '2018': [1844397, 814069, 510516, 394328, 305505, 304960, 273535, 237539, 214295, 132081, 136157, 5609607],
    '2019': [1990813, 880818, 551499, 413384, 351916, 346702, 272328, 241065, 227281, 141050, 104264, 5889254],
    '2020': [412179, 200136, 113258, 79077, 57105, 54103, 40603, 40909, 49240, 20529, 22119, 1369808]
}

df = pd.DataFrame(data)

# Calcul des angles de départ et de fin pour chaque wedge
df['angle'] = df['2020'] / df['2020'].sum() * 2 * pi
df['color'] = Category20c[len(df)]

# Création du graphique à secteurs
p_nationalite = figure(height=500, title="Répartition des nationalités des visiteurs en 2020", toolbar_location=None,
                       tools="wheel_zoom,box_zoom,reset,hover", tooltips="@nationalite: @counts", x_range=(-0.55, 0.55))

# Ajout de chaque wedge individuellement pour un contrôle de légende individuel
start_angle = 0
for i in range(len(df)):
    end_angle = start_angle + df['angle'][i]
    source = ColumnDataSource(data=dict(start_angle=[start_angle], end_angle=[end_angle], color=[df['color'][i]], counts=[df['2020'][i]], nationalite=[df['nationalite'][i]]))
    p_nationalite.wedge(x=0, y=1, radius=0.4,
                        start_angle='start_angle', end_angle='end_angle',
                        line_color="white", fill_color='color',
                        legend_label=df['nationalite'][i],
                        source=source,
                        name=df['nationalite'][i])
    start_angle = end_angle

# Configuration de la légende et des autres propriétés du graphique
p_nationalite.axis.axis_label = None
p_nationalite.axis.visible = False
p_nationalite.grid.grid_line_color = None

# Configuration de la légende interactive
p_nationalite.legend.click_policy = "hide"

# Ajout d'un outil de survol pour afficher les informations des touristes
hover = HoverTool(tooltips=[("Nationalité", "@nationalite"), ("Nombre de touristes", "@counts")])
p_nationalite.add_tools(hover)

# Création du sélecteur d'années
select_year = Select(title="Année", value="2020", options=[str(year) for year in range(2012, 2021)])

# Callback JavaScript pour mettre à jour les données
callback = CustomJS(args=dict(df=df.to_dict('list'), p=p_nationalite), code="""
    const year = cb_obj.value;
    const counts = df[year];
    const total = counts.reduce((a, b) => a + b, 0);
    let start_angle = 0;

    for (let i = 0; i < counts.length; i++) {
        const wedge = p.renderers[i];
        const angle = counts[i] / total * 2 * Math.PI;
        wedge.glyph.start_angle = {value: start_angle};
        wedge.glyph.end_angle = {value: start_angle + angle};
        wedge.data_source.data['counts'] = [counts[i]];
        wedge.data_source.data['start_angle'] = [start_angle];
        wedge.data_source.data['end_angle'] = [start_angle + angle];
        wedge.data_source.change.emit();
        start_angle += angle;
    }

    p.title.text = "Répartition des nationalités des visiteurs en " + year;
""")
select_year.js_on_change('value', callback)

# Affichage
layout_nationalite = column(select_year, p_nationalite)
output_file("pie_chart_nationalities.html")





import pandas as pd
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource, Select, CustomJS, LegendItem, Legend
from bokeh.plotting import figure
from bokeh.layouts import column

# Données fournies
data = {
    'provinces': ['T.AIR', 'A Marrakech Ménara', 'A Mohammed V', 'A Agadir Almassira', 'A Tanger Ibn Battouta', 
                  'A Fes-Saiss', 'A Rabat-Salé', 'A Laaroui', 'A Oujda', 'A Essaouira', 
                  'A Ouarzazate', 'A Al Hoceima', 'T.MER', 'P Tanger Med', 'P Tanger', 
                  'P Nador', 'T.TERRE', 'T Bab Sebta', 'T Béni Anzar'],
    '2012': [6018566, 1704466, 2072133, 620892, 520313, 308680, 165599, 335068, 201287, 14192, 20692, 33036, 
             1941411, 1283665, 453297, 173138, 1415179, 955716, 423511],
    '2013': [6691449, 1945749, 2244025, 672779, 552301, 373996, 216177, 329741, 242308, 41167, 18355, 25674, 
             1993108, 1255511, 497551, 202191, 1361707, 927826, 400409],
    '2014': [6949937, 2127712, 2287427, 677415, 504430, 379615, 328844, 296864, 246585, 32073, 18076, 20047, 
             2036256, 1287987, 504139, 195402, 1296751, 886907, 372393],
    '2015': [6772274, 2018946, 2195330, 653281, 514425, 418920, 330339, 298765, 240298, 33075, 16895, 21655, 
             2113132, 1306118, 496452, 200662, 1291356, 879517, 381192],
    '2016': [6803955, 1836803, 2302466, 618100, 569166, 410869, 408442, 318942, 235559, 34593, 13411, 19360, 
             2198274, 1387661, 478478, 216609, 1329502, 899747, 395602],
    '2017': [7619256, 2039428, 2469405, 739447, 711604, 492418, 420603, 343139, 270977, 43933, 16720, 28481, 
             2482494, 1425155, 594654, 349342, 1247594, 865097, 348348],
    '2018': [8399533, 2554542, 2545734, 864229, 692511, 541353, 428196, 335032, 287256, 52265, 21630, 29194, 
             2471635, 1371880, 659795, 312585, 1417540, 992323, 383462],
    '2019': [9081490, 3093694, 2527306, 874336, 697941, 574188, 462914, 354843, 291963, 60559, 45003, 36656, 
             2320959, 1258640, 670513, 315461, 1529811, 1049168, 435843],
    '2020': [2265090, 657343, 716387, 194983, 190007, 162607, 104383, 117353, 69484, 19236, 10054, 6143, 
             293270, 179745, 64774, 42625, 219442, 157483, 49863]
}

df = pd.DataFrame(data)

# Séparer les données par catégorie
category_colors = {
    'T.AIR': 'red',
    'T.MER': 'blue',
    'T.TERRE': 'green'
}

# Mapper les couleurs pour chaque province
def get_color(province):
    if province == 'T.AIR' or province.startswith('A'):
        return category_colors['T.AIR']
    elif province == 'T.MER' or province.startswith('P'):
        return category_colors['T.MER']
    elif province == 'T.TERRE' or (province.startswith('T') and not province == 'T.AIR'):
        return category_colors['T.TERRE']
    else:
        return 'black'

# Ajouter la couleur aux données
df['color'] = df['provinces'].apply(get_color)

# Convertir les données pour chaque année en une source de données distincte
data_sources = {str(year): ColumnDataSource(data=dict(provinces=df['provinces'], counts=df[str(year)], color=df['color'])) for year in range(2012, 2021)}

# Créer une figure pour le graphique à barres horizontales
bar_chart = figure(y_range=df['provinces'], height=800, width=800, title="Nombre de touristes arrivés aux frontières marocaines par année",
                   toolbar_location=None, tools="")

# Ajouter des barres horizontales pour chaque catégorie
bars = bar_chart.hbar(y='provinces', right='counts', height=0.4, color='color', source=data_sources['2020'])

# Créer des glyphes invisibles pour chaque catégorie pour la légende
dummy_data = {'provinces': [''], 'counts': [0]}
dummy_source_air = ColumnDataSource(data=dict(provinces=[''], counts=[0], color=[category_colors['T.AIR']]))
dummy_source_mer = ColumnDataSource(data=dict(provinces=[''], counts=[0], color=[category_colors['T.MER']]))
dummy_source_terre = ColumnDataSource(data=dict(provinces=[''], counts=[0], color=[category_colors['T.TERRE']]))

dummy_bars_air = bar_chart.hbar(y='provinces', right='counts', height=0.4, color='color', source=dummy_source_air, visible=False)
dummy_bars_mer = bar_chart.hbar(y='provinces', right='counts', height=0.4, color='color', source=dummy_source_mer, visible=False)
dummy_bars_terre = bar_chart.hbar(y='provinces', right='counts', height=0.4, color='color', source=dummy_source_terre, visible=False)

# Configuration de la légende interactive
legend_items = [
    LegendItem(label='T.AIR', renderers=[dummy_bars_air]),
    LegendItem(label='T.MER', renderers=[dummy_bars_mer]),
    LegendItem(label='T.TERRE', renderers=[dummy_bars_terre])
]

legend = Legend(items=legend_items, location="center")
bar_chart.add_layout(legend, 'right')
bar_chart.legend.click_policy = "hide"

# Configuration des propriétés du graphique
bar_chart.ygrid.grid_line_color = None
bar_chart.xaxis.axis_label = "Nombre de touristes"
bar_chart.yaxis.axis_label = "Provinces"

# Création du sélecteur d'années
year_selector = Select(title="Année", value="2020", options=[str(year) for year in range(2012, 2021)])

# Callback JavaScript pour mettre à jour les données
callback = CustomJS(args=dict(data_sources=data_sources, bar_chart=bar_chart, bars=bars), code="""
    const year = cb_obj.value;
    const source = data_sources[year];
    bar_chart.y_range.factors = source.data['provinces'];
    bars.data_source.data = source.data;
    bar_chart.title.text = "Transport des touristes par type et par année " + year;
    bar_chart.change.emit();
""")
year_selector.js_on_change('value', callback)

# Disposition des éléments dans la colonne
layout_6 = column(year_selector, bar_chart)

# Sortie vers un fichier HTML
output_file("horizontal_bar_chart.html")

import pandas as pd
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource, Select, CustomJS, Div
from bokeh.layouts import column

# Données fournies
data = {
    'Année': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
    'Montant en MDHs': [56421.5, 58904, 57835, 57614, 62034, 61150, 64226, 72127, 73039, 78654, 36364]
}

df = pd.DataFrame(data)

# Convertir les données en une source de données
source_data = ColumnDataSource(data=dict(annee=df['Année'], montant=df['Montant en MDHs']))

# Créer une figure pour le cadran
montant_div = Div(text=f"""
<div style='display: flex; align-items: center; justify-content: center; height: 200px; border: 2px solid black;'>
    <h1 style='font-size:300%; color:black; text-align:center'>{df['Montant en MDHs'].iloc[-1]} MDHs</h1>
</div>
""", width=400, height=200)

# Création du sélecteur d'années
select_annee = Select(title="Année", value=str(df['Année'].iloc[-1]), options=[str(year) for year in df['Année']])

# Callback JavaScript pour mettre à jour les données
update_montant_callback = CustomJS(args=dict(source=source_data, div=montant_div), code="""
    const data = source.data;
    const year = cb_obj.value;
    const index = data['annee'].indexOf(parseInt(year));
    const montant = data['montant'][index];
    div.text = `
    <div style='display: flex; align-items: center; justify-content: center; height: 200px; border: 2px solid black;'>
        <h1 style='font-size:300%; color:black; text-align:center'>${montant} MDHs</h1>
    </div>
    `;
""")
select_annee.js_on_change('value', update_montant_callback)

# Disposition des éléments dans la colonne
layout_colonne = column(select_annee, montant_div)

# Sortie vers un fichier HTML
output_file("gauge_chart.html")

# Affichage du cadran


# Disposer les deux graphiques dans un tableau de bord
dashboard = column(p_langues,p, p_villes,layout_H,layout_DC, layout_nationalite,layout_6 ,layout_colonne)

# Afficher les graphiques dans le tableau de bord
output_file("dashboard.html")
show(dashboard)
