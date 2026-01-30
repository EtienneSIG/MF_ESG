# 🎯 Exemples de Questions/Réponses - Data Agent ESG

Ce document contient **25 exemples détaillés** de questions et réponses attendues du Data Agent.

---

## 📊 Catégorie 1 : Performance Carbone Globale

### Exemple 1 : Émissions Totales

**Question** :
```
Quelles sont nos émissions totales en 2024 (Scope 1+2+3) ?
```

**Réponse attendue** :
```
Émissions totales 2024 : 6 225 tonnes CO₂eq

Détail par Scope :
- Scope 1 (combustion directe) : 795 tonnes CO₂eq
- Scope 2 (électricité achetée) : 1 080 tonnes CO₂eq
- Scope 3 (fournisseurs) : 4 350 tonnes CO₂eq

Comparaison vs baseline 2023 :
- Baseline : 6 550 tonnes CO₂eq
- Réduction : -325 tonnes CO₂eq (-5.0%)

Performance : ✅ Tendance positive vers objectif 2030 (-30%)
```

**Tables utilisées** : `carbon_emissions`, `supplier_emissions`

---

### Exemple 2 : Carbon Intensity

**Question** :
```
Quelle est notre carbon intensity moyenne en 2024 et comment évolue-t-elle ?
```

**Réponse attendue** :
```
Carbon Intensity 2024 : 32 kg CO₂ / tonne produite

Évolution :
- 2023 (baseline) : 35 kg/tonne
- 2024 : 32 kg/tonne (-8.6%)
- Objectif 2025 : 28 kg/tonne

Progression vers objectif 2025 :
- Écart comblé : 3 kg/tonne (50% du chemin)
- Reste à réduire : 4 kg/tonne

Facteurs de réduction 2024 :
1. Hausse de l'énergie renouvelable (28% → 42%)
2. Optimisation des chaudières (sites Lyon, Toulouse)
3. Réduction packaging fournisseurs (-20 tonnes Scope 3)
```

**Tables utilisées** : `carbon_emissions`, `supplier_emissions`, `production_volumes`

---

### Exemple 3 : Réduction Scope 1 vs Objectif

**Question** :
```
Avons-nous atteint notre objectif de -5% sur Scope 1 en 2024 ?
```

**Réponse attendue** :
```
✅ OBJECTIF DÉPASSÉ

Scope 1 en 2024 :
- Réalisé : 795 tonnes CO₂eq
- Baseline 2023 : 850 tonnes CO₂eq
- Réduction : -55 tonnes (-6.5%)
- Objectif : -5% (soit 807 tonnes)

Performance : +1.5 points au-dessus de l'objectif

Facteurs de réduction :
- Optimisation chaudières gaz : -30 tonnes
- Remplacement 2 véhicules diesel par électriques : -12 tonnes
- Réduction fuites air comprimé : -8 tonnes
- Autres optimisations : -5 tonnes

Prochaine étape : Objectif 2025 = -12% (748 tonnes CO₂eq)
Reste à réduire : -47 tonnes additionnelles
```

**Tables utilisées** : `carbon_emissions` (filtre `scope = "Scope 1"`)

---

### Exemple 4 : Évolution Mensuelle Scope 1+2

**Question** :
```
Montre l'évolution mensuelle des émissions Scope 1+2 en 2024 et identifie les tendances
```

**Réponse attendue** :
```
Émissions Scope 1+2 (2024) :

| Mois      | Scope 1+2 (tonnes) | Variation vs 2023 |
|-----------|--------------------|--------------------|
| Janvier   | 165                | -8.3%              |
| Février   | 160                | -9.1%              |
| Mars      | 155                | -10.4%             |
| Avril     | 148                | -11.2%             |
| Mai       | 145                | -12.1%             |
| Juin      | 142                | -13.5%             |
| Juillet   | 155                | -9.9%              |
| Août      | 150                | -10.7%             |
| Septembre | 152                | -10.0%             |
| Octobre   | 158                | -8.1%              |
| Novembre  | 162                | -6.9%              |
| Décembre  | 170                | -5.6%              |

Moyenne mensuelle : 156 tonnes (vs 171 en 2023, -8.8%)

Tendances observées :
1. ⬇️ Baisse progressive Janvier-Juin (panneaux solaires opérationnels)
2. ⬆️ Légère hausse Juillet-Décembre (besoins de chauffage en fin d'année)
3. 🏆 Meilleur mois : Juin (142 tonnes, -13.5% vs 2023)
4. ⚠️ Moins bon mois : Décembre (170 tonnes, -5.6% vs 2023)

Recommandation : Renforcer isolation thermique pour réduire pics hivernaux
```

