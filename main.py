from utilities.invoke_agent import invoke_agent
from utilities.create_client import create_client, get_first_agent_id, list_agents
from utilities.create_agent import create_azure_ai_agent
from utilities.delete_agent import delete_azure_ai_agent
import asyncio

async def main():
    client = await create_client()
    try:
        while True:
            print("Menu:")
            print("1. Create Azure AI Agent")
            print("2. List Azure AI Agents")
            print("3. Get First Agent ID")
            print("4. Delete Azure AI Agent")
            print("5. Chat with Azure AI Agent")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                """Create Agents"""
                name = input("Enter agent name: ")
                instructions = input("Enter agent instructions: ")
                print("[INFO] [main.py] Creating Azure AI Agent")
                agent = await create_azure_ai_agent(name=name, instructions=instructions)
                print("[INFO] [main.py] Azure AI Agent created successfully")

            elif choice == "2":
                """List Agents"""
                print("[INFO] [main.py] [list_agents] Listing Azure AI Agents")
                agent_list = await list_agents(client)
                print("[INFO] [main.py] [list_agents] Azure AI Agents List:")
                for agent in agent_list:
                    print(f"Agent ID: {agent['id']}, Name: {agent['name']}, Status: {agent['status']}")

            elif choice == "3":
                """Get First Agent ID"""
                first_agent_id, first_agent = await get_first_agent_id(agent_list)
                print(f"[INFO] [main.py] [get_first_agent_id] First Agent ID: {first_agent_id}")

            elif choice == "4":
                """Delete Agents"""
                agent_id_to_delete = input("Enter the Agent ID to delete: ")
                delete_agent_response = await delete_azure_ai_agent(agent_id_to_delete)
                print("[INFO] [main.py] [delete_agents] Azure AI Agent deleted successfully", delete_agent_response)

            elif choice == "5":
                """Invoke Agent"""
                print("[INFO] [main.py] [invoke_agent] Invoking Azure AI Agent")
                user_input = input("Enter your message (type 'exit' to stop chatting): ")
                while user_input.lower() != "exit":
                    res = await invoke_agent(user_inputs=[user_input], client=client)
                    # print("[RESPONSE] [main.py] [invoke_agent_response] Azure AI Agent response", res)
                    user_input = input("Enter your message (type 'exit' to stop chatting): ")

            elif choice == "6":
                print("[INFO] [main.py] Exiting the program")
                break

            else:
                print("[ERROR] [main.py] Invalid choice, please try again.")

    except Exception as e:
        print(f"[ERROR] [main.py] An error occurred: {e}")
    finally:
        print("[INFO] [main.py] Closing client")
        await client.close()

# Call the main function
asyncio.run(main())