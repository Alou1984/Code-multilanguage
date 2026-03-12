# Directives

This folder contains **Standard Operating Procedures (SOPs)** written in Markdown.

## Purpose

Directives define:
- **Goals** - What the task should accomplish
- **Inputs** - What data/parameters are needed
- **Tools/Scripts** - Which execution scripts to use
- **Outputs** - Expected deliverables
- **Edge Cases** - Known issues and how to handle them

## Format

Each directive should follow this template:

```markdown
# [Task Name]

## Goal
What this directive accomplishes.

## Inputs
- Input 1: Description
- Input 2: Description

## Execution
1. Step 1 - Use `execution/script_name.py`
2. Step 2 - ...

## Outputs
- Output 1: Description

## Edge Cases
- Case 1: How to handle
- Case 2: How to handle

## Learnings
- (Updated as you discover new constraints or better approaches)
```

## Principles

1. Directives are **living documents** - update them as you learn
2. Write instructions like you would for a mid-level employee
3. Be specific about which scripts to use and in what order
