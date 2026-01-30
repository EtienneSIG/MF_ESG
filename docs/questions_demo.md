# 🎤 Questions de Démo - ESG & Carbon Analytics

Ces 20 questions permettent de tester le **Data Agent** pendant la démo. Elles couvrent tous les cas d'usage ESG.

---

## 📊 Catégorie 1 : Performance Carbone Globale

### Q1 : Émissions Totales 2024
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
```

---

### Q2 : Carbon Intensity 2024
**Question** :
```
Quelle est notre carbon intensity moyenne en 2024 ?
```

**Réponse attendue** :
```
Carbon Intensity 2024 : 32 kg CO₂ par tonne produite

Évolution :
- 2023 : 35 kg/tonne (baseline)
- 2024 : 32 kg/tonne (-8.6%)
- Objectif 2025 : 28 kg/tonne
```

---

### Q3 : Réduction vs Baseline
**Question** :
```
Avons-nous atteint notre objectif de réduction de -5% sur Scope 1 en 2024 ?
```

**Réponse attendue** :
```
✅ OBJECTIF DÉPASSÉ

Scope 1 en 2024 :
- Réalisé : 795 tonnes CO₂eq
- Baseline 2023 : 850 tonnes CO₂eq
- Réduction : -6.5%
- Objectif : -5%

Performance : +1.5 points au-dessus de l'objectif
```

---

### Q4 : Évolution Mensuelle Scope 1+2
**Question** :
```
Montre l'évolution mensuelle des émissions Scope 1+2 sur 2024
```

**Réponse attendue** :
```
Émissions Scope 1+2 (2024) :

Janvier : 165 tonnes | Février : 160 tonnes | Mars : 155 tonnes
Avril : 148 tonnes | Mai : 145 tonnes | Juin : 142 tonnes
Juillet : 155 tonnes | Août : 150 tonnes | Septembre : 152 tonnes
Octobre : 158 tonnes | Novembre : 162 tonnes | Décembre : 170 tonnes

Moyenne mensuelle : 156 tonnes (vs 171 tonnes en 2023, -8.8%)
Tendance : Baisse progressive avec pic en hiver (chauffage)
```

---

## ⚡ Catégorie 2 : Énergie Renouvelable

### Q5 : Part d'Énergie Renouvelable Actuelle
**Question** :
```
Quelle est notre part d'énergie renouvelable en 2024 ?
```

**Réponse attendue** :
```
Part d'énergie renouvelable 2024 : 42%

Évolution :
- 2023 : 28%
- 2024 : 42% (+14 points)
- Objectif 2025 : 50%

Progression vers objectif : 78% (reste +8 points à gagner)
```

---

### Q6 : Sites avec Plus de 50% de Renouvelable
**Question** :
```
Quels sites ont dépassé 50% d'énergie renouvelable en 2024 ?
```

**Réponse attendue** :
```
2 sites ont dépassé 50% renouvelable en 2024 :

SITE_001 - Usine Lyon Gerland
- Part renouvelable : 55%
- Production solaire : 380 000 kWh/an
- Réduction CO₂ : -85 tonnes vs 2023

SITE_007 - Bureau Dallas
- Part renouvelable : 52%
- Contrat électricité verte : 100% éolien
- Réduction CO₂ : -12 tonnes vs 2023
```

---

### Q7 : Impact des Panneaux Solaires
**Question** :
```
Quel a été l'impact des installations solaires sur nos émissions Scope 2 ?
```

**Réponse attendue** :
```
Installations solaires 2023-2024 :
- Lyon : 2 500 m² (400 kWc)
- Toulouse : 1 800 m² (300 kWc)

Impact Scope 2 :
- Production totale : 900 000 kWh/an
- Réduction CO₂ : -120 tonnes/an
- Économies financières : 135 000 €/an
- ROI : 7 ans

Part dans réduction totale Scope 2 : 56%
```

---

### Q8 : Consommation Énergétique par Site
**Question** :
```
Classe les sites par consommation énergétique totale en 2024
```

**Réponse attendue** :
```
Top 5 sites par consommation énergétique (2024) :

