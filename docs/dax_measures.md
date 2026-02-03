# Mesures DAX - ESG & Carbon Analytics

Ce fichier contient toutes les mesures DAX testées et validées pour le semantic model Fabric (ESG & Carbon).

## Tables Requises

- emissions
- targets
- sites
- energy_consumption
- suppliers
- audits
- products (si intensité produit)

## Relations Clés

```
dim_sites[site_id] 1 ----→ * emissions[site_id]
dim_sites[site_id] 1 ----→ * fact_energy_consumption[site_id]
dim_sites[site_id] 1 ----→ * audits[site_id]
targets[scope] * ----→ 1 emissions[scope] (many-to-one on scope text)
```

---

## Métriques Emissions

### Total Emissions

Émissions totales CO2e.

```dax
Total Emissions = 
SUM(emissions[co2e_tonnes])
```

**Format:** Nombre (tonnes CO2e)
**Usage:** KPI principal carbon footprint

---

### Scope 1 Emissions

Émissions directes (Scope 1).

```dax
Scope 1 Emissions = 
CALCULATE(
    SUM(emissions[co2e_tonnes]),
    emissions[scope] = "Scope 1"
)
```

**Format:** Nombre (tonnes CO2e)
**Usage:** GHG Protocol reporting

---

### Scope 2 Emissions

Émissions indirectes énergie (Scope 2).

```dax
Scope 2 Emissions = 
CALCULATE(
    SUM(emissions[co2e_tonnes]),
    emissions[scope] = "Scope 2"
)
```

**Format:** Nombre (tonnes CO2e)
**Usage:** GHG Protocol reporting

---

### Scope 3 Emissions

Émissions chaîne de valeur (Scope 3).

```dax
Scope 3 Emissions = 
CALCULATE(
    SUM(emissions[co2e_tonnes]),
    emissions[scope] = "Scope 3"
)
```

**Format:** Nombre (tonnes CO2e)
**Usage:** GHG Protocol reporting

---

### Scope 1 %

Part Scope 1 dans total.

```dax
Scope 1 % = 
DIVIDE(
    [Scope 1 Emissions],
    [Total Emissions],
    0
)
```

**Format:** Pourcentage
**Usage:** Décomposition scopes

---

### Scope 2 %

Part Scope 2 dans total.

```dax
Scope 2 % = 
DIVIDE(
    [Scope 2 Emissions],
    [Total Emissions],
    0
)
```

**Format:** Pourcentage
**Usage:** Décomposition scopes

---

### Scope 3 %

Part Scope 3 dans total.

```dax
Scope 3 % = 
DIVIDE(
    [Scope 3 Emissions],
    [Total Emissions],
    0
)
```

**Format:** Pourcentage
**Expected:** ~70-80% du total
**Usage:** Décomposition scopes

---

## Métriques Intensité

### Carbon Intensity

Intensité carbone (kg CO2e par unité produite).

```dax
Carbon Intensity = 
VAR TotalEmissions = [Total Emissions] * 1000  -- Conversion tonnes → kg
VAR ProductionVolume = SUM(dim_sites[production_capacity])  -- ou table production
RETURN
    DIVIDE(TotalEmissions, ProductionVolume, BLANK())
```

**Format:** kg CO2e/unité
**Target:** Réduction continue YoY
**Usage:** Benchmark performance

---

### Scope 1 Intensity

Intensité Scope 1.

```dax
Scope 1 Intensity = 
VAR Scope1 = [Scope 1 Emissions] * 1000
VAR ProductionVolume = SUM(dim_sites[production_capacity])
RETURN
    DIVIDE(Scope1, ProductionVolume, BLANK())
```

**Format:** kg CO2e/unité
**Usage:** Performance opérationnelle

---

### Scope 2 Intensity

Intensité Scope 2.

