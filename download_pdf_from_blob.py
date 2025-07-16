from azure.storage.blob import BlobServiceClient

# Replace with your actual connection string
conn_str = "DefaultEndpointsProtocol=https;AccountName=;AccountKey=;EndpointSuffix=core.windows.net"

container_name = "financial-docs"
blob_name = "tesla_10k_2024.pdf"

# Connect to Blob Storage
blob_service_client = BlobServiceClient.from_connection_string(conn_str)
container_client = blob_service_client.get_container_client(container_name)
blob_client = container_client.get_blob_client(blob_name)

# Download the PDF to your local machine
with open(blob_name, "wb") as download_file:
    download_file.write(blob_client.download_blob().readall())

print(f"✅ PDF '{blob_name}' downloaded successfully.")