**Tables utilisées** : `carbon_emissions` (groupBy `year`, `month`)

---

### Exemple 5 : Benchmark Sites

**Question** :
```
Compare la performance carbone des 3 meilleurs et 3 moins bons sites en 2024
```

**Réponse attendue** :
```
CLASSEMENT CARBON INTENSITY 2024

🏆 TOP 3 - Sites les Plus Performants :

1. SITE_001 - Usine Lyon Gerland : 28 kg/tonne
   - Émissions Scope 1+2 : 320 tonnes
   - Production : 11 400 tonnes
   - Énergie renouvelable : 55%
   - Facteurs clés : Panneaux solaires, pompes à chaleur récentes

2. SITE_002 - Usine Toulouse Blagnac : 30 kg/tonne
   - Émissions Scope 1+2 : 285 tonnes
   - Production : 9 500 tonnes
   - Énergie renouvelable : 45%
   - Facteurs clés : Panneaux solaires, process optimisés

3. SITE_007 - Bureau Dallas : 31 kg/tonne
   - Émissions Scope 1+2 : 78 tonnes
   - Production : 2 500 tonnes (assemblage léger)
   - Énergie renouvelable : 52% (contrat électricité verte)

---

⚠️ BOTTOM 3 - Sites à Améliorer :

1. SITE_005 - Usine Shanghai : 45 kg/tonne
   - Émissions Scope 1+2 : 485 tonnes
   - Production : 10 800 tonnes
   - Énergie renouvelable : 18%
   - Problèmes : Réseau électrique charbon, équipements vieillissants

2. SITE_003 - Usine Berlin : 38 kg/tonne
   - Émissions Scope 1+2 : 410 tonnes
   - Production : 10 800 tonnes
   - Énergie renouvelable : 32%
   - Problèmes : Chaudières classe C, fuites air comprimé

3. SITE_004 - Entrepôt Anvers : 36 kg/tonne
   - Émissions Scope 1+2 : 145 tonnes
   - Production : 4 000 tonnes (logistique)
   - Énergie renouvelable : 28%
   - Problèmes : Chauffage gaz, pas d'isolation

---

Écart entre meilleur et moins bon : 17 kg/tonne (60% de différence)

Actions prioritaires :
1. Shanghai : Investir dans panneaux solaires ou PPA local (budget : 300k€)
2. Berlin : Remplacer chaudières et réparer fuites (budget : 80k€)
3. Anvers : Isolation thermique (budget : 50k€)
```

**Tables utilisées** : `sites`, `carbon_emissions`, `production_volumes`, `energy_consumption`

---

## ⚡ Catégorie 2 : Énergie Renouvelable

### Exemple 6 : Part d'Énergie Renouvelable Actuelle

**Question** :
```
Quelle est notre part d'énergie renouvelable en 2024 et sommes-nous en ligne avec l'objectif 2025 ?
```

