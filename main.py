from utilities.invoke_agent import invoke_agent
from utilities.create_client import create_client, get_first_agent_id, list_agents
from utilities.create_agent import create_azure_ai_agent
from utilities.delete_agent import delete_azure_ai_agent
import asyncio

async def main():
    client = await create_client()
    try:
        """Create Agents"""
        print("[INFO] [main.py] Creating Azure AI Agent")
        agent = await create_azure_ai_agent(name="Assistant", instructions="Friendly respond to user")
        print("[INFO] [main.py] Azure AI Agent created successfully")

        """List Agents"""
        # print("[INFO] [main.py] [list_agents] Listing Azure AI Agents")
        # agent_list = await list_agents(client)

        """Get First Agent ID"""
        # first_agent_id, first_agent = await get_first_agent_id(agent_list)

        """Delete Agents"""
        # delete_agent_response = await delete_azure_ai_agent("asst_riOZd6oR9iXoDr1gZDncMhsq")
        # print("[INFO] [main.py] [delete_agents] Azure AI Agent deleted successfully", delete_agent_response)

        """Invoke Agent"""
        print("[INFO] [main.py] [invoke_agent] Invoking Azure AI Agent")
        res = await invoke_agent(agent_id=agent.id, user_inputs=["Hello"], client=agent)
        print("[RESPONSE] [main.py] [invoke_agent_response] Azure AI Agent response", res)
    except Exception as e:
        print(f"[ERROR] [main.py] An error occurred: {e}")
    finally:
        print("[INFO] [main.py] Closing client")
        await client.close()

# Call the main function
asyncio.run(main())