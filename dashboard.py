#!/usr/bin/env python
# coding: utf-8

# In[3]:





# In[1]:


import streamlit as st
import pandas as pd
import plotly.express as px


# In[3]:


# In[4]:



# In[5]:



# -------------------------
# Page config
# -------------------------
# -------------------------
# Load data
# -------------------------
@st.cache_data
def load_data():
    return pd.read_csv(r"C:\Users\MAITHILI\Gen-AI_FraudGuard\paysim_processed_with_scores_with_txn_id.csv")

df = load_data()

st.set_page_config(page_title="FraudGuard", layout="centered")
st.title("💡 FraudGuard — Transaction Lookup")

st.markdown(
    "Enter a **transaction step number** to view full transaction details and AI investigation."
)

# -------------------------
# Transaction Lookup Input
# -------------------------
txn_id = st.number_input(
    "🔎 Enter Transaction ID",
    min_value=int(df["transaction_id"].min()),
    max_value=int(df["transaction_id"].max()),
    step=1
)

txn = df[df["transaction_id"] == txn_id]
if txn.empty:
    st.error("Transaction not found")
    st.stop()

txn = txn.iloc[0]

# -------------------------
# Risk Badge
# -------------------------
if txn["total_fraud_score"] >= 0.7:
    risk_label = "🔴 HIGH RISK"
elif txn["total_fraud_score"] >= 0.5:
    risk_label = "🟡 MEDIUM RISK"
else:
    risk_label = "🟢 LOW RISK"

st.subheader(f"Risk Level: {risk_label}")

# -------------------------
# Transaction Details
# -------------------------
st.subheader("💳 Transaction Details")

c1, c2 = st.columns(2)

with c1:
    st.metric("Amount", f"{txn['amount']:.2f}")
    st.metric("ML Fraud Score", f"{txn['ml_fraud_score']:.2f}")
    st.metric("Rule Score", int(txn["rule_score"]))
    st.metric("Total Fraud Score", f"{txn['total_fraud_score']:.2f}")

with c2:
    st.metric("Sender Balance Before", f"{txn['oldbalanceOrg']:.2f}")
    st.metric("Sender Balance After", f"{txn['newbalanceOrig']:.2f}")
    st.metric("Receiver Balance Before", f"{txn['oldbalanceDest']:.2f}")
    st.metric("Receiver Balance After", f"{txn['newbalanceDest']:.2f}")

# -------------------------
# Balance Changes
# -------------------------
st.subheader("💰 Balance Changes")

st.write(
    f"""
- **Sender balance change:** {txn['balance_delta_org']:.2f}  
- **Receiver balance change:** {txn['balance_delta_dest']:.2f}
"""
)

# -------------------------
# Fraud Flags
# -------------------------
st.subheader("🚨 Fraud Flags")

st.write(f"- **ML Anomaly Flag:** {txn['ml_anomaly_flag']}")
st.write(f"- **Rule Score:** {txn['rule_score']}")
st.write(f"- **Flagged Fraud:** {txn['flagged_fraud']}")

# -------------------------
# Rule Reasons
# -------------------------
if txn["rule_reasons"]:
    st.subheader("📜 Rule Engine Reasons")
    st.info(txn["rule_reasons"])

# -------------------------
# LLM Explanation
# -------------------------
st.subheader("🧠 AI Investigator Explanation")

if txn["flagged_fraud"] == 1:
    st.success(txn["llm_explanation"])
else:
    st.warning("Low-risk transaction — not investigated by AI.")

# In[ ]:




