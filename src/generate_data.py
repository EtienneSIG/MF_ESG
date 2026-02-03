#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur de données ESG & Carbon Analytics pour Microsoft Fabric
Génère des données fictives pour démonstration Fabric Data Agent
"""

import csv
import random
import yaml
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Any

# Configuration des chemins
SCRIPT_DIR = Path(__file__).parent
CONFIG_FILE = SCRIPT_DIR / "config.yaml"
DATA_DIR = SCRIPT_DIR.parent / "data" / "raw"
OPERATIONS_DIR = DATA_DIR / "operations"
ESG_DIR = DATA_DIR / "esg"
TEXT_DIR = DATA_DIR / "text"


def load_config() -> Dict[str, Any]:
    """Charge la configuration depuis config.yaml"""
    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def generate_sites(config: Dict) -> List[Dict]:
    """Génère les sites opérationnels"""
    print("🏭 Génération des sites...")
    
    sites = []
    site_id = 1
    
    for region in config['sites']['regions']:
        region_name = region['name']
        site_count = region['count']
        renewable_pct = region['renewable_energy_pct']
        
        for _ in range(site_count):
            # Déterminer le type de site
            type_rand = random.random()
            if type_rand < 5/12:
                site_type = "manufacturing_plant"
                size_sqm = random.randint(5000, 20000)
            elif type_rand < 9/12:
                site_type = "warehouse"
                size_sqm = random.randint(3000, 10000)
            else:
                site_type = "office"
                size_sqm = random.randint(500, 3000)
            
            sites.append({
                'site_id': f'SITE_{site_id:03d}',
                'site_name': f'{region_name} {site_type.replace("_", " ").title()} {site_id}',
                'site_type': site_type,
                'region': region_name,
                'country': random.choice(['France', 'Germany', 'USA', 'Canada', 'China', 'Japan']),
                'size_sqm': size_sqm,
                'employees': random.randint(50, 500) if site_type == "manufacturing_plant" else random.randint(10, 100),
                'renewable_energy_pct': round(renewable_pct + random.uniform(-0.1, 0.1), 2),
                'opened_date': (datetime(2010, 1, 1) + timedelta(days=random.randint(0, 4000))).strftime('%Y-%m-%d'),
                'is_active': 'true'
            })
            site_id += 1
    
    print(f"  ✓ {len(sites)} sites créés")
    return sites


def generate_assets(config: Dict, sites: List[Dict]) -> List[Dict]:
    """Génère les assets (équipements)"""
    print("⚙️ Génération des assets...")
    
    assets = []
    asset_id = 1
    
    for site in sites:
        site_id = site['site_id']
        site_type = site['site_type']
        
        # Nombre d'assets selon le type de site
        if site_type == "manufacturing_plant":
            num_assets = random.randint(25, 40)
        elif site_type == "warehouse":
            num_assets = random.randint(15, 25)
        else:  # office
            num_assets = random.randint(8, 15)
        
        for _ in range(num_assets):
            # Catégorie d'asset
            cat = random.choice(config['assets']['categories'])
            category = cat['name']
            power_kw = cat['avg_power_kw'] * random.uniform(0.7, 1.3)
            efficiency = random.choice(cat['efficiency_class'])
            
            assets.append({
                'asset_id': f'ASSET_{asset_id:06d}',
                'site_id': site_id,
                'asset_name': f'{category.replace("_", " ").title()} {asset_id}',
                'asset_category': category,
                'power_rating_kw': round(power_kw, 2),
                'efficiency_class': efficiency,
                'installation_date': (datetime(2015, 1, 1) + timedelta(days=random.randint(0, 3000))).strftime('%Y-%m-%d'),
                'status': random.choice(['operational', 'operational', 'operational', 'maintenance'])
            })
            asset_id += 1
    
    print(f"  ✓ {len(assets)} assets créés")
    return assets


def generate_energy_consumption(config: Dict, sites: List[Dict]) -> List[Dict]:
    """Génère la consommation énergétique mensuelle"""
    print("⚡ Génération de la consommation énergétique...")
    
    consumption_records = []
    record_id = 1
    
    start_date = datetime.strptime(config['start_date'], '%Y-%m-%d')
    end_date = datetime.strptime(config['end_date'], '%Y-%m-%d')
    
    # Scénario renewable energy ramp
    renewable_ramp = config['scenarios']['renewable_energy_ramp']
    
    current_date = start_date
    while current_date <= end_date:
        year = current_date.year
        month = current_date.month
        
        # Saisonnalité (hiver = +20%, été = -10%)
        if month in [12, 1, 2]:
            seasonal_factor = 1.20
        elif month in [6, 7, 8]:
            seasonal_factor = 0.90
        else:
            seasonal_factor = 1.0
        
        for site in sites:
            site_id = site['site_id']
            site_type = site['site_type']
            region = site['region']
            
            # Facteur d'intensité selon le type
            if site_type == "manufacturing_plant":
                base_kwh = 50000
            elif site_type == "warehouse":
                base_kwh = 30000
            else:  # office
                base_kwh = 10000
            
            # Scénario: best performers vs underperformers
            perf_scenario = config['scenarios']['site_performance_variance']
            if site_id in perf_scenario['best_performers']:
                efficiency_factor = 0.85  # -15% de consommation
            elif site_id in perf_scenario['underperformers']:
                efficiency_factor = 1.25  # +25% de consommation
            else:
                efficiency_factor = 1.0
            
            # Pourcentage renouvelable selon l'année (ramp-up)
            if year == 2023:
                renewable_pct = renewable_ramp['year_2023']
            elif year == 2024:
                renewable_pct = renewable_ramp['year_2024']
            else:  # 2025
                renewable_pct = renewable_ramp['year_2025']
            
            # Variation aléatoire
            renewable_pct = renewable_pct + random.uniform(-0.05, 0.05)
            renewable_pct = max(0, min(1, renewable_pct))
            
            for source_config in config['energy_consumption']['sources']:
                source_type = source_config['type']
                avg_kwh = source_config['avg_kwh_per_site_per_month']
                cost_per_kwh = source_config['cost_per_kwh_eur']
                
                # Adapter selon le type de site
                if source_type == "electricity":
                    kwh = base_kwh * seasonal_factor * efficiency_factor * random.uniform(0.9, 1.1)
                    # Part renouvelable
                    renewable_kwh = kwh * renewable_pct
                    grid_kwh = kwh * (1 - renewable_pct)
                elif source_type == "natural_gas":
                    kwh = avg_kwh * seasonal_factor * efficiency_factor * random.uniform(0.8, 1.2)
                    renewable_kwh = 0
                    grid_kwh = kwh
                else:  # diesel
                    kwh = avg_kwh * efficiency_factor * random.uniform(0.7, 1.3)
                    renewable_kwh = 0
                    grid_kwh = kwh
                
                total_cost = kwh * cost_per_kwh
                
                consumption_records.append({
                    'record_id': f'REC_{record_id:08d}',
                    'site_id': site_id,
                    'year': year,
                    'month': month,
                    'record_date': current_date.strftime('%Y-%m-%d'),
                    'energy_source': source_type,
                    'consumption_kwh': round(kwh, 2),
                    'renewable_kwh': round(renewable_kwh, 2),
                    'grid_kwh': round(grid_kwh, 2),
                    'renewable_pct': round(renewable_pct, 3),
                    'cost_eur': round(total_cost, 2)
                })
                record_id += 1
        
        # Mois suivant
        if month == 12:
            current_date = datetime(year + 1, 1, 1)
        else:
            current_date = datetime(year, month + 1, 1)
    
    print(f"  ✓ {len(consumption_records)} enregistrements de consommation créés")
    return consumption_records


def generate_production_volumes(config: Dict, sites: List[Dict]) -> List[Dict]:
    """Génère les volumes de production"""
    print("📦 Génération des volumes de production...")
    
    production_records = []
    record_id = 1
    
    start_date = datetime.strptime(config['start_date'], '%Y-%m-%d')
    end_date = datetime.strptime(config['end_date'], '%Y-%m-%d')
    
    current_date = start_date
    while current_date <= end_date:
        year = current_date.year
        month = current_date.month
        
        for site in sites:
            if site['site_type'] == "manufacturing_plant":
                # Seulement les sites de production
                units = config['production']['units_per_month'] * random.uniform(0.85, 1.15)
                
                production_records.append({
                    'record_id': f'PROD_{record_id:08d}',
                    'site_id': site['site_id'],
                    'year': year,
                    'month': month,
                    'record_date': current_date.strftime('%Y-%m-%d'),
                    'units_produced': int(units),
                    'unit_type': config['production']['unit']
                })
                record_id += 1
        
        # Mois suivant
        if month == 12:
            current_date = datetime(year + 1, 1, 1)
        else:
            current_date = datetime(year, month + 1, 1)
    
    print(f"  ✓ {len(production_records)} enregistrements de production créés")
    return production_records


def generate_emission_factors(config: Dict) -> List[Dict]:
    """Génère les facteurs d'émission"""
    print("🌍 Génération des facteurs d'émission...")
    
    factors = []
    factor_id = 1
    
    # Électricité par région
    for region, factor in config['emission_factors']['electricity'].items():
        factors.append({
            'factor_id': f'EF_{factor_id:04d}',
            'energy_source': 'electricity',
            'region': region,
            'emission_factor_kg_co2_per_kwh': factor,
            'unit': 'kg CO₂/kWh',
            'source': 'Grid mix average',
            'valid_from': '2023-01-01'
        })
        factor_id += 1
    
    # Autres sources (constant)
    for source in ['natural_gas', 'diesel', 'renewable']:
        factors.append({
            'factor_id': f'EF_{factor_id:04d}',
            'energy_source': source,
            'region': 'global',
            'emission_factor_kg_co2_per_kwh': config['emission_factors'][source],
            'unit': 'kg CO₂/kWh',
            'source': 'Standard conversion factor',
            'valid_from': '2023-01-01'
        })
        factor_id += 1
    
    print(f"  ✓ {len(factors)} facteurs d'émission créés")
    return factors


