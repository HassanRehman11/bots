# Divorce Assistance Bot 💔
![Divorce Assistant Bot](https://github.com/HassanRehman11/bots/blob/master/divorce_assistance_bot/bot.png)
This chatbot is designed to guide users through the divorce process with empathy, legal insights, and practical tools. The bot provides location-specific legal advice, generates legal documents, schedules appointments, and offers a divorce process checklist.

## Features

### 1. **Location-Based Legal Guidance**
   - The bot asks the user to select their location (country) to tailor responses based on jurisdiction-specific divorce laws.
   - Locations available include:
     - **USA**
     - **UK**
     - **Canada**
     - **UAE**
     - **Saudi Arabia**
     - **Pakistan**
     - **Indonesia**
     - **Egypt**
   - If the user selects an Islamic country, the bot will include **Sharia-based divorce processes** (e.g., *Talaq*, *Khula*) and explain relevant details.

### 2. **Sharia-Based Divorce Information**
   - For users in Islamic countries (UAE, Saudi Arabia, Pakistan, Indonesia, Egypt), the bot provides insights into Islamic divorce processes, including:
     - **Talaq** (Divorce initiated by the husband)
     - **Khula** (Divorce initiated by the wife)
     - Explanation of various steps in the divorce process, such as reconciliation, and the role of the court.

### 3. **Chatbot Interaction**
   - The chatbot allows users to ask any questions related to divorce, including emotional support and legal guidance.
   - The bot provides clear and compassionate responses and walks the user through the divorce steps in their location.
   - Uses **OpenAI GPT-4** to respond to user queries.

### 4. **Separation Agreement Generator (PDF)**
   - Users can generate a **Separation Agreement PDF** for divorce purposes by entering the names of both parties.
   - The generated PDF contains a basic, non-legally binding separation agreement with placeholders for signature and date.
   - The document includes sections on child custody, asset division, and financial responsibilities.
   - Users can **download the generated PDF** directly.

### 5. **Appointment Scheduling**
   - Users can **schedule a consultation** with a legal advisor, therapist, or mediator through a link to a **Calendly** (or similar appointment scheduler).
   - The link is provided in the app for easy access to book appointments for emotional or legal support.

### 6. **Divorce Process Checklist**
   - A **divorce process checklist** is available to guide users through the important steps of divorce:
     - **Decide to file for divorce**
     - **Notify your spouse**
     - **Divide assets and debts**
     - **Handle child custody arrangements**
     - **Submit paperwork to court**
     - **Attend hearings**
     - **Receive final divorce decree**
   - Users can **check off** each step as they progress in their divorce journey.

### 7. **Empathetic Support**
   - The bot provides **compassionate, supportive responses**, helping users navigate emotional and legal challenges during the divorce process.

## Requirements

1. **Python 3.x**
2. **Streamlit** – `pip install streamlit`
3. **OpenAI API Key** – Get your key from [OpenAI](https://beta.openai.com/signup/)
4. **FPDF** – `pip install fpdf` (for PDF generation)

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/divorce-assistant-bot.git
    cd divorce-assistant-bot
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Add your **OpenAI API key** to the `.streamlit/secrets.toml` file:
    ```toml
    OPENAI_API_KEY = "your_openai_api_key"
    ```

4. Run the app:
    ```bash
    streamlit run divorce_assistant_bot.py
    ```

5. Open your browser and visit `http://localhost:8501` to use the Divorce Assistance Bot.

## Limitations

- **Legal Advice Disclaimer**: This bot is intended to provide general guidance. It is **not a substitute for professional legal advice**.
- **Jurisdiction Accuracy**: The bot uses general legal knowledge for each location. Laws may vary based on specific local jurisdictions and should be verified by a legal professional.
- **Emotional Support**: While the bot provides empathetic guidance, users are encouraged to seek professional counseling for emotional support.


