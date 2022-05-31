from google.cloud import bigquery
from google.oauth2 import service_account
from google.cloud import storage

def connectBQ():
    try:
        credentials = service_account.Credentials.from_service_account_file(
            r"C:\dev\greenstock\optimiser_files\key_prod.json", scopes=["https://www.googleapis.com/auth/cloud-platform"],
        )
        client = bigquery.Client(credentials=credentials, project='gcp-wow-pvc-grnstck-prod')        
    except:
        client = bigquery.Client(project='gcp-wow-pvc-grnstck-prod')
    return client

def connectStorage():
    try:
        credentials = service_account.Credentials.from_service_account_file(
            r"C:\dev\greenstock\optimiser_files\key_prod.json", scopes=["https://www.googleapis.com/auth/cloud-platform"],
        )
        client = storage.Client(credentials=credentials, project='gcp-wow-pvc-grnstck-prod')        
    except:
        client = storage.Client(project='gcp-wow-pvc-grnstck-prod')
    return client

def get_file_from_bucket(client, bucket, fn):
    if client is None:
        client = connectStorage()
    bucket = client.get_bucket(bucket)
    # Then do other things...
    blob = bucket.get_blob(fn)
    return blob
