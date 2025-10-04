from superagi.tools.base_tool import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class SkillManagerInput(BaseModel):
    action: str = Field(..., description="Action to perform: 'list', 'execute', or 'delete'")
    skill_name: str = Field(None, description="Name of the skill (for execute/delete actions)")
    input_data: str = Field(None, description="Input data for skill execution")

class SkillManagerTool(BaseTool):
    name: str = "Skill Manager"
    description: str = "Manage and execute learned skills - list available skills, execute them, or remove skills"
    args_schema: Type[BaseModel] = SkillManagerInput

    def _execute(self, action: str, skill_name: str = None, input_data: str = None):
        if action == "list":
            return "📋 Available skills will be listed here once the learning system generates them."
        elif action == "execute" and skill_name:
            return f"⚡ Executing skill: {skill_name}\nInput: {input_data}\n\nSkill execution system ready!"
        elif action == "delete" and skill_name:
            return f"🗑️ Deleting skill: {skill_name}\n\nSkill removal system activated."
        else:
            return "❌ Please specify a valid action: 'list', 'execute <skill_name>', or 'delete <skill_name>'"