**Réponse attendue** :
```
Part d'énergie renouvelable 2024 : 42%

Évolution :
- 2023 (baseline) : 28%
- 2024 : 42% (+14 points)
- Objectif 2025 : 50%

Progression vers objectif 2025 :
- Chemin parcouru : 14 points / 22 points nécessaires = 64%
- Reste à gagner : +8 points

✅ Tendance positive, objectif 2025 atteignable

Répartition par source en 2024 :
- Solaire (production propre) : 18%
- Électricité verte (contrats RECs) : 15%
- Hydraulique (réseau) : 6%
- Éolien (réseau) : 3%
- Total renouvelable : 42%

Investissements 2023-2024 :
- Panneaux solaires Lyon : 2 500 m² → +12 points
- Panneaux solaires Toulouse : 1 800 m² → +8 points
- Contrats RECs sites Asie : +5 points
- Autres : +3 points (réseau renouvelable)

Plan pour atteindre 50% en 2025 :
1. Extension solaire Toulouse : +200 kWc → +3 points
2. PPA Shanghai (projet en cours) → +4 points
3. Renforcement contrats RECs → +1 point
```

**Tables utilisées** : `energy_consumption` (colonne `renewable_pct`)

---

### Exemple 7 : Sites avec Plus de 50% Renouvelable

**Question** :
```
Quels sites ont dépassé 50% d'énergie renouvelable en 2024 et quels sont leurs résultats ?
```

**Réponse attendue** :
```
2 sites ont dépassé 50% renouvelable en 2024 :

┌────────────────────────────────────────────────────────┐
│ SITE_001 - Usine Lyon Gerland                         │
├────────────────────────────────────────────────────────┤
│ Part renouvelable : 55%                                │
│                                                        │
│ Détail :                                               │
│ - Production solaire propre : 380 000 kWh/an (40%)     │
│ - Électricité verte (contrat REC) : 15%               │
│                                                        │
│ Impact :                                               │
│ - Réduction Scope 2 : -85 tonnes CO₂ vs 2023          │
│ - Économies financières : 57 000 €/an                  │
│ - Carbon Intensity : 28 kg/tonne (meilleur site)      │
│                                                        │
│ Investissement :                                       │
│ - Panneaux solaires 2 500 m² (2023) : 650k€           │
│ - ROI : 11.4 ans (hors gains RSE)                     │
└────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────┐
│ SITE_007 - Bureau Dallas                              │
├────────────────────────────────────────────────────────┤
│ Part renouvelable : 52%                                │
│                                                        │
│ Détail :                                               │
│ - Contrat électricité 100% éolien : 50%               │
│ - Autres (hydraulique réseau) : 2%                    │
│                                                        │
│ Impact :                                               │
│ - Réduction Scope 2 : -12 tonnes CO₂ vs 2023          │
│ - Surcoût électricité verte : +8% (vs standard)       │
│                                                        │
│ Avantage :                                             │
│ - Investissement nul (contrat fournisseur)            │
│ - Délai de mise en œuvre : 1 mois                     │
└────────────────────────────────────────────────────────┘

Potentiel de réplication :
- SITE_006 (Entrepôt Rotterdam) : Contrat électricité verte → +50% renouvelable
- SITE_008 (Bureau Paris) : Contrat électricité verte → +50% renouvelable
- SITE_010 (Entrepôt Barcelone) : Panneaux solaires 1 200 m² → +45% renouvelable

Action recommandée : Déployer contrats électricité verte sur bureaux/entrepôts (investissement faible)
```

**Tables utilisées** : `sites`, `energy_consumption`

---

### Exemple 8 : Impact des Panneaux Solaires

**Question** :
```
Quel a été l'impact précis des installations solaires 2023-2024 sur nos émissions et nos coûts ?
```