def generate_carbon_emissions(config: Dict, energy_consumption: List[Dict], 
                              emission_factors: List[Dict], sites: List[Dict]) -> List[Dict]:
    """Génère les émissions carbone (Scope 1, 2, 3)"""
    print("💨 Génération des émissions carbone...")
    
    emissions = []
    emission_id = 1
    
    # Créer un mapping facteurs d'émission
    ef_map = {}
    for ef in emission_factors:
        key = (ef['energy_source'], ef['region'])
        ef_map[key] = ef['emission_factor_kg_co2_per_kwh']
    
    # Mapper sites → régions
    site_region_map = {site['site_id']: site['region'].lower().replace(' ', '_') for site in sites}
    
    for energy_rec in energy_consumption:
        site_id = energy_rec['site_id']
        region = site_region_map.get(site_id, 'europe')
        source = energy_rec['energy_source']
        grid_kwh = energy_rec['grid_kwh']
        renewable_kwh = energy_rec['renewable_kwh']
        
        # Déterminer le scope
        if source in ['natural_gas', 'diesel']:
            scope = 'Scope 1'  # Combustion directe
        elif source == 'electricity':
            scope = 'Scope 2'  # Électricité achetée
        else:
            scope = 'Scope 2'
        
        # Trouver le facteur d'émission
        ef_key_grid = (source, region)
        ef_key_global = (source, 'global')
        
        emission_factor = ef_map.get(ef_key_grid, ef_map.get(ef_key_global, 0.3))
        
        # Calcul émissions
        emissions_kg_co2 = grid_kwh * emission_factor
        emissions_tonnes_co2 = emissions_kg_co2 / 1000
        
        emissions.append({
            'emission_id': f'EM_{emission_id:08d}',
            'site_id': site_id,
            'year': energy_rec['year'],
            'month': energy_rec['month'],
            'record_date': energy_rec['record_date'],
            'scope': scope,
            'emission_source': source,
            'consumption_kwh': energy_rec['consumption_kwh'],
            'renewable_kwh': renewable_kwh,
            'grid_kwh': grid_kwh,
            'emission_factor_kg_co2_per_kwh': emission_factor,
            'emissions_kg_co2': round(emissions_kg_co2, 2),
            'emissions_tonnes_co2': round(emissions_tonnes_co2, 3)
        })
        emission_id += 1
    
    print(f"  ✓ {len(emissions)} enregistrements d'émissions créés")
    return emissions


