import streamlit as st
from resume_agent import ResumeGenerator
from utils import create_docx

def main():
    st.title("Resume Draft Builder AI")
    st.write("Generate a draft resume to help you apply for jobs faster")

    # Create tabs for different sections
    tab1, tab2 = st.tabs(["Generate Resume", "Settings"])
    
    with tab1:
        st.subheader("Enter Your Details")

        # Contact information
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            email = st.text_input("Email Address:")
        with col2:
            full_name = st.text_input("Full Name:")
        with col3:
            website = st.text_input("Personal Website URL:")
        with col4:
            linkedin = st.text_input("LinkedIn Profile URL:")

        
        # Basic Information
        col1, col2 = st.columns(2)
        with col1:
            job_title = st.text_input("Desired Job Title:")
        with col2:
            years_exp = st.number_input("Years of Experience:", min_value=0, max_value=50)
            
        # Detailed Information
        experience = st.text_area("Professional Experience (List all your roles and achievements):")
        education = st.text_area("Education Background:", height=100)
        skills = st.text_area("Technical Skills:", height=100)

        # Other details
        st.subheader("Additional Information")
        col1, col2 = st.columns(2)
        with col1:
            certifications = st.text_area("Certifications (if any):", height=100)
        with col2:
            projects = st.text_area("Projects (if any):", height=100)
      
    
        
        if st.button("Generate Resume"):
            if job_title and experience:
                with st.spinner('Generating your professional resume...'):
                    generator = ResumeGenerator()
                    resume_draft = generator.generate_resume(
                        job_title=job_title,
                        experience=experience,
                        education=education,
                        skills=skills,
                        email=email,
                        linkedin=linkedin,
                        website=website,
                        full_name=full_name,
                        certifications=certifications,
                        projects=projects
                    )
                    
                    st.success("Resume Generated!")
                    st.markdown(resume_draft)
                    
                    # Download buttons
                    st.subheader("Download Options")
                    download_col1, download_col2 = st.columns(2)
                    
                    with download_col1:
                        st.download_button(
                            label="📄 Download as TXT",
                            data=resume_draft,
                            file_name=f"{job_title.lower().replace(' ', '_')}_resume.txt",
                            mime="text/plain",
                            help="Download your resume as a plain text file"
                        )
                    
                    with download_col2:
                        docx_data = create_docx(resume_draft)
                        st.download_button(
                            label="📑 Download as DOCX",
                            data=docx_data,
                            file_name=f"{job_title.lower().replace(' ', '_')}_resume.docx",
                            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                            help="Download your resume as a Word document"
                        )
            else:
                st.error("Please provide at least the job title and experience.")

    with tab2:
        st.subheader("Resume Settings")
        st.slider("AI Creativity Level", min_value=0.0, max_value=1.0, value=0.7, step=0.1)

if __name__ == "__main__":
    main()