import streamlit as st
import requests
import openai
import yaml
import json

# Set your OpenAI API key from secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("🔍 Swagger Chatbot")
st.write("Query your OpenAPI documentation using natural language.")

# Input: Swagger URL
swagger_url = st.text_input("Enter your Swagger/OpenAPI URL (YAML or JSON)")

spec = None

if swagger_url:
    try:
        response = requests.get(swagger_url)
        response.raise_for_status()
        content_type = response.headers.get('Content-Type', '')

        if "yaml" in content_type or swagger_url.endswith((".yaml", ".yml")):
            spec = yaml.safe_load(response.text)
        else:
            spec = response.json()

        st.success("✅ OpenAPI spec loaded!")

    except Exception as e:
        st.error(f"❌ Failed to fetch or parse spec: {e}")

# Ask a question if spec is loaded
if spec:
    user_query = st.text_input("Ask a question (e.g., 'How do I create a user?')")

    if user_query:
        # Create context from OpenAPI paths
        endpoint_context = ""
        for path, methods in spec.get("paths", {}).items():
            for method, details in methods.items():
                summary = details.get("summary", "")
                desc = details.get("description", "")
                endpoint_context += f"{method.upper()} {path} - {summary or ''} {desc or ''}\n"

        # Prompt for OpenAI
        prompt = f"""
You are an expert in OpenAPI documentation.
Given the following endpoints:

{endpoint_context}

Answer the user's question: "{user_query}"

Respond with:
1. Method
2. Path
3. Summary (if available)
4. Example curl command (with dummy body if needed)
"""

        with st.spinner("🧠 Thinking..."):
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
            )

        st.subheader("🔍 Matched Endpoint")
        st.markdown(response.choices[0].message.content)
