import google.generativeai as genai
import os

# 1. Setup your API Key
# Replace "YOUR_API_KEY_HERE" with your actual key from Google AI Studio
os.environ["GEMINI_API_KEY"] = "AIzaSyCUsYRh2HfV5EbZz6V2O2zUZOOaoSXHMv0"
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# 2. Define your "Base Profile" 
# The AI will pull facts exclusively from this text to match the job requirements.
my_profile = """
Name: Olori Nelson
Education: B.Eng. Electrical and Electronics Engineering, Federal University of Technology Minna (Expected 2028).
Academic Standing: Current GPA 4.36 / 5.00 (Dean's List).
Technical Skills: Python (Scikit-learn, Pandas), MATLAB & Simulink, Arduino IDE, Circuit Design, LLM Prompt Engineering, Workflow Automation.
Memberships: Space Generation Advisory Council (SGAC), Global Navigation Satellite Systems (GNSS) Community.
Key Experience: 
- Volunteer Mentorship Coordinator: Streamlined outreach workflows and conducted stakeholder engagement via LinkedIn.
- Projects: Designed an Automated Arduino Water Level System; participated in Data-Driven Hackathons (Kaggle & MATLAB) focusing on predictive modeling.
- Research: Authored an essay on utilizing GNSS and remote sensing for regional water security in West Africa.
"""

# 3. Define the Job or Scholarship Description
# Paste the text of the role you want to apply for right here.
target_job_description = """
[PASTE THE JOB OR SCHOLARSHIP DESCRIPTION HERE]
"""

# 4. The Agent Logic
def generate_tailored_application(profile, job_desc):
    print("Agent is analyzing the job description and mapping your profile...")
    
    # Initialize the model 
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Construct the prompt instructing the AI how to behave
    prompt = f"""
    You are an expert technical career strategist. 
    I am applying for the following role:
    
    {job_desc}
    
    Here is my core profile and experience:
    
    {profile}
    
    Based ONLY on my profile, please generate the following to help me apply:
    1. A customized 3-sentence professional summary for my CV tailored to this specific role.
    2. 3-4 tailored bullet points highlighting my most relevant projects/skills for this specific role. Focus on action verbs and workflow logic.
    3. A short, highly targeted cover letter paragraph explaining why my technical background makes me a great fit.
    """
    
    # Call the LLM
    response = model.generate_content(prompt)
    return response.text

# 5. Run the automation and save the result
if __name__ == "__main__":
    if "[PASTE THE JOB" in target_job_description:
        print("Error: Please paste a real job description into the 'target_job_description' variable to run.")
    else:
        result = generate_tailored_application(my_profile, target_job_description)
        
        # Save to a text file for easy copying
        output_filename = "Tailored_Application_Material.md"
        with open(output_filename, "w") as file:
            file.write(result)
            
        print(f"\nSuccess! Your tailored application materials have been saved to {output_filename}")
        print("\n--- Preview of Generated Content ---\n")
        print(result)