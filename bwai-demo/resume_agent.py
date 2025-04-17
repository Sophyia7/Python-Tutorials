import google.generativeai as genai
from config import GOOGLE_API_KEY, MODEL_NAME

class ResumeGenerator:
    def __init__(self):
        genai.configure(api_key=GOOGLE_API_KEY)
        self.model = genai.GenerativeModel(MODEL_NAME)

    def generate_resume(self, job_title: str, full_name: str, experience: str, education: str = "", 
                       skills: str = "", email: str = "", linkedin: str = "", website: str = "", certifications = str, projects = str ) -> str:
        prompt = f"""
        Create a professional resume for a {job_title} position using the following information.
        Format as a modern, ATS-friendly resume with clear sections.

        INPUTS:
        Position: {job_title}
        Experience: {experience}
        Education: {education}
        Skills: {skills}
        Contact: {email}
        LinkedIn: {linkedin}
        Website: {website}
        Full Name: {full_name}
        Certifications: {certifications}
        Projects: {projects}


        FORMATTING REQUIREMENTS:
        1. Use markdown for consistent formatting
        2. Each section should start with ## (heading level 2)
        3. Use clean bullet points (•) for lists
        4. Keep content concise and achievement-focused
        5. Focus on measurable results and key responsibilities
        6. Use active voice and professional language
        7. No placeholder text or AI suggestions

        REQUIRED SECTIONS AND FORMAT:
        ## Contact Information
        • Email: {email if email else '[Email will be added by user]'}
        • LinkedIn: {linkedin if linkedin else '[Optional]'}
        • Portfolio: {website if website else '[Optional]'}
        • Full Name: {full_name if full_name else '[Full Name]'}

        ## Professional Summary
        [1-2 paragraph summary highlighting key qualifications and expertise in {job_title} role based on {experience}]

        ## Professional Experience
        [Transform the experience into achievement-focused bullet points]

        ## Education
        [Education details in reverse chronological order]

        ## Technical Skills
        [Skills grouped by proficiency level or category]

        ## Certifications (if applicable)
        {certifications if certifications else '[Optional]'}

        ## Projects 
        [Highlight key projects relevant to {job_title}]

        IMPORTANT:
        - Use strong action verbs
        - Include metrics and achievements where possible
        - Focus on relevant experience for {job_title}
        - Keep formatting clean and consistent
        - Make it ATS (Applicant Tracking System) friendly
        """
        
        response = self.model.generate_content(
            prompt,
            generation_config={
                "temperature": 0.7,
                "top_p": 0.8,
            }
        )
        
        return response.text