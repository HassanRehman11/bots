import streamlit as st
import openai
from PIL import Image
import base64

# Page configuration
st.set_page_config(page_title="🦷 Dental Bot", page_icon="🦷")
st.title("🦷 Dental Health Assistant")
st.write("Upload a photo of your teeth, and I'll analyze and help you understand your dental condition.")

# Set OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Upload image
uploaded_image = st.file_uploader("📷 Upload an image of your teeth (front-facing photo)", type=["jpg", "jpeg", "png"])

if uploaded_image and "image_analyzed" not in st.session_state:
    image = Image.open(uploaded_image)
    st.image(image, caption="🖼️ Uploaded Teeth Image", use_column_width=True)

    if st.button("🧠 Analyze Teeth"):
        with st.spinner("Analyzing image..."):
            image_bytes = uploaded_image.getvalue()
            base64_image = base64.b64encode(image_bytes).decode("utf-8")
            image_url = f"data:image/jpeg;base64,{base64_image}"

            # OpenAI Vision API request
            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You're a dental assistant AI that can visually analyze uploaded teeth photos and explain the condition in human terms. Do not give diagnoses. Only describe visible characteristics (color, alignment, decay, gaps, etc.) and suggest general care."},
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": "Analyze this image and describe what you observe about my teeth (color, alignment, visible issues)."},
                            {"type": "image_url", "image_url": {"url": image_url}}
                        ]
                    }
                ],
                max_tokens=700
            )

            analysis = response.choices[0].message.content
            st.session_state["analysis"] = analysis
            st.session_state["image_analyzed"] = True
            st.session_state["chat_history"] = [
                {"role": "system", "content": "You're a dental care assistant AI. Refer to the initial analysis to help the user with their concerns."},
                {"role": "assistant", "content": analysis}
            ]
            st.success("✅ Analysis complete!")

# Display previous analysis (if exists)
if "analysis" in st.session_state:
    st.markdown("### 📝 Analysis")
    st.markdown(st.session_state["analysis"])

# Follow-up chat
if "analysis" in st.session_state:
    st.markdown("## 💬 Ask Follow-Up Questions")
    user_input = st.chat_input("Ask a dental care question...")

    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.spinner("Responding..."):
            followup_response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=st.session_state.chat_history
            )
            reply = followup_response.choices[0].message.content
            st.session_state.chat_history.append({"role": "assistant", "content": reply})
            st.markdown(f"**Assistant:** {reply}")