def generate_suppliers(config: Dict) -> List[Dict]:
    """Génère les fournisseurs"""
    print("🏢 Génération des fournisseurs...")
    
    suppliers = []
    supplier_id = 1
    
    for segment_config in config['suppliers']['segments']:
        segment = segment_config['name']
        count = segment_config['count']
        avg_spend = segment_config['avg_annual_spend_eur']
        esg_ratings = segment_config['esg_rating']
        
        for _ in range(count):
            esg_rating = random.choice(esg_ratings)
            
            suppliers.append({
                'supplier_id': f'SUP_{supplier_id:05d}',
                'supplier_name': f'Supplier {supplier_id:05d} {segment.title()}',
                'segment': segment,
                'country': random.choice(['France', 'Germany', 'USA', 'China', 'India', 'Brazil']),
                'category': random.choice(['Raw Materials', 'Components', 'Services', 'Logistics', 'Energy']),
                'annual_spend_eur': round(avg_spend * random.uniform(0.7, 1.3), 2),
                'esg_rating': esg_rating,
                'carbon_disclosure': random.choice(['yes', 'yes', 'no']),  # 67% disclosent
                'contract_start_date': (datetime(2020, 1, 1) + timedelta(days=random.randint(0, 1500))).strftime('%Y-%m-%d'),
                'is_active': 'true'
            })
            supplier_id += 1
    
    print(f"  ✓ {len(suppliers)} fournisseurs créés")
    return suppliers


