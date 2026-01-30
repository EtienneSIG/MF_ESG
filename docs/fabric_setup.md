# 🚀 Guide de Déploiement Microsoft Fabric - ESG & Carbon Analytics

Ce guide décrit pas à pas le déploiement de la démo **ESG & Carbon Analytics** dans Microsoft Fabric.

---

## 📋 Prérequis

### Comptes et Licences

- ✅ **Microsoft Fabric** activé (licence F64 ou supérieure)
- ✅ **Capacité Fabric** : Min F4 (pour AI Transformations)
- ✅ **OneLake** activé dans le tenant
- ✅ **Data Agent** preview activé

### Rôles Requis

- **Fabric Administrator** : Pour créer le workspace
- **Workspace Admin** : Pour configurer OneLake et Semantic Model
- **Contributor** : Pour créer les objets Fabric (Lakehouse, Pipelines, etc.)

### Données Générées

- ✅ Exécuter `src/generate_data.py` (cf. [`README.md`](../README.md))
- ✅ Vérifier la structure `data/raw/` :
  - `production/` : 4 fichiers CSV (sites, assets, energy_consumption, production_volumes)
  - `esg/` : 4 fichiers CSV (emission_factors, carbon_emissions, suppliers, supplier_emissions)
  - `text/sustainability_reports_txt/` : 36 fichiers `.txt`
  - `text/audit_notes_txt/` : 80 fichiers `.txt`

---

## 🏗️ Architecture de la Solution

```
┌──────────────────────────────────────────────────────────────┐
│                     MICROSOFT FABRIC                         │
│                                                              │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐    │
│  │   OneLake    │   │  Lakehouse   │   │  Shortcuts   │    │
│  │              │◄──┤              │◄──┤              │    │
│  │  (Storage)   │   │  (SQL/Spark) │   │  (External)  │    │
│  └──────────────┘   └──────────────┘   └──────────────┘    │
│         │                   │                                │
│         ▼                   ▼                                │
│  ┌──────────────────────────────────────┐                   │
│  │      AI Transformations              │                   │
│  │  • sustainability_reports_txt/       │                   │
│  │  • audit_notes_txt/                  │                   │
│  └──────────────────────────────────────┘                   │
│         │                                                    │
│         ▼                                                    │
│  ┌──────────────────────────────────────┐                   │
│  │      Semantic Model (DAX)            │                   │
│  │  • Measures Carbon Intensity         │                   │
│  │  • Measures Renewable Energy %       │                   │
│  │  • Relationships (sites ↔ emissions) │                   │
│  └──────────────────────────────────────┘                   │
│         │                                                    │
│         ▼                                                    │
│  ┌──────────────────────────────────────┐                   │
│  │         Data Agent                   │                   │
│  │  • ESG Manager (NL Queries)          │                   │
│  │  • System Prompt Configured          │                   │
│  └──────────────────────────────────────┘                   │
│         │                                                    │
│         ▼                                                    │
│  ┌──────────────────────────────────────┐                   │
│  │      Power BI Dashboard              │                   │
│  │  • Carbon Footprint KPIs             │                   │
│  │  • Site Performance Map              │                   │
│  │  • Supplier Risk Matrix              │                   │
│  └──────────────────────────────────────┘                   │
└──────────────────────────────────────────────────────────────┘
```

---

## 📦 Étape 1 : Créer le Workspace

### 1.1 Nouveau Workspace

1. Dans Fabric, cliquer sur **Workspaces** (menu gauche)
2. Cliquer sur **+ New workspace**
3. Nom : `ESG Analytics Demo`
4. Description : `Démo ESG & Carbon Analytics avec Data Agent`
5. **Advanced** :
   - Licence : Premium (Fabric F64 ou supérieure)
   - Contributors : Ajouter les utilisateurs de la démo

### 1.2 Activer OneLake

1. Dans **Workspace Settings** → **OneLake**
2. Activer **OneLake Storage**
3. **Region** : West Europe (ou proche de vos données)

---

## 🗄️ Étape 2 : Créer le Lakehouse

### 2.1 Nouveau Lakehouse

1. Dans le workspace, cliquer sur **+ New** → **Lakehouse**
2. Nom : `ESG_Lakehouse`
3. Cliquer sur **Create**

### 2.2 Structure de Dossiers

Créer la structure suivante dans le Lakehouse :

```
ESG_Lakehouse/
├── Files/
│   ├── production/          # CSV opérationnels
│   ├── esg/                 # CSV ESG
│   └── text/
│       ├── sustainability_reports_txt/  # 36 rapports
│       └── audit_notes_txt/             # 80 audits
└── Tables/
    └── (tables transformées après AI)
```

