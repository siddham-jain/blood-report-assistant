# BloodSampleAgent Crew

This is a project made in accordance with assignment guidelines of WingyfiAI.

In my project, I’m using CrewAI to automate the analysis of blood test reports and deliver personalized health recommendations. I’ve set up a multi-agent system with the CrewAI framework that starts by accepting a sample blood test report.

Documentation: [link](https://docs.crewai.com/)

In short CrewAI is a framework for creating multi-agent systems where specialized agents collaborate to achieve complex tasks. It enables efficient teamwork among agents, making it ideal for automation, AI-driven research, and personalized recommendations.

## About my Crew

### Agents

1. Medical analyst: This agent analyzes the blood test report, interpreting key health indicators and summarizing them in an understandable format.
2. Health Researcher:
Using the analysis from the Medical Analyst, this agent searches the internet for relevant health articles that align with the individual’s needs.
3. Health Advisor:
Based on the analysis and the articles found, this agent provides personalized health recommendations tailored to the individual’s current health status.
4. Coordinator:
This agent manages the workflow, ensuring that the Medical Analyst, Health Researcher, and Health Advisor work together smoothly and efficiently.

### Tasks
1. Analyze Blood Test:
The Medical Analyst starts by reviewing the patient's details, then examines and summarizes the provided blood test report. The output includes patient details followed by a simple summary of the blood test findings.
2. Search for Articles:
The Health Researcher searches for online articles related to the health concerns identified in the blood test summary. The expected output is a collection of articles with URLs and brief descriptions of each.
3. Provide Recommendations:
The Health Advisor offers personalized health advice based on the blood test summary and the articles found. The output is a comprehensive report with a summary, a table of blood parameter levels, and actionable health tips linked to relevant sources, formatted according to specific guidelines.
4. Coordinate Process:
The Coordinator oversees the workflow, ensuring that tasks are executed smoothly by the Medical Analyst, Health Researcher, and Health Advisor. The expected output is an organized task flow with combined results from all agents.

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [Poetry](https://python-poetry.org/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install Poetry:

```bash
pip install poetry
```

Next, navigate to your project directory and install the dependencies:

1. First lock the dependencies and then install them:
```bash
poetry lock
```
```bash
poetry install
```
### Customizing

**Add your `GROQ_API_KEY` and `SERPER_API_KEY` into the `.env` file**

By default it uses `OPENAI_API_KEY`

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```
or
```bash
poetry run blood_sample_agent
```

This command initializes the blood_sample_agent Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.