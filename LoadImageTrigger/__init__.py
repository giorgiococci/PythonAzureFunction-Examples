import logging

import io
import os
import requests
import json
from datetime import datetime, timedelta

from azure.storage.blob import (
    BlobServiceClient,
    ResourceTypes, 
    AccountSasPermissions, 
    generate_account_sas
)


import azure.functions as func

def getAzureStorageAccessSignature():
    blob_service_client = BlobServiceClient.from_connection_string(os.environ['aiengstorageaccntcode_STORAGE'])    
    
    sas_token = generate_account_sas(
       blob_service_client.account_name,
       account_key=blob_service_client.credential.account_key,
       resource_types=ResourceTypes(object=True),
       permission=AccountSasPermissions(read=True),
       expiry=datetime.utcnow() + timedelta(hours=1)
   )
    
    return sas_token

def getImageTags(image_uri):

    body = json.dumps({"url": image_uri})

    response = requests.post(f"https://aiengcomputervision.cognitiveservices.azure.com/vision/v3.1/analyze?visualFeatures=Tags",
                headers={"Content-Type": "application/json", "Ocp-Apim-Subscription-Key": os.environ['cognitiveservicevisionkey']},
                data = body
                )

    return response

def main(myblob: func.InputStream, blobout: func.Out[bytes], context: func.Context):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes\n"
                 f"Blob Uri: {myblob.uri}")

    sas_token = getAzureStorageAccessSignature()

    json_response = getImageTags(f"{myblob.uri}?{sas_token}")
    logging.info(f"Cognitive Service Response: {json_response.content}")

    blobout.set(json_response.content)