1. SITE_001 (Lyon) : 4 250 000 kWh | Type : Manufacturing
2. SITE_003 (Berlin) : 3 800 000 kWh | Type : Manufacturing
3. SITE_005 (Shanghai) : 3 600 000 kWh | Type : Manufacturing
4. SITE_002 (Toulouse) : 3 200 000 kWh | Type : Manufacturing
5. SITE_004 (Entrepôt Anvers) : 1 850 000 kWh | Type : Warehouse

Total entreprise : 22 500 000 kWh
```

---

## 🏢 Catégorie 3 : Fournisseurs & Scope 3

### Q9 : Fournisseurs à Risque ESG
**Question** :
```
Combien de fournisseurs ont un rating ESG D (risque élevé) ?
```

**Réponse attendue** :
```
8 fournisseurs avec rating ESG D identifiés

Représentent :
- 10% du total fournisseurs (8/80)
- 25% des émissions Scope 3 (1 120 tonnes CO₂)
- Catégories : Packaging (3), Raw Materials (3), Transport (2)

Action recommandée : Plan d'engagement ou changement de fournisseur
```

---

### Q10 : Top Émetteurs Scope 3
**Question** :
```
Quels sont les 5 fournisseurs qui génèrent le plus d'émissions Scope 3 ?
```

**Réponse attendue** :
```
Top 5 fournisseurs par émissions Scope 3 (2024) :

1. PlastikCorp (Chine) : 185 tonnes CO₂ | Rating : D | Packaging
2. MetalWorks Ltd (Inde) : 160 tonnes CO₂ | Rating : D | Raw Materials
3. ChemSupply Co (USA) : 140 tonnes CO₂ | Rating : D | Components
4. SteelPro GmbH (Allemagne) : 128 tonnes CO₂ | Rating : B | Raw Materials
5. LogisticPartner SA (France) : 115 tonnes CO₂ | Rating : C | Transport

Total : 728 tonnes CO₂ (17% du Scope 3)
```

---

### Q11 : Fournisseurs par Certification
**Question** :
```
Combien de fournisseurs ont une certification ISO 14001 ?
```

**Réponse attendue** :
```
Fournisseurs avec certification ISO 14001 : 45 (56%)

Répartition par certification :
- ISO 14001 : 45 fournisseurs (56%)
- B Corp : 12 fournisseurs (15%)
- Aucune : 23 fournisseurs (29%)

Corrélation :
- Fournisseurs ISO 14001 → Rating moyen : B
- Fournisseurs sans certification → Rating moyen : C
```

---

### Q12 : Réduction Scope 3 vs 2023
**Question** :
```
Quelle a été l'évolution de nos émissions Scope 3 entre 2023 et 2024 ?
```

**Réponse attendue** :
```
Scope 3 - Évolution 2023 → 2024 :

2023 : 4 500 tonnes CO₂eq
2024 : 4 350 tonnes CO₂eq

Réduction : -150 tonnes (-3.3%)

Facteurs de réduction :
- Engagement fournisseurs (-80 tonnes)
- Optimisation transport (-50 tonnes)
- Réduction packaging (-20 tonnes)
```

---

## 🏭 Catégorie 4 : Performance par Site

### Q13 : Site le Plus Performant
**Question** :
```
Quel site a la meilleure carbon intensity en 2024 ?
```

**Réponse attendue** :
```
Site le plus performant : SITE_001 (Usine Lyon Gerland)

Carbon Intensity : 28 kg CO₂ / tonne produite

Facteurs de performance :
- 55% d'énergie renouvelable (panneaux solaires)
- Pompes à chaleur récentes (haute efficacité)
- Taux de rebut faible (2.5%)

Comparaison moyenne entreprise : 32 kg/tonne (-12.5% vs moyenne)
```

---

### Q14 : Site à Améliorer
**Question** :
```
Quel site a la carbon intensity la plus élevée et pourquoi ?
```

**Réponse attendue** :
```
Site le moins performant : SITE_005 (Usine Shanghai)