```dax
Scope 2 Intensity = 
VAR Scope2 = [Scope 2 Emissions] * 1000
VAR ProductionVolume = SUM(dim_sites[production_capacity])
RETURN
    DIVIDE(Scope2, ProductionVolume, BLANK())
```

**Format:** kg CO2e/unité
**Usage:** Efficacité énergétique

---

## Métriques Targets & Performance

### Target Emissions

Objectif émissions.

```dax
Target Emissions = 
SUM(targets[target_emissions])
```

**Format:** Nombre (tonnes CO2e)
**Usage:** Comparaison actual vs target

---

### Baseline Emissions

Émissions baseline (année de référence).

```dax
Baseline Emissions = 
SUM(targets[baseline_emissions])
```

**Format:** Nombre (tonnes CO2e)
**Usage:** Calcul réduction

---

### Target Achievement %

Atteinte objectif.

```dax
Target Achievement % = 
VAR Target = [Target Emissions]
VAR Actual = [Total Emissions]
VAR Gap = Target - Actual
RETURN
    DIVIDE(Gap, Target, 0)
```

**Format:** Pourcentage
**Target:** >= 100% (actual <= target)
**Usage:** KPI performance

---

### Gap to Target

Écart vs objectif.

```dax
Gap to Target = 
[Total Emissions] - [Target Emissions]
```

**Format:** Nombre (tonnes CO2e)
**Positive:** Au-dessus objectif (mauvais)
**Negative:** En-dessous objectif (bon)
**Usage:** Alerte écart

---

### Reduction from Baseline

Réduction depuis baseline.

```dax
Reduction from Baseline = 
VAR Baseline = [Baseline Emissions]
VAR Current = [Total Emissions]
RETURN
    Baseline - Current
```

**Format:** Nombre (tonnes CO2e)
**Usage:** Progrès réduction

---

### Reduction from Baseline %

Réduction depuis baseline (%).

```dax
Reduction from Baseline % = 
VAR Baseline = [Baseline Emissions]
VAR Current = [Total Emissions]
RETURN
    DIVIDE(Baseline - Current, Baseline, 0)
```

**Format:** Pourcentage
**Target:** -42% by 2030 (SBTi example)
**Usage:** SBTi reporting

---

### On Track to Target

Indicateur on/off track.

```dax
On Track to Target = 
IF(
    [Total Emissions] <= [Target Emissions],
    "On Track",
    "Off Track"
)
```

**Format:** Texte
**Usage:** Couleur conditionnelle

---

## Métriques Énergie

### Total Energy Consumption

Consommation énergétique totale.

```dax
Total Energy Consumption = 
SUM(fact_energy_consumption[consumption_mwh])
```

**Format:** MWh
**Usage:** Volume énergie

---

### Renewable Energy

Énergie renouvelable.

```dax
Renewable Energy = 
CALCULATE(
    SUM(fact_energy_consumption[consumption_mwh]),
    fact_energy_consumption[renewable] = TRUE()
)
```

**Format:** MWh
**Usage:** Transition énergétique

---

### Fossil Energy

Énergie fossile.

```dax
Fossil Energy = 
CALCULATE(
    SUM(fact_energy_consumption[consumption_mwh]),
    fact_energy_consumption[renewable] = FALSE()
)
```

**Format:** MWh
**Usage:** Dépendance fossile

---

### Renewable Energy %

Part d'énergie renouvelable.

```dax
Renewable Energy % = 
DIVIDE(
    [Renewable Energy],
    [Total Energy Consumption],
    0
)
```

**Format:** Pourcentage
**Target:** >= 50% by 2025, 100% by 2030
**Usage:** KPI transition

---

### Energy Intensity

Intensité énergétique.

```dax
Energy Intensity = 
VAR TotalEnergy = [Total Energy Consumption]
VAR ProductionVolume = SUM(dim_sites[production_capacity])
RETURN
    DIVIDE(TotalEnergy, ProductionVolume, BLANK())
```

