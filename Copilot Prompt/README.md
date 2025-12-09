# Agent Refinement Prompt

A simple prompt for Microsoft 365 Copilot to refine your declarative agent instructions based on Microsoft's best practices.

## Overview

This folder contains a ready-to-use prompt that helps you improve your agent instructions directly in **Microsoft 365 Copilot Chat**. No need to create a dedicated agent - just paste the prompt and get instant feedback on your agent instructions.

## How to Use

### Option 1: With Web Search (Recommended)

If **Web Search** is enabled in your Copilot:

1. **Open Microsoft 365 Copilot Chat**
2. **Copy the entire prompt** from `Prompt.md`
3. **Paste it into Copilot**
4. **Add your agent instructions** after the prompt
5. **Review and refine** the improved output

Copilot will use web search to access Microsoft's latest guidance on [declarative agents](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/declarative-agent-instructions).

### Option 2: With Uploaded Knowledge File

If Web Search is **not available**:

1. **Open Microsoft 365 Copilot Chat**
2. **Upload the file**: `Write effective instructions for declarative agents.md`
3. **Copy the prompt** from `Prompt.md`
4. **Paste it into Copilot** along with your agent instructions
5. **Review and refine** the output

The uploaded file provides the same guidance that Copilot would retrieve via web search.

## Files Included

| File | Purpose |
|------|---------|
| `Prompt.md` | The refinement prompt - copy and paste this into Copilot |
| `Write effective instructions for declarative agents.md` | Microsoft's official guidance from [learn.microsoft.com](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/declarative-agent-instructions) - upload if web search is not available |
| `README.md` | This documentation |

## Example Usage

**Step 1:** Copy the prompt from `Prompt.md`

**Step 2:** In Copilot Chat, paste the prompt followed by your draft instructions:

```
[Paste the prompt here]

Here are my agent instructions:
You are a travel assistant. Help users book flights and hotels.
```

**Step 3:** Copilot returns:
- Structured instructions with Purpose, Guidelines, and 6 Skills
- Conversation examples
- 6 conversation starters
- Ready-to-use format

**Step 4:** Copy the refined output and use it in your agent

## What You Get

The refined output includes:

✅ **Purpose** - Clear mission and scope  
✅ **Guidelines** - Tone, boundaries, error handling  
✅ **Terminology** - Domain-specific definitions (if needed)  
✅ **6 Skills** - Each with workflows, examples, and output formats  
✅ **Conversation Starters** - 6 prompts for user guidance  

## When to Use This vs. Agent Builder Template

| Use This (Copilot Prompt) | Use Agent Builder Template |
|---------------------------|---------------------------|
| Quick, one-time refinement | Reusable refinement agent |
| Ad-hoc improvements | Standardized team process |
| No agent setup needed | Consistent agent quality |
| Paste and go | Upload knowledge once |

## Tips for Best Results

1. **Be specific** - Include your agent's domain, audience, and key capabilities
2. **Provide context** - Mention data sources, compliance needs, or restrictions
3. **Iterate** - Use the refined output, test it, and refine again if needed
4. **Customize** - The output is a starting point; adjust to your specific needs

## Requirements

- Access to **Microsoft 365 Copilot Chat**
- Either:
  - Web Search capability enabled, OR
  - Ability to upload files to Copilot Chat

## Limitations

- One-time use per conversation (not reusable like a dedicated agent)
- Requires pasting the full prompt each time
- Web search may retrieve outdated content (use uploaded file for consistency)

---

**Method:** Copy-paste prompt into Microsoft 365 Copilot Chat  
**Last Updated:** December 2025  
**Source:** [Microsoft's declarative agent best practices ](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/declarative-agent-instructions)
