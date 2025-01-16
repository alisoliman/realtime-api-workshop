# Implement VoiceRAG

## Overview

In this exercise, you will implement a RAG (Retrieval Augmented Generation) solution with native audio input and output leveraging an existing [solution accelerator](https://github.com/Azure-Samples/aisearch-openai-rag-audio) that provides a simple front-end and back-end implementation. The back-end is a proxy that implements tools/functions to provide RAG and to connect with the real-time API.

## Prerequisites

- Azure OpenAI
    - Real-time model: gpt-4o-realtime-preview
    - Embedding model: text-embeddings-ada-002 or text-embedding-003-large/text-embedding-003-small
- Azure AI Search
- Azure Blob Storage
- Development environment (_or leverage the preconfigured VSCode Dev Container_)
    - Python 3.11
    - Node.js
    - Git
    - [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) (optional, needed for identity based authentication)

## Create an Azure AI Search index 

_If you don't have access to the Azure Portal or other policies prevent you from creating an Azure AI Search index, you can skip this step and ask the coaches for a preconfigured Azure AI Search index._

In this step we will generate a vector index based on your own documents. If you don't want to leverage your own documents, you can download [this sample dataset](https://github.com/Azure-Samples/aisearch-openai-rag-audio/tree/main/data).

(Detailed instructions can be found here:)
1. Navigate to your Azure AI Search in the [Azure Portal](https://portal.azure.com).
1. On the "Overview" page, select "Import and vectorize data" in the top bar.
1. Select Azure Blob Storage as the data source and select your storage account.
1. Select your Azure OpenAI service and the embedding model you want to use.
1. Don't select "Vectorize images" and "Extract text from images" for this exercise.
1. Optionally you can change the schedule to your own preference, or leave it at "Once".
1. Change the name of your vector store to reflect your documents and select the "Create" button. Store the name of this vector store, as you will need this later.

After a few minutes, your index will be populated with chunks and vectors from your documents. 

1. Go back to the main page of your Azure AI Search solution.
1. Copy and store the URL of your AI Search solution, you will need this later.
1. If you want to leverage key based authentication, navigate to "Settings -> Keys". Create a new query key and copy and store this value.
1. If you want to leverage user identity authentication, navigate to "Access control (IAM)" and add your user to the "Search Service Contributor" role.

## Run VoiceRAG sample

Now we have a preconfigured Azure AI Search index, we can run the VoiceRAG sample. In this exercise we will run the sample locally, but you can also deploy it to Azure in a later stage.

### Setup your development environment

The easiest way to setup your development environment is to leverage the provided VSCode Dev Container. This container is preconfigured with all the necessary tools and dependencies to run the sample. You can run this Dev Container locally in VSCode or in GitHub Codespaces.

#### GitHub Codespaces

TODO

#### Local (DevContainer)

TODO


#### Local (Manual)

1. Make sure you meet the prerequisites mentinoed earlier.

1. Clone the repository

```bash
git clone https://github.com/Azure-Samples/aisearch-openai-rag-audio.git
```

### Configure the environment

TODO explain key based vs identity based authentication
TODO explain .env creation

#### Key based authentication

#### Identity based authentication

Login to your Azure account and select your subscription.

```az login```

TODO document which rights an user need

## Troubleshooting
- [TODO document common mistakes]

### Run the solution

TODO explain how to run the scripts on Windows / Linux

Now you can navigate to url and start using the solution.

### Advanced

If you have more time bla bla

## Prompt Engineering

In this part of the workshop we will tweak the prompt for the VoiceRAG model. The default prompt is very basic, and we can improve the grounding and behavior by adding more context to the prompt. Due to nature of the model, you can also tune the voice by changing the prompt.

1. TODO: grounding tips
1. TODO: Change the voice to reflect your brand. Prompt engineering.

### Function calling

Exercise to improve the function calling. Explain how it currently works.

TODO Highlight why grounding is more difficult in voice.
TODO add concrete examples



