from semantic_kernel.agents import AzureAIAgent
from azure.identity import DefaultAzureCredential

async def create_client():
    try:
        creds = DefaultAzureCredential()
        client = AzureAIAgent.create_client(credential=creds)
        print("[INFO] [utilities/create_client.py] [create_client] Client created")
        return client
    except Exception as e:
        print(f"[ERROR] [utilities/create_client.py] [create_client] An error occurred while creating the client: {e}")
        raise e

async def list_agents(client) -> any:
    try:
        agents = await client.agents.list_agents()
        print("[INFO] [utilities/create_client.py] [list_agents] agents listed", type(agents))
        return agents
    except Exception as e:
        print(f"[ERROR] [utilities/create_client.py] [list_agents] An error occurred while listing agents: {e}")
        raise e

async def get_first_agent_id(agents) -> str:
    try:
        if agents:
            try:
                dict_agents = dict(agents)
                print("[INFO] [utilities/create_client.py] [get_first_agent_id] Successfully converted first agent to a dictionary")
            except Exception as e:
                print(f"[ERROR] [utilities/create_client.py] [get_first_agent_id] An error occurred while converting the first agent to a dictionary: {e}")
                raise e
            print("[INFO] [utilities/create_client.py] Agent keys:", dict_agents.keys())
            first_agent_id = dict_agents["data"][0].id
            print("[DEBUG] [TYPE]",type(dict_agents["data"][0]))
            print("[INFO] [utilities/create_client.py] [get_first_agent_id] First agent ID:", first_agent_id)
            return first_agent_id, dict_agents["data"][0]
        else:
            print("[INFO] [utilities/create_client.py] [get_first_agent_id] No agents found")
            return None, None
    except Exception as e:
        print(f"[ERROR] [utilities/create_client.py] [get_first_agent_id] An error occurred while getting the first agent ID: {e}")
        raise e
