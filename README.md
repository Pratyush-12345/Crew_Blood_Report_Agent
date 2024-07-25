Here is the updated README in proper markdown format:

```markdown
# Blood Test Analysis and Health Recommendation System

This project uses CrewAI to analyze blood test reports and provide personalized health recommendations. It leverages AI agents to interpret blood test results, search for relevant health information, and compile actionable advice.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have a Google API key for the Gemini model.
- You have Python 3.7+ installed.
- You have a blood test report in PDF format.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/Pratyush-12345/Crew_Blood_Report_Agent.git
    ```

2. Install the required packages:
    ```bash
    pip install -U crewai langchain langchain-community langchain-google-genai duckduckgo-search pypdf
    ```

## Configuration

1. Open the `crew.py` file.

2. Replace `'your_google_api_key_here'` with your actual Google API key:
    ```python
    os.environ['GOOGLE_API_KEY'] = 'your_actual_google_api_key'
    ```

3. Ensure your blood test report PDF is in the same directory as the script, or update the file path in the task1 description:
    ```python
    task1 = Task(
        description='''
        1. Use the PDF Processor tool to read the blood test report at "Your_Blood_Report.pdf".
        ...
        ''',
        ...
    )
    ```

## Usage

1. Place your blood test report PDF in the same directory as the script, named `Blood_Report.pdf` (or update the file name in the script).

2. Run the script:
    ```bash
    python crew.py
    ```

3. The script will process the blood test report, analyze it, search for relevant health information, and provide recommendations.

4. The results will be saved in a file named `output.md` in the same directory.

## Output

The `output.md` file will contain:

- A summary of the blood test analysis.
- Relevant health information found from web searches.
- Specific health recommendations based on the analysis.
- Lifestyle advice and dietary suggestions.
- Any necessary medical follow-ups.

## Troubleshooting

- If you encounter PDF processing errors, ensure your PDF file is not corrupted and is readable.
- If you face API errors, check your Google API key and ensure it has the necessary permissions.
- For any other issues, check the console output for error messages and ensure all prerequisites are met.
```
