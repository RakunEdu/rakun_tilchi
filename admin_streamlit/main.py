import streamlit as st 
import pandas as pd 


def build_word_json(data): 
    pass  



def main(): 
    st.sidebar.subheader("Tilchi Plan Adder") 
    st.logo("images/RAKUN_LOGO.png") 
    st.sidebar.image("images/add_new.png") 
    

    mode = st.sidebar.selectbox("Select Mode", ["Add Plan", "Add Words"])


    if mode == "Add Plan": 
        st.header("🌏Add Plan") 

        plan_name = st.text_input("Plan Name: ") 
        plan_language = st.text_input("Language: ")  
        plan_level = st.text_input("Level (A1, A2): ")   
        plan_translation_to = st.text_input("Translation Language: ")  

        file = st.file_uploader("Upload words file") 

        submit = st.button("Add", type="primary")

        if file: 
            df = pd.read_csv(file)
            st.dataframe(df)

            words_json = build_word_json(df)

            # API call for entering words 


    
    if mode == "Add Words":  
        st.header("📜 Add Words") 

        # API list of Plans 
        mode = st.selectbox("Plans", ["Plan 1", "Plan 2"]) 

        file = st.file_uploader("Upload words file") 

        if file: 
            df = pd.read_csv(file)
            st.dataframe(df) 




if __name__ == "__main__":
    main()