# Predicting Credit-Worthiness of Small Businesses

![sba](SBAimage.png) 

This task is aimed at building a loan approval classifier that predicts whether or not a loan application will be approved, based on the business' financial and credit history.
#### Case study of businesses supported by the U.S. Small Business Administration(SBA) found [here](https://github.com/LynneMutwiri/Credit_Worthiness_of_Small_Businesses).

#### Authors
1. [Brian Njau](https://github.com/Brian-Njau)
2. [Grace Nyongesa](https://github.com/Grace-01-cell)
3. [Josiah Okumu](https://github.com/josiah-okumu)
4. [Leo Kariuki](https://github.com/leokariuki)
5. [Lynne Mutwiri](https://github.com/LynneMutwiri)
6. [Stella Kitur](https://github.com/stellacherotich)

## <span style="color:darkred"> Project Overview </span>
This project focuses on utilizing the dataset from the U.S. Small Business Administration to develop a predictive model for loan application approval. By analyzing relevant factors and historical loan data, the project aims to create a reliable system that assists the SBA in making informed decisions while minimizing the risk of defaults.
The ultimate goal is to provide the SBA with a robust loan approval model that enhances their ability to make accurate and efficient lending decisions.

<b> Stakeholders: Small Businesses, Government, and Lending institutions such as the SBA </b>
### Project Objectives
1. Conduct a comprehensive analysis of the dataset from the U.S. Small Business Administration to identify patterns and trends for accurate loan approval predictions.

2. Develop a robust machine learning model that utilizes the identified patterns and trends to predict loan approval outcomes effectively.

3. Deploy and evaluate the developed machine learning model in the loan approval process of the U.S. Small Business Administration, continuously optimizing its predictive capabilities for informed lending decisions.

### <b> Success Metrics </b>
Accuracy: 85% accuracy which measures the overall correctness of the model's predictions by classifying loan applications as Approved or Rejected. 

## <span style="color:darkred"> Data Understanding </span>

The data was sourced from this [link]().

-- Brief summary of the data (rows, columns)

-- Brief data dictionary of the dataset; especially for the columns 


## <span style="color:darkred"> Data Preparation and EDA </span>
-- what methods in data prep did we use ?

## <span style="color:darkred"> Modeling </span>

- what models did we use; what was the best performing model?


## <span style="color:darkred"> Navigating the Repo </span>

- Under the [Deliverables](https://github.com/LynneMutwiri/Credit_Worthiness_of_Small_Businesses/tree/main/Deliverables) folder, you will find the following files stored in pdf format:

        Presentation
        Write-up
        Jupyter Notebook
        GitHub 

- The Notebook used is under the file name `SBA.ipynb`


##  Deployment 

This loan filtering app was deployed on [Streamlit](https://streamlit.io/). 
To deploy the app, you will need to have Streamlit installed.

You can install Streamlit by running the following command in your terminal:

<b> Install Streamlit:</b>

    pip install streamlit

You will need to clone this repository by following these steps:

    git clone https://github.com/LynneMutwiri/Credit_Worthiness_of_Small_Businesses.git
    cd Credit_Worthiness_of_Small_Businesses
    
<b> To run the app locally run the following on terminal:</b>

    streamlit run App/App.py

The input features were: `Gross Approval`, `Industry`, `Loan Term`,  `Number of Employees`, `NewExist` and `UrbanRural`  to predict  loan approval. 

Upon doing a feature importance on the pre-trained model, we found out that the <b> Loan Term and the Gross Approval amount </b> are the two key features in determining whether a loan would pass the initial filtering sta
