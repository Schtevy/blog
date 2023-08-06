
# Contributing Guide 

## How to name Git Feature-Branches

Every **Feature-Branches** must follow the naming convetion (RegEx)

```zsh
^[\d]{1,3}-[a-z0-9\-]{7,20}[a-z0-9]$
```

Example:
- [1-init-project-setup](https://github.com/Schtevy/blog/tree/1-init-project-setup)

The prefix number must be [linked to an existing and active GitHub issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-a-branch-for-an-issue).

> The exception of this naming convention is obviously the [main](https://github.com/Schtevy/blog/tree/main) and [stable](https://github.com/Schtevy/blog/tree/stable) branch.

## How to write a Git Commit Message

1. Separate subject from body with a blank line
2. Limit the subject line to 50 characters
3. Capitalize the subject line
4. Do not end the subject line with a period
5. Use the imperative mood in the subject line
6. Wrap the body at 72 characters
7. Use the body to explain what and why vs. how

See https://cbea.ms/git-commit/