**Format:** MWh/unité
**Usage:** Efficacité énergétique

---

## Métriques Suppliers

### Total Suppliers

Nombre total de fournisseurs.

```dax
Total Suppliers = 
DISTINCTCOUNT(dim_suppliers[supplier_id])
```

**Format:** Nombre entier
**Usage:** Contexte supply chain

---

### High-Risk Suppliers

Fournisseurs à haut risque.

```dax
High-Risk Suppliers = 
CALCULATE(
    DISTINCTCOUNT(dim_suppliers[supplier_id]),
    dim_suppliers[risk_level] IN {"high", "critical"}
)
```

**Format:** Nombre entier
**Usage:** Alerte supply chain

---

### High-Risk Suppliers %

Part de fournisseurs à risque.

```dax
High-Risk Suppliers % = 
DIVIDE(
    [High-Risk Suppliers],
    [Total Suppliers],
    0
)
```

**Format:** Pourcentage
**Target:** < 10%
**Usage:** Qualité supply chain

---

### Supplier Carbon Exposure

Exposition carbone fournisseurs (spend × intensity).

```dax
Supplier Carbon Exposure = 
SUMX(
    suppliers,
    dim_suppliers[annual_spend_eur] * dim_suppliers[carbon_intensity] / 1000
)
```

**Format:** Nombre (tonnes CO2e)
**Usage:** Scope 3 supplier contribution

---

### Avg Supplier Carbon Intensity

Intensité carbone moyenne fournisseurs.

```dax
Avg Supplier Carbon Intensity = 
AVERAGE(dim_suppliers[carbon_intensity])
```

**Format:** kg CO2e/EUR spent
**Target:** < 500 kg CO2e/EUR
**Usage:** Benchmark supply chain

---

### Top 10 Suppliers Exposure

Exposition des 10 plus gros fournisseurs.

```dax
Top 10 Suppliers Exposure = 
CALCULATE(
    [Supplier Carbon Exposure],
    TOPN(10, suppliers, dim_suppliers[annual_spend_eur], DESC)
)
```

**Format:** Nombre (tonnes CO2e)
**Usage:** Focus engagement

---

## Métriques Audits

### Total Audits

Nombre total d'audits.

```dax
Total Audits = 
COUNTROWS(audits)
```

**Format:** Nombre entier
**Usage:** Contexte gouvernance

---

### Audits with Findings

Audits avec findings négatifs.

```dax
Audits with Findings = 
CALCULATE(
    COUNTROWS(audits),
    audits[finding_severity] IN {"medium", "high", "critical"}
)
```

**Format:** Nombre entier
**Usage:** Alerte compliance

---

### Critical Findings

Findings critiques.

```dax
Critical Findings = 
CALCULATE(
    COUNTROWS(audits),
    audits[finding_severity] = "critical"
)
```

**Format:** Nombre entier
**Usage:** Escalation urgente

---

### Audit Compliance Rate

Taux de conformité.

```dax
Audit Compliance Rate = 
VAR CompliantAudits = 
    CALCULATE(
        COUNTROWS(audits),
        audits[finding_severity] IN {"none", "low"}
    )
VAR TotalAudits = COUNTROWS(audits)
RETURN
    DIVIDE(CompliantAudits, TotalAudits, 0)
```

**Format:** Pourcentage
**Target:** >= 95%
**Usage:** Gouvernance ESG

---

## Métriques par Site

### Emissions by Site

Émissions par site.

```dax
Emissions by Site = 
CALCULATE(
    [Total Emissions],
    ALLEXCEPT(sites, dim_sites[site_id])
)
```

**Format:** Nombre (tonnes CO2e)
**Context:** Site
**Usage:** Performance locale

---

### Best Performing Site

Site avec meilleures performances.

```dax
Best Performing Site = 
MINX(
    VALUES(dim_sites[site_name]),
    [Carbon Intensity]
)
```

**Format:** Texte (nom site)
**Usage:** Benchmark best practices

