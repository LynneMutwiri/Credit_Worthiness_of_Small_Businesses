import streamlit as st
import pickle
import pandas as pd 
def main():
    st.title("SBA Prime")

    # Allow user input for loan application
    st.subheader("Classify your Loan Application in Seconds")
    GrAppv = st.number_input("Loan Amount")
    Term = st.number_input("Loan Term")
    NewExist = st.text_input("How long has the business been in operation?")
    Location = st.selectbox("Where is the business located?", ["Urban", "Rural"])
    if Location == 'Urban':
        UrbanRural = 1
    else:
        UrbanRural = 2
    NoEmp = st.selectbox("Number of employees?", [1, 5, 10, 20, 50, 100])
    
    dictionary = {'Other': 12,
        'Construction': 4,
        'Prof/Science/Tech': 14,
        'Accom/Food_serv': 0,
        'Manufacturing': 9,
        'Wholesale_trade': 20,
        'Retail_trade': 17,
        'Other_no_pub': 13,
        'Healthcare/Social_assist': 7,
        'Admin_sup/Waste_Mgmt_Rem': 1,
        'Arts/Entertain/Rec': 3,
        'RE/Rental/Lease': 16,
        'Information': 8,
        'Ag/For/Fish/Hunt': 2,
        'Educational': 5,
        'Trans/Ware': 18,
        'Min/Quar/Oil_Gas_ext': 11,
        'Mgmt_comp': 10,
        'Utilities': 19,
        'Finance/Insurance': 6,
        'Public_Admin': 15}
    
    
    Category = st.selectbox("What industry is the business operating in?", list(dictionary.keys()))
    
    Industry = dictionary[Category]
    # Processing
    columns = ['GrAppv', 'Term', 'NoEmp', 'NewExist', 'UrbanRural', 'Industry']
    df=pd.DataFrame([[GrAppv,Term,NoEmp,NewExist,UrbanRural,Industry]],columns=columns)
    # Validate input values
    if not NewExist or not UrbanRural:
        st.warning("Please fill in all fields.")
        return

    # Load the pre-trained model
    with open("pipeline.pkl", "rb") as file:
        pipeline = pickle.load(file)

    # Make predictions using the loaded model
    prediction = pipeline.predict(df)

    # Display the prediction result
    if prediction[0] == 0:
        result= 'Sorry, your loan request was not succesful. \n\
        Please check on the following to improving your chances \
        of getting an SBA loan'
    else:
        result= "Congratulations. You have passed the SBA initial loan processing analysis.\n\
        Please proceed to the next step and upload necessary documents. \
        We'll be in touch shortly"
    
    submit_button = st.button('Submit')
    if submit_button:
        st.write(result)
        
if __name__ == "__main__":
    main()
