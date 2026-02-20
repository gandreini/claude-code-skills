---
name: n8n-pr-description
description: Generate n8n-compliant PR description following their conventions
allowed-tools: Bash(git diff:*), Bash(git status:*), Bash(git log:*), Bash(git show:*), Bash(git branch:*), Bash(git rev-parse:*), Bash(cat:*), Bash(ls:*), Bash(find:*)
---

# Context

- Current branch: !`git rev-parse --abbrev-ref HEAD`
- Base branch: master
- Commits in this branch (not in base): !`git log origin/master..HEAD --oneline 2>/dev/null || git log -10 --oneline`
- Full commit messages: !`git log origin/master..HEAD --pretty=format:"%s%n%b---" 2>/dev/null || git log -5 --pretty=format:"%s%n%b---"`
- Changed files: !`git diff origin/master..HEAD --name-only 2>/dev/null || git diff --name-only HEAD~5`
- Full diff: !`git diff origin/master..HEAD 2>/dev/null || git diff HEAD~5`

# n8n PR Description Template

```markdown
## Summary

<!--
Describe what the PR does and how to test.
Photos and videos are recommended.
-->

<description of what the PR does>

## Related Linear tickets, Github issues, and Community forum posts

<!--
Include links to **Linear ticket** or Github issue or Community forum post.
Important in order to close *automatically* and provide context to reviewers.
https://linear.app/n8n/issue/
-->
<!-- Use "closes #<issue-number>", "fixes #<issue-number>", or "resolves #<issue-number>" to automatically close issues when the PR is merged. -->

<leave empty or extract from commit messages if mentioned>

## Review / Merge checklist

- [ ] PR title and summary are descriptive. ([conventions](../blob/master/.github/pull_request_title_conventions.md)) <!--
   **Remember, the title automatically goes into the changelog.
   Use `(no-changelog)` otherwise.**
-->
- [ ] [Docs updated](https://github.com/n8n-io/n8n-docs) or follow-up ticket created.
- [ ] Tests included. <!--
   A bug is not considered fixed, unless a test is added to prevent it from happening again.
   A feature is not complete without tests.
-->
- [ ] PR Labeled with `release/backport` (if the PR is an urgent fix that needs to be backported)
```

# Instructions

Analyze the commits and code changes above, then generate a PR description that:

1. **Summary section**:
   - Describe what the PR accomplishes based on the actual code changes
   - If testing steps can be inferred from the changes (e.g., UI changes, API endpoints, specific functionality), include them
   - If testing steps cannot be determined, leave a placeholder: `<!-- Add testing instructions -->`

2. **Related tickets section**:
   - Look for issue numbers in commit messages (e.g., `#123`, `fixes #456`, `closes #789`)
   - Look for Linear ticket references (e.g., `N8N-1234` or `ADO-1234`)
   - Extract the ticket ID from the branch name if it follows a pattern like `ado-1234-description`
   - If found, format them properly (e.g., `closes #123` or `https://linear.app/n8n/issue/ADO-1234`)
   - If none found, leave the section empty with a comment: `<!-- Add related tickets/issues -->`

3. **Checklist**: Include the checklist exactly as-is with all inline HTML comments (unchecked)

## Tips for good descriptions:

- Focus on the "what" and "why", not the "how"
- Be specific about user-facing changes
- Mention any breaking changes or deprecations
- Note any configuration changes required
- If it's a Node change, mention which node and what capability changed

# Output

Output ONLY the PR description in markdown format, ready to paste into GitHub. Do not include any explanatory text before or after.
