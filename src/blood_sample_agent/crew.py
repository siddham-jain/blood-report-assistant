import yaml
import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
from langchain_groq import ChatGroq
import dotenv

dotenv.load_dotenv()

def load_yaml(filename):
    folder = os.path.join(os.path.dirname(__file__), 'config')
    with open(os.path.join(folder, filename), 'r') as file:
        return yaml.safe_load(file)

agent_config = load_yaml('agents.yaml')
tasks_config = load_yaml('tasks.yaml')

llm = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0.5
)

def create_agents(text):
    agents = {}
    for agent_name, agent_info in agent_config.items():
        tools = []
        if 'SerperDevTool' in agent_info.get('tools', []):
            tools.append(SerperDevTool())

        goal_with_text = agent_info['goal'].replace("${blood_test_report}", text)

        # Create the Agent instance
        agent = Agent(
            role=agent_info['role'],
            goal=goal_with_text,
            backstory=agent_info['backstory'],
            tools=tools,
            llm=llm
        )
        agents[agent_name] = agent

    return agents

def create_tasks(agents):
    tasks = []
    for task_name, task_info in tasks_config['tasks'].items():
        agent_name = task_info['agent']
        task = Task(
            name=task_name,
            description=task_info['description'],
            expected_output=task_info['expected_output'],
            agent=agents[agent_name],
            llm=llm
        )
        tasks.append(task)

    return tasks

def create_crew(text):
    agents = create_agents(text)
    tasks = create_tasks(agents)

    process = Process.sequential

    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        process=process
    )

    return crew