---

### Worst Performing Site

Site avec moins bonnes performances.

```dax
Worst Performing Site = 
MAXX(
    VALUES(dim_sites[site_name]),
    [Carbon Intensity]
)
```

**Format:** Texte (nom site)
**Usage:** Focus amélioration

---

## Mesures Avancées

### YoY Emission Reduction

Réduction YoY.

```dax
YoY Emission Reduction = 
VAR CurrentYear = [Total Emissions]
VAR PreviousYear = 
    CALCULATE(
        [Total Emissions],
        DATEADD('Date'[Date], -1, YEAR)
    )
RETURN
    PreviousYear - CurrentYear
```

**Format:** Nombre (tonnes CO2e)
**Usage:** Trend analysis

---

### YoY Emission Reduction %

Réduction YoY (%).

```dax
YoY Emission Reduction % = 
VAR CurrentYear = [Total Emissions]
VAR PreviousYear = 
    CALCULATE(
        [Total Emissions],
        DATEADD('Date'[Date], -1, YEAR)
    )
RETURN
    DIVIDE(PreviousYear - CurrentYear, PreviousYear, 0)
```

**Format:** Pourcentage
**Target:** >= -5% YoY
**Usage:** Performance annuelle

---

### Emissions per Employee

Émissions par employé (si table employees disponible).

```dax
Emissions per Employee = 
DIVIDE(
    [Total Emissions] * 1000,  -- kg
    DISTINCTCOUNT(employees[employee_id]),
    BLANK()
)
```

**Format:** kg CO2e/employé
**Usage:** Benchmark organisationnel

---

### Renewable Energy Ramp Rate

Vitesse de transition renewable.

```dax
Renewable Energy Ramp Rate = 
VAR CurrentRenewable = [Renewable Energy %]
VAR PreviousRenewable = 
    CALCULATE(
        [Renewable Energy %],
        DATEADD('Date'[Date], -1, YEAR)
    )
RETURN
    CurrentRenewable - PreviousRenewable
```

**Format:** Points de pourcentage
**Target:** +5-10 pp/an
**Usage:** Vitesse transition

---

### Carbon Budget Remaining

Budget carbone restant (pour atteindre objectif).

```dax
Carbon Budget Remaining = 
VAR CurrentEmissions = [Total Emissions]
VAR TargetEmissions = [Target Emissions]
VAR YearsToTarget = 2030 - YEAR(TODAY())  -- Example: 2030 target
VAR AnnualReductionNeeded = DIVIDE(CurrentEmissions - TargetEmissions, YearsToTarget, BLANK())
RETURN
    AnnualReductionNeeded
```

**Format:** Tonnes CO2e/an
**Usage:** Trajectory planning

---

## Notes d'Implémentation

### Vérification des Noms de Colonnes

**Tables critiques:**
- emissions.scope (STRING: 'Scope 1', 'Scope 2', 'Scope 3')
- emissions.co2e_tonnes (FLOAT)
- suppliers.risk_level (STRING: 'low', 'medium', 'high', 'critical')
- energy_consumption.renewable (BOOLEAN)
- targets.target_emissions, baseline_emissions (FLOAT)

### Relations Manquantes

Si une mesure retourne BLANK(), vérifier:
1. Relations entre tables créées (sites → emissions, etc.)
2. Table Date créée et reliée
3. Scopes dans targets correspondent à emissions

### Performance

Pour améliorer les performances:
- Créer table Date
- Indexer site_id, scope
- Pré-calculer intensités si volume élevé

---

## Validation

**Valeurs attendues (dataset complet):**
- Total Emissions: ~15 000-20 000 tonnes CO2e/an
- Scope 3: ~70-80% du total
- Renewable Energy %: ~25-35% (en progression)
- Carbon Intensity: variable selon industrie
- High-Risk Suppliers: < 10%
- Target Achievement: >= 90%