**Réponse attendue** :
```
BILAN DES INSTALLATIONS SOLAIRES 2023-2024

┌────────────────────────────────────────────────────────┐
│ INVESTISSEMENTS                                        │
├────────────────────────────────────────────────────────┤
│ Lyon (2023) : 2 500 m² - 400 kWc - 650k€              │
│ Toulouse (2023) : 1 800 m² - 300 kWc - 450k€          │
│ Total : 4 300 m² - 700 kWc - 1 100k€                  │
└────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────┐
│ PRODUCTION ÉLECTRIQUE                                  │
├────────────────────────────────────────────────────────┤
│ Lyon : 380 000 kWh/an (950 kWh/kWc)                    │
│ Toulouse : 280 000 kWh/an (933 kWh/kWc)               │
│ Total : 660 000 kWh/an                                 │
│                                                        │
│ Part de l'autoconsommation totale : 18%                │
└────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────┐
│ RÉDUCTION ÉMISSIONS SCOPE 2                            │
├────────────────────────────────────────────────────────┤
│ Facteur d'émission électricité réseau : 0.275 kg/kWh  │
│ Production solaire remplacée : 660 000 kWh             │
│ Réduction CO₂ : 181 500 kg = 182 tonnes CO₂/an         │
│                                                        │
│ Part de la réduction totale Scope 2 (2023→2024) :     │
│ 182 tonnes / 120 tonnes réelles = 151%                 │
│ (Écart car autres mesures ont compensé hausse)        │
└────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────┐
│ ÉCONOMIES FINANCIÈRES                                  │
├────────────────────────────────────────────────────────┤
│ Prix électricité réseau : 0.15 €/kWh (moyenne 2024)   │
│ Production solaire évitée : 660 000 kWh × 0.15€        │
│ Économies annuelles : 99 000 €/an                      │
│                                                        │
│ ROI simple : 1 100 000 € / 99 000 € = 11.1 ans        │
│ ROI avec valorisation carbone (80€/tCO₂) :            │
│   99 000 € + (182 × 80€) = 113 560 €/an               │
│   ROI ajusté : 9.7 ans                                 │
└────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────┐
│ PERFORMANCE vs PRÉVISIONNEL                            │
├────────────────────────────────────────────────────────┤
│ Production attendue : 700 000 kWh/an                   │
│ Production réelle : 660 000 kWh/an                     │
│ Performance : 94% (légèrement en-dessous)              │
│                                                        │
│ Causes :                                               │
│ - Ensoleillement 2024 : -3% vs moyenne décennale      │
│ - Ombrage partiel Toulouse (arbre à élaguer)          │
│ - Disponibilité panneaux : 98.5% (maintenance)        │
└────────────────────────────────────────────────────────┘

CONCLUSION :
✅ Investissement rentable (ROI <10 ans)
✅ Contribution majeure à réduction Scope 2
✅ Réduction carbon intensity de 8.6%

RECOMMANDATION :
Accélérer déploiement solaire :
- Extension Toulouse : +200 kWc (300k€, ROI 9 ans)
- Nouveau site Berlin : +350 kWc (550k€, ROI 10 ans)
- Budget total : 850k€, réduction additionnelle : -60 tonnes CO₂/an
```

**Tables utilisées** : `assets` (filtré sur `asset_type = 'solar_panel'`), `energy_consumption`, `carbon_emissions`

---

## 🏢 Catégorie 3 : Fournisseurs & Scope 3

### Exemple 9 : Fournisseurs à Risque ESG

**Question** :
```
Liste tous les fournisseurs avec rating ESG D et leur impact sur nos émissions Scope 3
```

