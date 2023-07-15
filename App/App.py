import streamlit as st
import pandas as pd
import pickle

def main():
    st.title("Small Business Administration Prime")

    # Allow user input for loan application
    st.subheader("Classify your Loan Application in Seconds")
    MembershipStatus = st.selectbox("Are you a member of the SBA?",["Yes", "No"])

    # Check if the user is a member of the SBA
    if MembershipStatus == 'Yes':
        PrevLoan = st.selectbox("Have you applied for an SBA Loan before",["Yes", "No"])
        if PrevLoan == "Yes":
            PrevLoanStatus = st.selectbox("Did you repay your previous loan in time? \n \
            Note: You'll be required to submit verification documents if you proceed",["Yes", "No", "In Progress"])
        else:
            PrevLoanStatus = "Yes"
        
        GrAppv = int(st.number_input("Loan Amount",value=0,step=1))
        Term = int(st.number_input("Loan Term (In months)",value=0,step=1))
        NewExist = int(st.number_input("How long has the business been in operation? (In Months)",value=0,step=1))
        Location = st.selectbox("Where is the business located?", ["Urban", "Semi-Urban" , "Rural"])
        if Location == 'Urban':
            UrbanRural = 1
        elif Location == 'Rural':
            UrbanRural = 2
        else:
            UrbanRural = 0
        
        NoEmp = st.slider("Number of employees?", min_value=0, max_value=100, step=1, value=0)
        
        dictionary = {'Other': 12, 'Construction': 4, 'Prof/Science/Tech': 14, 'Accom/Food_serv': 0, 'Manufacturing': 9,
                      'Wholesale_trade': 20, 'Retail_trade': 17, 'Other_no_pub': 13, 'Healthcare/Social_assist': 7,
                      'Admin_sup/Waste_Mgmt_Rem': 1, 'Arts/Entertain/Rec': 3, 'RE/Rental/Lease': 16, 'Information': 8,
                      'Ag/For/Fish/Hunt': 2, 'Educational': 5, 'Trans/Ware': 18, 'Min/Quar/Oil_Gas_ext': 11,
                      'Mgmt_comp': 10, 'Utilities': 19, 'Finance/Insurance': 6, 'Public_Admin': 15}
        
        Category = st.selectbox("What industry is the business operating in?", list(dictionary.keys()))
        Industry = dictionary[Category]
        
        # Processing
        columns = ['GrAppv', 'Term', 'NoEmp', 'NewExist', 'UrbanRural', 'Industry']
        df = pd.DataFrame([[GrAppv, Term, NoEmp, NewExist, UrbanRural, Industry]], columns=columns)

        # Load the pre-trained model
        file = open("App/pipeline.pkl", "rb")
        pipeline = pickle.load(file)
        file.close()

        # Make predictions using the loaded model
        prediction = pipeline.predict(df)

        # Display the prediction result
        if PrevLoanStatus == 'No':
            result= 'Sorry. The SBA does not guarantee new loans to businesses who have not repaid their previous loan. \
                Kindly repay your previous loan in order to apply for a new loan'
        else:
            if prediction[0] == 0:
                result= '''Sorry, your loan request was not successful. \n \
                \n Please check on the following to improve your chances of getting an SBA loan: \n \
                \n 1. Find a suitable balance between the loan amount and the repayment period \n \
                \n 2. Contact one of our agents to assist you in your application process \n \
                    \n https://www.sba.gov/local-assistance) \n \
                \n 3. Explore some of our resources to help you get started \n \
                \n https://www.sba.gov/local-assistance/resource-partners/score-business-mentoring \n'''
            else:
                result= """Congratulations. You have passed the SBA initial loan processing analysis.\n\
                Please proceed to the next step and upload necessary documents. \
                We'll be in touch shortly"""
        submit_button = st.button("Submit")
        if submit_button:
            st.write(result)
    else:
        # Display a message for non-members
        st.write("You need to be an SBA member to apply. Kindly get in touch or visit our [website](https://www.sba.gov/) to apply")

if __name__ == "__main__":
    main()
