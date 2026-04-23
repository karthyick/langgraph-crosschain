# langgraph-crosschain

> **Call a node in one LangGraph chain directly from a node in another.**

[![PyPI version](https://img.shields.io/pypi/v/langgraph-crosschain.svg?color=8B5CF6)](https://pypi.org/project/langgraph-crosschain/)
[![Downloads](https://static.pepy.tech/badge/langgraph-crosschain)](https://pepy.tech/project/langgraph-crosschain)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/karthyick/langgraph-crosschain?style=social)](https://github.com/karthyick/langgraph-crosschain)

Vanilla LangGraph treats each chain as an island — `Chain1.NodeA` can't call `Chain2.NodeB`. This package adds a **chain registry + router + shared state manager** so specialized agents can call into each other without bolting on message queues.

⭐ **[Star on GitHub](https://github.com/karthyick/langgraph-crosschain)** if this unblocks your multi-agent architecture.

---

## The Problem

```
Standard LangGraph:
  Chain_A.Node1 → Chain_A.Node2 → Chain_A.Node3 → DONE
  Chain_B.NodeX → Chain_B.NodeY → Chain_B.NodeZ → DONE
  (no way to go A.Node2 → B.NodeY)

With langgraph-crosschain:
  Chain_A.Node2 ──cross-chain call──► Chain_B.NodeY ──returns────┐
       │                                                          │
       └──────────── continues with result ◄──────────────────────┘
```

Build modular agents that talk to each other instead of one monolithic graph.

---

## 🎯 Project Overview

This framework addresses a critical gap in current AI agent frameworks by enabling:

- **Cross-Chain Node Calls**: Direct communication between nodes in different chains (Chain1.Node2 → Chain2.Node3)
- **Shared State Management**: Share state between separate chain instances
- **Dynamic Inter-Chain Workflows**: Create flexible workflows that span multiple chains
- **Modular Components**: Build reusable chain components that can communicate seamlessly

## 💡 Innovation Gap Being Addressed

## 🚀 Quick Start

### Installation

```bash
pip install langgraph-crosschain
```

Or install from source:

```bash
git clone https://github.com/yourusername/langgraph-crosschain.git
cd langgraph-crosschain
pip install -e .
```

### Basic Example

```python
from langgraph.graph import StateGraph
from langgraph_crosschain import ChainRegistry, CrossChainNode

# Create a registry to manage chains
registry = ChainRegistry()

# Define your chains
def analyzer_node(state):
    # Process data
    return {"analyzed": True, "result": state.get("data")}

def processor_node(state):
    # Call a node in another chain
    node = CrossChainNode("chain2", "processor", processor_node)
    result = node.call_remote("chain1", "analyzer", {"data": "test"})
    return {"processed": True, "result": result}

# Build your chains
chain1 = StateGraph(...)
chain2 = StateGraph(...)

# Register chains
registry.register("chain1", chain1.compile())
registry.register("chain2", chain2.compile())

# Now chains can communicate with each other!
```

## 📚 Core Components

### ChainRegistry

Central registry for managing multiple chain instances:

```python
from langgraph_crosschain import ChainRegistry

registry = ChainRegistry()
registry.register("my_chain", chain_instance)
chain = registry.get("my_chain")
```

### CrossChainNode

Base class for nodes that can communicate across chains:

```python
from langgraph_crosschain import CrossChainNode

node = CrossChainNode(
    chain_id="chain1",
    node_id="processor",
    func=my_node_function
)

# Call a node in another chain
result = node.call_remote("chain2", "analyzer", {"data": "test"})

# Broadcast to multiple chains
node.broadcast(["chain2", "chain3"], "receiver", {"data": "broadcast"})
```

### MessageRouter

Handles routing of messages between chains:

```python
from langgraph_crosschain import MessageRouter

router = MessageRouter()
# Messages are automatically routed by CrossChainNode
```

### SharedStateManager

Manages shared state across multiple chains:

```python
from langgraph_crosschain import SharedStateManager

state_manager = SharedStateManager()
state_manager.set("shared_data", {"key": "value"})
data = state_manager.get("shared_data")

# Subscribe to state changes
def on_change(value):
    print(f"State changed: {value}")

state_manager.subscribe("shared_data", on_change)
```

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Chain Registry                           │
│              (Manages all chain instances)                   │
└───────────────────┬─────────────────────────────────────────┘
                    │
        ┌───────────┴───────────┐
        │                       │
┌───────▼────────┐     ┌────────▼──────┐
│    Chain 1     │     │    Chain 2    │
│  ┌──────────┐  │     │  ┌──────────┐ │
│  │  Node A  │  │────►│  │  Node X  │ │
│  └──────────┘  │     │  └──────────┘ │
│  ┌──────────┐  │     │  ┌──────────┐ │
│  │  Node B  │  │◄────│  │  Node Y  │ │
│  └──────────┘  │     │  └──────────┘ │
└────────────────┘     └───────────────┘
        │                       │
        └───────────┬───────────┘
                    │
        ┌───────────▼────────────┐
        │   Message Router       │
        │  (Routes messages)     │
        └────────────────────────┘
                    │
        ┌───────────▼────────────┐
        │ Shared State Manager   │
        │  (Shared state store)  │
        └────────────────────────┘
```

## 📖 Use Cases

### 1. Multi-Agent Systems

Create specialized chains for different tasks that collaborate:

```python
# Analytics chain
analytics_chain = build_analytics_chain()
registry.register("analytics", analytics_chain)

# Execution chain
execution_chain = build_execution_chain()
registry.register("execution", execution_chain)

# Chains can now call each other as needed
```

### 2. Modular Workflows

Break complex workflows into reusable, communicating components:

```python
# Data ingestion chain
ingestion = build_ingestion_chain()

# Processing chain (calls ingestion)
processing = build_processing_chain()

# Output chain (calls processing)
output = build_output_chain()
```

### 3. Distributed Processing

Distribute workload across multiple specialized chains:

```python
# Master chain coordinates work
master_node.broadcast(
    ["worker1", "worker2", "worker3"],
    "process_task",
    {"task": task_data}
)
```

## 🧪 Testing

Run the test suite:

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run with coverage
pytest --cov=langgraph_crosschain --cov-report=html
```

## 🔧 Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/yourusername/langgraph-crosschain.git
cd langgraph-crosschain

# Install in editable mode with dev dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

### Code Quality

```bash
# Format code
black langgraph_crosschain tests

# Lint code
ruff check langgraph_crosschain tests

# Type checking
mypy langgraph_crosschain
```

## 📝 Examples

Check out the [examples](./examples) directory for complete working examples:

- `basic_communication.py` - Simple cross-chain communication
- `shared_state.py` - Using shared state between chains
- `multi_agent_system.py` - Building a multi-agent system
- `distributed_workflow.py` - Distributed processing example

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built on top of [LangGraph](https://github.com/langchain-ai/langgraph)
- Inspired by the need for more modular AI agent architectures
- Thanks to all contributors!


## 🗺️ Roadmap

- [x] Core cross-chain communication
- [x] Shared state management
- [x] Message routing
- [ ] Async/await support
- [ ] Distributed execution
- [ ] Event streaming
- [ ] Performance monitoring
- [ ] Web UI for visualization
- [ ] More examples and tutorials

---

## Ecosystem — other tools by the same author

If `langgraph-crosschain` unblocks your multi-agent work, these might too:

| Package | What it does |
|---------|--------------|
| [**distill-json**](https://pypi.org/project/distill-json/) | Compress JSON state passed between chains by 60-85% — massive token savings on multi-agent flows |
| [**tracemaid**](https://pypi.org/project/tracemaid/) | Auto-generate Mermaid diagrams of cross-chain calls for debugging |
| [**semantic-llm-cache**](https://pypi.org/project/semantic-llm-cache/) | Cache LLM responses by semantic similarity — agents stop re-asking the same questions |

---

Built by [Karthick Raja M](https://github.com/karthyick) · [aichargeworks.com](https://aichargeworks.com)
