# FAQ Integration Guide

## Overview

The issue_autoreply skill integrates with the vLLM-Ascend FAQ knowledge base as the primary reference for problem analysis and solution lookup.

## FAQ Knowledge Base

- **URL**: https://gitcode.com/raintBN/vLLM_Ascend_FAQ
- **Content**: Historical closed issues and troubleshooting guides
- **Usage**: Primary reference for Agent 1

## Integration Architecture

```
┌─────────────────┐
│   Agent 1       │
│  (Analyzer)     │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────────────┐
│      FAQ Knowledge Base            │
│  (https://gitcode.com/...)         │
│                                     │
│  - Known issues                     │
│  - Root causes                      │
│  - Solutions                        │
│  - Workarounds                      │
└─────────────────────────────────────┘
         │
         ▼
┌─────────────────┐
│  Solution Plan  │
└─────────────────┘
```

## FAQ Search Strategy

### Step 1: Keyword Extraction
Extract keywords from issue:
- Error messages
- Environment identifiers
- Problem description

### Step 2: Search Execution
Search FAQ repository for:
- Exact error message matches
- Similar problem descriptions
- Environment-specific issues

### Step 3: Solution Matching
Match found solutions to current issue:
- Version compatibility check
- Environment requirements
- Success probability ranking

## FAQ Entry Structure

Each FAQ entry typically contains:
- **Title**: Issue summary
- **Environment**: NPU model, CANN version, vLLM version
- **Problem**: Error description
- **Root Cause**: Technical explanation
- **Solution**: Step-by-step fix
- **Verification**: Test results

## Access Methods

### Manual Access
```bash
# Clone FAQ repository
git clone https://gitcode.com/raintBN/vLLM_Ascend_FAQ.git
cd vLLM_Ascend_FAQ
```

### Programmatic Access (Future)
```python
import requests

def search_faq(keywords):
    # Search FAQ knowledge base
    # Return matching entries
    pass
```

## Best Practices

1. **Always search FAQ first** - Most issues have known solutions
2. **Match environment details** - Version compatibility matters
3. **Cross-reference multiple entries** - Similar issues may have different solutions
4. **Document search results** - Record what was found for Agent 2

## Caching Strategy

To improve performance:
1. Cache frequently accessed FAQ entries
2. Index by common error keywords
3. Store environment-specific solutions separately

## Error Handling

If FAQ search fails:
1. Log the failure
2. Proceed with source code analysis
3. Document that FAQ lookup was attempted but unsuccessful