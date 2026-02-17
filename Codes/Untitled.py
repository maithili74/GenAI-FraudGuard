#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title(" FraudGuard – Transaction Investigator")

df = pd.read_csv(r"C:\Users\MAITHILI\Gen-AI_FraudGuard\Datasets\paysim_processed_with_scores.csv")

transaction_id = st.number_input("Enter Transaction ID", min_value=0)

if st.button("Search"):

    transaction = df[df["transaction_id"] == transaction_id]

    if transaction.empty:
        st.error("Transaction not found.")
    else:
        row = transaction.iloc[0]

        
        if row["total_fraud_score"] > 0.7:
            st.error(" HIGH RISK")
        elif row["total_fraud_score"] > 0.5:
            st.warning(" MEDIUM RISK")
        else:
            st.success(" LOW RISK")

        st.subheader(" Transaction Details")
        st.write(row[[
            "amount",
            "oldbalanceOrg",
            "newbalanceOrig",
            "oldbalanceDest",
            "newbalanceDest"
        ]])

        st.subheader(" Fraud Scores")
        st.write("ML Score:", row["ml_fraud_score"])
        st.write("Rule Score:", row["rule_score"])
        st.write("Total Score:", row["total_fraud_score"])

        st.subheader(" AI Investigator")
        st.write(row["llm_explanation"])

