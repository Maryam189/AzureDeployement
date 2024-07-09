# Machine Learning Model Deployment on Azure with MLflow

## Project Description
This project involves deploying a machine learning model that classifies whether individuals have diabetes, based on various health metrics from the `diabetes.csv` dataset. The deployment was performed using Azure Machine Learning (Azure ML) and MLflow for managing the model lifecycle.

## Detailed Workflow Documentation

### Step 1: Setup Compute Resources
- **Compute Instance Creation**: Initiated by setting up a minimal quota compute instance suitable for development and testing phases.
- **Compute Cluster Creation**: Configured a compute cluster, which is essential for scalable model training, especially when dealing with larger datasets or more complex models.

### Step 2: Initialize Azure ML Workspace
- **Workspace Setup**: Created an Azure Machine Learning Workspace from the Azure portal. This workspace serves as the central place for managing all aspects of the model training and deployment lifecycle.

![ml workspace 1](https://github.com/Maryam189/AzureMLDeployment/assets/76420523/92673e9b-703d-4504-b9cb-12062ab5c70b)


### Step 3: Launch Azure ML Studio
- **Accessing ML Studio**: Opened Azure ML Studio to leverage its integrated tools and interfaces for machine learning project management.

![launch ML Studio 3](https://github.com/Maryam189/AzureMLDeployment/assets/76420523/68d720eb-371b-4de0-b031-e69f5f9b8be6)


### Step 4: Repository Management
- **Clone GitHub Repository**: Cloned a GitHub repository directly within the Azure ML workspace environment. This repository contains:
  - `Notebook.ipynb`: The Jupyter notebook with exploratory data analysis and initial model training.
  - `train.py`: A Python script derived from the notebook for automated and reusable training.
  - `test.txt`: A text file with test inputs for making predictions.
  - `diabetes.csv`: The dataset used for training the classifier.

### Step 5: Model Training and Evaluation
- **Notebook Execution**: Executed the `Notebook.ipynb` in Azure ML Studio to train the initial model and perform exploratory data analysis.
- **Script Execution**: Ran the `train.py` script to structure the training process into reusable functions, facilitating automation and reproducibility.

### Step 6: Job Creation and Model Registration
- **Job Monitoring**: Created and monitored a machine learning job that handles the training operations managed by Azure ML.
  
![image](https://github.com/Maryam189/AzureMLDeployment/assets/76420523/c12b3aa4-e2ab-4837-b234-b4e6d3215ec8)

- **Model Registration**: Registered the trained model within Azure ML to manage different versions and facilitate deployment.

### Step 7: Resource Management
- **Cost Considerations**: Highlighted the importance of managing compute resources to control costs. Detailed that the compute cost was approximately $0.9 per hour.
- **Quota Management**: Discussed the significance of deleting unnecessary compute resources to prevent quota exceedance and manage budget effectively. Emphasized stopping or deleting the compute cluster if not in use to avoid unnecessary charges.

### Challenges Faced
During the execution of this project, I encountered several significant obstacles which tested my resolve and resourcefulness:

- **Account Creation Issues**: Initially, setting up an account on the Azure portal proved challenging. My first attempt using a Nayapay prepaid card was unsuccessful as Azure does not accept prepaid cards. Subsequent attempts with a debit card linked to my bank account also failed because international transactions were disabled. It was not until I used a third card, belonging to a friend, that I was able to successfully create my account and proceed.

- **Resource Management and Quota Limitations**: My first attempt at deploying the model failed due to fully utilized quota resources. Despite the setback, I invested time in a comprehensive two-hour Azure ML model deployment course offered by a Microsoft student ambassador. This education enabled me to understand that I needed to delete compute instances before deployment. Armed with this new knowledge, I was able to successfully deploy the model using Azure MLflow.

### Step 8: Model Deployment
- **Deployment Preparation**: Prepared for deploying the registered model by ensuring all resources were optimally used and within budget constraints.
- **Deployment Strategy**: Outlined the intended deployment strategy, taking into consideration the Azure infrastructure and the operational demands.

![Deployment Succeeded](https://github.com/Maryam189/AzureMLDeployment/assets/76420523/d4a07d01-ae2c-499d-af80-95b17629c8d1)


## Conclusion
This documentation outlines the comprehensive process undertaken to deploy a machine learning model on Azure, using MLflow for lifecycle management. Each step from setting up the infrastructure to training, registering, and planning for deployment has been meticulously executed to ensure a successful deployment in a cost-effective and efficient manner. The challenges encountered were significant, yet they provided valuable learning opportunities and demonstrated my ability to navigate complex problems.

## Future Work
- **Model Optimization**: Continuous monitoring and tuning of the model to improve accuracy.
- **Resource Optimization**: Further refinement of resource usage to optimize costs while maintaining performance.

