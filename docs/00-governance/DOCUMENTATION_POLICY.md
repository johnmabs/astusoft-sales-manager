# Documentation Policy — Astusoft Sales Manager

**Document ID:** GOV-001
**Status:** Accepted
**Owner:** Project Maintainer

## 1. Purpose

This document defines the principles governing the creation,
organization, maintenance and evolution of project documentation.

Its purpose is to ensure that the project remains understandable,
traceable and resumable after an extended interruption.

These rules apply to both human contributors and AI assistants.

## 2. Documentation principles

### 2.1 Documentation as code

Project documentation MUST:

- Be stored in the Git repository.
- Use Markdown unless another format is explicitly justified.
- Be reviewed and versioned with the relevant changes.
- Remain readable without specialized proprietary tools.
- Use repository-relative links for internal references.

### 2.2 Single source of truth

Every important piece of information MUST have one authoritative
location.

Other documents SHOULD reference that location instead of
duplicating its content.

Examples:

- Business rules belong to domain specifications.
- Architectural decisions belong to ADRs.
- Implementation tasks belong to delivery documentation.
- Current implementation progress belongs to the project
  tracking system.

If two authoritative sources conflict, the conflict MUST be
resolved explicitly.

### 2.3 Separation of responsibilities

Documentation MUST distinguish between:

- Product vision and requirements.
- Business discovery and domain modeling.
- Architecture and technical decisions.
- Implementation planning.
- Implementation progress and validation.
- Operations and maintenance.
- AI collaboration instructions.

A document SHOULD NOT combine unrelated responsibilities.

### 2.4 Explicit uncertainty

Unverified assumptions MUST NOT be presented as established facts.

Documents MUST distinguish:

- Confirmed facts.
- Working assumptions.
- Proposed decisions.
- Accepted decisions.
- Implemented behavior.
- Verified behavior.

A planned capability MUST NOT be described as implemented.

### 2.5 Traceability

Requirements, business rules, decisions, implementation tasks
and validation evidence SHOULD be traceable through stable
identifiers and references.

A completed implementation task MUST reference its validation
evidence.

### 2.6 Incremental documentation

Documentation SHOULD evolve alongside the implementation.

Contributors MUST NOT create speculative documentation for
features whose requirements have not yet been established.

Documentation changes SHOULD remain small and focused.

## 3. Documentation directory structure

The following structure defines the intended responsibilities
of the documentation directories.

Directories are created progressively when needed.

| Directory               | Responsibility                             |
| ----------------------- | ------------------------------------------ |
| `docs/00-governance/`   | Project rules and conventions              |
| `docs/01-product/`      | Product vision, actors and requirements    |
| `docs/02-domain/`       | Domain knowledge and business models       |
| `docs/03-architecture/` | Architecture, ADRs and contracts           |
| `docs/04-delivery/`     | Roadmap, Lots, Epics, Tasks and Gates      |
| `docs/05-quality/`      | Testing and quality assurance              |
| `docs/06-operations/`   | Deployment and operations                  |
| `docs/07-knowledge/`    | Lessons learned and knowledge records      |
| `docs/ai/`              | Instructions and prompts for AI assistants |

This table describes intended ownership, not existing
implementation.

## 4. Document identification

Documents requiring long-term traceability MUST have stable
identifiers.

Initial identification families:

| Prefix | Purpose                   |
| ------ | ------------------------- |
| `GOV`  | Governance                |
| `REQ`  | Product requirements      |
| `BR`   | Business rules            |
| `ADR`  | Architectural decisions   |
| `LOT`  | Delivery Lots             |
| `EPIC` | Epics                     |
| `TASK` | Implementation tasks      |
| `GATE` | Delivery validation gates |

Examples:

- `GOV-001`
- `REQ-001`
- `BR-001`
- `ADR-0001`
- `LOT-00`
- `EPIC-00-01`
- `TASK-00-01-02`
- `GATE-00`

Identifiers MUST NOT be reused for different subjects.

Detailed identification and lifecycle rules will be defined
in the delivery governance documentation.

## 5. Naming conventions

### 5.1 Directory names

Directories SHOULD use lowercase kebab-case unless a stable
identifier provides a clearer name.

Examples:

- `00-governance`
- `domain-model`
- `LOT-00`

### 5.2 File names

Use descriptive file names.

Examples:

- `DOCUMENTATION_POLICY.md`
- `PROJECT_STATE.md`
- `ADR-0001-modular-monolith.md`

Documents identified by a formal ID MUST preserve that ID
when renamed or moved.

### 5.3 Language

Business-facing documentation SHOULD use French.

Code identifiers, API contracts and technical symbols SHOULD
use English where appropriate.

Technical documentation MAY use English when it improves
consistency and interoperability with development tools.

Within a document, terminology MUST remain consistent.

### 5.4 Terminology

Business terms MUST be defined in the domain glossary when
their meaning is ambiguous or important to business rules.

The same concept SHOULD use the same term throughout
its bounded context.

## 6. Cross-document references

Internal documents MUST use relative Markdown links.

Examples:

- `[Project README](../../README.md)`
- `[Documentation Policy](DOCUMENTATION_POLICY.md)`

References MUST NOT depend on local absolute filesystem paths.

Broken internal references MUST be corrected before a
documentation change is validated.

## 7. Document lifecycle

Documents MAY use the following lifecycle statuses:

- `Draft`
- `In Review`
- `Accepted`
- `Superseded`
- `Archived`

Definitions:

**Draft:** Content is being prepared and is not authoritative.

**In Review:** Content is awaiting explicit approval.

**Accepted:** Content is approved and authoritative within
its defined scope.

**Superseded:** Another accepted document replaces it.

**Archived:** Preserved for historical reference and no longer
used for active decisions.

These statuses describe documents, not implementation tasks.

Implementation task statuses will have their own lifecycle.

## 8. Change management

A documentation change MUST identify its purpose.

Changes affecting accepted business rules or architectural
decisions MUST update the corresponding authoritative source.

An accepted ADR MUST NOT be silently rewritten to change its
decision. A new ADR SHOULD supersede the former decision.

Historical information SHOULD remain accessible through Git
and explicit references when useful.

## 9. Validation requirements

Before a documentation change is accepted:

1. Verify that the document belongs to the correct directory.
2. Verify that its purpose is clearly defined.
3. Check for contradictions with accepted documents.
4. Verify relative links.
5. Verify identifiers and references.
6. Review assumptions and unsupported claims.
7. Verify that the proposed Git commit is focused.

Automated validation will be added progressively.

Until then, manual verification remains mandatory.

## 10. AI collaboration

AI assistants MUST follow the same documentation rules
as human contributors.

AI-generated content MUST be reviewed before acceptance.

AI assistants MUST NOT:

- Invent business requirements.
- Invent implementation progress.
- Claim tests were executed without evidence.
- Mark a task completed without validation.
- Silently change accepted architectural decisions.
- Treat previous conversations as more authoritative
  than the current repository.

AI-specific workflows and context-loading rules will be
defined separately.

## 11. Project resumption

The repository MUST eventually provide a concise entry point
describing:

- The last confirmed project state.
- Current Lot, Epic and Task.
- Completed and verified work.
- Known blockers.
- Open decisions.
- The next actionable step.
- Commands required to resume development.

The dedicated project-state mechanism will be introduced
in a subsequent governance task.

## 12. Evolution of this policy

Changes to this policy require explicit review.

Significant changes MUST document:

- The reason for the change.
- The affected documents or workflows.
- Any migration required.
- The commit introducing the change.