**Créer les dossiers** :
1. Dans **Lakehouse Explorer** → **Files**
2. Clic droit → **New folder**
3. Créer : `production`, `esg`, `text`
4. Dans `text/`, créer `sustainability_reports_txt` et `audit_notes_txt`

---

## 📤 Étape 3 : Upload des Fichiers CSV

### 3.1 Upload Production

1. Dans **Lakehouse Explorer** → **Files** → `production/`
2. Cliquer sur **Upload** → **Upload files**
3. Sélectionner :
   - `data/raw/production/sites.csv`
   - `data/raw/production/assets.csv`
   - `data/raw/production/energy_consumption.csv`
   - `data/raw/production/production_volumes.csv`

### 3.2 Upload ESG

1. Dans **Files** → `esg/`
2. Upload :
   - `data/raw/esg/emission_factors.csv`
   - `data/raw/esg/carbon_emissions.csv`
   - `data/raw/esg/suppliers.csv`
   - `data/raw/esg/supplier_emissions.csv`

### 3.3 Upload Textes

**Rapports de Durabilité** :
1. Dans **Files** → `text/sustainability_reports_txt/`
2. Upload en batch : Sélectionner les 36 fichiers `REPORT_*.txt`

**Notes d'Audit** :
1. Dans **Files** → `text/audit_notes_txt/`
2. Upload en batch : Sélectionner les 80 fichiers `AUDIT_*.txt`

**⏱️ Durée estimée** : 5 minutes (avec connexion rapide)

---

## 🔗 Étape 4 : Créer les Shortcuts (Optionnel)

Si les données sont dans Azure Blob Storage ou ADLS Gen2, créer des Shortcuts au lieu d'uploader.

### 4.1 Shortcut vers Blob Storage

1. Dans **Lakehouse Explorer** → **Files**
2. Clic droit → **New shortcut**
3. Source : **Azure Data Lake Storage Gen2**
4. Configuration :
   - **URL** : `https://<storage_account>.blob.core.windows.net/<container>/production/`
   - **Authentication** : Account Key ou SAS Token
5. Nom du shortcut : `production`
6. **Create**

Répéter pour `esg/` et `text/`.

---

## 🧠 Étape 5 : Configurer AI Transformations

### 5.1 AI Transformation sur Rapports de Durabilité

**Objectif** : Extraire sentiment, thèmes, KPIs depuis les rapports texte.

#### 5.1.1 Créer la Transformation

1. Dans **Lakehouse** → **Files** → `text/sustainability_reports_txt/`
2. Clic droit → **AI Transformation**
3. **Transformation Type** : Text Analytics
4. Nom : `Transform_Sustainability_Reports`

#### 5.1.2 Configurer les Colonnes Extraites

**Input** : 
- Source Folder : `text/sustainability_reports_txt/`
- File Pattern : `REPORT_*.txt`

**Output Schema** :
| Colonne | Type | AI Task | Description |
|---------|------|---------|-------------|
| `report_id` | STRING | Extract Filename | ID du rapport (ex: `REPORT_2024_Q1`) |
| `period` | STRING | Extract | Période (année ou trimestre) |
| `sentiment` | STRING | Sentiment Analysis | Positive, Neutral, Negative |
| `key_topics` | ARRAY<STRING> | Topic Extraction | Liste des thèmes (max 10) |
| `emissions_mentioned` | JSON | Named Entity Recognition | Émissions citées avec valeurs |
| `targets_mentioned` | JSON | Named Entity Recognition | Objectifs cités |
| `full_text` | STRING | Raw | Texte complet |

#### 5.1.3 Configurer le Prompt AI

**Prompt Template** :
```
Analyse ce rapport de durabilité et extrais :

1. SENTIMENT : Détermine si le rapport est globalement Positive, Neutral ou Negative
   (basé sur l'atteinte des objectifs et le ton général)

2. KEY TOPICS : Extrais les 5-10 thèmes principaux mentionnés 
   (ex: "solar installation", "carbon reduction", "supplier engagement")

3. EMISSIONS : Extrais toutes les mentions d'émissions CO₂ avec leurs valeurs
   Format JSON : [{"scope": "Scope 1", "value": 795, "unit": "tonnes CO₂eq"}]

4. TARGETS : Extrais tous les objectifs mentionnés
   Format JSON : [{"metric": "Scope 1 reduction", "target": "-5%", "year": 2024}]

Texte à analyser :
{full_text}
```