def generate_supplier_emissions(config: Dict, suppliers: List[Dict]) -> List[Dict]:
    """Génère les émissions Scope 3 des fournisseurs"""
    print("📊 Génération des émissions fournisseurs (Scope 3)...")
    
    supplier_emissions = []
    emission_id = 1
    
    # Scénario: fournisseurs à risque
    risk_scenario = config['scenarios']['scope3_suppliers_risk']
    high_risk_suppliers = random.sample([s['supplier_id'] for s in suppliers], 
                                       min(risk_scenario['high_risk_count'], len(suppliers)))
    
    start_date = datetime.strptime(config['start_date'], '%Y-%m-%d')
    end_date = datetime.strptime(config['end_date'], '%Y-%m-%d')
    
    for supplier in suppliers:
        supplier_id = supplier['supplier_id']
        annual_spend = supplier['annual_spend_eur']
        esg_rating = supplier['esg_rating']
        
        # Facteur d'émission selon le rating ESG
        if esg_rating == 'A':
            emission_intensity = 0.5  # kg CO₂ par € dépensé
        elif esg_rating == 'B':
            emission_intensity = 1.0
        elif esg_rating == 'C':
            emission_intensity = 1.8
        else:  # D
            emission_intensity = 2.5
        
        # Scénario: high risk suppliers
        if supplier_id in high_risk_suppliers:
            emission_intensity *= risk_scenario['impact_multiplier']
        
        # Générer émissions annuelles
        for year in range(start_date.year, end_date.year + 1):
            annual_emissions_kg = annual_spend * emission_intensity
            annual_emissions_tonnes = annual_emissions_kg / 1000
            
            supplier_emissions.append({
                'emission_id': f'SE_{emission_id:08d}',
                'supplier_id': supplier_id,
                'year': year,
                'scope': 'Scope 3',
                'category': 'Purchased Goods & Services',
                'annual_spend_eur': annual_spend,
                'emission_intensity_kg_co2_per_eur': round(emission_intensity, 3),
                'emissions_kg_co2': round(annual_emissions_kg, 2),
                'emissions_tonnes_co2': round(annual_emissions_tonnes, 3),
                'is_estimated': 'true' if supplier['carbon_disclosure'] == 'no' else 'false'
            })
            emission_id += 1
    
    print(f"  ✓ {len(supplier_emissions)} enregistrements d'émissions fournisseurs créés")
    return supplier_emissions


