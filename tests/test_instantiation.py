import os
import sys

# Ensure the src directory is importable
sys.path.insert(0, os.path.abspath("src"))

from crewai.agents.base import Agent
from crewai.tasks.base import Task
from crewai.tools.base import Tool


class DummyTool(Tool):
    def use(self, *args, **kwargs):
        return "used"


class DummyTask(Task):
    def execute(self):
        return "task done"


class DummyAgent(Agent):
    def act(self, task: Task):
        return task.execute()


def test_instantiation():
    tool = DummyTool(name="dummy")
    task = DummyTask(description="demo")
    agent = DummyAgent(role="tester", goal="demo", tools=[tool])

    assert agent.role == "tester"
    assert agent.goal == "demo"
    assert agent.tools[0].use() == "used"
    assert agent.act(task) == "task done"
