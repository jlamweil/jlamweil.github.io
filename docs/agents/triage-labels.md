# Triage Labels

The following five canonical labels are used for issue triage:

| Role | Label String | Description |
|---|---|---|
| Needs triage | `needs-triage` | New issue awaiting evaluation by a maintainer |
| Needs info | `needs-info` | Waiting on additional information from the reporter |
| Ready for agent | `ready-for-agent` | Fully specified; an autonomous agent can pick this up with no human context |
| Ready for human | `ready-for-human` | Requires human judgement or implementation |
| Won't fix | `wontfix` | Will not be actioned |

## Conventions

- Every new issue starts with `needs-triage`.
- An issue moves to `ready-for-agent` only when the scope is unambiguous and success criteria are explicit.
- Labels are mutually exclusive within this set (only one active at a time).