def generate_sustainability_reports(config: Dict, sites: List[Dict]):
    """Génère les rapports de durabilité (fichiers texte)"""
    print("📄 Génération des rapports de durabilité...")
    
    output_dir = TEXT_DIR / "sustainability_reports_txt"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    report_templates = [
        "In {year}, {site_name} achieved {achievement}. Our renewable energy usage reached {renewable_pct}%, "
        "contributing to a {reduction_pct}% reduction in carbon emissions compared to baseline. "
        "Key initiatives included: {initiative}. Energy efficiency improvements resulted in {savings_kwh} kWh savings. "
        "Looking ahead, we plan to {future_plan}.",
        
        "Sustainability Report {year} - {site_name}: Total energy consumption: {total_kwh} kWh. "
        "Carbon footprint: {carbon_tonnes} tonnes CO₂. Renewable energy: {renewable_pct}%. "
        "Water consumption reduced by {water_reduction}%. Waste recycling rate: {recycling_pct}%. "
        "Employee engagement: {engagement_score} sustainability training hours completed. "
        "Community impact: {community_initiative}.",
        
        "{site_name} - Annual Sustainability Performance {year}: Scope 1 emissions: {scope1} tonnes CO₂. "
        "Scope 2 emissions: {scope2} tonnes CO₂. Energy intensity: {intensity} kWh per unit. "
        "Progress towards net-zero: {netzero_progress}%. Certifications obtained: {certifications}. "
        "Supplier ESG assessments completed: {supplier_assessments}. Circular economy initiatives: {circular_initiatives}."
    ]
    
    achievements = ["carbon neutrality certification", "ISO 14001 recertification", "30% emissions reduction",
                   "zero waste to landfill status", "100% renewable electricity procurement"]
    initiatives = ["LED lighting retrofits", "solar panel installation", "heat recovery systems",
                  "employee carpooling program", "smart building management system"]
    future_plans = ["install additional solar capacity", "electrify fleet vehicles", "implement AI-based energy optimization",
                   "achieve carbon neutrality by 2030", "expand recycling programs"]
    
    report_id = 1
    for site in sites:
        for year in [2023, 2024, 2025]:
            template = random.choice(report_templates)
            
            report_text = template.format(
                year=year,
                site_name=site['site_name'],
                achievement=random.choice(achievements),
                renewable_pct=random.randint(25, 60),
                reduction_pct=random.randint(5, 20),
                initiative=random.choice(initiatives),
                savings_kwh=random.randint(10000, 50000),
                future_plan=random.choice(future_plans),
                total_kwh=random.randint(300000, 800000),
                carbon_tonnes=random.randint(150, 400),
                water_reduction=random.randint(5, 25),
                recycling_pct=random.randint(60, 95),
                engagement_score=random.randint(500, 2000),
                community_initiative=random.choice(["tree planting", "STEM education", "local renewable energy"]),
                scope1=random.randint(50, 150),
                scope2=random.randint(100, 250),
                intensity=round(random.uniform(20, 50), 2),
                netzero_progress=random.randint(20, 60),
                certifications=random.choice(["ISO 14001, ISO 50001", "LEED Gold", "BREEAM Excellent"]),
                supplier_assessments=random.randint(10, 50),
                circular_initiatives=random.choice(["product take-back program", "remanufacturing", "material recovery"])
            )
            
            filename = f"{site['site_id']}_{year}.txt"
            filepath = output_dir / filename
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(report_text)
            
            report_id += 1
    
    print(f"  ✓ {report_id-1} rapports de durabilité créés")