#### 5.1.4 Exécuter la Transformation

1. Cliquer sur **Run AI Transformation**
2. **Compute** : Sélectionner un cluster Spark (ou créer un nouveau : Small, 4 cores)
3. **Run**

**⏱️ Durée estimée** : 5-10 minutes (36 fichiers)

#### 5.1.5 Vérifier la Table Créée

1. Dans **Lakehouse** → **Tables**
2. Vérifier que `sustainability_reports_transformed` existe
3. Prévisualiser les données (clic droit → **Preview data**)

**Vérification attendue** :
- 36 lignes (1 par rapport)
- Colonnes : `report_id`, `period`, `sentiment`, `key_topics`, `emissions_mentioned`, `targets_mentioned`, `full_text`
- Sentiment distribué : ~75% Positive, ~25% Neutral

---

### 5.2 AI Transformation sur Notes d'Audit

**Objectif** : Classifier audits (Positive/Neutral/Negative), extraire non-conformités et recommandations.

#### 5.2.1 Créer la Transformation

1. Dans **Files** → `text/audit_notes_txt/`
2. Clic droit → **AI Transformation**
3. Nom : `Transform_Audit_Notes`

#### 5.2.2 Configurer les Colonnes Extraites

**Input** : 
- Source Folder : `text/audit_notes_txt/`
- File Pattern : `AUDIT_*.txt`

**Output Schema** :
| Colonne | Type | AI Task | Description |
|---------|------|---------|-------------|
| `audit_id` | STRING | Extract Filename | ID de l'audit (ex: `AUDIT_SITE_001_2024_10_15`) |
| `site_id` | STRING | Extract | Site audité (ex: `SITE_001`) |
| `audit_date` | DATE | Extract | Date de l'audit |
| `auditor_name` | STRING | Named Entity Recognition | Nom de l'auditeur (PII) |
| `classification` | STRING | Sentiment Analysis | Positive, Neutral, Negative |
| `positive_findings` | ARRAY<STRING> | Extract | Observations positives |
| `issues_found` | ARRAY<STRING> | Extract | Points d'attention / non-conformités |
| `recommendations` | ARRAY<STRING> | Extract | Recommandations d'amélioration |
| `full_text` | STRING | Raw | Texte complet |

#### 5.2.3 Configurer le Prompt AI

**Prompt Template** :
```
Analyse cette note d'audit ESG et extrais :

1. CLASSIFICATION : Détermine si l'audit est globalement :
   - Positive : Majoritairement conforme, peu de non-conformités mineures
   - Neutral : Conformités et non-conformités équilibrées
   - Negative : Non-conformités majeures ou multiples

2. POSITIVE FINDINGS : Liste des observations positives (✓)
   Format : ["Observation 1", "Observation 2", ...]

3. ISSUES FOUND : Liste des points d'attention ou non-conformités (⚠)
   Format : ["Issue 1", "Issue 2", ...]

4. RECOMMENDATIONS : Liste des recommandations d'amélioration
   Format : ["Recommandation 1", "Recommandation 2", ...]

5. AUDITOR NAME : Extrais le nom de l'auditeur (dans section "Auditeur :")

Texte à analyser :
{full_text}
```

#### 5.2.4 Exécuter la Transformation

1. **Run AI Transformation**
2. **Compute** : Même cluster que précédemment
3. **Run**

**⏱️ Durée estimée** : 8-12 minutes (80 fichiers)

#### 5.2.5 Vérifier la Table Créée

1. **Tables** → `audit_notes_transformed`
2. Prévisualiser les données

**Vérification attendue** :
- 80 lignes (1 par audit)
- Colonnes : `audit_id`, `site_id`, `audit_date`, `auditor_name`, `classification`, `positive_findings`, `issues_found`, `recommendations`, `full_text`
- Classification : ~50% Positive, ~35% Neutral, ~15% Negative

---

## 📊 Étape 6 : Créer les Tables Delta depuis CSV

### 6.1 Créer Table "sites"

1. Dans **Lakehouse** → **Files** → `production/sites.csv`
2. Clic droit → **Load to Tables** → **New table**
3. Nom de table : `sites`
4. **Schema Inference** : Automatic
5. **Vérifier le schéma** :
   - `site_id` : STRING
   - `site_name` : STRING
   - `site_type` : STRING
   - `country` : STRING
   - `region` : STRING
   - `size_sqm` : INTEGER
   - `employee_count` : INTEGER
   - `renewable_energy_pct` : DOUBLE
   - `opening_date` : DATE
