# Importation de la bibliothèque pandas
import pandas as pd

# Charger le fichier CSV dans un DataFrame Pandas
df = pd.read_csv('ventes.csv')

# Afficher les 5 premières lignes du DataFrame pour vérifier que tout est correct
print(df.head())

# Vérifier les types de données de chaque colonne
print("\nTypes de données :")
print(df.dtypes)

# Ajouter une colonne "Chiffre_d_affaire" qui calcule le chiffre d'affaire pour chaque ligne
df['Chiffre_d_affaire'] = df['Ventes'] * df['Prix_Unitaire']
print("\nDataFrame après ajout de la colonne 'Chiffre_d_affaire' :")
print(df)

# Filtrer les données pour ne garder que les ventes du produit "Produit A"
produit_a = df[df['Produit'] == 'Produit A']
print("\nVentes pour le 'Produit A' :")
print(produit_a)

# Calculer le total des ventes par produit
ventes_par_produit = df.groupby('Produit')['Ventes'].sum()
print("\nVentes totales par produit :")
print(ventes_par_produit)

# Calculer le chiffre d'affaire total par produit
chiffre_affaire_par_produit = df.groupby('Produit')['Chiffre_d_affaire'].sum()
print("\nChiffre d'affaire total par produit :")
print(chiffre_affaire_par_produit)

# Sauvegarder le DataFrame modifié dans un nouveau fichier CSV
df.to_csv('ventes_modifiees.csv', index=False)
print("\nLes données modifiées ont été sauvegardées dans 'ventes_modifiees.csv'.")
