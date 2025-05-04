## 🦷 Dental Health Assistant

This is a **Streamlit web app** that uses **OpenAI's GPT-4o vision model** to analyze a user's uploaded photo of their teeth. It provides visual observations (like color, alignment, visible dental issues) and allows for follow-up chat-based questions related to dental care.

---

### Features

* Upload a **photo of your teeth**
* Get **AI-powered analysis** on:

  * Color
  * Alignment
  * Visible signs of decay, plaque, gaps, etc.
* Ask **follow-up questions** based on the analysis
* Designed for **informational use only** (not medical diagnosis)

---

### 🚀 Demo

![demo](https://github.com/HassanRehman11/bots/blob/master/dental_care_bot/bot.png) *(Optional)*

---

### 🧰 Tech Stack

* [Streamlit](https://streamlit.io)
* [OpenAI GPT-4o](https://openai.com/gpt-4)
* Python
* PIL (Pillow)

---

### ⚙️ Setup Instructions

#### 1. Clone the Repository

```bash
git clone https://github.com/your-username/dental-health-assistant.git
cd dental-health-assistant
```

#### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Configure OpenAI API Key

Create a file at `.streamlit/secrets.toml` with your OpenAI key:

```toml
OPENAI_API_KEY = "your-openai-api-key"
```

---

### 🧪 Run the App

```bash
streamlit run dental_bot.py
```

Then open your browser to [http://localhost:8501](http://localhost:8501).

---

### 📁 File Structure

```bash
├── dental_bot.py           # Main app code
├── requirements.txt        # Python dependencies
└── .streamlit/
    └── secrets.toml        # API Key config
```

---

### 📌 Requirements

* Python 3.8+
* Access to **GPT-4o with Vision** via OpenAI
* Streamlit installed

---

### ⚠️ Disclaimer

This app is **not a replacement for professional dental advice**. It provides **visual insights only**. Always consult a licensed dentist for diagnosis or treatment.

---

