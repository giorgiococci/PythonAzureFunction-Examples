# Overview

This function is triggered by the insert of an image into an Azure Blob Storage.  

When triggered, the function calls the Azure Cognitive Service Computer Vision passing the url of the uploaded image. This API return the tags information about the passed image and save the JSON result into another folder of the Azure Blob Storage.  

## Requirements
1. Have an azure storage account
2. Have a cognitive services resource

## Information collection
Before starting, you need to retrieve the following information:  
- Azure Storage Account: 
    - **Connection String**: You can retrieve this information in the "Access Keys" tab of the resource, where it says "Connection string".
- Cognitive Services:
    - **Key**: You can retrieve this information in the "Keys and Endpoint" tab of the resource.
    - **Endpoint**: You can retrieve this information in the "Keys and Endpoint" tab of the resource.


<TODO> Documentation