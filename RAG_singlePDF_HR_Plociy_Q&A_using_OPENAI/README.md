Steps to Execute the Code

Follow these instructions to run the notebook successfully in Google Colab:
1. Configure OpenAI Credentials:
    Go to the Secrets (key icon 🔑) in the left sidebar of Google Colab.
    Add a new secret with the name: OPENAI_API_KEY.
    Paste your actual OpenAI API key into the value field.
    Ensure the "Notebook access" toggle is turned ON for this secret.

2. Upload the Document:
    When you run the code cells, a FILE UPLOAD dialogue will appear in the output cell.
    Please upload the file named: sample_hr_policy.pdf.
    The system will automatically index this file into a local FAISS vector store.

3. Ask Questions:
    Once the indexing is complete, use the chain.invoke() cell to ask questions about notice periods, leave policies, or employee benefits.
