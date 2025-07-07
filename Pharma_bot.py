import streamlit as st
import random
import json

# Load JSON data
with open("pharma_data.json", "r") as f:
    pharma_data = json.load(f)

st.set_page_config(page_title="Pharmacology Mnemonic Bot", layout="centered")
st.title("🧠 Pharmacology Mnemonic & Quiz Bot")

# Choose drug class
all_classes = list(pharma_data.keys())
drug_class = st.selectbox("📘 Choose a drug class to learn:", all_classes)

if drug_class:
    st.subheader(f"📚 Classification of {drug_class}")
    classification = pharma_data[drug_class].get("classification", [])
    for item in classification:
        st.markdown(f"- {item}")

    st.subheader("💡 Mnemonic")
    st.markdown(f"**Mnemonic:** {pharma_data[drug_class]['mnemonic']}")

    st.subheader("📝 Quick Quiz")
    quiz = random.choice(pharma_data[drug_class].get("quiz", []))
    question = quiz["question"]
    correct_answer = quiz["answer"]

    user_answer = st.text_input(f"Q: {question}", key=question)
    if user_answer:
        if user_answer.strip().lower() == correct_answer.strip().lower():
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Incorrect. Correct answer: {correct_answer}")
