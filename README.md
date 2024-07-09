# Machine Learning Model Deployment on Azure with MLflow

## Project Description
This project involves deploying a machine learning model that classifies whether individuals have diabetes, based on various health metrics from the `diabetes.csv` dataset. The deployment was performed using Azure Machine Learning (Azure ML) and MLflow for managing the model lifecycle.

## Detailed Workflow Documentation

### Step 1: Setup Compute Resources
- **Compute Instance Creation**: Initiated by setting up a minimal quota compute instance suitable for development and testing phases.
- **Compute Cluster Creation**: Configured a compute cluster, which is essential for scalable model training, especially when dealing with larger datasets or more complex models.

### Step 2: Initialize Azure ML Workspace
- **Workspace Setup**: Created an Azure Machine Learning Workspace from the Azure portal. This workspace serves as the central place for managing all aspects of the model training and deployment lifecycle.

### Step 3: Launch Azure ML Studio
- **Accessing ML Studio**: Opened Azure ML Studio to leverage its integrated tools and interfaces for machine learning project management.

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
- **Model Registration**: Registered the trained model within Azure ML to manage different versions and facilitate deployment.

### Step 7: Resource Management
- **Cost Considerations**: Highlighted the importance of managing compute resources to control costs. Detailed that the compute cost was approximately $0.9 per hour.
- **Quota Management**: Discussed the significance of deleting unnecessary compute resources to prevent quota exceedance and manage budget effectively. Emphasized stopping or deleting the compute cluster if not in use to avoid unnecessary charges.

### Step 8: Model Deployment
- **Deployment Preparation**: Prepared for deploying the registered model by ensuring all resources were optimally used and within budget constraints.
- **Deployment Strategy**: Outlined the intended deployment strategy, taking into consideration the Azure infrastructure and the operational demands.

## Conclusion
This documentation outlines the comprehensive process undertaken to deploy a machine learning model on Azure, using MLflow for lifecycle management. Each step from setting up the infrastructure to training, registering, and planning for deployment has been meticulously executed to ensure a successful deployment in a cost-effective and efficient manner.

## Future Work
- **Model Optimization**: Continuous monitoring and tuning of the model to improve accuracy.
- **Resource Optimization**: Further refinement of resource usage to optimize costs while maintaining performance.

---

For additional details or specific operational queries, please refer to the Azure ML and MLflow documentation or contact the project supervisor.
