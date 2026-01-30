# 📖 Histoire de la Démo - ESG & Carbon Analytics

Cette démo raconte l'histoire d'**Emma Rousseau**, Directrice RSE (Responsabilité Sociétale des Entreprises) d'une entreprise industrielle européenne, dans sa mission de réduction de l'empreinte carbone.

---

## 👤 Personnages

### Emma Rousseau - Directrice RSE
- **Mission** : Réduire l'empreinte carbone de 30% d'ici 2030 (vs baseline 2023)
- **Objectifs 2024** : -5% Scope 1, -8% Scope 2
- **Objectifs 2025** : -12% Scope 1, -15% Scope 2
- **Défis** : Décarbonation, fournisseurs à risque, budget contraint

### L'Équipe
- **Marc Leblanc** : Auditeur externe (EcoAudit SAS)
- **Sophie Martin** : Responsable Énergie & Climat
- **Julie Fontaine** : Responsable Achats Durables
- **Pierre Blanchard** : Directeur Industriel

---

## 🌍 Contexte de l'Entreprise

**Secteur** : Industrie manufacturière (composants électroniques)

**Empreinte Carbone 2023 (baseline)** :
- Scope 1 (combustion directe) : **850 tonnes CO₂eq**
- Scope 2 (électricité achetée) : **1 200 tonnes CO₂eq**
- Scope 3 (fournisseurs) : **4 500 tonnes CO₂eq**
- **Total : 6 550 tonnes CO₂eq**

**Parc de Sites** :
- 4 usines de production (Europe & Asie)
- 4 entrepôts logistiques
- 4 bureaux commerciaux

**Indicateur Clé** : Carbon Intensity = 35 kg CO₂ / tonne produite (2023)

---

## 📅 Chronologie de la Démo

### 🗓️ Janvier 2023 : La Prise de Conscience

**Contexte** : L'entreprise doit se conformer à la directive CSRD (Corporate Sustainability Reporting Directive).

**Emma à la Direction Générale** :
> "Nous devons mesurer précisément nos émissions Scope 1, 2 et 3. Actuellement, nous n'avons que des estimations. Je propose de déployer OneLake avec des Shortcuts vers nos systèmes ERP, IoT et fournisseurs."

**Décision** :
- ✅ Déploiement Microsoft Fabric Q1 2023
- ✅ Installation de compteurs IoT sur sites
- ✅ Collecte données fournisseurs via plateforme EcoVadis

**Premier Bilan (Mars 2023)** :
- 6 550 tonnes CO₂eq mesurées
- Carbon Intensity : 35 kg/tonne
- Seulement 25% d'énergie renouvelable

---

### ☀️ Juin 2023 : Lancement du Plan Solaire

**Contexte** : Les prix de l'électricité restent élevés. Emma propose d'installer des panneaux solaires.

**Investissement** :
- **Lyon** : 2 500 m² de panneaux (400 kWc)
- **Toulouse** : 1 800 m² de panneaux (300 kWc)
- **Budget** : 1,2 M€
- **ROI attendu** : 7 ans

**Emma à Sophie (Responsable Énergie)** :
> "Sophie, peux-tu simuler l'impact de ces installations sur notre carbon intensity ?"

**Résultat (Simulation Data Agent)** :
```
Question à Data Agent :
"Quelle serait notre part d'énergie renouvelable si on installe 
700 kWc de panneaux solaires sur Lyon et Toulouse ?"

Réponse :
Avec une production estimée de 900 000 kWh/an, votre part 
d'énergie renouvelable passerait de 25% à 38% (+13 points).
```

**Décision** :
- ✅ Projet approuvé en Juillet 2023
- ✅ Installation Q3-Q4 2023
- ✅ Mise en service Janvier 2024

---

### 📊 Décembre 2023 : Bilan Annuel

**Contexte** : Emma prépare le rapport de durabilité annuel.

