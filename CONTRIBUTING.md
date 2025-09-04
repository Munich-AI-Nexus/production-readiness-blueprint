# Contributing to the Production Readiness Blueprint

This is a practitioner-led, vendor-neutral knowledge base for **production-grade AI systems**.
We maintain **high signal** via a review-first workflow. Read this once; follow it every time.

---

## 0) Ways to contribute (choose one)

**A. Private intake (recommended for first-timers or sensitive topics)**
- Use the private form → we help **refine / anonymize** → we publish a sanitized summary.
- Intake form: [Submit privately](https://forms.office.com/e/jS1ve678XN)  
- After curation, maintainers create the public Issue/PR on your behalf (with your credit).

**B. Public GitHub (for non-sensitive, already-shaped work)**
- Open a GitHub Issue using a template (topic, case study, RFC, etc.).
- Discuss, gather 👍 votes, then submit a PR linked to the Issue.

> Rule of thumb: if you hesitate to post it publicly, use **private intake** first.

---

## 1) What you can submit

Use **Issue templates** (click “New issue”):

- `Topic Request` — propose a topic for a session/module (`type:topic-request`)
- `Case Study Submission` — real system/project for review (`type:case-study`)
- `RFC Proposal` — pattern/standard/guidance to adopt (`type:rfc`)
- `Tooling Request` — tool/library to evaluate (`type:tooling`)
- `Paper / Project Submission` — external research or repo (`type:resource`)
- `Production-Readiness Review Request` — office-hours/live review (`type:review`)
- `Question` — focused question with context (`type:question`)
- `Event Notes` — use for capturing events if you’re a scribe (`type:event`)

> Templates auto-apply `status:triage` and a `type:*` label. Our labeler may add a `module:*` based on content.

---

## 2) Workflow (Issue → Discussion → PR → Merge)

1) **Open an Issue** (or submit privately)  
   - Provide enough context to be actionable.  
   - If public, remove sensitive info; if unsure, use private intake.

2) **Discussion & voting**  
   - Community adds comments and 👍.  
   - Maintainers label, assign module(s), and move to `status:in-discussion`.  
   - When scoped, maintainers mark `status:ready-for-pr`.

3) **Create a Pull Request**  
   - **Must link an Issue** in the PR body: `Closes #<issue_number>`.  
   - Follow the PR checklist (placement, clarity, anonymization, labels).  
   - PRs without a linked Issue will fail CI.

4) **Review & merge**  
   - Maintainers review. CODEOWNERS approval required on `main`.  
   - On merge, the linked Issue is marked `status:merged`.

Stale items: Issues without activity may be auto-closed after 45+14 days (RFCs exempt).

---

## 3) Folder placement (mandatory)

| Contribution                           | Folder                                  |
|----------------------------------------|-----------------------------------------|
| Module content (overviews/patterns)    | `curriculum/module-XX-*/`               |
| Case study (sanitized)                  | `case-studies/YYYY-MM-DD-*/`            |
| RFC (draft/accepted)                   | `rfcs/rfc-XXXX-*.md`                    |
| Event agenda/notes/links               | `events/YYYY-MM-DD-*/`                  |

Diagrams → `artifacts/` subfolder. Use `.svg` or `.png`. No binaries if avoidable.

---

## 4) Labels we use

**Type (one):** `type:topic-request`, `type:case-study`, `type:rfc`, `type:event`, `type:tooling`, `type:resource`, `type:review`, `type:question`  
**Status:** `status:triage`, `status:in-discussion`, `status:ready-for-pr`, `status:in-progress`, `status:merged`, `status:closed`, `status:stale`  
**Module:** `module:context`, `module:behavior`, `module:execution`, `module:state`, `module:collaboration`, `module:observability`, `module:security`, `module:scale-roi`, `module:learning`  
**Priority (optional):** `priority:high|medium|low`

---

## 5) Quality standards

- **Neutral & technical.** No vendor pitches or recruiting.  
- **Clear scope.** What problem, for whom, under which constraints.  
- **Actionable.** Patterns, trade-offs, failure modes, and examples.  
- **Cited.** Link prior art where relevant.  
- **Anonymized.** Remove proprietary names/data unless you have explicit permission.

---

## 6) Security & confidentiality

We **do not merge sensitive details**. You are responsible for redaction.  
Levels we accept:
- **Public:** safe to publish as-is.  
- **Sanitized:** anonymized names, abstracted diagrams.  
- **Summary-only:** we publish takeaways, no artifacts.

If in doubt, use **private intake**: [Submit privately](https://forms.office.com/e/jS1ve678XN).

---

## 7) PR requirements (CI will enforce)

- PR body contains `Closes #<issue_number>`.  
- Files are in the correct folders; names are descriptive.  
- No secrets or confidential identifiers.  
- Markdown passes lint & link checks.  
- At least **one maintainer review** (CODEOWNERS).

---

## 8) Recognition

- You’re credited in commit history and module credits.  
- After **3+ merged PRs** (or equivalent reviews), you may be invited as a **Maintainer**.  
- Major contributions may be highlighted in events and release notes.

---

## 9) Contact

- Questions: open a `Question` Issue or ask in Slack `#nexus-curriculum`.  
- Sensitive topics: use **private intake** or DM an organizer.  
- Governance & conduct: see [`GOVERNANCE.md`](./GOVERNANCE.md) and [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md).

---

**One line summary:** *Start with an Issue (or private intake), gather signal, ship a PR, get reviewed, get merged. Keep it high-signal and production-focused.*
