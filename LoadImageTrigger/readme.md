# BlobTrigger - Python

The `BlobTrigger` makes it incredibly easy to react to new Blobs inside of Azure Blob Storage. This sample demonstrates a simple use case of processing data from a given Blob using Python.

## How it works

For a `BlobTrigger` to work, you provide a path which dictates where the blobs are located inside your container, and can also help restrict the types of blobs you wish to return. For instance, you can set the path to `samples/{name}.png` to restrict the trigger to only the samples path and only blobs with ".png" at the end of their name.

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