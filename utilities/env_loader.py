import os
from dotenv import load_dotenv

class EnvLoader:
    def __init__(self):
        load_dotenv(override=True)
        self.AGENT_ID_Stone_paper_sessior = os.getenv("AGENT_ID_Stone_paper_sessior")
        self.AGENT_ID = os.getenv("AGENT_ID")
        self.AZURE_AI_AGENT_MODEL_DEPLOYMENT_NAME = os.getenv("AZURE_AI_AGENT_MODEL_DEPLOYMENT_NAME")
        self.AZURE_AI_AGENT_PROJECT_CONNECTION_STRING = os.getenv("AZURE_AI_AGENT_PROJECT_CONNECTION_STRING")