6. **Create**

### 6.2 Créer les Autres Tables

Répéter pour toutes les tables CSV :

**Tables Production** :
- `assets` (depuis `production/assets.csv`)
- `energy_consumption` (depuis `production/energy_consumption.csv`)
- `production_volumes` (depuis `production/production_volumes.csv`)

**Tables ESG** :
- `emission_factors` (depuis `esg/emission_factors.csv`)
- `carbon_emissions` (depuis `esg/carbon_emissions.csv`)
- `suppliers` (depuis `esg/suppliers.csv`)
- `supplier_emissions` (depuis `esg/supplier_emissions.csv`)

**⚠️ Attention aux Types de Colonnes** :

**Pour `energy_consumption`** :
- `consumption_kwh` : DOUBLE (pas INTEGER)
- `renewable_pct` : DOUBLE
- `cost_eur` : DOUBLE

**Pour `carbon_emissions`** :
- `total_co2_kg` : DOUBLE
- `emission_factor_kg_co2_per_kwh` : DOUBLE

**Pour Dates** :
- Format : `YYYY-MM-DD` (sera auto-détecté comme DATE)

---

## 🔗 Étape 7 : Créer le Semantic Model

### 7.1 Nouveau Semantic Model

1. Dans le workspace, cliquer sur **+ New** → **Semantic Model**
2. Nom : `ESG_Analytics`
3. **Data Source** : Lakehouse → `ESG_Lakehouse`
4. **Select Tables** :
   - ✅ sites
   - ✅ assets
   - ✅ energy_consumption
   - ✅ production_volumes
   - ✅ emission_factors
   - ✅ carbon_emissions
   - ✅ suppliers
   - ✅ supplier_emissions
   - ✅ sustainability_reports_transformed
   - ✅ audit_notes_transformed
5. **Create**

### 7.2 Définir les Relations

Ouvrir le Semantic Model en mode **Model View**.

#### Relations à Créer :

**1. sites ↔ energy_consumption**
- Table A : `sites`
- Colonne A : `site_id`
- Table B : `energy_consumption`
- Colonne B : `site_id`
- Cardinalité : 1:N (one-to-many)
- Direction de filtrage : Both

**2. sites ↔ production_volumes**
- `sites[site_id]` ↔ `production_volumes[site_id]`
- Cardinalité : 1:N
- Direction : Both

**3. sites ↔ carbon_emissions**
- `sites[site_id]` ↔ `carbon_emissions[site_id]`
- Cardinalité : 1:N
- Direction : Both

**4. sites ↔ supplier_emissions**
- `sites[site_id]` ↔ `supplier_emissions[site_id]`
- Cardinalité : 1:N
- Direction : Both

**5. assets ↔ energy_consumption**
- `assets[asset_id]` ↔ `energy_consumption[asset_id]`
- Cardinalité : 1:N
- Direction : Both
- ⚠️ **Optionnel** (car `asset_id` est NULL dans beaucoup de lignes)

**6. suppliers ↔ supplier_emissions**
- `suppliers[supplier_id]` ↔ `supplier_emissions[supplier_id]`
- Cardinalité : 1:N
- Direction : Both

**7. sites ↔ audit_notes_transformed**
- `sites[site_id]` ↔ `audit_notes_transformed[site_id]`
- Cardinalité : 1:N
- Direction : Both

**Schéma de Relations** :

```
sites (12)
  ├─► energy_consumption (1 300) [site_id]
  ├─► production_volumes (144) [site_id]
  ├─► carbon_emissions (3 900) [site_id]
  ├─► supplier_emissions (240) [site_id]
  └─► audit_notes_transformed (80) [site_id]

assets (250)
  └─► energy_consumption (1 300) [asset_id]

suppliers (80)
  └─► supplier_emissions (240) [supplier_id]

sustainability_reports_transformed (36)
  (pas de relation directe, analyse indépendante)
```

---

## 📐 Étape 8 : Créer les Measures DAX

### 8.1 Measures de Base

Dans le Semantic Model, aller dans **Modeling** → **New Measure**.

#### Measure 1 : Total Emissions (Scope 1+2+3)

```dax
Total Emissions = 
SUM(carbon_emissions[total_co2_kg]) + SUM(supplier_emissions[total_co2_kg])
```

**Format** : `#,0 "tonnes CO₂"`

**Description** : Émissions totales Scope 1+2+3 en kg CO₂ (converti en tonnes)

---

#### Measure 2 : Scope 1 Emissions

