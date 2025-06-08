# python-crewai

This repository provides a minimal starting point for experimenting with [CrewAI](https://pypi.org/project/crewai/), a framework for orchestrating multiple agents working together to accomplish complex tasks.

## Getting started

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-org/python-crewai.git
   cd python-crewai
   ```
2. **Create a virtual environment** (Python 3.9 or newer)
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Install dependencies**
   ```bash
   pip install crewai
   ```

## Usage example

Below is a short snippet showing how to define an agent and run a simple task with CrewAI:

```python
from crewai import Agent, Crew, Task

researcher = Agent(
    role="Researcher",
    goal="Provide a short overview of CrewAI",
    backstory="Experienced in analyzing frameworks"
)

overview_task = Task(description="Summarize the purpose of CrewAI")
crew = Crew(agents=[researcher], tasks=[overview_task])

result = crew.run()
print(result)
```

Running the script will execute the agent and print the task output. See the [CrewAI documentation](https://docs.crewai.com/) for more advanced features and configuration options.

## Project goals

The goal of this project is to explore CrewAI's capabilities in a lightweight Python environment. Additional examples and utilities may be added over time as the framework evolves.
