# 📊 Schéma des Données - ESG & Carbon Analytics

Ce document décrit la structure complète des tables du jeu de données ESG.

---

## 📂 Vue d'ensemble

### Données Opérationnelles (4 tables)
- **sites** : Sites de production/bureaux avec localisation
- **assets** : Équipements (chaudières, panneaux solaires, véhicules)
- **energy_consumption** : Consommation énergétique par site
- **production_volumes** : Volumes produits par site

### Données ESG (4 tables)
- **emission_factors** : Facteurs d'émission par source d'énergie
- **carbon_emissions** : Émissions carbone Scope 1 & 2
- **suppliers** : Fournisseurs avec rating ESG
- **supplier_emissions** : Émissions Scope 3 fournisseurs

### Données Texte (2 corpus)
- **sustainability_reports_txt/** : Rapports de durabilité annuels/trimestriels
- **audit_notes_txt/** : Notes d'audit ESG par site

---

## 🏭 Table : sites

**Description** : Sites opérationnels (usines, entrepôts, bureaux)

| Colonne | Type | Description | Exemple |
|---------|------|-------------|---------|
| `site_id` | STRING | Identifiant unique du site | `SITE_001` |
| `site_name` | STRING | Nom du site | `Usine Lyon Gerland` |
| `site_type` | STRING | Type de site | `manufacturing`, `warehouse`, `office` |
| `country` | STRING | Pays | `France` |
| `region` | STRING | Région géographique | `Europe`, `North America`, `Asia` |
| `size_sqm` | INTEGER | Surface en m² | `15000` |
| `employee_count` | INTEGER | Nombre d'employés | `120` |
| `renewable_energy_pct` | FLOAT | % d'énergie renouvelable | `0.35` (35%) |
| `opening_date` | DATE | Date d'ouverture | `2018-03-15` |

**Cardinalité** : 12 sites (4 manufacturing, 4 warehouse, 4 office)

**Relations** :
- `site_id` → `energy_consumption.site_id`
- `site_id` → `production_volumes.site_id`
- `site_id` → `carbon_emissions.site_id`

---

## ⚙️ Table : assets

**Description** : Équipements et infrastructures (chaudières, panneaux solaires, véhicules)

| Colonne | Type | Description | Exemple |
|---------|------|-------------|---------|
| `asset_id` | STRING | Identifiant unique | `ASSET_00001` |
| `site_id` | STRING | Site propriétaire | `SITE_001` |
| `asset_name` | STRING | Nom de l'équipement | `Chaudière gaz B1` |
| `asset_type` | STRING | Type d'équipement | `boiler`, `solar_panel`, `vehicle`, `hvac`, `compressor` |
| `fuel_type` | STRING | Source d'énergie | `natural_gas`, `electricity`, `diesel`, `renewable` |
| `capacity_kw` | FLOAT | Capacité en kW | `500.0` |
| `efficiency_class` | STRING | Classe d'efficacité | `A`, `B`, `C`, `D` |
| `installation_date` | DATE | Date d'installation | `2020-06-12` |
| `last_maintenance_date` | DATE | Dernière maintenance | `2024-11-20` |

**Cardinalité** : ~250 assets (distribution par type)

**Relations** :
- `asset_id` → `energy_consumption.asset_id` (optionnel)

---

## ⚡ Table : energy_consumption

**Description** : Consommation énergétique mensuelle par site et source

| Colonne | Type | Description | Exemple |
|---------|------|-------------|---------|
| `consumption_id` | STRING | Identifiant unique | `CONS_0000001` |
| `site_id` | STRING | Site concerné | `SITE_001` |
| `asset_id` | STRING | Équipement (optionnel) | `ASSET_00001` |
| `year` | INTEGER | Année | `2024` |
| `month` | INTEGER | Mois | `10` |
| `energy_source` | STRING | Type d'énergie | `electricity`, `natural_gas`, `diesel`, `renewable` |
| `consumption_kwh` | FLOAT | Consommation en kWh | `125000.0` |
| `renewable_pct` | FLOAT | % d'origine renouvelable | `0.40` (40%) |
| `cost_eur` | FLOAT | Coût en EUR | `18750.00` |

**Cardinalité** : ~1 300 enregistrements (12 sites × 3 ans × 3-4 sources)

**Relations** :
- `site_id` → `sites.site_id`
- `asset_id` → `assets.asset_id`

**Notes** :
- `renewable_pct` : 0.0 si fossile pur, 1.0 si 100% renouvelable
- Sources mixtes : électricité peut être 40% renouvelable selon contrat

---

## 📦 Table : production_volumes

**Description** : Volumes de production mensuels par site

| Colonne | Type | Description | Exemple |
|---------|------|-------------|---------|
| `production_id` | STRING | Identifiant unique | `PROD_0000001` |
| `site_id` | STRING | Site producteur | `SITE_001` |
| `year` | INTEGER | Année | `2024` |
| `month` | INTEGER | Mois | `10` |
| `production_volume` | FLOAT | Volume produit (tonnes) | `850.0` |
| `production_hours` | FLOAT | Heures de production | `720.0` |
| `scrap_rate_pct` | FLOAT | Taux de rebut | `0.03` (3%) |

**Cardinalité** : ~144 enregistrements (4 manufacturing sites × 36 mois)

**Relations** :
- `site_id` → `sites.site_id`

**Métriques dérivées** :
- **Carbon Intensity** = `carbon_emissions.total_co2_kg` / `production_volume`
- **Energy Efficiency** = `energy_consumption.consumption_kwh` / `production_volume`

---

## 🌍 Table : emission_factors

**Description** : Facteurs d'émission CO₂ par source d'énergie et région

| Colonne | Type | Description | Exemple |
|---------|------|-------------|---------|
| `factor_id` | STRING | Identifiant unique | `EF_001` |
| `region` | STRING | Région géographique | `Europe` |
| `energy_source` | STRING | Type d'énergie | `electricity` |
| `year` | INTEGER | Année d'applicabilité | `2024` |
| `emission_factor_kg_co2_per_kwh` | FLOAT | kg CO₂ / kWh | `0.275` |
| `source` | STRING | Source de référence | `ADEME France 2024` |

**Cardinalité** : ~36 enregistrements (3 régions × 4 sources × 3 années)

**Relations** :
- Utilisé dans les calculs de `carbon_emissions`

**Valeurs typiques** (kg CO₂ / kWh) :
- Électricité France : 0.055 (majoritairement nucléaire)
- Électricité Europe moyenne : 0.275
- Gaz naturel : 0.202
- Diesel : 0.267
- Renouvelable : 0.010 (cycle de vie)

---

## ☁️ Table : carbon_emissions

**Description** : Émissions carbone mensuelles Scope 1 & 2 par site

| Colonne | Type | Description | Exemple |
|---------|------|-------------|---------|
| `emission_id` | STRING | Identifiant unique | `EMIS_0000001` |
| `site_id` | STRING | Site émetteur | `SITE_001` |
| `year` | INTEGER | Année | `2024` |
| `month` | INTEGER | Mois | `10` |
| `scope` | STRING | Scope GHG Protocol | `Scope 1`, `Scope 2` |
| `emission_source` | STRING | Source d'émission | `natural_gas`, `electricity`, `diesel` |
| `consumption_kwh` | FLOAT | Consommation énergétique | `125000.0` |
| `emission_factor_kg_co2_per_kwh` | FLOAT | Facteur d'émission | `0.202` |
| `total_co2_kg` | FLOAT | Total CO₂ (kg) | `25250.0` |

**Cardinalité** : ~3 900 enregistrements

**Relations** :
- `site_id` → `sites.site_id`

**Calcul** :
```
total_co2_kg = consumption_kwh × emission_factor_kg_co2_per_kwh
```

**Scopes GHG Protocol** :
- **Scope 1** : Émissions directes (gaz naturel, diesel, fuel)
- **Scope 2** : Émissions indirectes (électricité achetée)
- **Scope 3** : Chaîne de valeur (fournisseurs) → voir `supplier_emissions`

---

## 🏢 Table : suppliers

**Description** : Fournisseurs avec évaluation ESG

| Colonne | Type | Description | Exemple |
|---------|------|-------------|---------|
| `supplier_id` | STRING | Identifiant unique | `SUPP_001` |
| `supplier_name` | STRING | Nom du fournisseur | `AcierTech France` |
| `country` | STRING | Pays d'origine | `France` |
| `category` | STRING | Catégorie de produits | `raw_materials`, `components`, `packaging`, `transport` |
| `esg_rating` | STRING | Note ESG | `A`, `B`, `C`, `D` |
| `renewable_energy_pct` | FLOAT | % énergie renouvelable | `0.60` (60%) |
| `certification` | STRING | Certifications | `ISO 14001`, `B Corp`, `None` |
| `risk_level` | STRING | Niveau de risque ESG | `low`, `medium`, `high` |

**Cardinalité** : 80 fournisseurs

**Relations** :
- `supplier_id` → `supplier_emissions.supplier_id`

**Distribution ESG** :
- A (Excellent) : 20%
- B (Bon) : 40%
- C (Moyen) : 30%
- D (Faible) : 10%

---

## 🚛 Table : supplier_emissions

**Description** : Émissions Scope 3 liées aux fournisseurs (mensuelles)

| Colonne | Type | Description | Exemple |
|---------|------|-------------|---------|
| `emission_id` | STRING | Identifiant unique | `SUPP_EMIS_0000001` |
| `supplier_id` | STRING | Fournisseur concerné | `SUPP_001` |
| `site_id` | STRING | Site destinataire | `SITE_001` |
| `year` | INTEGER | Année | `2024` |
| `month` | INTEGER | Mois | `10` |
| `emission_category` | STRING | Catégorie Scope 3 | `purchased_goods`, `transport`, `waste` |
| `total_co2_kg` | FLOAT | Total CO₂ (kg) | `15000.0` |
| `volume_units` | FLOAT | Volume livré (unités) | `1000.0` |

**Cardinalité** : ~240 enregistrements

**Relations** :
- `supplier_id` → `suppliers.supplier_id`
- `site_id` → `sites.site_id`

**Catégories Scope 3** :
- `purchased_goods` : Matières premières/composants
- `transport` : Transport amont/aval
- `waste` : Traitement des déchets

---

## 📄 Corpus : sustainability_reports_txt/

**Description** : Rapports de durabilité (PDF → texte) annuels et trimestriels

**Fichiers** : 36 fichiers `.txt` (3 ans × 12 périodes)

**Nomenclature** :
- `REPORT_2023_ANNUAL.txt` : Rapport annuel 2023
- `REPORT_2024_Q1.txt` : Rapport trimestriel Q1 2024

**Contenu type** :
```
=== RAPPORT DE DURABILITÉ Q2 2024 ===
Période : Avril - Juin 2024
Rédacteur : Sophie Martin, Directrice RSE

RÉSUMÉ EXÉCUTIF
Au deuxième trimestre 2024, nous avons réalisé une réduction de 8% de nos émissions 
Scope 1 et 2 comparé à 2023, dépassant notre objectif de -5%. Cette performance est 
principalement due à l'installation de 2500 m² de panneaux solaires sur le site de 
Lyon, augmentant notre part d'énergie renouvelable à 42%.

INDICATEURS CLÉS
- Émissions totales Scope 1+2 : 1 245 tonnes CO₂eq (-8% vs 2023)
- Part d'énergie renouvelable : 42% (+7 points vs Q1)
- Émissions Scope 3 (fournisseurs) : 3 850 tonnes CO₂eq (-2% vs 2023)

...
```

**AI Transformation** :
- **Analyse de sentiment** : Positive, Negative, Neutral
- **Extraction d'entités** : Sites, Fournisseurs, Indicateurs
- **KPI extraction** : Émissions, Objectifs, Performances

**Table transformée** : `sustainability_reports_transformed`

**Colonnes après transformation** :
- `report_id` : ID du rapport
- `period` : Période (année ou trimestre)
- `sentiment` : Sentiment global (Positive/Negative/Neutral)
- `key_topics` : Thèmes principaux (liste)
- `emissions_mentioned` : Émissions citées (JSON)
- `targets_mentioned` : Objectifs cités (JSON)
- `full_text` : Texte complet

---

## 📝 Corpus : audit_notes_txt/

**Description** : Notes d'audit ESG par site (inspections terrain)

**Fichiers** : 80 fichiers `.txt` (12 sites × 2-3 ans × 2-3 audits/an)

**Nomenclature** :
- `AUDIT_SITE_001_2024_10_15.txt` : Audit site 001 du 15/10/2024

**Contenu type** :
```
=== NOTE D'AUDIT ESG ===
Site : SITE_001 - Usine Lyon Gerland
Date : 15 octobre 2024
Auditeur : Marc Leblanc (Externe - EcoAudit SAS)
Référentiel : ISO 14001:2015

OBSERVATIONS POSITIVES
✓ Système de management environnemental bien documenté
✓ Formation du personnel aux éco-gestes (95% de participation)
✓ Réduction de 12% de la consommation d'eau vs 2023

POINTS D'ATTENTION
⚠ Compteurs énergétiques sur ligne 3 non calibrés depuis 18 mois
⚠ Stockage de produits chimiques : bac de rétention insuffisant
⚠ Manque de visibilité sur émissions Scope 3 (transport aval)

RECOMMANDATIONS
1. Planifier calibration des compteurs avant fin Q4
2. Renforcer dispositifs de rétention (investissement ~8k€)
3. Déployer outil de tracking Scope 3 avec partenaires logistiques

...
```

**AI Transformation** :
- **Classification** : Positive, Neutral, Negative
- **Extraction de non-conformités** : Liste des points d'attention
- **Extraction de recommandations** : Actions correctives
- **Détection PII** : Noms d'auditeurs (à masquer)

**Table transformée** : `audit_notes_transformed`

**Colonnes après transformation** :
- `audit_id` : ID de l'audit
- `site_id` : Site audité
- `audit_date` : Date d'audit
- `auditor_name` : Nom auditeur (PII détectée)
- `classification` : Positive/Neutral/Negative
- `positive_findings` : Observations positives (liste)
- `issues_found` : Points d'attention (liste)
- `recommendations` : Recommandations (liste)
- `full_text` : Texte complet

---

## 🔗 Relations Entre Tables

```
sites (12)
├── energy_consumption (1 300) [site_id]
├── production_volumes (144) [site_id]
├── carbon_emissions (3 900) [site_id]
├── supplier_emissions (240) [site_id]
└── audit_notes_transformed (80) [site_id]

assets (250)
└── energy_consumption (1 300) [asset_id] (optionnel)

suppliers (80)
└── supplier_emissions (240) [supplier_id]

emission_factors (36)
└── (utilisé dans calculs carbon_emissions)

sustainability_reports_txt/ (36 fichiers)
└── sustainability_reports_transformed (36) [AI]

audit_notes_txt/ (80 fichiers)
└── audit_notes_transformed (80) [AI]
```

---

## 📊 Métriques Calculées (DAX)

### Carbon Intensity (kg CO₂ / tonne produite)

```dax
Carbon Intensity = 
DIVIDE(
    SUM(carbon_emissions[total_co2_kg]) + SUM(supplier_emissions[total_co2_kg]),
    SUM(production_volumes[production_volume]),
    0
)
```

### Renewable Energy %

```dax
Renewable Energy % = 
DIVIDE(
    SUMX(
        energy_consumption,
        energy_consumption[consumption_kwh] * energy_consumption[renewable_pct]
    ),
    SUM(energy_consumption[consumption_kwh]),
    0
)
```

### Total Emissions (Scope 1 + 2 + 3)

```dax
Total Emissions = 
SUM(carbon_emissions[total_co2_kg]) + SUM(supplier_emissions[total_co2_kg])
```

### Réduction vs Baseline

```dax
Reduction vs Baseline = 
VAR BaselineEmissions = 
    CALCULATE(
        [Total Emissions],
        YEAR(carbon_emissions[year]) = 2023
    )
VAR CurrentEmissions = [Total Emissions]
RETURN
    DIVIDE(BaselineEmissions - CurrentEmissions, BaselineEmissions, 0)
```

### High Risk Suppliers Count

```dax
High Risk Suppliers = 
CALCULATE(
    DISTINCTCOUNT(suppliers[supplier_id]),
    suppliers[risk_level] = "high"
)
```

---

## 🎯 Scénarios Intégrés

### Scenario 1 : Renewable Energy Ramp-Up

**Objectif** : Passer de 25% à 50% d'énergie renouvelable (2023 → 2025)

**Données affectées** :
- `sites.renewable_energy_pct` : Progression graduelle
- `energy_consumption.renewable_pct` : Hausse mensuelle
- `sustainability_reports_txt/` : Mentions d'installations solaires

**Métriques cibles** :
- 2023 : 25% renouvelable
- 2024 : 35% renouvelable
- 2025 : 50% renouvelable

### Scenario 2 : Supplier Risk Alert

**Objectif** : Identifier fournisseurs à risque ESG élevé

**Données affectées** :
- `suppliers.esg_rating` : 10% notés D (risque élevé)
- `supplier_emissions.total_co2_kg` : Émissions plus élevées pour fournisseurs D
- `audit_notes_txt/` : Mentions de non-conformités fournisseurs

**Alertes** :
- Fournisseurs D avec >50 tonnes CO₂/mois
- Certification absente + risque élevé

### Scenario 3 : Site Performance Variance

**Objectif** : Analyser les écarts de performance entre sites

**Données affectées** :
- `carbon_emissions.total_co2_kg` : Variabilité site par site
- `production_volumes.scrap_rate_pct` : Taux de rebut variable
- `audit_notes_txt/` : Notes positives pour sites performants, négatives pour autres

**Exemple** :
- SITE_001 (Lyon) : Carbon Intensity = 28 kg/tonne (excellent)
- SITE_005 (Berlin) : Carbon Intensity = 45 kg/tonne (à améliorer)

---

## 💡 Cas d'Usage Data Agent

### Questions Typiques

**Performance Carbone** :
- "Quelles sont nos émissions Scope 1+2 en 2024 ?"
- "Quel est notre carbon intensity moyen sur 2024 ?"
- "Avons-nous atteint notre objectif de -5% en 2024 ?"

**Énergie Renouvelable** :
- "Quelle est notre part d'énergie renouvelable actuelle ?"
- "Quels sites ont dépassé 50% de renouvelable ?"
- "Quelle est l'évolution du % renouvelable depuis 2023 ?"

**Fournisseurs** :
- "Combien de fournisseurs ont un rating ESG D ?"
- "Quel fournisseur génère le plus d'émissions Scope 3 ?"
- "Liste des fournisseurs à risque élevé"

**Analyse de Texte (AI)** :
- "Quels sont les thèmes principaux dans les rapports 2024 ?"
- "Quels sites ont eu des audits avec findings négatifs ?"
- "Extraire les objectifs mentionnés dans le rapport Q3 2024"

---

## 📝 Notes Techniques

### Formats de Données

- **Dates** : `YYYY-MM-DD` (ISO 8601)
- **Floats** : Point décimal (ex: `0.35`)
- **Encoding** : UTF-8 (tous fichiers)
- **Séparateur CSV** : `,`

### Volumes

- **Total CSV rows** : ~6 000 lignes
- **Total text files** : 116 fichiers
- **Total size** : ~3 MB (compressed)

### Cohérence Référentielle

- ✅ Tous les `site_id` dans `energy_consumption` existent dans `sites`
- ✅ Tous les `supplier_id` dans `supplier_emissions` existent dans `suppliers`
- ✅ Les émissions Scope 1+2 correspondent aux consommations énergétiques
- ✅ Les dates sont cohérentes (2023-01-01 à 2025-12-31)

### Conformité ESG

- **GHG Protocol** : Scopes 1, 2, 3 respectés
- **CSRD** : Structure alignée sur reporting CSRD
- **ISO 14001** : Mentions dans audit_notes
- **SBTi** : Objectifs compatibles Science Based Targets

---

**Dernière mise à jour** : Décembre 2024  
**Version** : 1.0
