# Agent Builder Refinement for Copilot Studio Light

A comprehensive toolkit for creating, refining, and generating declarative agents for **Microsoft 365 Copilot** using **Copilot Studio Light** (also known as **Agent Builder**).

## Overview

This repository provides **four different approaches** to help you build high-quality declarative agents that follow Microsoft's best practices. Choose the method that best fits your workflow and technical requirements.

---

## 🎯 Four Ways to Refine Your Agents

### 1. Quick Prompt in Microsoft 365 Copilot Chat

**Best for:** One-time refinements, quick improvements, ad-hoc usage

📁 **Location:** [`Copilot Prompt/`](Copilot%20Prompt/)

**How it works:**
1. Open Microsoft 365 Copilot Chat
2. Copy the prompt from `Copilot Prompt/Prompt.md`
3. Paste it into Copilot along with your draft agent instructions
4. Get instant refined output

**Requirements:**
- Microsoft 365 Copilot access
- Web Search enabled (recommended) OR upload the knowledge file

**Pros:** No setup, instant results, easy to use  
**Cons:** Must paste prompt each time, not reusable

📖 [**Read the Copilot Prompt Guide →**](Copilot%20Prompt/README.md)

---

### 2. Dedicated Agent in Agent Builder / Copilot Studio Light

**Best for:** Reusable refinement workflow, team standardization, production use

📁 **Location:** [`Agent Builder Template/`](Agent%20Builder%20Template/)

**How it works:**
1. Create a new agent in Copilot Studio or Agent Builder
2. Copy configuration from `Agent Refinement Agent - Configuration.md`
3. Upload the knowledge file
4. Use the agent repeatedly to refine any agent instructions

**Requirements:**
- Copilot Studio light or Agent Builder access
- Ability to upload knowledge files

**Pros:** Reusable, consistent quality, team-friendly  
**Cons:** Requires initial agent setup

📖 [**Read the Agent Builder Guide →**](Agent%20Builder%20Template/README.md)

---

### 3. GitHub Copilot (VS Code)

**Best for:** Developers using VS Code, integrated workflow, version control

📁 **Location:**

[.github/agents/agent-improvement.agent.md](.github/agents/agent-improvement.agent.md)

[.github/prompts/refine-agent.prompt.md](.github/prompts/refine-agent.prompt.md)

**How it works:**
1. Open VS Code with GitHub Copilot enabled
2. Run `/improve-agent` in Copilot Chat with your agent instructions
3. Get refined output directly in your IDE

**Requirements:**
- VS Code with GitHub Copilot
- Custom agents feature enabled

**Pros:** IDE-integrated, version controlled, developer-friendly  
**Cons:** Requires VS Code setup, GitHub Copilot subscription

