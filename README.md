# GenAI-FraudGuard

FraudGuard is an end-to-end fraud detection and investigation system built on the PaySim dataset, combining Machine Learning, Rule-Based Scoring, and LLM-driven explanations, with an interactive Streamlit dashboard for real-time analysis.

This project demonstrates how modern financial fraud systems move beyond binary flags into explainable, investigator-ready intelligence.

## Ket Features

## Multi-Layer Fraud Scoring

FraudGuard evaluates each transaction using:

* ML Fraud Score (anomaly detection model)
* Rule Engine Score (domain rules: balance mismatch, risky transaction types, etc.)
* Final Fraud Score (weighted ensemble of ML + rules)
* 
Transactions crossing a risk threshold are automatically flagged.

## AI Investigator (LLM)

For high-risk transactions only, FraudGuard generates:

* Risk Level (Low / Medium / High)
* Key Risk Explanation
* Recommended Action

## Interactive Streamlit Dashboard

The dashboard allows users to:

* Enter a Transaction ID to view full transaction details
* Instantly see:

    * Fraud scores
    * Balance changes
    * Rule engine reasons
    * AI investigator explanation

## Tech Stack

* Python
* Pandas / NumPy
* Scikit-learn
* LLMs via Free APIs - Groq (LLaMA-3.1)
* Streamlit
