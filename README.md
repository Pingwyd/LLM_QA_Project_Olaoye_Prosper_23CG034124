# Prospers' NLP Question & Answering System 🤲

A powerful and elegant Question & Answering system powered by the **Gemma 2 (9B)** Large Language Model via the Hugging Face API. This project features both a modern web interface and a command-line tool.

## 🌟 Features

-   **Advanced NLP**: Utilizes Google's Gemma 2-9b-it model for high-quality responses.
-   **Modern UI**: A beautiful, glassmorphism-inspired dark theme web interface.
-   **Dual Interface**:
    -   **Web App**: User-friendly Flask-based web GUI.
    -   **CLI Tool**: Efficient command-line interface for quick queries.
-   **Responsive Design**: Works seamlessly on desktop and mobile.
-   **Deployment Ready**: Configured for easy deployment on Render.

## 🛠️ Tech Stack

-   **Backend**: Python, Flask
-   **AI/ML**: Hugging Face Inference API (Gemma 2)
-   **Frontend**: HTML5, CSS3 (Glassmorphism design)
-   **Deployment**: Gunicorn, Render

## 🚀 Getting Started

### Prerequisites

-   Python 3.8 or higher
-   A Hugging Face Account & API Key

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/Pingwyd/LLM_QA_Project_Olaoye_Prosper_23CG034124.git
    cd LLM_QA_Project_Olaoye_Prosper_23CG034124
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment Variables**
    -   Create a `.env` file in the root directory.
    -   Add your Hugging Face API key:
        ```
        HUGGINGFACE_API_KEY=hf_your_actual_api_key_here
        ```

### Running the Application

#### 🌐 Web Interface
1.  Start the Flask server:
    ```bash
    python app.py
    ```
2.  Open your browser and navigate to `http://127.0.0.1:5000`.

#### 💻 CLI Tool
1.  Run the command-line script:
    ```bash
    python LLM_QA_CLI.py
    ```
2.  Follow the prompts to ask questions directly in your terminal.

## 📦 Deployment

This project is ready for deployment on **Render**.

1.  Push your code to GitHub.
2.  Create a new **Web Service** on Render.
3.  Connect your repository.
4.  Add the `HUGGINGFACE_API_KEY` in the **Environment Variables** section of your Render dashboard.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).