from semantic_kernel.agents import AzureAIAgent, AzureAIAgentThread
from azure.ai.projects import AIProjectClient
from utilities.env_loader import EnvLoader

env_loader = EnvLoader()
AGENT_ID = env_loader.AGENT_ID

# Check if AGENT_ID is empty or None and throw an error if so
if not AGENT_ID:
    raise ValueError("[ERROR] [utilities/invoke_agent.py] [invoke_agent] AGENT_ID environment variable is empty or None")

async def invoke_agent(user_inputs: list, client: AIProjectClient) -> None:
    try:
        # 1. Get the agent definition using AGENT_ID
        agent_definition = await client.agents.get_agent(agent_id=AGENT_ID)
        
        # 2. Instantiate the AzureAIAgent
        agent = AzureAIAgent(client=client, definition=agent_definition)
        # 3. Create a thread
        # thread: AzureAIAgentThread = AzureAIAgentThread(client=client)
        thread: AzureAIAgentThread = AzureAIAgentThread(client=client, thread_id="thread_qwqw7I2h1VsjVCyHLr4jqnxS")
        for user_input in user_inputs:
            # 4. Use the AGENT'S get_response method (not client's)
            response = await agent.get_response(
                messages=user_input,
                thread=thread
            )
            try:
                response_dict = eval(str(response.content))  # Assuming response.content is a string representation of a dictionary
                formatted_response = "{\n"+"\n,".join([f"\t{key}: {value}" for key, value in response_dict.items()])+"\n}"
                print(f"[RESPONSE] [utilities/invoke_agent.py] [invoke_agent] Response:\n{formatted_response}")
            except Exception as parse_error:
                print(f"[ERROR] [utilities/invoke_agent.py] [invoke_agent] Failed to parse response content: {parse_error}")
            
    except Exception as e:
        print(f"[ERROR] [utilities/invoke_agent.py] [invoke_agent] An error occurred while invoking the Azure AI agent: {e}")

        raise
    # finally:
        # if 'thread' in locals():
        #     await thread.delete()
