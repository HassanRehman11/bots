import streamlit as st
import openai
import requests
from fpdf import FPDF

# Set page config
st.set_page_config(page_title="Divorce Assistance Bot", page_icon="💔")
st.title("💔 Divorce Assistant Chatbot")
st.write("I'm here to guide you through the divorce process with empathy and legal insights.")

# Set OpenAI API Key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "location" not in st.session_state:
    st.session_state.location = ""

# Jurisdiction selection
locations = ["", "USA", "UK", "Canada", "UAE", "India", "Australia", "Saudi Arabia", "Pakistan", "Indonesia", "Egypt"]
location_selected = st.selectbox(
    "Please select your location to begin:",
    locations,
    index=locations.index(st.session_state.get("location", ""))
)

# Only proceed if location is selected
if location_selected:
    st.session_state.location = location_selected

    # Determine if Islamic law should apply
    islamic_countries = ["UAE", "Saudi Arabia", "Pakistan", "Indonesia", "Egypt"]
    is_sharia = st.session_state.location in islamic_countries

    # Define system prompt
    base_prompt = f"""
You are a compassionate legal assistant who helps users navigate divorce based on their location: {st.session_state.location}.
Provide supportive, accurate, and step-by-step legal guidance.
Be empathetic and clear. Avoid offering legal advice beyond public information.
"""

    if is_sharia:
        sharia_prompt = "Provide information about Islamic/Shariah-based divorce processes (e.g., talaq, khula) where relevant. Clarify that laws may vary by country and interpretations."
        system_prompt = base_prompt + sharia_prompt
    else:
        system_prompt = base_prompt

    # Initialize messages
    if not st.session_state.messages:
        st.session_state.messages.append({"role": "system", "content": system_prompt})

    # Chat input
    for msg in st.session_state.messages[1:]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Ask a question about divorce or share how you're feeling..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=st.session_state.messages
                )
                reply = response.choices[0].message.content
                st.markdown(reply)

        st.session_state.messages.append({"role": "assistant", "content": reply})

    # --- Legal Form Generator ---
    st.header("📄 Generate a Separation Agreement")
    name1 = st.text_input("Partner 1 Full Name")
    name2 = st.text_input("Partner 2 Full Name")

    if st.button("Generate PDF Agreement"):
        if name1 and name2:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            text = f"""
Separation Agreement

This agreement is made between {name1} and {name2}.

1. Both parties agree to live separately.
2. Child custody, asset division, and financial responsibilities will be addressed in good faith.
3. This document is a non-legally-binding summary unless notarized.

Date: _______________
Signatures: _______________     _______________
"""
            pdf.multi_cell(0, 10, text)
            pdf.output("separation_agreement.pdf")
            with open("separation_agreement.pdf", "rb") as f:
                st.download_button("Download PDF", f, file_name="separation_agreement.pdf")
        else:
            st.warning("Please enter both names.")

    # --- Scheduler ---
    st.header("🗓️ Schedule an Appointment")
    st.markdown("[Book a legal or emotional support consultation](https://calendly.com)")

    # --- Divorce Checklist ---
    st.header("✅ Divorce Process Checklist")
    steps = [
        "🔢 Decide to file for divorce",
        "📅 Notify your spouse",
        "💼 Divide assets and debts",
        "👩‍👧 Handle child custody arrangements",
        "📄 Submit paperwork to court",
        "📍 Attend hearings (if required)",
        "🛎️ Receive final divorce decree"
    ]
    for step in steps:
        st.checkbox(step, key=step)

    st.caption("This tool provides general guidance and is not a substitute for professional legal advice.")
else:
    st.warning("Please select your location to begin using the assistant.")