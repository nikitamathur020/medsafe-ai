import streamlit as st
from PIL import Image
from utils.matcher import match_medicine, MEDICINE_DATABASE
from utils.ocr_helper import extract_text_from_image
from utils.llama_helper import query_llama3

st.set_page_config(
    page_title="Medsafe AI - Clinical Safety Platform",
    page_icon="💊",
    layout="wide"
)

st.title("💊 Medsafe AI Capstone Platform")
st.markdown("AI-powered healthcare safety, prescription extraction, and interaction validator.")
st.markdown("---")


scenario = st.sidebar.selectbox(
    "Select Project Scenario",
    (
        "1. Medicine Interaction Analysis", 
        "2. Prescription OCR & Extraction", 
        "3. Symptom Guidance & Risk Assessment"
    )
)


# SCENARIO 1: MEDICINE INTERACTION ANALYSIS
if scenario == "1. Medicine Interaction Analysis":
    st.header("Scenario 1: Medicine Interaction Analysis")
    st.write("Enter multiple medicines to check for fuzzy matches and adverse drug-drug interactions.")

    user_input = st.text_area("Enter medications (comma-separated)", "Aspirin, Ibuprofen, Paracetamol")

    if st.button("Analyze Interactions", type="primary"):
        meds_list = [m.strip() for m in user_input.split(",") if m.strip()]
        
        st.markdown("### 🔍 Fuzzy Matching Results")
        validated_meds = []
        for m in meds_list:
            match = match_medicine(m)
            if match:
                st.success(f"Matched **{m}** to database entry: **{match['name']}** ({match['category']})")
                validated_meds.append(match['name'])
            else:
                st.warning(f"Could not find a secure match for **{m}** in the standard database.")

        if validated_meds:
            st.markdown("### 🤖 LLaMA 3 Clinical Reasoning Report")
            prompt = f"Analyze the following validated medications for potential adverse drug-drug interactions and provide safety guidance: {', '.join(validated_meds)}"
            with st.spinner("Generating AI safety evaluation via LLaMA 3..."):
                report = query_llama3(prompt)
                st.write(report)

# SCENARIO 2: PRESCRIPTION OCR & EXTRACTION
elif scenario == "2. Prescription OCR & Extraction":
    st.header("Scenario 2: Prescription OCR and Medicine Extraction")
    st.write("Upload an image of a prescription to extract text using Tesseract OCR and process it with LLaMA 3.")

    uploaded_file = st.file_uploader("Upload Prescription Image", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Prescription", use_container_width=True)

        if st.button("Extract and Process Text", type="primary"):
            with st.spinner("Extracting text via Tesseract OCR..."):
                raw_text = extract_text_from_image(image)
            
            st.subheader("Raw Extracted Text")
            st.code(raw_text)

            with st.spinner("Analyzing extraction via LLaMA 3..."):
                prompt = f"Extract active medicine names, dosages, and instructions from the following raw OCR prescription text:\n\n{raw_text}"
                structured_output = query_llama3(prompt)
                
                st.subheader("Structured Clinical Extraction")
                st.markdown(structured_output)

# SCENARIO 3: SYMPTOM GUIDANCE & RISK ASSESSMENT
elif scenario == "3. Symptom Guidance & Risk Assessment":
    st.header("Scenario 3: Symptom Guidance and Risk Assessment")
    st.write("Describe patient symptoms and demographics for risk scoring and home-care suggestions.")

    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Patient Age", 1, 120, 25)
    with col2:
        risk_factors = st.text_input("Existing Conditions / History", "None")

    symptoms = st.text_area("Describe Symptoms", "e.g., severe headache, persistent fever, fatigue")

    if st.button("Assess Risk & Guidance", type="primary"):
        prompt = f"""
        Provide an educational symptom risk assessment based on the following:
        - Age: {age}
        - History: {risk_factors}
        - Symptoms: {symptoms}
        
        Provide: 1. Risk Score Level (Low/Moderate/High), 2. Potential Causes (Educational), 3. Home-Care Guidance, 4. When to seek emergency care.
        """
        with st.spinner("Running AI risk evaluation via LLaMA 3..."):
            assessment = query_llama3(prompt)
            st.markdown("### 📋 Risk & Guidance Report")
            st.markdown(assessment)