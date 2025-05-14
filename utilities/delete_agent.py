from azure.identity.aio import DefaultAzureCredential
from semantic_kernel.agents import AzureAIAgent
from azure.core.exceptions import ResourceNotFoundError

async def delete_azure_ai_agent(agent_id: str) -> None:
    async with (
        DefaultAzureCredential() as creds,
        AzureAIAgent.create_client(credential=creds) as client,
    ):
        try:
            # Delete the agent using its ID
            await client.agents.delete_agent(agent_id)
            print(f"[INFO] [utilities/delete_agent.py] [delete_azure_ai_agent] Agent with ID {agent_id} deleted successfully")
        except ResourceNotFoundError:
            print(f"[WARNING] [utilities/delete_agent.py] [delete_azure_ai_agent] Agent with ID {agent_id} does not exist.")
        except Exception as e:
            print(f"[ERROR] [utilities/delete_agent.py] [delete_azure_ai_agent] An error occurred while deleting the Azure AI agent: {e}")
            raise e