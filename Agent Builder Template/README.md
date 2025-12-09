# Agent Refinement Agent

A declarative agent for Microsoft 365 Copilot designed to review and improve agent instructions based on Microsoft's best practices.

## Overview

This agent helps you refine your declarative agent prompts and instructions for **Copilot Studio Light** (also known as **Copilot Agent Builder**). It analyzes your agent's description and instructions, then returns a revised, production-ready instruction set that follows Microsoft's official guidance.

## What It Does

The Agent Refinement Agent:

- ✅ Reviews your agent instructions for clarity, structure, and best practices
- ✅ Ensures proper formatting with Purpose, Guidelines, and Skills sections
- ✅ Creates exactly 6 well-defined skills with clear workflows
- ✅ Adds error handling, decision logic, and transition criteria
- ✅ Generates conversation starters for each skill
- ✅ Follows Microsoft's declarative agent schema and size constraints

## Use Cases

Perfect for:

- **New agent creators** who want to ensure their instructions follow best practices
- **Existing agents** that need refinement or restructuring
- **Teams** standardizing agent quality across multiple Copilot agents
- **Migration** from prototype to production-ready agents

## How to Use

### In Copilot Studio Light / Agent Builder

1. **Create a new agent** in Copilot Studio or Agent Builder
2. **Copy the configuration** from `Agent Refinement Agent - Configuration.md`:
   - Name: Agent Refinement Agent
   - Description: Agent to refine declarative Agent Prompts from Agent Builder/Copilot Studio light
   - Instructions: Copy the full instructions block
3. **Upload knowledge file**: Add `Write effective instructions for declarative agents.md` (or PDF version)
4. **Add conversation starter**: "Rewrite my Prompt: [Prompt]"
5. **Test the agent** by pasting your draft agent instructions

### Example Usage

**You:**
```
Rewrite my Prompt: You are a travel assistant. Help users book flights and hotels.
```

**Agent:**
Returns a complete, structured instruction set with:
- Clear Purpose statement
- Detailed Guidelines
- 6 specific Skills (e.g., "Search Available Flights", "Validate Booking Details", etc.)
- Conversation examples
- 6 conversation starters

## Files Included

| File | Purpose |
|------|---------|
| `Agent Refinement Agent - Configuration.md` | Complete agent configuration for copy-paste into Agent Builder |
| `Write effective instructions for declarative agents.md` | Microsoft's official guidance from [learn.microsoft.com](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/declarative-agent-instructions) (upload as knowledge) |
| `README.md` | This documentation |

## Configuration Details

- **Instruction Length:** ~1,200 words max
- **Skills:** Exactly 6 per agent
- **Conversation Starters:** 6 (one per skill)
- **Knowledge Source:** Microsoft's declarative agent best practices

## Requirements

- Access to **Microsoft 365 Copilot**
- **Copilot Studio** or **Agent Builder** (Copilot Studio Light)
- Ability to upload knowledge files (PDF or Markdown)

## Best Practices

When using this agent:

1. **Be specific** about your agent's domain and purpose
2. **Include context** like target audience, data sources, or compliance needs
3. **Review the output** - the agent provides a starting point; customize as needed
4. **Iterate** - use the refined output to create your agent, then refine again if needed

## Limitations

- Cannot import JSON manifests directly (use configuration file for manual setup)
- Requires knowledge file upload for best results
- Output must be manually copied into Agent Builder UI

---

**Created for:** Copilot Studio Light / Copilot Agent Builder  
**Last Updated:** December 2025  

This template follows Microsoft's guidance and best practices for Microsoft 365 Copilot declarative agents.
**Source:** [Microsoft's declarative agent best practices ](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/declarative-agent-instructions)