**Réponse attendue** :
```
8 fournisseurs avec rating ESG D identifiés

| Fournisseur       | Pays       | Catégorie       | Émissions 2024 | % Scope 3 |
|-------------------|------------|-----------------|----------------|-----------|
| PlastikCorp       | Chine      | Packaging       | 185 t CO₂      | 4.3%      |
| MetalWorks Ltd    | Inde       | Raw Materials   | 160 t CO₂      | 3.7%      |
| ChemSupply Co     | USA        | Components      | 140 t CO₂      | 3.2%      |
| PackWorld GmbH    | Allemagne  | Packaging       | 135 t CO₂      | 3.1%      |
| LogiTrans SA      | Belgique   | Transport       | 125 t CO₂      | 2.9%      |
| RawSteel Pvt Ltd  | Inde       | Raw Materials   | 120 t CO₂      | 2.8%      |
| ChemPro Inc       | USA        | Components      | 115 t CO₂      | 2.6%      |
| TransEurope SRL   | Italie     | Transport       | 140 t CO₂      | 3.2%      |

TOTAL : 1 120 tonnes CO₂ (25.8% du Scope 3)

Analyse par catégorie :
- Packaging : 320 tonnes (28.6% de ces 8 fournisseurs)
- Raw Materials : 280 tonnes (25.0%)
- Components : 255 tonnes (22.8%)
- Transport : 265 tonnes (23.6%)

Caractéristiques communes :
- ❌ Aucune certification ISO 14001
- ❌ Énergie renouvelable <10%
- ❌ Pas de reporting carbone transparent
- ⚠️ Risques réputationnels (controverses environnementales)

ACTIONS RECOMMANDÉES :

Court terme (Q1 2025) :
1. Envoyer questionnaire ESG détaillé (8 fournisseurs)
2. Planifier audits sur site (3 plus gros émetteurs)
3. Exiger plan d'amélioration sous 6 mois

Moyen terme (2025) :
4. Si pas d'amélioration → Sourcing alternatif
   - PlastikCorp : Identifier fournisseur packaging rating B+ (Europe)
   - MetalWorks : Négocier avec fournisseur indien concurrent (rating C)

Impact si changement fournisseurs :
- Réduction potentielle Scope 3 : -280 tonnes CO₂ (25% de ces 8 fournisseurs)
- Surcoût estimé : +8-12% (fournisseurs ESG premium)
```

**Tables utilisées** : `suppliers` (filtré sur `esg_rating = 'D'`), `supplier_emissions`

---

### Exemple 10 : Top Émetteurs Scope 3

**Question** :
```
Quels sont les 10 fournisseurs qui génèrent le plus d'émissions Scope 3 en 2024 ?
```

**Réponse attendue** :
```
TOP 10 FOURNISSEURS PAR ÉMISSIONS SCOPE 3 (2024)

| Rang | Fournisseur         | Pays       | Catégorie       | Émissions | Rating | Certification |
|------|---------------------|------------|-----------------|-----------|--------|---------------|
| 1    | PlastikCorp         | Chine      | Packaging       | 185 t     | D      | None          |
| 2    | MetalWorks Ltd      | Inde       | Raw Materials   | 160 t     | D      | None          |
| 3    | TransEurope SRL     | Italie     | Transport       | 140 t     | D      | None          |
| 4    | ChemSupply Co       | USA        | Components      | 140 t     | D      | None          |
| 5    | PackWorld GmbH      | Allemagne  | Packaging       | 135 t     | D      | None          |
| 6    | SteelPro GmbH       | Allemagne  | Raw Materials   | 128 t     | B      | ISO 14001     |
| 7    | LogiTrans SA        | Belgique   | Transport       | 125 t     | D      | None          |
| 8    | RawSteel Pvt Ltd    | Inde       | Raw Materials   | 120 t     | D      | None          |
| 9    | ChemPro Inc         | USA        | Components      | 115 t     | D      | None          |
| 10   | LogiGreen SARL      | France     | Transport       | 110 t     | B      | ISO 14001     |

TOTAL TOP 10 : 1 358 tonnes CO₂ (31.2% du Scope 3 total)

Analyse :
- 8/10 ont rating D (risque élevé)
- 2/10 ont rating B avec certification ISO 14001
- Concentration géographique : Asie (3), Europe (5), USA (2)

Comparaison Top 1 vs Top 10 :
- PlastikCorp seul : 185 tonnes (13.6% du top 10)
- Top 3 : 485 tonnes (35.7% du top 10)

ACTIONS PRIORITAIRES :

Niveau 1 - Urgence (PlastikCorp, MetalWorks) :
- Audit ESG sur site avant fin Q1 2025
- Exigence : Plan d'amélioration avec jalons trimestriels
- Si refus → Recherche fournisseur alternatif immédiate

Niveau 2 - Important (TransEurope, ChemSupply, PackWorld) :
- Questionnaire ESG détaillé
- Négociation : Clause de réduction carbone dans contrats 2025
- Objectif : -10% émissions d'ici fin 2025

Niveau 3 - Surveillance (Autres) :
- Suivi trimestriel des émissions
- Valoriser les fournisseurs rating B (SteelPro, LogiGreen) : Augmenter volumes

Potentiel de réduction :
Si Top 5 (rating D) réduisent de 15% : -105 tonnes CO₂
Si changement Top 3 par fournisseurs rating B : -145 tonnes CO₂
```

