# Azure ML Deployment Guide

This repository contains the code and instructions to manually deploy a text summarization model using Azure ML Studio.

## Steps to Deploy the Model

### 1. Set Up Azure Resources

- Create a Resource Group
  - Go to the Azure portal home page.
  - Select `Create a resource`.
  - Search for `Resource group` and create a new resource group.
  - Fill in the details and create the resource group.

- Create an Azure Machine Learning Workspace
  - Search for `Azure Machine Learning` in the Azure portal.
  - Create a new workspace and fill in the details.
  - Launch the Azure ML Studio from the workspace page.

### 2. Prepare the Compute Resources

- In Azure ML Studio, go to `Manage` and select `Compute`.
- Create a Compute Instance with `STANDARD_DS11_V2`.
- Create a Compute Cluster with `STANDARD_DS11_V2`.

### 3. Clone the Repository and Run the Notebook

- Go to the `Notebooks` section in Azure ML Studio.
- Open a terminal and clone your GitHub repository:
  ```sh
  git clone https://github.com/RashmiNirasha/mlops-event.git
