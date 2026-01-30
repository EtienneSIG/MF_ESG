# GitHub Copilot Agents Configuration

Ce fichier configure les agents GitHub Copilot spécifiques au scénario ESG & Carbon Analytics.

## Agent ESG Manager

**Rôle** : Assistant Responsable ESG pour analyses de durabilité

**Compétences** :
- Analyse carbon footprint (Scope 1/2/3)
- Suivi objectifs de réduction
- Identification fournisseurs à risque
- Analyse performance énergétique
- Extraction insights rapports durabilité

**Instructions système** :
Voir [`docs/data_agent_instructions.md`](docs/data_agent_instructions.md)

**Exemples de questions** :
- "Quels sites dépassent nos objectifs carbone 2025 ?"
- "Où agir en priorité pour réduire le Scope 3 ?"
- "Résume les audits avec findings négatifs"
- "Quelle est notre intensité carbone ?"

## Configuration Fabric Data Agent

Lors du déploiement dans Microsoft Fabric, configurer le Data Agent avec :
- **Nom** : ESG_Manager
- **Source** : Semantic Model ESG
- **Instructions** : Coller le contenu de `data_agent_instructions.md`
- **Exemples** : Utiliser `data_agent_examples.md` pour tests

## Tests Recommandés

Utiliser les 25 questions de [`docs/data_agent_examples.md`](docs/data_agent_examples.md) pour valider :
- ✅ Calculs émissions Scope 1/2/3 corrects
- ✅ Objectifs vs réel identifiés
- ✅ Fournisseurs à risque détectés
- ✅ Insights AI extraits des rapports texte

## Contexte ESG

L'agent comprend :
- **Scopes GHG Protocol** : Scope 1 (direct), Scope 2 (indirect énergie), Scope 3 (chaîne de valeur)
- **Objectifs SBTi** : Réduction alignée Paris Agreement
- **CSRD** : Corporate Sustainability Reporting Directive
- **Intensité carbone** : Émissions par unité de production

## Scénarios Prédéfinis

L'agent peut répondre sur :
1. **Renewable energy ramp-up** : 25% → 35% → 50%
2. **Supplier risk analysis** : 10 fournisseurs problématiques
3. **Site performance** : Best performers vs underperformers
