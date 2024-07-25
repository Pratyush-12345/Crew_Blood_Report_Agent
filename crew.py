import os
from crewai import Agent, Task, Crew, Process
from langchain.tools import BaseTool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.tools import DuckDuckGoSearchRun

# Disable telemetry
os.environ['CREWAI_DISABLE_TELEMETRY'] = 'true'

# Set up your Google API key
os.environ['GOOGLE_API_KEY'] = 'YOUR_API_KEY'

# Initialize the Gemini model
gemini = ChatGoogleGenerativeAI(model="gemini-pro")

# Custom tool for PDF processing
class PDFProcessorTool(BaseTool):
    name = "PDF Processor"
    description = "Process a PDF file and extract its content"

    def _run(self, file_path: str) -> str:
        try:
            loader = PyPDFLoader(file_path)
            pages = loader.load_and_split()
            return "\n".join(page.page_content for page in pages)
        except Exception as e:
            return f"Error processing PDF: {str(e)}"

    async def _arun(self, file_path: str) -> str:
        return self._run(file_path)

# Initialize tools
pdf_tool = PDFProcessorTool()
web_search_tool = DuckDuckGoSearchRun()

# Define the agents
analyzer_researcher = Agent(
    role='Blood Test Analyzer and Researcher',
    goal='Analyze blood test reports and find relevant health information',
    backstory='You are an expert in interpreting blood test results and conducting medical research.',
    verbose=True,
    allow_delegation=False,
    tools=[pdf_tool, web_search_tool],
    llm=gemini
)

health_advisor = Agent(
    role='Health Advisor',
    goal='Provide health recommendations based on blood test results and research',
    backstory='You are an experienced health advisor with a background in nutrition and preventive medicine.',
    verbose=True,
    allow_delegation=False,
    tools=[web_search_tool],
    llm=gemini
)

# Define the tasks
task1 = Task(
    description='''
    1. Use the PDF Processor tool to read the blood test report at "YOUR_PDF_PATH.pdf".
    2. Analyze the report and identify key health indicators.
    3. Use the Web Search tool to find relevant health information based on the report's contents.
    4. Compile a summary of the findings and relevant web information.
    ''',
    agent=analyzer_researcher,
    expected_output="A comprehensive summary of the blood test analysis and relevant health information from web searches."
)

task2 = Task(
    description='''
    1. Review the analysis and web research provided by the Blood Test Analyzer and Researcher.
    2. Based on this information, provide specific health recommendations.
    3. If needed, use the Web Search tool to find additional information for your recommendations.
    4. Include lifestyle advice, dietary suggestions, and any necessary medical follow-ups.
    5. Compile all recommendations into a clear, actionable report for the patient.
    ''',
    agent=health_advisor,
    expected_output="A detailed report with specific health recommendations, lifestyle advice, and dietary suggestions based on the blood test analysis and research."
)

# Create the crew
crew = Crew(
    agents=[analyzer_researcher, health_advisor],
    tasks=[task1, task2],
    verbose=2,
    process=Process.sequential
)

# Execute the crew's tasks
result = crew.kickoff()

# Save the output to output.md file
with open('output.md', 'w', encoding='utf-8') as f:
    f.write("# Blood Test Analysis and Health Recommendations\n\n")
    f.write(str(result))  # Convert CrewOutput to string

print("Analysis and recommendations have been saved to output.md")

