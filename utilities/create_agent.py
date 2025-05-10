from azure.identity.aio import DefaultAzureCredential
from semantic_kernel.agents import AzureAIAgent, AzureAIAgentSettings

async def create_azure_ai_agent(name: str, instructions: str) -> AzureAIAgent:
    ai_agent_settings = AzureAIAgentSettings.create()

    async with (
        DefaultAzureCredential() as creds,
        AzureAIAgent.create_client(credential=creds) as client,
    ):
        try:
            # 1. Define an agent on the Azure AI agent service
            agent_definition = await client.agents.create_agent(
                model=ai_agent_settings.model_deployment_name,
                name=name,
                instructions=instructions,
            )

            # 2. Create a Semantic Kernel agent based on the agent definition
            agent = AzureAIAgent(
                client=client,
                definition=agent_definition,
            )
            print(f"[INFO] [utilities/create_agent.py] [create_azure_ai_agent] SUCCESS")
            return agent
        except Exception as e:
            print(f"[ERROR] [utilities/create_agent.py] [create_azure_ai_agent] An error occurred while creating the Azure AI agent: {e}")
            raise