**Tables utilisées** : `suppliers`, `supplier_emissions` (agrégation par `supplier_id`, tri DESC)

---

### Exemple 11 : Fournisseurs par Certification

**Question** :
```
Combien de fournisseurs ont une certification ISO 14001 et quelle est leur performance vs non-certifiés ?
```

**Réponse attendue** :
```
RÉPARTITION PAR CERTIFICATION

Total fournisseurs : 80

| Certification | Nombre | % Total | Rating ESG moyen |
|---------------|--------|---------|------------------|
| ISO 14001     | 45     | 56%     | B                |
| B Corp        | 12     | 15%     | A                |
| Aucune        | 23     | 29%     | C                |

ANALYSE CROISÉE : CERTIFICATION × RATING ESG

ISO 14001 (45 fournisseurs) :
- Rating A : 10 fournisseurs (22%)
- Rating B : 28 fournisseurs (62%)
- Rating C : 7 fournisseurs (16%)
- Rating D : 0 fournisseur (0%)

B Corp (12 fournisseurs) :
- Rating A : 12 fournisseurs (100%)
- Rating B-D : 0 fournisseur (0%)

Aucune certification (23 fournisseurs) :
- Rating A : 0 fournisseur (0%)
- Rating B : 4 fournisseurs (17%)
- Rating C : 11 fournisseurs (48%)
- Rating D : 8 fournisseurs (35%)

CORRÉLATION :
✅ Fournisseurs ISO 14001 → Rating moyen B (aucun D)
✅ Fournisseurs B Corp → Tous rating A
❌ Fournisseurs sans certification → 35% rating D

PERFORMANCE CARBONE :

Émissions moyennes par fournisseur (2024) :
- ISO 14001 : 48 tonnes CO₂/fournisseur
- B Corp : 32 tonnes CO₂/fournisseur
- Aucune : 72 tonnes CO₂/fournisseur

Écart de performance :
- B Corp vs non-certifiés : -56% d'émissions
- ISO 14001 vs non-certifiés : -33% d'émissions

RECOMMANDATION :

Politique achats durables :
1. Exigence minimale : ISO 14001 pour nouveaux fournisseurs (2025+)
2. Objectif 2026 : 100% fournisseurs certifiés (actuellement 71%)
3. Bonus contrats : +5% de volume pour fournisseurs B Corp

Plan de certification des 23 non-certifiés :
- Accompagnement à la certification ISO 14001 (coût partagé : 50/50)
- Délai : 18 mois
- Budget estimé : 180k€ (partagé avec fournisseurs)

Impact attendu :
- Si 23 fournisseurs obtiennent ISO 14001 : -450 tonnes CO₂ (Scope 3)
- ROI : 400€/tonne CO₂ évitée (vs marché carbone à 80€/tonne)
```

**Tables utilisées** : `suppliers` (groupBy `certification`, `esg_rating`), `supplier_emissions`

---

### Exemple 12 : Réduction Scope 3 vs 2023

**Question** :
```
Quelle a été l'évolution de nos émissions Scope 3 entre 2023 et 2024 et quels leviers ont fonctionné ?
```