```dax
Scope 1 Emissions = 
CALCULATE(
    SUM(carbon_emissions[total_co2_kg]),
    carbon_emissions[scope] = "Scope 1"
) / 1000
```

**Format** : `#,0 "tonnes CO₂"`

---

#### Measure 3 : Scope 2 Emissions

```dax
Scope 2 Emissions = 
CALCULATE(
    SUM(carbon_emissions[total_co2_kg]),
    carbon_emissions[scope] = "Scope 2"
) / 1000
```

**Format** : `#,0 "tonnes CO₂"`

---

#### Measure 4 : Scope 3 Emissions

```dax
Scope 3 Emissions = 
SUM(supplier_emissions[total_co2_kg]) / 1000
```

**Format** : `#,0 "tonnes CO₂"`

---

#### Measure 5 : Carbon Intensity

```dax
Carbon Intensity = 
DIVIDE(
    SUM(carbon_emissions[total_co2_kg]) + SUM(supplier_emissions[total_co2_kg]),
    SUM(production_volumes[production_volume]),
    0
)
```

**Format** : `#,0.0 "kg/tonne"`

**Description** : kg CO₂ par tonne produite (indicateur d'efficacité carbone)

---

#### Measure 6 : Renewable Energy %

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

**Format** : `0.0%`

---

### 8.2 Measures de Comparaison vs Baseline

#### Measure 7 : Baseline Emissions 2023

```dax
Baseline Emissions 2023 = 
CALCULATE(
    [Total Emissions],
    carbon_emissions[year] = 2023,
    supplier_emissions[year] = 2023
)
```

**Format** : `#,0 "tonnes CO₂"`

---

#### Measure 8 : Reduction vs Baseline %

```dax
Reduction vs Baseline % = 
VAR CurrentEmissions = [Total Emissions]
VAR BaselineEmissions = [Baseline Emissions 2023]
RETURN
    DIVIDE(
        BaselineEmissions - CurrentEmissions,
        BaselineEmissions,
        0
    )
```

**Format** : `0.0%`

**Description** : % de réduction vs baseline 2023 (positif = réduction, négatif = hausse)

---

#### Measure 9 : Scope 1 Reduction vs Baseline %

```dax
Scope 1 Reduction % = 
VAR CurrentScope1 = [Scope 1 Emissions]
VAR BaselineScope1 = 
    CALCULATE(
        [Scope 1 Emissions],
        carbon_emissions[year] = 2023
    )
RETURN
    DIVIDE(
        BaselineScope1 - CurrentScope1,
        BaselineScope1,
        0
    )
```

**Format** : `0.0%`

---

#### Measure 10 : Scope 2 Reduction vs Baseline %

```dax
Scope 2 Reduction % = 
VAR CurrentScope2 = [Scope 2 Emissions]
VAR BaselineScope2 = 
    CALCULATE(
        [Scope 2 Emissions],
        carbon_emissions[year] = 2023
    )
RETURN
    DIVIDE(
        BaselineScope2 - CurrentScope2,
        BaselineScope2,
        0
    )
```

**Format** : `0.0%`

---

### 8.3 Measures Avancées

#### Measure 11 : High Risk Suppliers Count

```dax
High Risk Suppliers = 
CALCULATE(
    DISTINCTCOUNT(suppliers[supplier_id]),
    suppliers[esg_rating] = "D"
)
```

**Format** : `0`

---

#### Measure 12 : Top Emitter Supplier

```dax
Top Emitter Supplier = 
VAR TopSupplier = 
    TOPN(
        1,
        SUMMARIZE(
            supplier_emissions,
            suppliers[supplier_name],
            "Total", SUM(supplier_emissions[total_co2_kg])
        ),
        [Total],
        DESC
    )
RETURN
    MAXX(TopSupplier, suppliers[supplier_name])
```

**Format** : Texte

---

#### Measure 13 : Best Performing Site (Carbon Intensity)

```dax
Best Site (Carbon Intensity) = 
VAR BestSite = 
    TOPN(
        1,
        SUMMARIZE(
            sites,
            sites[site_name],
            "CI", [Carbon Intensity]
        ),
        [CI],
        ASC
    )
RETURN
    MAXX(BestSite, sites[site_name])
```

**Format** : Texte

---

#### Measure 14 : Renewable Energy Gap to Target (50%)

```dax
Gap to 50% Target = 
0.50 - [Renewable Energy %]
```

**Format** : `+0.0%;-0.0%`

**Description** : Points de pourcentage manquants pour atteindre 50%

---

#### Measure 15 : Positive Sentiment Reports %

```dax
Positive Sentiment % = 
DIVIDE(
    CALCULATE(
        COUNTROWS(sustainability_reports_transformed),
        sustainability_reports_transformed[sentiment] = "Positive"
    ),
    COUNTROWS(sustainability_reports_transformed),
    0
)
```

**Format** : `0%`

---

### 8.4 Measures pour AI Insights

#### Measure 16 : Negative Audits Count

```dax
Negative Audits = 
CALCULATE(
    COUNTROWS(audit_notes_transformed),
    audit_notes_transformed[classification] = "Negative"
)
```

**Format** : `0`

---

#### Measure 17 : Sites with Negative Audits

```dax
Sites with Negative Audits = 
CALCULATE(
    DISTINCTCOUNT(audit_notes_transformed[site_id]),
    audit_notes_transformed[classification] = "Negative"
)
```

**Format** : `0`

---

## 📊 Étape 9 : Créer le Dashboard Power BI

### 9.1 Nouveau Report

1. Dans le workspace, cliquer sur **+ New** → **Report**
2. **Data Source** : Semantic Model → `ESG_Analytics`
3. Nom : `ESG Dashboard`

### 9.2 Page 1 : Carbon Footprint Overview

**Layout** :
```
┌────────────────────────────────────────────────────────┐
│                  ESG DASHBOARD                         │
│  Émissions Carbone | Énergie Renouvelable | Fournisseurs │
├───────────┬───────────┬───────────┬────────────────────┤
│  Scope 1  │  Scope 2  │  Scope 3  │  Carbon Intensity  │
│  795 t    │ 1 080 t   │ 4 350 t   │    32 kg/tonne     │
│  -6.5%    │  -10%     │  -3.3%    │      -8.6%         │
├───────────┴───────────┴───────────┴────────────────────┤
│                                                        │
│       Évolution Mensuelle Scope 1+2 (Line Chart)      │
│       2023-2025                                        │
│                                                        │
├─────────────────────────────┬──────────────────────────┤
│   Carbon Intensity by Site  │  Renewable Energy % by   │
│   (Map with Bubbles)        │  Site (Bar Chart)        │
│                             │                          │
└─────────────────────────────┴──────────────────────────┘
```

**Visuals à Créer** :

**1. KPI Cards (4)** :
- **Scope 1 Emissions** :
  - Value : `[Scope 1 Emissions]`
  - Trend : `[Scope 1 Reduction %]`
  - Target : `-5%`
  
- **Scope 2 Emissions** :
  - Value : `[Scope 2 Emissions]`
  - Trend : `[Scope 2 Reduction %]`
  - Target : `-8%`
  
- **Scope 3 Emissions** :
  - Value : `[Scope 3 Emissions]`
  - Trend : (calculé vs 2023)
  
- **Carbon Intensity** :
  - Value : `[Carbon Intensity]`
  - Trend : `DIVIDE([Carbon Intensity] - 35, 35)` (vs baseline 35 kg/tonne)

**2. Line Chart : Évolution Scope 1+2** :
- **X-Axis** : `carbon_emissions[year]`, `carbon_emissions[month]`
- **Y-Axis** : `[Scope 1 Emissions] + [Scope 2 Emissions]`
- **Legend** : Année
- **Filtres** : 2023-2025

**3. Map : Carbon Intensity by Site** :
- **Location** : `sites[country]`, `sites[site_name]`
- **Size** : `[Total Emissions]`
- **Color** : `[Carbon Intensity]` (gradient : vert <30 → rouge >40)
- **Tooltip** : Site name, Carbon Intensity, Renewable %

**4. Bar Chart : Renewable Energy % by Site** :
- **X-Axis** : `sites[site_name]`
- **Y-Axis** : `[Renewable Energy %]`
- **Target Line** : 50%
- **Color** : Conditionnel (vert si >50%, orange 30-50%, rouge <30%)

---

### 9.3 Page 2 : Supplier Risk Analysis

**Layout** :
```
┌────────────────────────────────────────────────────────┐
│              SUPPLIER ESG RISK MATRIX                  │
├───────────┬───────────┬───────────┬────────────────────┤
│  Total    │  Rating A │  Rating D │  High Risk Supp.   │
│  Suppliers│    16     │     8     │       8            │
│    80     │   (20%)   │   (10%)   │                    │
├───────────┴───────────┴───────────┴────────────────────┤
│                                                        │
│   Top 10 Emitters (Bar Chart)                         │
│   Supplier Name | Emissions | Rating                  │
│                                                        │
├─────────────────────────────┬──────────────────────────┤
│  Scope 3 by Category        │  Supplier by Country     │
│  (Pie Chart)                │  (Map)                   │
│                             │                          │
└─────────────────────────────┴──────────────────────────┘
```

**Visuals** :

**1. KPI Cards** :
- **Total Suppliers** : `DISTINCTCOUNT(suppliers[supplier_id])`
- **Rating A Suppliers** : `CALCULATE(DISTINCTCOUNT(...), rating = "A")`
- **Rating D Suppliers** : `[High Risk Suppliers]`

**2. Bar Chart : Top 10 Emitters** :
- **X-Axis** : `suppliers[supplier_name]`
- **Y-Axis** : `SUM(supplier_emissions[total_co2_kg])`
- **Color** : `suppliers[esg_rating]`
- **Top N** : 10
- **Sort** : Descending

**3. Pie Chart : Scope 3 by Category** :
- **Values** : `SUM(supplier_emissions[total_co2_kg])`
- **Legend** : `supplier_emissions[emission_category]`

**4. Map : Suppliers by Country** :
- **Location** : `suppliers[country]`
- **Size** : `COUNT(suppliers[supplier_id])`
- **Color** : `AVERAGE(suppliers[esg_rating])` (A=4, B=3, C=2, D=1)

---

### 9.4 Page 3 : AI Insights (Reports & Audits)

**Layout** :
```
┌────────────────────────────────────────────────────────┐
│                  AI INSIGHTS                           │
├───────────┬───────────┬───────────┬────────────────────┤
│  Reports  │ Positive  │ Negative  │  Sites with Neg.   │
│  Analyzed │ Sentiment │  Audits   │  Audits            │
│    36     │   75%     │     12    │       2            │
├───────────┴───────────┴───────────┴────────────────────┤
│                                                        │
│   Key Topics (Word Cloud)                             │
│   From sustainability_reports_transformed              │
│                                                        │
├─────────────────────────────┬──────────────────────────┤
│  Audit Classification       │  Recommendations Extract │
│  (Pie Chart)                │  (Table)                 │
│                             │                          │
└─────────────────────────────┴──────────────────────────┘
```

**Visuals** :

**1. KPI Cards** :
- **Reports Analyzed** : `COUNTROWS(sustainability_reports_transformed)`
- **Positive Sentiment %** : `[Positive Sentiment %]`
- **Negative Audits** : `[Negative Audits]`
- **Sites with Negative Audits** : `[Sites with Negative Audits]`

**2. Word Cloud : Key Topics** :
- **Category** : `sustainability_reports_transformed[key_topics]` (déplier le array)
- **Values** : `COUNT()`
- Visual : Word Cloud (custom visual)

**3. Pie Chart : Audit Classification** :
- **Values** : `COUNTROWS(audit_notes_transformed)`
- **Legend** : `audit_notes_transformed[classification]`
- **Colors** : Positive = Vert, Neutral = Orange, Negative = Rouge

**4. Table : Recommendations from Negative Audits** :
- **Columns** : `site_id`, `audit_date`, `recommendations` (déplier le array)
- **Filter** : `classification = "Negative"`

---

## 🤖 Étape 10 : Configurer le Data Agent

### 10.1 Créer le Data Agent

1. Dans le workspace, cliquer sur **+ New** → **Data Agent**
2. Nom : `ESG Manager`
3. Description : `Assistant ESG & Carbon Analytics`

### 10.2 Associer le Semantic Model

1. Dans **Agent Settings** → **Data Sources**
2. **Add Data Source** → **Semantic Model**
3. Sélectionner : `ESG_Analytics`
4. **Permissions** : Read
5. **Tables** : Sélectionner toutes (10 tables)
6. **Save**

### 10.3 Configurer le System Prompt

1. Dans **Agent Settings** → **Instructions**
2. Copier-coller le contenu de [`data_agent_instructions.md`](data_agent_instructions.md) (section "Tu es un Assistant ESG...")
3. **Save**

### 10.4 Paramètres Avancés

**Model** : GPT-4 Turbo  
**Temperature** : `0.3` (précision, pas de créativité)  
**Max Tokens** : `2000`  
**Top P** : `0.9`

### 10.5 Tester le Data Agent

Tester avec ces 5 questions :

```
Q1 : Quelles sont nos émissions totales en 2024 ?
Q2 : Quelle est notre part d'énergie renouvelable ?
Q3 : Combien de fournisseurs ont un rating ESG D ?
Q4 : Quel site a la meilleure carbon intensity ?
Q5 : Extrais les thèmes des rapports 2024
```

**Vérifier** :
- ✅ Réponses contiennent les unités (tonnes CO₂eq, %, etc.)
- ✅ Comparaisons vs baseline 2023 présentes
- ✅ Tableaux Markdown bien formatés
- ✅ AI Transformations fonctionnent (Q5)

---

## ✅ Checklist de Validation Finale

### Données

- [ ] 10 tables présentes dans Lakehouse
- [ ] `sustainability_reports_transformed` : 36 lignes
- [ ] `audit_notes_transformed` : 80 lignes
- [ ] Toutes les tables ont >0 lignes

### Semantic Model

- [ ] 10 tables importées
- [ ] 7 relations créées (sites ↔ autres tables)
- [ ] 17 measures DAX créées et fonctionnelles
- [ ] Preview des données fonctionne (pas d'erreurs)

### Dashboard

- [ ] 3 pages créées (Carbon Footprint, Suppliers, AI Insights)
- [ ] KPI Cards affichent des valeurs cohérentes
- [ ] Visuels interactifs (filtres fonctionnent)
- [ ] Pas d'erreurs de calcul DAX

### Data Agent

- [ ] Agent créé et associé au Semantic Model
- [ ] System Prompt configuré
- [ ] Test de 5 questions : 5/5 réponses correctes
- [ ] AI Transformations accessibles depuis l'agent

---

## 🎬 Scénario de Démo Recommandé

### Phase 1 : Dashboard (5 min)

1. Ouvrir **ESG Dashboard** → Page 1
2. Montrer KPI Cards : Scope 1/2/3, Carbon Intensity
3. **Clic sur carte Lyon** → Détail du site (drill-through)
4. **Filtre sur 2024** → Évolution mensuelle Scope 1+2

### Phase 2 : Data Agent Questions (7 min)

1. Ouvrir **Data Agent** → `ESG Manager`
2. Poser 5-7 questions (cf. [`questions_demo.md`](questions_demo.md)) :
   - "Quelles sont nos émissions 2024 ?"
   - "Quel site a la meilleure carbon intensity ?"
   - "Liste les fournisseurs rating D"
   - "Extrais les thèmes des rapports 2024"
   - "Recommandations audit Shanghai ?"

### Phase 3 : AI Insights (3 min)

1. Dashboard → Page 3 (AI Insights)
2. Montrer **Word Cloud** des thèmes
3. Montrer **Pie Chart** classification audits
4. **Table** : Recommandations des audits négatifs

### Phase 4 : What-If Scenario (2 min)

1. Data Agent : "Si on remplace les chaudières gaz par pompes à chaleur, impact Scope 1 ?"
2. Montrer calcul estimé de réduction

**Durée totale** : 17 minutes

---

## 🔧 Troubleshooting

### Problème : AI Transformation échoue

**Cause** : Capacité Fabric insuffisante (besoin F4 minimum)

**Solution** :
1. Workspace Settings → Capacity
2. Vérifier que Capacity ≥ F4
3. Si F2, passer temporairement à F4 pour les transformations

### Problème : Relations ne fonctionnent pas

**Cause** : Clés étrangères NULL ou types incompatibles

**Solution** :
1. Vérifier types de colonnes (STRING vs INTEGER)
2. Filtrer les NULL : `CALCULATE(..., NOT(ISBLANK(...)))`

### Problème : Data Agent ne répond pas correctement

**Cause** : System Prompt incomplet ou Semantic Model non connecté

**Solution** :
1. Vérifier que le Semantic Model est bien associé
2. Re-coller le System Prompt complet
3. Tester avec question simple : "Combien de sites ?"

### Problème : Dates non reconnues

**Cause** : Format de date incorrect dans CSV

**Solution** :
1. Vérifier format dans CSV : `YYYY-MM-DD`
2. Forcer type lors de l'import : DATE (pas STRING)

---

## 📚 Ressources Complémentaires

- **Schéma des données** : [`schema.md`](schema.md)
- **Histoire de la démo** : [`demo_story.md`](demo_story.md)
- **Questions de test** : [`questions_demo.md`](questions_demo.md)
- **Configuration Data Agent** : [`data_agent_instructions.md`](data_agent_instructions.md)
- **Exemples détaillés** : [`data_agent_examples.md`](data_agent_examples.md)

---

**Durée totale de déploiement** : 2-3 heures (selon vitesse réseau)

**Happy Fabric Setup! 🚀✅**