**Données 2023** :
- Scope 1+2 : 2 050 tonnes CO₂eq (stable)
- Scope 3 : 4 500 tonnes CO₂eq (stable)
- Énergie renouvelable : 28% (légère hausse en fin d'année)

**Extraction des KPI avec Data Agent** :
```
Question :
"Génère un résumé de notre performance carbone 2023 avec 
comparaison vs objectif 2024"

Réponse :
PERFORMANCE 2023
- Émissions totales : 6 550 tonnes CO₂eq
- Carbon Intensity : 35 kg/tonne
- Énergie renouvelable : 28%

OBJECTIFS 2024
- Réduction Scope 1 : -5% → cible 807 tonnes
- Réduction Scope 2 : -8% → cible 1 104 tonnes
- Énergie renouvelable : 40%

ÉCART À COMBLER
- Scope 1 : -43 tonnes CO₂ (optimisation chaudières)
- Scope 2 : -96 tonnes CO₂ (panneaux solaires)
```

**Rapport publié** : Mars 2024 (fichier `REPORT_2023_ANNUAL.txt`)

---

### 🌞 Avril 2024 : Résultats du Plan Solaire

**Contexte** : Les panneaux solaires sont opérationnels depuis 3 mois.

**Emma interroge le Data Agent** :
```
Question :
"Quelle est notre part d'énergie renouvelable en Q1 2024 
sur les sites Lyon et Toulouse ?"

Réponse :
LYON (SITE_001)
- Q1 2024 : 48% renouvelable (+23 points vs Q1 2023)
- Production solaire : 95 000 kWh
- Réduction Scope 2 : -22 tonnes CO₂

TOULOUSE (SITE_002)
- Q1 2024 : 42% renouvelable (+18 points vs Q1 2023)
- Production solaire : 68 000 kWh
- Réduction Scope 2 : -16 tonnes CO₂
```

**Constat** :
- ✅ Objectif 40% renouvelable dépassé sur ces 2 sites
- ⚠️ Sites Asie encore à 15% (électricité charbon dominante)

**Sophie (Responsable Énergie)** :
> "Emma, je recommande d'acheter des certificats d'énergie renouvelable (RECs) pour nos sites asiatiques. Coût estimé : 80k€/an pour passer à 50%."

---

### ⚠️ Juillet 2024 : Alerte Fournisseurs

**Contexte** : Emma reçoit un audit EcoVadis montrant que 8 fournisseurs ont un rating D (risque élevé).

**Emma à Julie (Achats Durables)** :
> "Julie, peux-tu lister les fournisseurs avec rating ESG D et leurs émissions Scope 3 ?"

**Requête Data Agent** :
```
Question :
"Liste les fournisseurs avec rating ESG D et calcule leur 
contribution aux émissions Scope 3"

Réponse :
8 fournisseurs avec rating D identifiés :

| Fournisseur       | Pays  | Catégorie       | Émissions 2024 (t CO₂) |
|-------------------|-------|-----------------|------------------------|
| PlastikCorp       | Chine | Packaging       | 185                    |
| MetalWorks Ltd    | Inde  | Raw Materials   | 160                    |
| ChemSupply Co     | USA   | Components      | 140                    |
| ...               | ...   | ...             | ...                    |

TOTAL : 1 120 tonnes CO₂ (25% du Scope 3)
```

**Décision** :
- 🚨 Plan d'action : Engagement fournisseurs à améliorer rating sous 12 mois
- 🚨 Si pas d'amélioration → Changement de fournisseur
- 📝 Audit sur site prévu pour PlastikCorp (plus gros émetteur)

---

### 🔍 Septembre 2024 : Analyse des Audits

**Contexte** : Marc Leblanc (auditeur externe) réalise des audits sur 4 sites.

**Fichiers générés** :
- `AUDIT_SITE_001_2024_09_10.txt` (Lyon) → ✅ Positive
- `AUDIT_SITE_003_2024_09_12.txt` (Berlin) → ⚠️ Neutral
- `AUDIT_SITE_005_2024_09_15.txt` (Shanghai) → ❌ Negative
- `AUDIT_SITE_007_2024_09_18.txt` (Dallas) → ✅ Positive

**Emma utilise l'AI Transformation** :
```
Question :
"Quels sites ont eu des findings négatifs dans les audits 
septembre 2024 et quelles sont les recommandations ?"

Réponse (AI extraite de audit_notes_txt/) :

SITE_005 - Shanghai (NEGATIVE)
Issues trouvées :
- Compteurs énergétiques non calibrés depuis 24 mois
- Stockage diesel non conforme (risque fuite)
- Manque de formation du personnel aux urgences environnementales

Recommandations :
1. Calibration urgente des compteurs (budget : 15k€)
2. Installation bac de rétention (budget : 25k€)
3. Formation obligatoire de 100% du personnel (Q4 2024)
```

**Emma à Pierre (Directeur Industriel)** :
> "Pierre, le site de Shanghai a des non-conformités. Je demande un plan d'action sous 30 jours avec budget alloué."

**Plan d'action approuvé** : 45k€ investis pour mise en conformité.

---

### 📈 Décembre 2024 : Bilan Annuel Encourageant

**Contexte** : Emma prépare le rapport 2024 avec le Data Agent.

**Résultats 2024** :
```
Question :
"Calcule notre performance 2024 vs objectifs pour Scope 1, 
Scope 2, et énergie renouvelable"

Réponse :

SCOPE 1 (Combustion directe)
- Réalisé : 795 tonnes CO₂ (-6.5% vs 2023)
- Objectif : -5%
- Performance : ✅ OBJECTIF DÉPASSÉ

SCOPE 2 (Électricité achetée)
- Réalisé : 1 080 tonnes CO₂ (-10% vs 2023)
- Objectif : -8%
- Performance : ✅ OBJECTIF DÉPASSÉ

ÉNERGIE RENOUVELABLE
- Réalisé : 42%
- Objectif : 40%
- Performance : ✅ OBJECTIF DÉPASSÉ

SCOPE 3 (Fournisseurs)
- Réalisé : 4 350 tonnes CO₂ (-3.3% vs 2023)
- Objectif : Stabilisation
- Performance : ✅ AMÉLIORATION
```

**Emma en Comité de Direction** :
> "Nous avons dépassé tous nos objectifs 2024. Le plan solaire a permis une réduction de 120 tonnes CO₂. Les actions sur les fournisseurs à risque ont réduit le Scope 3 de 150 tonnes."

**Carbon Intensity** : 32 kg/tonne (-8.6% vs 2023)

**Rapport publié** : `REPORT_2024_ANNUAL.txt`

---

### 🚀 Janvier 2025 : Nouveaux Objectifs Ambitieux

**Contexte** : Emma fixe les objectifs 2025 plus ambitieux.

**Objectifs 2025** :
- Scope 1 : -12% vs 2023 → **748 tonnes CO₂**
- Scope 2 : -15% vs 2023 → **1 020 tonnes CO₂**
- Énergie renouvelable : **50%**
- Scope 3 : -10% vs 2023 → **4 050 tonnes CO₂**

**Investissements prévus** :
- 🌞 Extension solaire Toulouse : +200 kWc (300k€)
- ⚡ Remplacement chaudières gaz par pompes à chaleur Lyon : 450k€
- 🚛 Programme fret ferroviaire (Scope 3) : 120k€
- 📊 Plateforme supplier collaboration : 80k€

**Emma à l'équipe** :
> "2025 sera l'année de l'accélération. Nous visons 50% de renouvelable et une réduction de 25% du carbon intensity vs 2023."

---

### 🌍 Juin 2025 : Analyse des Rapports Trimestriels (AI)

**Contexte** : Emma souhaite extraire automatiquement les insights des rapports Q1 et Q2 2025.

**Utilisation de l'AI Transformation** :
```
Question :
"Extrais les 3 principaux succès et 3 principaux défis 
mentionnés dans les rapports Q1 et Q2 2025"

Réponse (AI extraite de sustainability_reports_txt/) :

SUCCÈS Q1-Q2 2025
✅ Lyon a atteint 55% d'énergie renouvelable (pompes à chaleur opérationnelles)
✅ 6 fournisseurs ont amélioré leur rating ESG (D → C ou C → B)
✅ Carbon intensity réduit à 29 kg/tonne (-17% vs 2023)

DÉFIS Q1-Q2 2025
⚠️ Site Shanghai toujours à 18% renouvelable (réseau électrique local limité)
⚠️ Coût des RECs (certificats verts) en hausse de 20% vs 2024
⚠️ Retards sur projet de plateforme supplier collaboration (+3 mois)
```

**Emma à Sophie** :
> "Sophie, on doit trouver une alternative aux RECs pour Shanghai. Investir dans un projet solaire local avec PPA (Power Purchase Agreement) ?"

**Étude de faisabilité lancée** : Partenariat avec développeur solaire chinois.

---

### 🏆 Octobre 2025 : Certification B Corp

**Contexte** : L'entreprise obtient la certification B Corp (entreprise à impact positif).

**Emma en interview presse** :
> "Grâce à Microsoft Fabric et notre Data Agent, nous avons une visibilité en temps réel sur notre empreinte carbone. Nous avons réduit de 20% nos émissions Scope 1+2 en 2 ans et engagé 80% de nos fournisseurs dans une démarche d'amélioration ESG."

**Indicateurs 2025 (projection)** :
- Scope 1+2 : 1 700 tonnes CO₂ (-17% vs 2023)
- Scope 3 : 4 100 tonnes CO₂ (-9% vs 2023)
- Énergie renouvelable : 48% (cible 50% en Q4)
- Carbon Intensity : 28 kg/tonne (-20% vs 2023)

**Reconnaissance** :
- 🏆 Prix "Entreprise Durable" décerné par EcoVadis
- 📰 Article Forbes : "Comment cette PME a réduit de 20% son empreinte carbone avec l'IA"

---

### 🎯 Décembre 2025 : Bilan et Perspectives 2030

**Contexte** : Emma présente la roadmap 2030 au Conseil d'Administration.

**Bilan 2023-2025** :
- ✅ Réduction Scope 1+2 : -18% (vs baseline 2023)
- ✅ Énergie renouvelable : 50% atteint
- ✅ Carbon Intensity : 27 kg/tonne (-23%)
- ✅ 72% des fournisseurs rating ESG A ou B

**Objectif 2030** : -30% émissions totales (vs 2023)

**Roadmap 2026-2030** :
1. **2026** : Électrification complète de la flotte de véhicules (Scope 1)
2. **2027** : 100% énergie renouvelable sur sites européens
3. **2028** : Contrats PPA (Power Purchase Agreement) pour sites Asie
4. **2029** : Engagement Scope 3 : 90% des fournisseurs rating A ou B
5. **2030** : Carbon neutrality sur Scope 1+2

**Emma au CA** :
> "Nous avons démontré qu'avec de la data, de l'IA et de la volonté, la décarbonation est possible ET rentable. Le ROI de nos investissements solaires est déjà atteint. Je demande un budget de 5 M€ sur 5 ans pour atteindre la neutralité carbone."

**Décision** :
- ✅ Budget approuvé : 5 M€ (2026-2030)
- ✅ Emma promue Vice-Présidente Développement Durable
- 🌍 Ambition : Devenir leader européen de la décarbonation industrielle

---

## 🎬 Scènes Clés de la Démo

### Scène 1 : Dashboard en Temps Réel (3 min)

**Emma ouvre Power BI** :
- KPI Cards : Émissions Scope 1+2+3, Carbon Intensity, % Renouvelable
- Line Chart : Évolution mensuelle 2023-2025
- Map : Carbon Intensity par site (bubble size = émissions)
- Table : Top 10 fournisseurs à risque ESG

**Interaction** :
- Clic sur site Lyon → Détail de la consommation énergétique
- Filtre sur fournisseurs rating D → Liste des 8 fournisseurs à auditer

---

### Scène 2 : Questions au Data Agent (5 min)

**Emma tape des questions en langage naturel** :

```
Q1 : "Quelle est notre carbon intensity en 2024 ?"
R1 : "Votre carbon intensity moyenne en 2024 est de 32 kg CO₂ par tonne 
      produite, soit une réduction de 8.6% vs 2023 (35 kg/tonne)."

Q2 : "Quels sites ont le plus réduit leurs émissions en 2024 ?"
R2 : "SITE_001 (Lyon) : -22% | SITE_002 (Toulouse) : -18% | 
      SITE_007 (Dallas) : -15%"

Q3 : "Liste les fournisseurs avec rating ESG D et émissions >100 tonnes CO₂"
R3 : "3 fournisseurs identifiés : PlastikCorp (185t), MetalWorks Ltd (160t), 
      ChemSupply Co (140t)"

Q4 : "Extrais les recommandations de l'audit du site Shanghai septembre 2024"
R4 : "Recommandations (AI extraite) :
      1. Calibration urgente des compteurs énergétiques
      2. Installation bac de rétention pour stockage diesel
      3. Formation 100% du personnel aux urgences environnementales"

Q5 : "Quelle est la tendance de notre part d'énergie renouvelable ?"
R5 : "Tendance croissante : 2023 (28%) → 2024 (42%) → 2025 proj. (50%)"
```

---

### Scène 3 : Analyse des Rapports avec AI (3 min)

**Emma explore les rapports transformés** :

- **Sentiment Analysis** : 80% des rapports 2024 ont un sentiment positif
- **Key Topics** : "solar installation", "supplier engagement", "carbon reduction"
- **KPI Extraction** : Objectifs mentionnés automatiquement extraits

**Exemple** :
```
REPORT_2024_Q2.txt → AI Transform

Sentiment : Positive
Topics : [solar energy, renewable targets, supplier collaboration]
KPIs Extracted :
  - Émissions Scope 1+2 : 1 245 tonnes CO₂eq (-8% vs 2023)
  - Énergie renouvelable : 42% (+7 points vs Q1)
  - Carbon Intensity : 32 kg/tonne
```

---

### Scène 4 : Scénario "What-If" (2 min)

**Emma teste un scénario** :

> "Si on remplace toutes les chaudières gaz par des pompes à chaleur, 
> quel sera l'impact sur Scope 1 ?"

**Data Agent calcule** :
```
Scénario : Remplacement 8 chaudières gaz par pompes à chaleur

Impact Scope 1 :
- Réduction consommation gaz : -450 000 kWh/an
- Réduction émissions : -91 tonnes CO₂/an
- Nouvelle consommation électrique : +180 000 kWh/an (Scope 2)
- Émissions Scope 2 additionnelles : +9 tonnes CO₂/an (si réseau standard)
- Si électricité 100% renouvelable : +0 tonnes CO₂/an

BILAN NET : -91 tonnes CO₂/an (si électricité renouvelable)
Investissement estimé : 800k€
Temps de retour : 9 ans (économies énergétiques)
```

---

## 🎯 Messages Clés de la Démo

### Pour le C-Level

1. **Visibilité en Temps Réel** : Suivez vos KPIs ESG comme vos KPIs financiers
2. **Data-Driven Decisions** : Investissements basés sur ROI carbone mesurable
3. **Conformité Réglementaire** : CSRD, GHG Protocol, ISO 14001 automatisés

### Pour les Équipes Techniques

1. **OneLake = Single Source of Truth** : Données Scope 1/2/3 centralisées
2. **AI Transformations** : Extraction automatique d'insights depuis rapports PDF/texte
3. **Data Agent** : Questions en langage naturel → Réponses instantanées

### Pour les Équipes Métier (RSE, Achats, Production)

1. **Autonomie** : Plus besoin d'attendre l'IT pour avoir des réponses
2. **Collaboration** : Plateforme partagée entre RSE, Achats, Production
3. **Action** : De la donnée à l'action corrective en quelques minutes

---

## 📚 Ressources Complémentaires

- **Schéma complet** : [`schema.md`](schema.md)
- **Questions de démo** : [`questions_demo.md`](questions_demo.md)
- **Configuration Data Agent** : [`data_agent_instructions.md`](data_agent_instructions.md)
- **Exemples Q&A** : [`data_agent_examples.md`](data_agent_examples.md)
- **Déploiement Fabric** : [`fabric_setup.md`](fabric_setup.md)

---

**Durée totale de la démo** : 15-20 minutes  
**Format recommandé** : Démo live + Q&A  
**Public cible** : Directeurs RSE, CFO, CIO, Responsables Développement Durable

---

**Happy ESG Journey! 🌍💚**