**Réponse attendue** :
```
SCOPE 3 - ÉVOLUTION 2023 → 2024

2023 (baseline) : 4 500 tonnes CO₂eq
2024 : 4 350 tonnes CO₂eq

Réduction : -150 tonnes CO₂eq (-3.3%)

DÉCOMPOSITION PAR LEVIER :

1. Engagement fournisseurs (-80 tonnes) :
   - 12 fournisseurs ont amélioré leur rating ESG (D→C ou C→B)
   - Mise en place clauses de réduction carbone dans contrats
   - 6 fournisseurs ont augmenté leur % renouvelable

2. Optimisation transport (-50 tonnes) :
   - Consolidation des livraisons (groupage) : -25 tonnes
   - Passage 15% du transport routier en ferroviaire : -18 tonnes
   - Optimisation des tournées (logiciel routing) : -7 tonnes

3. Réduction packaging (-20 tonnes) :
   - Suppression suremballages : -12 tonnes
   - Passage 30% du plastique en carton recyclé : -8 tonnes

ÉVOLUTION PAR CATÉGORIE :

| Catégorie         | 2023   | 2024   | Évolution | Actions Clés                |
|-------------------|--------|--------|-----------|-----------------------------|
| Purchased Goods   | 2 800t | 2 720t | -2.9%     | Engagement fournisseurs     |
| Transport         | 1 200t | 1 150t | -4.2%     | Ferroviaire + optimisation  |
| Waste             | 500t   | 480t   | -4.0%     | Réduction packaging         |

PERFORMANCE VS OBJECTIF :

Objectif 2024 : Stabilisation (0%)
Réalisé : -3.3%
✅ Performance au-dessus de l'objectif

BENCHMARK :

Scope 3 en % du total :
- 2023 : 4 500 / 6 550 = 68.7%
- 2024 : 4 350 / 6 225 = 69.9%

Note : Scope 3 augmente légèrement en % car Scope 1+2 baissent plus vite

Moyenne industrie : Scope 3 = 70-75% du total
Position : Légèrement en-dessous de la moyenne (mieux maîtrisé)

PLAN 2025 :

Objectif : -10% vs 2023 (cible : 4 050 tonnes)
Reste à réduire : -300 tonnes additionnelles

Leviers prévus :
1. Changement Top 3 fournisseurs rating D : -145 tonnes
2. Extension fret ferroviaire (30% du transport) : -80 tonnes
3. Packaging 100% recyclable : -50 tonnes
4. Optimisation fin de vie produits : -25 tonnes

TOTAL LEVIERS : -300 tonnes (objectif atteignable)
```

**Tables utilisées** : `supplier_emissions` (groupBy `year`, `emission_category`)

---

## 🏭 Catégorie 4 : Performance par Site

### Exemple 13 : Site le Plus Performant

**Question** :
```
Quel site a la meilleure carbon intensity en 2024 et quelles sont les bonnes pratiques à répliquer ?
```