📖 [**Learn about VS Code Custom Agents →**](https://code.visualstudio.com/docs/copilot/customization/custom-agents)

---

## 🔧 Bonus: Generate Declarative Agent Manifests

### GitHub Copilot Manifest Generator (VS Code)

**Generate complete JSON manifests** following the [declarative agent schema v1.6](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/declarative-agent-manifest-1.6).

📁 **Location:** 
- Agent: [`.github/agents/generate-agent-manifest.agent.md`](.github/agents/generate-agent-manifest.agent.md)
- Prompt: [`.github/prompts/generate-manifest.prompt.md`](.github/prompts/generate-manifest.prompt.md)

**How it works:**
1. Run `/generate-manifest` in VS Code Copilot Chat
2. Describe your agent's purpose and capabilities
3. Get a complete, valid JSON manifest
4. Use it in your Copilot Studio or Teams app package

**What it generates:**
- Complete `declarativeAgent.json` file
- All required fields (version, name, description, instructions)
- Capabilities configuration (web search, SharePoint, Teams, etc.)
- Conversation starters
- Actions/plugins (if needed)
- Schema-compliant v1.6 format

---

## 📋 Comparison Table

| Method | Setup Required | Reusable | Best For | Platform |
|--------|----------------|----------|----------|----------|
| **Copilot Prompt** | None | No | Quick refinements | M365 Copilot Chat |
| **Agent Builder** | Medium | Yes | Production use | Copilot Studio Light |
| **VS Code Agent** | Low | Yes | Developers | VS Code + GitHub Copilot |
| **VS Code Prompt** | None | Yes | Quick dev workflow | VS Code + GitHub Copilot |
| **Manifest Generator** | Low | Yes | JSON generation | VS Code + GitHub Copilot |

---

## 📚 What You'll Get

All refinement methods produce:

✅ **Purpose** - Clear mission statement  
✅ **Guidelines** - Tone, boundaries, error handling  
✅ **Terminology** - Domain-specific definitions  
✅ **6 Skills** - Complete workflows with examples  
✅ **Conversation Starters** - 6 user-facing prompts  
✅ **Schema Compliance** - Follows Microsoft v1.6 spec  

---

## 🚀 Quick Start Guide

### For Non-Developers
1. Start with [**Copilot Prompt**](Copilot%20Prompt/) for immediate results
2. Upgrade to [**Agent Builder**](Agent%20Builder%20Template/) for production use

### For Developers
1. Use [**VS Code Prompt**](.github/prompts/improve-agent.prompt.md) for quick refinements
2. Set up [**VS Code Agent**](.github/agents/agent-improvement.agent.md) for ongoing use
3. Use [**Manifest Generator**](.github/agents/generate-agent-manifest.agent.md) to create JSON files

---

## 📖 Documentation & Resources

- [Write effective instructions for declarative agents](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/declarative-agent-instructions) - Microsoft's official guide
- [Declarative agent manifest schema v1.6](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/declarative-agent-manifest-1.6) - Complete schema reference
- [VS Code Custom Agents](https://code.visualstudio.com/docs/copilot/customization/custom-agents) - GitHub Copilot agents
- [VS Code Prompt Files](https://code.visualstudio.com/docs/copilot/customization/prompt-files) - Reusable prompts

---

## 📁 Repository Structure

```
agent_builder/
├── .github/
│   ├── agents/                          # VS Code custom agents
│   │   ├── agent-improvement.agent.md   # Agent refinement expert
│   │   └── generate-agent-manifest.agent.md  # Manifest generator
│   └── prompts/                         # VS Code prompt files
│       ├── improve-agent.prompt.md      # Quick refinement prompt
│       └── generate-manifest.prompt.md  # Manifest generation prompt
├── Agent Builder Template/              # Copilot Studio Light setup
│   ├── Agent Refinement Agent - Configuration.md
│   ├── Write effective instructions for declarative agents.md
│   └── README.md
├── Copilot Prompt/                      # M365 Copilot Chat prompt
│   ├── Prompt.md
│   ├── Write effective instructions for declarative agents.md
│   └── README.md
└── README.md                            # This file
```

---

## 🎯 Use Cases

- **Create new agents** - Start with best practices from day one
- **Refine existing agents** - Improve clarity, structure, and quality
- **Standardize team output** - Ensure consistent agent quality
- **Learn best practices** - Understand Microsoft's guidance through examples
- **Generate manifests** - Create schema-compliant JSON files
- **Migrate prototypes** - Transform drafts into production-ready agents

---

## 🔐 Requirements

### Minimum (Copilot Prompt)
- Microsoft 365 Copilot access
- Web Search OR file upload capability

### For Agent Builder
- Copilot Studio or Agent Builder access
- Knowledge file upload capability

### For VS Code Integration
- Visual Studio Code
- GitHub Copilot subscription
- Custom agents/prompts feature enabled

---

## 🤝 Contributing

Contributions welcome! This toolkit is based on Microsoft's official guidance and evolves with the declarative agent schema.

---

## 📄 License

This toolkit follows Microsoft's guidance and best practices for Microsoft 365 Copilot declarative agents.

---

**Last Updated:** December 2025  
**Schema Version:** v1.6  
**Platforms:** Microsoft 365 Copilot, Copilot Studio Light, GitHub Copilot (VS Code)
