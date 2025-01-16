# Implement VoiceRAG

## Overview
In this exercise, you will implement RAG (Retrieval Augmented Generation) with native audio input and output leveraging an existing [solution accelerator](https://github.com/Azure-Samples/aisearch-openai-rag-audio) that provides a simple front-end and back-end implementation. The back-end is a proxy that implements tools/functions to provide RAG and to connect with the real-time API.

## Prerequisites

- Azure OpenAI
    - Real-time model: gpt-4o-realtime-preview
    - Embedding model: text-embeddings-ada-002 or text-embedding-003-large/text-embedding-003-small
- Azure AI Search
- Azure Blob Storage

- Development environment (_or leverage the preconfigured VSCode Dev Container)
    - Python 3.8+
    - [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) (optional, needed for identity based authentication)
    - [uv](https://docs.astral.sh/uv/getting-started/installation/) (optional, but highly recommended)

## Create an Azure AI Search index 

_If you don't have access to the Azure Portal or other policies prevent you from creating an Azure AI Search index, you can skip this step and ask the coaches for a preconfigured Azure AI Search index._

In this step we will generate a vector index based on your own documents. If you don't want to leverage your own documents, you can download [this sample dataset]().

(Detailed instructions can be found here:)
1. Navigate to the Azure Portal.



## Run VoiceRAG sample locally

1. Clone the repository

```bash

```


Key based?


## Tips and tricks

- Leverage the provided devcontainer

[TODO document common made mistakes]


TODO Highlight why grounding is more difficult in voice.


## Prompt Engineering

Change voice.
In this part of the workshop we will tweak the prompt for the VoiceRAG model.

1. Navigate