Carbon Intensity : 45 kg CO₂ / tonne produite

Facteurs explicatifs :
- Énergie renouvelable : 18% (vs 42% moyenne)
- Électricité réseau : 70% charbon (facteur d'émission élevé)
- Équipements vieillissants (chaudières classe D)

Actions recommandées :
1. Investissement panneaux solaires ou PPA local
2. Remplacement chaudières (budget : 120k€)
3. Formation équipe aux éco-gestes
```

---

### Q15 : Comparaison Lyon vs Berlin
**Question** :
```
Compare les performances carbone des sites de Lyon et Berlin en 2024
```

**Réponse attendue** :
```
Comparaison SITE_001 (Lyon) vs SITE_003 (Berlin)

| Indicateur               | Lyon      | Berlin    | Écart   |
|--------------------------|-----------|-----------|---------|
| Émissions Scope 1+2      | 320 t CO₂ | 410 t CO₂ | -22%    |
| Carbon Intensity         | 28 kg/t   | 38 kg/t   | -26%    |
| Énergie renouvelable     | 55%       | 32%       | +23 pts |
| Production               | 11 400 t  | 10 800 t  | +6%     |

Conclusion : Lyon surperforme grâce aux investissements solaires 2023
```

---

## 📄 Catégorie 5 : Rapports & Audits (AI Transformations)

### Q16 : Sentiment des Rapports 2024
**Question** :
```
Quel est le sentiment global des rapports de durabilité en 2024 ?
```

**Réponse attendue** :
```
Analyse de sentiment (AI) sur 4 rapports 2024 :

Sentiments détectés :
- Positive : 3 rapports (75%)
- Neutral : 1 rapport (25%)
- Negative : 0 rapport (0%)

Rapports positifs :
- REPORT_2024_Q1.txt : "Dépassement objectifs solaires"
- REPORT_2024_Q2.txt : "Réduction 8% Scope 1+2"
- REPORT_2024_ANNUAL.txt : "Tous objectifs atteints"

Rapport neutre :
- REPORT_2024_Q3.txt : "Progression normale, défis Scope 3"
```

---

### Q17 : Thèmes Principaux des Rapports
**Question** :
```
Quels sont les thèmes les plus récurrents dans nos rapports 2024 ?
```

**Réponse attendue** :
```
Top 5 thèmes (AI extraction) :

1. "solar installation" : 8 mentions
2. "carbon reduction" : 7 mentions
3. "supplier engagement" : 6 mentions
4. "renewable energy targets" : 6 mentions
5. "scope 3 challenges" : 4 mentions

Thèmes émergents 2024 :
- "circular economy" : 3 mentions
- "employee training" : 2 mentions
```

---

### Q18 : Audits avec Findings Négatifs
**Question** :
```
Quels sites ont eu des findings négatifs dans les audits 2024 ?
```

**Réponse attendue** :
```
2 sites avec findings négatifs (AI classification) :

SITE_005 - Shanghai (Audit 15/09/2024)
Issues :
- Compteurs énergétiques non calibrés (24 mois)
- Stockage diesel non conforme
- Manque formation urgences environnementales

SITE_003 - Berlin (Audit 12/09/2024)
Issues :
- Suivi manuel des consommations (erreurs de saisie)
- Fuites d'air comprimé non réparées

Actions correctives : 45k€ Shanghai, 12k€ Berlin
```

---

### Q19 : Extraction d'Objectifs des Rapports
**Question** :
```
Extrais les objectifs 2025 mentionnés dans le rapport annuel 2024
```

**Réponse attendue** :
```
Objectifs 2025 (AI extraite de REPORT_2024_ANNUAL.txt) :

Scope 1 :
- Réduction -12% vs baseline 2023
- Cible : 748 tonnes CO₂eq

Scope 2 :
- Réduction -15% vs baseline 2023
- Cible : 1 020 tonnes CO₂eq

Énergie renouvelable :
- Atteindre 50%
- Investissement extension solaire Toulouse

Scope 3 :
- Réduction -10% vs baseline 2023
- Cible : 4 050 tonnes CO₂eq
- Plan d'engagement 100% fournisseurs
```

---

### Q20 : Recommandations d'Audit Shanghai
**Question** :
```
Quelles sont les recommandations de l'audit du site Shanghai de septembre 2024 ?
```

**Réponse attendue** :
```
Recommandations (AI extraite de AUDIT_SITE_005_2024_09_15.txt) :

1. URGENCE : Calibration compteurs énergétiques
   - Délai : Avant fin Q4 2024
   - Budget : 15 000 €

2. PRIORITÉ : Installation bac de rétention stockage diesel
   - Délai : Q1 2025
   - Budget : 25 000 €

3. IMPORTANT : Formation 100% du personnel
   - Délai : Q4 2024
   - Budget : 5 000 €

Total investissement : 45 000 €
Responsable : Pierre Blanchard (Directeur Industriel)
```

---

## 🎯 Questions Bonus (Scenarios What-If)

### Q21 : Scénario Pompes à Chaleur
**Question** :
```
Si on remplace toutes les chaudières gaz par des pompes à chaleur, 
quel sera l'impact sur Scope 1 ?
```

**Réponse attendue** :
```
Scénario : Remplacement 8 chaudières gaz → pompes à chaleur

Impact Scope 1 :
- Réduction consommation gaz : -450 000 kWh/an
- Réduction émissions : -91 tonnes CO₂/an

Impact Scope 2 :
- Hausse consommation électrique : +180 000 kWh/an
- Si réseau standard : +9 tonnes CO₂/an
- Si électricité 100% renouvelable : 0 tonnes CO₂/an

BILAN NET : -91 tonnes CO₂/an (avec électricité verte)
Investissement : 800 000 €
Temps de retour : 9 ans
```

---

### Q22 : Scénario Fret Ferroviaire
**Question** :
```
Si on passe 50% de notre transport routier en fret ferroviaire, 
quel sera l'impact sur Scope 3 ?
```

**Réponse attendue** :
```
Scénario : 50% transport routier → fret ferroviaire

Transport actuel (2024) :
- Émissions transport Scope 3 : 320 tonnes CO₂/an
- Mode : 100% routier

Transport avec 50% ferroviaire :
- Émissions routier (50%) : 160 tonnes CO₂
- Émissions ferroviaire (50%) : 28 tonnes CO₂ (facteur 6x inférieur)

Réduction Scope 3 : -132 tonnes CO₂/an (-41% sur transport)

Coût additionnel : +15% sur budget transport
ROI : Compensé par valorisation reporting ESG
```

---

## 📊 Utilisation de ces Questions

### Ordre Recommandé pour la Démo

**Phase 1 - Performance Globale (5 min)** : Q1, Q2, Q3, Q4  
**Phase 2 - Énergie Renouvelable (3 min)** : Q5, Q6, Q7  
**Phase 3 - Fournisseurs (3 min)** : Q9, Q10, Q12  
**Phase 4 - Sites (2 min)** : Q13, Q14, Q15  
**Phase 5 - AI Insights (3 min)** : Q16, Q18, Q20  
**Phase 6 - What-If (2 min)** : Q21

**Durée totale** : 18 minutes

### Questions par Niveau de Complexité

**Basique** (découverte) : Q1, Q2, Q5, Q9  
**Intermédiaire** (analyse) : Q3, Q6, Q10, Q13, Q14  
**Avancé** (AI + scenarios) : Q16, Q17, Q18, Q19, Q20, Q21, Q22

### Questions par Persona

**Directrice RSE** : Q1, Q2, Q3, Q5, Q13, Q16, Q21  
**Responsable Achats Durables** : Q9, Q10, Q11, Q12  
**Directeur Industriel** : Q8, Q13, Q14, Q15, Q18, Q20  
**CFO** : Q2, Q7, Q21, Q22

---

**Happy Testing! 🧪✅**
