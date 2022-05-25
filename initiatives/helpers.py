from google.cloud import bigquery
from google.oauth2 import service_account

def connectBQ():
    try:
        credentials = service_account.Credentials.from_service_account_file(
            r"C:\dev\greenstock\optimiser_files\key_prod.json", scopes=["https://www.googleapis.com/auth/cloud-platform"],
        )
        client = bigquery.Client(credentials=credentials, project='gcp-wow-pvc-grnstck-prod')        
    except:
        client = bigquery.Client(project='gcp-wow-pvc-grnstck-prod')
    return client
