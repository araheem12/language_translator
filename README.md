# language_translator
Here’s a full README.md file for your Gemini Translator app:

````markdown
# 🌍 Gemini Language Translator

A simple and interactive web application built with **Streamlit** that uses Google’s **Gemini** language model via LangChain to translate text into multiple languages.

---

## Features

- Translation powered by Google Gemini (`gemini-1.5-flash-latest`) model
- Supports popular languages: Spanish, French, German, Chinese, Arabic, Urdu, Japanese, Russian, Hindi, Italian
- Easy-to-use web interface with Streamlit
- Real-time translation with spinner feedback
- Handles errors gracefully
- Configurable via environment variables


---

## Setup & Installation

### Prerequisites

- Python 3.8+
- [Google Cloud API Key](https://console.cloud.google.com/apis/credentials) with access to Gemini model
- `pip` package manager

### Installation Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/gemini-translator.git
   cd gemini-translator
````

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your Google API key:

   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```

5. Run the app:

   ```bash
   streamlit run app.py
   ```

---

## Usage

* Enter the text you want to translate in the text area.
* Select the target language from the dropdown.
* Click the **Translate** button.
* View the translated text below.

---

## Project Structure

```
.
├── app.py                # Main Streamlit app
├── .env                  # Environment variables (not committed)
├── requirements.txt      # Python dependencies
├── README.md             # This file
└── demo_screenshot.png   # (Optional) Screenshot for demo
```

---

## Technologies Used

* [Streamlit](https://streamlit.io/) — UI framework for the app
* [LangChain](https://python.langchain.com/en/latest/) — To integrate Google Gemini model
* Google Gemini Language Model via Google Cloud API

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

* Thanks to the Google Gemini and LangChain teams for their amazing tools.

---

