
# Azure AI Agent Utilities

This project provides a structured and reusable framework for creating and managing Azure AI agents. It is designed to be integrated into larger projects, offering utilities for agent creation, invocation, and management.

## Features

- **Agent Creation**: Easily create Azure AI agents with customizable settings.
- **Agent Invocation**: Invoke agents with user inputs and handle responses.
- **Agent Management**: List, retrieve, and delete agents as needed.
- **Asynchronous Operations**: Leverage Python's `asyncio` for efficient asynchronous operations.

## Requirements

- Python 3.11.0
- Azure SDK for Python
- Semantic Kernel

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/JinitVyas/azure-ai-agent-utilities.git
   cd azure-ai-agent-utilities
   ```
2. **Install Dependencies**

   Use `pip` to install the required packages:

   ```bash
   pip install -r requirements.txt
   ```
3. **Azure Configuration**

   Ensure you have the necessary Azure credentials set up. This project uses `DefaultAzureCredential` for authentication.

## Usage

### Creating an Azure AI Agent

To create an agent, use the `create_azure_ai_agent` function:

```python
from utilities.create_agent import create_azure_ai_agent

agent = await create_azure_ai_agent(name="Assistant", instructions="Friendly respond to user")
```

### Invoking an Agent

Invoke an agent with user inputs using the `invoke_agent` function:

```python
from utilities.invoke_agent import invoke_agent

response = await invoke_agent(agent_id=agent.id, user_inputs=["Hello"], client=agent)
```

### Managing Agents

List, retrieve, and delete agents using the provided utilities in `create_client.py` and `delete_agent.py`.

## Project Structure

- **main.py**: Entry point for running the project.
- **utilities/**: Contains utility scripts for agent creation, invocation, and management.
  - `create_agent.py`: Functions for creating Azure AI agents.
  - `invoke_agent.py`: Functions for invoking agents with user inputs.
  - `create_client.py`: Functions for creating and managing Azure clients.
  - `delete_agent.py`: Functions for deleting agents.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## *License*

This project is licensed under the Apache License, Version 2.0.

## Contact

For questions or support, please open an issue on the GitHub repository.
