# Scraping boutique-parquet.com

Bienvenue sur notre version d'un projet de scraping dans le cadre d'une formation **Data Engineering Simplon 2025**.

Notre mission est de collecter les données d'un site de bricolage à des fins d'analyse.  


# 🎬 Mise en situation

Votre nouveau client, BricoSimplon, est un grand site de e-commerce spécialisé dans le bricolage et l'aménagement de la maison. Face à une concurrence accrue, BricoSimplon souhaite optimiser sa politique tarifaire pour rester compétitif et fidéliser sa clientèle. Pour ce faire, ils ont besoin de connaître en temps réel les tarifs pratiqués par leurs principaux concurrents.  


# 📌 Description du projet

- Concevoir et développer un système de scraping capable de collecter les données tarifaires sur une large gamme de produits.
- Assurer la conformité légale et éthique du processus de collecte, en respectant les conditions d'utilisation des sites web ciblés et en mettant en place des mesures pour éviter toute intrusion ou surcharge des serveurs.
- Nettoyer et structurer les données collectées pour garantir leur qualité et leur fiabilité.  


## 🛠️ Technologies Utilisées  
  
- Python
  
- Scrapy  


## 🚀 Mise en route  
  
### 📦 Installation  
  
```bash  
git clone https://github.com/thomas-lefloch/simplon-scraping.git
cd simplon-scraping
pip install -r requirements.txt
```  

## ⚙️ Configuration

La configuration du projet se fait via scraping/settings.py  


## 🧪 Comment lancer

Une fois les dépendences installées et la configuration validée, vous pouvez lancer le scraping comme suit:

```bash
python scrap_all.py 
```
Ce script scrape les catégories de produits, puis à partir des catégories obtenu scrape les produits associés.

Deux fichiers csv seront crées (ils seront écrasé s'ils existent déjà):   
```categories.csv```: contient toutes les catégories.  
```products.csv```: contient tous les produits.  

Pour modifier le nom de ces fichiers vous devez modifier le nom des spiders.  

## 🔢 Structure des fichiers csv créés

### categories.csv
Fichier d'extraction des catégories filtrées sur le site.

id (obligatoire): identifiant de la catégorie  
name (obligatoire): nom de la catégorie  
page_list (facultatif): url de la catégorie si celle-ci contient des produits  


### produits.csv
Fichier d'extraction des produits filtrés sur le site.

id (obligatoire) : Identifiant unique du produit qui est le SKU (obligatoire).  
name (obligatoire) : Nom du produit (obligatoire).  
base_price (facultatif) : Prix initial (hors promotion), en euros.  
price (obligatoire) : Prix actuel du produit (avec ou sans promotion), en euros (obligatoire).  
vat_included (obligatoire) : Indique si le prix inclut la TVA — (obligatoire).  
unit (facultatif) : Unité de mesure (ex : m², kg, unité, ml).  
url (obligatoire) : URL de la page du produit (obligatoire).  
category_id (obligatoire) : Identifiant de la catégorie associée.  
image (facultatif) : URL de l'image du produit.    


## 📜 License

This project is licensed under the MIT License ©️ 2025.  
You are free to use, modify, and distribute this project with proper attribution.  


## 👥 Team

Ce projet a été développé dans un but éducatif lors d'une formation chez Sinmplon par une équipe de 4 apprenants:

🔗 [Azhar Elbaghazaoui](https:github.com/Azhar-ELBAGHAZAOUI)  
🔗 [Thomas Le Floch](https://github.com/thomas-lefloch)  
🔗 [Laurent Jean-Alphonse]  
🔗 [Sébastien Dewaelle](https://github.com/cebdewaelle)  