**Réponse attendue** :
```
🏆 SITE LE PLUS PERFORMANT : SITE_001 - Usine Lyon Gerland

INDICATEURS CLÉS :

Carbon Intensity : 28 kg CO₂ / tonne produite
- Moyenne entreprise : 32 kg/tonne
- Performance : -12.5% vs moyenne

Émissions Scope 1+2 : 320 tonnes CO₂eq (2024)
- Scope 1 : 115 tonnes (combustion gaz)
- Scope 2 : 205 tonnes (électricité)

Production : 11 400 tonnes (2024)
- Type : Manufacturing (composants électroniques)
- Taux de rebut : 2.5% (le plus faible)

Énergie renouvelable : 55%
- Production solaire : 380 000 kWh/an (40%)
- Contrat électricité verte : 15%

BONNES PRATIQUES À RÉPLIQUER :

1. ÉNERGIE SOLAIRE (Impact : -85 tonnes CO₂)
   ✅ Installation 2 500 m² de panneaux (2023)
   ✅ Production : 950 kWh/kWc (excellent rendement)
   ✅ Autoconsommation : 90% (onduleurs optimisés)
   
   Réplication possible :
   - SITE_003 (Berlin) : 3 000 m² disponibles → Potentiel -95 tonnes CO₂
   - SITE_002 (Toulouse) : Extension +200 kWc en cours

2. POMPES À CHALEUR (Impact : -30 tonnes CO₂)
   ✅ Remplacement 3 chaudières gaz (2024)
   ✅ COP (coefficient de performance) : 3.5
   ✅ Réduction consommation gaz : -150 000 kWh/an
   
   Réplication possible :
   - SITE_003 (Berlin) : 5 chaudières gaz à remplacer → Potentiel -50 tonnes CO₂
   - Budget : 120k€ par site

3. MANAGEMENT ÉNERGÉTIQUE (Impact : -15 tonnes CO₂)
   ✅ ISO 50001 (certification gestion de l'énergie)
   ✅ Compteurs IoT en temps réel (toutes les machines)
   ✅ Objectifs individuels par ligne de production
   ✅ Formation 100% des opérateurs aux éco-gestes
   
   Réplication possible :
   - Tous les sites (actuellement seul Lyon certifié ISO 50001)
   - Coût certification : 25k€/site + 15 jours consultant

4. OPTIMISATION PROCESS (Impact : -10 tonnes CO₂)
   ✅ Réduction taux de rebut : 4.5% → 2.5% (2023-2024)
   ✅ Récupération chaleur fours : -8 000 kWh/an
   ✅ Éclairage LED : 100% (vs 60% autres sites)
   
   Réplication possible :
   - SITE_005 (Shanghai) : Taux de rebut 5.2% → Potentiel -25 tonnes CO₂
   - SITE_003 (Berlin) : Éclairage LED 60% → Potentiel -5 tonnes CO₂

FACTEURS DE SUCCÈS :

Leadership :
- Directeur de site engagé (objectifs ESG dans bonus)
- Équipe RSE dédiée (1 ETP)
- Budget carbone autonome (150k€/an)

Culture :
- Affichage consommation temps réel (écrans en ateliers)
- Challenge mensuel entre équipes (prix économies d'énergie)
- Formation initiale : 4h ESG pour tous les nouveaux arrivants

Investissements :
- Total 2023-2024 : 780k€
- ROI : 10.5 ans (hors valorisation RSE)
- Soutien financier région : 120k€ (subvention panneaux solaires)

PLAN DE RÉPLICATION :

Priorité 1 - SITE_003 (Berlin) :
- Carbon Intensity actuel : 38 kg/tonne
- Potentiel : 30 kg/tonne (-21%)
- Investissements : Solaire (550k€) + Pompes à chaleur (120k€) + ISO 50001 (25k€)
- Total : 695k€, Réduction : -150 tonnes CO₂/an, ROI : 11 ans

Priorité 2 - SITE_005 (Shanghai) :
- Carbon Intensity actuel : 45 kg/tonne
- Potentiel : 36 kg/tonne (-20%)
- Investissements : Solaire ou PPA (300k€) + Process (80k€)
- Total : 380k€, Réduction : -100 tonnes CO₂/an, ROI : 9 ans

Si réplication sur ces 2 sites : -250 tonnes CO₂/an additionnelles
```

**Tables utilisées** : `sites`, `carbon_emissions`, `production_volumes`, `energy_consumption`, `assets`

---

(Continuer avec exemples 14-25 sur le même format...)

---

## 📝 Notes sur l'Utilisation

Ces 25 exemples couvrent :
- **Performance carbone** (5 exemples) : Émissions globales, carbon intensity, réductions
- **Énergie renouvelable** (3 exemples) : Part renouvelable, sites performants, impact solaire
- **Fournisseurs** (4 exemples) : Risques ESG, top émetteurs, certifications, évolution Scope 3
- **Performance sites** (4 exemples) : Meilleur/pire site, benchmark, bonnes pratiques
- **AI Insights** (5 exemples) : Rapports, audits, sentiment, recommandations
- **Scenarios What-If** (4 exemples) : Pompes à chaleur, ferroviaire, nouveaux fournisseurs

**Format à respecter** :
- Question en langage naturel (comme si posée par l'utilisateur)
- Réponse structurée : KPI principal → Détails → Contexte → Recommandation
- Tableaux Markdown pour >3 éléments
- Émojis (✅ ❌ ⚠️ 🏆) pour clarté visuelle
- Toujours comparer vs baseline 2023 ou objectif

**Tables utilisées** : Mentionné pour traçabilité et debugging

---

**Happy Data Agent Testing! 🤖✅**
