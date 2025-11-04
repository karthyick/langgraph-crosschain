# 🔗 LangGraph Cross-Chain Communication Framework

[![PyPI version](https://badge.fury.io/py/langgraph-crosschain.svg)](https://badge.fury.io/py/langgraph-crosschain)
[![Python Support](https://img.shields.io/pypi/pyversions/langgraph-crosschain.svg)](https://pypi.org/project/langgraph-crosschain/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://pepy.tech/badge/langgraph-crosschain)](https://pepy.tech/project/langgraph-crosschain)
[![GitHub stars](https://img.shields.io/github/stars/karthyick/langgraph-crosschain?style=social)](https://github.com/karthyick/langgraph-crosschain)

**Enable direct node-to-node communication across multiple LangGraph chains**

A powerful Python framework that extends LangGraph to enable cross-chain node communication, allowing nodes in different chains to call and communicate with each other directly.

## 🎯 Key Features

- ✅ **Direct peer-to-peer node communication** between chains
- ✅ **Shared state management** across multiple chains
- ✅ **Event-driven architecture** with pub/sub patterns
- ✅ **Multiple communication patterns**: Request-Response, Broadcast, Pipeline
- ✅ **Thread-safe** operations with comprehensive error handling
- ✅ **Production-ready** with extensive test coverage

## 📦 Installation

```bash
pip install langgraph-crosschain
```

## 🚀 Quick Start

```python
from langgraph_crosschain import ChainRegistry, CrossChainNode, SharedStateManager
from langgraph.graph import StateGraph, END

# Create registry
registry = ChainRegistry()

# Create chains
chain1 = StateGraph(dict)
chain2 = StateGraph(dict)

# Register chains
registry.register("chain1", chain1.compile())
registry.register("chain2", chain2.compile())

# Create a cross-chain node
def process_data(state):
    # Your processing logic
    return state

node = CrossChainNode(
    chain_id="chain1",
    node_id="processor",
    func=process_data
)

# Call a node in another chain
result = node.call_remote(
    target_chain="chain2",
    target_node="analyzer",
    payload={"data": "test"},
    wait_for_response=True,
    timeout=5.0
)

# Broadcast to multiple chains
node.broadcast(
    target_chains=["chain2", "chain3", "chain4"],
    target_node="listener",
    payload={"announcement": "Hello all chains!"}
)

# Share state across chains
manager = SharedStateManager()
manager.set("shared_counter", 0)
manager.subscribe("shared_counter", lambda x: print(f"Counter changed: {x}"))
```

## 🏗️ Architecture

The framework consists of four core components:

1. **ChainRegistry**: Centralized registry for managing multiple chains
2. **CrossChainNode**: Wrapper for nodes with cross-chain communication capabilities
3. **MessageRouter**: Handles message routing between chains
4. **SharedStateManager**: Manages shared state with pub/sub support

## 📚 Documentation

For detailed documentation, examples, and API reference, visit our [Documentation](https://github.com/karthyick/langgraph-crosschain#documentation).

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for details.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Karthick Raja M**
- Senior AI/ML Engineer & Full Stack Developer
- [LinkedIn](https://www.linkedin.com/in/karthick-raja-mohan-753431123/)
- [GitHub](https://github.com/karthyick)
- [Portfolio](https://www.mygreatlearning.com/eportfolio/karthick-raja-m)

## 🙏 Acknowledgments

- LangChain team for the excellent LangGraph framework
- The open-source community for inspiration and feedback

---

*Building the future of multi-agent orchestration, one chain at a time.* 🚀
