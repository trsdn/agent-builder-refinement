---
description: Generate a declarative agent JSON manifest based on schema v1.6
name: generate-manifest
argument-hint: Describe your agent's purpose and capabilities
agent: Generate_Agent_Manifest
tools: ['fetch', 'search']
---

# Generate Declarative Agent Manifest

Generate a complete declarative agent JSON manifest (v1.6) based on your requirements.

Provide details about your agent:
- **Purpose**: What should the agent do?
- **Capabilities**: What data sources or skills does it need? (web search, SharePoint, Teams, email, etc.)
- **Instructions**: Key behaviors, workflows, or guidelines
- **Conversation starters**: Example prompts users might ask (optional)
- **Actions**: Any API plugins it should use (optional)

The agent will generate a valid JSON manifest following the [v1.6 schema](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/declarative-agent-manifest-1.6).