def generate_audit_notes(config: Dict, sites: List[Dict]):
    """Génère les notes d'audit (fichiers texte)"""
    print("📋 Génération des notes d'audit...")
    
    output_dir = TEXT_DIR / "audit_notes_txt"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    positive_templates = [
        "Audit of {site_name} ({date}): Overall compliance: EXCELLENT. Energy management system fully operational. "
        "All metering equipment calibrated. Renewable energy certificates verified. "
        "Recommendation: Maintain current practices. No corrective actions required.",
        
        "Site visit {site_name} - {date}: Strong performance observed. Carbon accounting methodology robust. "
        "Data quality: HIGH. Emission factors correctly applied. Third-party verification completed successfully. "
        "Best practice identified: {best_practice}. Commendations to site team."
    ]
    
    neutral_templates = [
        "Audit {site_name} - {date}: Generally satisfactory. Minor documentation gaps identified in {area}. "
        "Energy consumption tracking adequate but could be improved. "
        "Recommendation: Implement automated data collection system. Follow-up audit in 6 months.",
        
        "Assessment of {site_name} ({date}): Compliance status: ADEQUATE. Some process improvements needed in {process}. "
        "Carbon data completeness: 85%. No major non-conformities. "
        "Action plan: {action}. Target completion: 3 months."
    ]
    
    negative_templates = [
        "CRITICAL AUDIT - {site_name} ({date}): Significant deficiencies found. {issue} not in compliance with standards. "
        "Carbon emissions underreported by estimated {underreporting_pct}%. "
        "Immediate corrective action required: {corrective_action}. "
        "Re-audit scheduled in 30 days. Escalation to management.",
        
        "Non-conformance Report - {site_name} - {date}: MAJOR FINDINGS. {major_finding}. "
        "Data integrity concerns regarding {data_concern}. Emissions inventory incomplete. "
        "Regulatory risk: HIGH. Mandatory actions: {mandatory_actions}. Deadline: URGENT."
    ]
    
    audit_id = 1
    for _ in range(config['audit_notes']['count']):
        site = random.choice(sites)
        
        # Distribution 40% positive, 40% neutral, 20% negative
        rand = random.random()
        if rand < 0.4:
            template = random.choice(positive_templates)
            finding_type = "positive"
        elif rand < 0.8:
            template = random.choice(neutral_templates)
            finding_type = "neutral"
        else:
            template = random.choice(negative_templates)
            finding_type = "negative"
        
        audit_date = (datetime(2023, 1, 1) + timedelta(days=random.randint(0, 1095))).strftime('%Y-%m-%d')
        
        if finding_type == "positive":
            audit_text = template.format(
                site_name=site['site_name'],
                date=audit_date,
                best_practice=random.choice(["real-time monitoring dashboard", "employee engagement program", "predictive maintenance"])
            )
        elif finding_type == "neutral":
            audit_text = template.format(
                site_name=site['site_name'],
                date=audit_date,
                area=random.choice(["Scope 3 emissions", "waste tracking", "water usage"]),
                process=random.choice(["data validation", "supplier engagement", "internal reporting"]),
                action=random.choice(["deploy new software", "train personnel", "update procedures"])
            )
        else:  # negative
            audit_text = template.format(
                site_name=site['site_name'],
                date=audit_date,
                issue=random.choice(["Metering equipment", "Emission factor application", "Scope 3 calculation"]),
                underreporting_pct=random.randint(10, 30),
                corrective_action=random.choice(["recalibrate meters", "recalculate emissions", "engage third-party verifier"]),
                major_finding=random.choice(["Missing electricity invoices Q3", "Incorrect natural gas conversion factors", "Undisclosed refrigerant leaks"]),
                data_concern=random.choice(["Scope 1 diesel consumption", "renewable energy certificates", "supplier emissions"]),
                mandatory_actions=random.choice(["re-submit inventory", "conduct internal investigation", "appoint compliance officer"])
            )
        
        filename = f"AUDIT_{audit_id:06d}_{site['site_id']}.txt"
        filepath = output_dir / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(audit_text)
        
        audit_id += 1
    
    print(f"  ✓ {audit_id-1} notes d'audit créées")


