# Rag-MultiplePDF-MedicalDoc-Assistant

An intelligent Retrieval-Augmented Generation (RAG) system built with **LangChain**, **ChromaDB**, and **Gradio**. This assistant allows users to upload multiple medical or technical PDF documents and perform context-aware Q&A using the **GPT-4o-mini** model.

## Features
*   **Multi-PDF Support:** Upload and index multiple files simultaneously.
*   **Semantic Search:** Uses OpenAI Embeddings and ChromaDB for high-accuracy retrieval.
*   **Strict Guardrails:** Optimized system prompt ensures the AI only answers based on the provided document context, preventing hallucinations.
*   **Interactive UI:** Clean, dual-column Gradio interface for easy file management and chatting.

---

## Setup & Installation

### 1. Configure OpenAI Credentials
Before running the code, you must securely provide your API key in the Google Colab environment:
1.  Go to the **Secrets** (key icon ) in the left sidebar of Google Colab.
2.  Add a new secret with the name: `OPENAI_API_KEY`.
3.  Paste your actual OpenAI API key into the value field.
4.  Ensure the **"Notebook access"** toggle is turned **ON** for this secret.

### 2. Install Dependencies
Run the following command to install the required libraries:
```bash
pip install -q langchain langchain-openai langchain-community pypdf langchain-text-splitters chromadb gradio
```

## Usage
1.  **Run the Notebook:** Execute all cells to launch the Gradio interface.
2.  **Step 1 — Upload:** Select your PDF files and click **"Index PDFs"**. The system will report the number of files and total chunks stored.
3.  **Step 2 — Ask:** Type your query into the text box. The assistant will retrieve relevant data and provide an answer based *only* on your documents.

## Author
**Senior Firmware Engineer & AI Enthusiast**
*Currently upskilling in Agentic AI and Generative AI (Microsoft & Simplilearn).*
