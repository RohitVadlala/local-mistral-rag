from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential

# ✅ Paste your actual endpoint and key here
endpoint = "https://genai-formrec.cognitiveservices.azure.com/"
key = "A97xd773BcoNS5uMJ3uLo7F1B47sFwfR6t2uHJib8sI9uuA0OGtkJQQJ99BFACYeBjFXJ3w3AAALACOGHBVw"  # ← replace this

document_analysis_client = DocumentAnalysisClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)

# PDF file that you downloaded to your desktop
with open("tesla_10k_2024.pdf", "rb") as f:
    poller = document_analysis_client.begin_analyze_document(
        model_id="prebuilt-document", document=f
    )
    result = poller.result()

# Save the extracted text
full_text = ""
for page in result.pages:
    for line in page.lines:
        full_text += line.content + "\n"

# Save to file
with open("extracted_text.txt", "w", encoding="utf-8") as out_file:
    out_file.write(full_text)

print("✅ Text extracted and saved to 'extracted_text.txt'")