def save_to_csv(data: List[Dict], filename: str, directory: Path):
    """Sauvegarde les données en CSV"""
    if not data:
        print(f"  ⚠ Aucune donnée à sauvegarder pour {filename}")
        return
    
    filepath = directory / filename
    directory.mkdir(parents=True, exist_ok=True)
    
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    
    print(f"  ✓ Sauvegardé: {filepath} ({len(data)} lignes)")


def main():
    """Fonction principale"""
    print("=" * 80)
    print("🌱 Générateur de données ESG & Carbon Analytics")
    print("=" * 80)
    print()
    
    # Charger la configuration
    config = load_config()
    print(f"📋 Configuration chargée depuis {CONFIG_FILE}")
    print()
    
    # Générer les données Operations
    sites = generate_sites(config)
    assets = generate_assets(config, sites)
    energy_consumption = generate_energy_consumption(config, sites)
    production_volumes = generate_production_volumes(config, sites)
    
    # Générer les données ESG
    emission_factors = generate_emission_factors(config)
    carbon_emissions = generate_carbon_emissions(config, energy_consumption, emission_factors, sites)
    suppliers = generate_suppliers(config)
    supplier_emissions = generate_supplier_emissions(config, suppliers)
    
    # Générer les rapports texte
    generate_sustainability_reports(config, sites)
    generate_audit_notes(config, sites)
    
    print()
    print("💾 Sauvegarde des fichiers CSV...")
    print()
    
    # Sauvegarder Operations
    save_to_csv(sites, 'dim_sites.csv', OPERATIONS_DIR)
    save_to_csv(assets, 'dim_assets.csv', OPERATIONS_DIR)
    save_to_csv(energy_consumption, 'fact_energy_consumption.csv', OPERATIONS_DIR)
    save_to_csv(production_volumes, 'fact_production_volumes.csv', OPERATIONS_DIR)
    
    # Sauvegarder ESG
    save_to_csv(emission_factors, 'dim_emission_factors.csv', ESG_DIR)
    save_to_csv(carbon_emissions, 'fact_carbon_emissions.csv', ESG_DIR)
    save_to_csv(suppliers, 'dim_suppliers.csv', ESG_DIR)
    save_to_csv(supplier_emissions, 'fact_supplier_emissions.csv', ESG_DIR)
    
    print()
    print("=" * 80)
    print("✅ Génération terminée avec succès!")
    print("=" * 80)
    print()
    print(f"📊 Statistiques:")
    print(f"  - Sites: {len(sites)}")
    print(f"  - Assets: {len(assets)}")
    print(f"  - Enregistrements énergie: {len(energy_consumption)}")
    print(f"  - Enregistrements production: {len(production_volumes)}")
    print(f"  - Facteurs d'émission: {len(emission_factors)}")
    print(f"  - Émissions carbone: {len(carbon_emissions)}")
    print(f"  - Fournisseurs: {len(suppliers)}")
    print(f"  - Émissions fournisseurs: {len(supplier_emissions)}")
    print(f"  - Rapports durabilité: {len(sites) * 3} fichiers texte")
    print(f"  - Notes d'audit: {config['audit_notes']['count']} fichiers texte")
    print()
    print(f"📁 Fichiers générés dans:")
    print(f"  - Operations: {OPERATIONS_DIR}")
    print(f"  - ESG: {ESG_DIR}")
    print(f"  - Text: {TEXT_DIR}")
    print()


if __name__ == "__main__":
    main()
