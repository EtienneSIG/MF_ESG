"""
Script de Validation des Noms de Colonnes - ESG & Carbon Analytics Demo

Vérifie que tous les noms de colonnes correspondent au schéma attendu
et que les données sont cohérentes pour les DAX queries.

Usage:
    cd src
    python validate_schema.py
"""

import pandas as pd
import sys
from pathlib import Path

class SchemaValidator:
    def __init__(self, data_root='../data/raw'):
        self.data_root = Path(data_root)
        self.errors = []
        self.warnings = []
        
    def validate_all(self):
        """Exécute toutes les validations"""
        print("=" * 80)
        print("VALIDATION DES SCHEMAS - ESG & Carbon Analytics Demo")
        print("=" * 80)
        print()
        
        # Validation des tables ESG
        self.validate_esg_tables()
        
        # Validation des tables Suppliers
        self.validate_supplier_tables()
        
        # Validation des relations
        self.validate_relationships()
        
        # Afficher le résumé
        self.print_summary()
        
        return len(self.errors) == 0
    
    def validate_esg_tables(self):
        """Valide les tables ESG"""
        print("--- Validation ESG Tables ---")
        
        # emissions (CRITIQUE pour Carbon Footprint)
        emissions = self.load_csv('esg/fact_carbon_emissions.csv')
        if emissions is not None:
            self.check_columns(emissions, 'emissions', [
                'emission_id', 'site_id', 'scope', 'emission_date',
                'co2e_tonnes', 'source', 'category'
            ])
            
            # Vérifier scope values (CRITIQUE)
            if 'scope' in emissions.columns:
                expected_scopes = {'Scope 1', 'Scope 2', 'Scope 3'}
                actual_scopes = set(emissions['scope'].unique())
                
                if expected_scopes != actual_scopes:
                    self.errors.append(
                        f"emissions.scope attendus: {expected_scopes}, "
                        f"trouvés: {actual_scopes}"
                    )
                else:
                    print(f"  ✅ emissions.scope correct: {actual_scopes}")
            
            # Vérifier co2e_tonnes > 0
            if 'co2e_tonnes' in emissions.columns:
                negative_emissions = emissions['co2e_tonnes'] < 0
                if negative_emissions.any():
                    self.errors.append(
                        f"{negative_emissions.sum()} emissions avec co2e_tonnes < 0"
                    )
        
        # targets (CRITIQUE pour Target Achievement)
        targets = self.load_csv('esg/dim_targets.csv')
        if targets is not None:
            self.check_columns(targets, 'targets', [
                'target_id', 'scope', 'baseline_year', 'target_year',
                'baseline_emissions', 'target_emissions', 'reduction_pct'
            ])
        
        # sites
        sites = self.load_csv('operations/dim_sites.csv')
        if sites is not None:
            self.check_columns(sites, 'sites', [
                'site_id', 'site_name', 'country', 'site_type', 'production_capacity'
            ])
        
        # energy_consumption
        energy = self.load_csv('operations/fact_energy_consumption.csv')
        if energy is not None:
            self.check_columns(energy, 'energy_consumption', [
                'consumption_id', 'site_id', 'energy_date', 'energy_type',
                'consumption_mwh', 'renewable'
            ])
        
        print()
    
    def validate_supplier_tables(self):
        """Valide les tables Suppliers"""
        print("--- Validation Supplier Tables ---")
        
        # suppliers (CRITIQUE pour Supply Chain Risk)
        suppliers = self.load_csv('esg/dim_suppliers.csv')
        if suppliers is not None:
            self.check_columns(suppliers, 'suppliers', [
                'supplier_id', 'supplier_name', 'country', 'category',
                'carbon_intensity', 'risk_level', 'annual_spend_eur'
            ])
            
            # Vérifier risk_level values (CRITIQUE)
            if 'risk_level' in suppliers.columns:
                expected_risks = {'low', 'medium', 'high', 'critical'}
                actual_risks = set(suppliers['risk_level'].unique())
                
                if expected_risks != actual_risks:
                    self.errors.append(
                        f"suppliers.risk_level attendus: {expected_risks}, "
                        f"trouvés: {actual_risks}"
                    )
                else:
                    print(f"  ✅ suppliers.risk_level correct: {actual_risks}")
        
        # audits
        audits = self.load_csv('esg/fact_audits.csv')
        if audits is not None:
            self.check_columns(audits, 'audits', [
                'audit_id', 'site_id', 'audit_date', 'audit_type',
                'finding_severity', 'status'
            ])
        
        print()
    
    def validate_relationships(self):
        """Valide les relations entre tables (foreign keys)"""
        print("--- Validation Relations (Foreign Keys) ---")
        
        # Charger les tables principales
        emissions = self.load_csv('esg/fact_carbon_emissions.csv')
        sites = self.load_csv('operations/dim_sites.csv')
        energy = self.load_csv('operations/fact_energy_consumption.csv')
        audits = self.load_csv('esg/fact_audits.csv')
        
        if emissions is None or sites is None:
            self.errors.append("Impossible de valider les relations: tables manquantes")
            return
        
        # Vérifier emissions.site_id → sites.site_id
        invalid_sites_em = ~emissions['site_id'].isin(sites['site_id'])
        if invalid_sites_em.any():
            self.errors.append(
                f"{invalid_sites_em.sum()} emissions avec site_id invalide"
            )
        else:
            print(f"  ✅ emissions.site_id → sites.site_id (100% valide)")
        
        # Vérifier energy_consumption.site_id → sites.site_id
        if energy is not None:
            invalid_sites_en = ~energy['site_id'].isin(sites['site_id'])
            if invalid_sites_en.any():
                self.errors.append(
                    f"{invalid_sites_en.sum()} energy_consumption avec site_id invalide"
                )
            else:
                print(f"  ✅ energy_consumption.site_id → sites.site_id (100% valide)")
        
        # Vérifier audits.site_id → sites.site_id
        if audits is not None:
            invalid_sites_au = ~audits['site_id'].isin(sites['site_id'])
            if invalid_sites_au.any():
                self.errors.append(
                    f"{invalid_sites_au.sum()} audits avec site_id invalide"
                )
            else:
                print(f"  ✅ audits.site_id → sites.site_id (100% valide)")
        
        print()
    
    def check_columns(self, df, table_name, expected_columns):
        """Vérifie que les colonnes attendues sont présentes"""
        missing = set(expected_columns) - set(df.columns)
        extra = set(df.columns) - set(expected_columns)
        
        if missing:
            self.errors.append(f"{table_name}: colonnes manquantes: {missing}")
        
        if extra:
            self.warnings.append(f"{table_name}: colonnes inattendues: {extra}")
        
        if not missing and not extra:
            print(f"  ✅ {table_name}: {len(expected_columns)} colonnes valides")
    
    def load_csv(self, relative_path):
        """Charge un CSV et gère les erreurs"""
        filepath = self.data_root / relative_path
        
        if not filepath.exists():
            self.errors.append(f"Fichier manquant: {filepath}")
            return None
        
        try:
            return pd.read_csv(filepath, encoding='utf-8')
        except Exception as e:
            self.errors.append(f"Erreur lecture {filepath}: {e}")
            return None
    
    def print_summary(self):
        """Affiche le résumé des validations"""
        print("=" * 80)
        print("RÉSUMÉ DE VALIDATION")
        print("=" * 80)
        
        if self.warnings:
            print(f"\n⚠️  {len(self.warnings)} AVERTISSEMENT(S):")
            for warning in self.warnings:
                print(f"  - {warning}")
        
        if self.errors:
            print(f"\n❌ {len(self.errors)} ERREUR(S):")
            for error in self.errors:
                print(f"  - {error}")
            print("\n🔧 ACTIONS REQUISES:")
            print("  1. Corriger les erreurs listées ci-dessus")
            print("  2. Régénérer les données avec generate_data.py")
            print("  3. Relancer ce script de validation")
            print("\n❌ VALIDATION ÉCHOUÉE")
        else:
            print("\n✅ VALIDATION RÉUSSIE - Tous les schémas sont corrects !")
            print("\n✅ Les DAX queries devraient fonctionner correctement.")
        
        print("=" * 80)


def main():
    """Point d'entrée principal"""
    validator = SchemaValidator()
    success = validator.validate_all()
    
    # Exit code pour CI/CD
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
