from semantic_kernel.agents import AzureAIAgentThread

async def invoke_agent(agent_id: str, user_inputs: list, client) -> None:
    try:
        print("[INFO] [utilities/invoke_agent.py] [invoke_agent] Retrieving agent by ID")
        # agent = await client.agents.get_agent(agent_id)
        thread = AzureAIAgentThread(client=client)

        try:
            for user_input in user_inputs:
                print(f"[INFO] [utilities/invoke_agent.py] [invoke_agent] Sending user input: {user_input}")
                # Assuming the correct method is 'agent.get_response' instead of 'client.get_response'
                response = await client.get_response(messages=[user_input], thread=thread)
                print(f"[INFO] [utilities/invoke_agent.py] [invoke_agent] Received response: {response}")
                thread = response.thread
        finally:
            if thread:
                print("[INFO] [utilities/invoke_agent.py] [invoke_agent] Deleting thread")
                await thread.delete()

    except Exception as e:
        print(f"[ERROR] [utilities/invoke_agent.py] [invoke_agent] An error occurred while invoking the Azure AI agent: {e}")
        raise e