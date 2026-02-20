---
name: writing-design-blog-posts
description: Write high-quality UX/design blog posts for Medium publications like UX Collective and Bootcamp. Use when asked to write, draft, outline, or revise a design article, blog post, case study, UX opinion piece, design tutorial, or career guide. Also use when asked to improve or review an existing design article draft. Captures a specific practitioner voice and enforces publication editorial standards.
---

# Writing design blog posts

Write design articles that meet UX Collective and Bootcamp editorial standards while capturing an authentic practitioner voice. Output is Medium-ready Markdown.

Before writing, read the relevant reference file for the article type:
- Case study → `references/TEMPLATES.md` § Case Study
- Opinion/essay → `references/TEMPLATES.md` § Opinion Piece
- Tutorial/methodology → `references/TEMPLATES.md` § Tutorial
- Career/guidelines → `references/TEMPLATES.md` § Career Guide
- Any article → `references/STYLE_GUIDE.md` for voice rules and examples
- Pre-submission → `references/CHECKLIST.md`

## Voice rules (non-negotiable)

The author writes as a **confident practitioner, never a theorist**. Authority comes from real projects, named tools, and shared resources — not academic frameworks.

1. **Open with a personal hook**: 1–2 paragraphs grounded in real work experience. Name a project, a year, a company, or a specific situation. Never open with a definition or a dictionary quote.
2. **"Why" before "how"**: Explain the rationale before the instruction. Every recommendation needs a reason.
3. **First person freely**: Use "I" for personal methodology, "we" for team work. Toggle fluidly, even within a paragraph.
4. **Parenthetical asides**: Quick context in parentheses — "(where I work)", "(remember the F-shape pattern?)". These create intimacy.
5. **Metaphorical language**: "disable autopilot," "pushing pixels," "don't reinvent the wheel." Vivid, never cliché.
6. **Warm closings**: Encouraging summary → bonus resource or recommendation → invitation to connect or try something. Use "I hope" language. Acknowledge collaborators by name when relevant.
7. **Generous sharing**: Link to tools, templates, spreadsheets, open-source resources. The author shares, not gatekeeps.
8. **Short paragraphs**: 2–4 sentences max. Single-sentence paragraphs are fine in lighter content.

### Formality dial

| Article type | Jargon | Tone | Emojis | Lists vs prose |
|---|---|---|---|---|
| Technical guide | High (assumes expertise) | Directive, authoritative | None | Prose-heavy + code blocks |
| Case study | Medium (explains UX terms) | Narrative, reflective | None | Prose-heavy + numbered figures |
| Methodology/tutorial | Low (beginner-friendly) | Instructional, encouraging | None | Mixed prose + templates |
| Career advice | Low (explains ATS etc.) | Casual, peer-to-peer | Sparingly (🤖🚀🌟) | Bullet-list dominant |

## UX Collective compliance (hard rules)

These are non-negotiable for any article targeting UX Collective or Bootcamp:

- **Sentence case titles only**: Only the first word capitalized, plus proper nouns. "Your title goes here" not "Your Title Goes Here"
- **Subtitle required**: One sentence that encapsulates the main idea
- **No bold/italic/all-caps headings**: Use Medium's native H2/H3 formatting
- **No promotional links**: No calls for claps, comments, follows, or affiliate links
- **Global audience**: No American-centric cultural references without explanation
- **Standalone articles only**: No "Part 1 / Part 2" series
- **Cover image required**: Simple, supportive — no text overlays
- **Human-written**: Must sound distinctly human. Personal anecdotes, specific experiences, named tools/projects, vulnerability, and idiosyncratic observations. If ChatGPT could produce essentially the same article, it's not good enough.
- **Max 2 exclamation marks** in the entire article
- **Proofread**: Clean grammar and spelling before submission

## Article structure template

Every article follows this skeleton. Adapt section count and depth to the article type.

```
# [Sentence-case title — specific point of view, not just a topic]
*[One-sentence subtitle expanding the promise]*

[PERSONAL HOOK: 1–2 paragraphs from real experience. Name a year, project, company, or specific situation.]

[CONTEXT BRIDGE: 1 paragraph — why this matters and who it's for.]

## [Descriptive H2 — scannable, not clever]
[Brief intro prose → detailed points → practical tip or example]

## [Next H2]
[Same pattern — each section advances an argument or teaches something new]

[... 5–7 H2 sections total for standard articles]

## [Closing section]
[Encouraging summary with "I hope" language → bonus resource or link → invitation]
```

### Section-level rules
- **Bold lead-in phrases** in bullet lists: each bullet starts with a bolded keyword or phrase, then explanation
- **Fig.N — Description** format for image captions in case studies and technical articles
- **Subheadings every 300–500 words**
- **External links as evidence**: Link to tools, NN Group articles, Wikipedia definitions, templates — never as academic citations
- **Cross-reference own work** where relevant

## Formatting and Medium specifics

- **Target length**: 1,600–2,100 words (7-min read) for standard articles. Case studies and deep analyses can run to 3,500 words (15-min read).
- **Topic tags**: Always recommend 5. Mix 2–3 broad (Design, UX, Product Design) with 2–3 specific.
- **Image placeholders**: Use `![Alt text description](image-placeholder.png)` with a caption line below: `*Fig.N — Description*`
- **Cover image**: Recommend 1500×1000 px, 5:4 or 1:1 for mobile
- **Inline images**: Recommend 1400 px min width for full column display
- **Code blocks**: Use fenced Markdown for any technical content

### Markdown-to-Medium import
Medium does not natively support Markdown. Recommend the GitHub Gist method: create a .md gist → import to Medium via "Import a story." Warn that nested lists and image captions may need manual adjustment after import.

## Anti-AI-slop rules

These patterns make writing sound AI-generated. Avoid all of them:

- ❌ Opening with a broad definition or "In the world of..."
- ❌ "In this article, we will explore..."
- ❌ "Let's dive in" / "Without further ado"
- ❌ Lists of 3 with parallel structure that feel machine-generated
- ❌ Concluding with "In conclusion" or "To sum up"
- ❌ Every paragraph starting with a topic sentence + elaboration pattern
- ❌ Encyclopedic tone without personal stake
- ❌ Hedging with "It's important to note that..."
- ❌ "This is a game-changer" / "revolutionize" / "landscape"
- ❌ Perfectly balanced "on the other hand" structures

Instead: be specific, be personal, be opinionated, be generous. Name real things. Show what you actually did. Admit what went wrong.

## Workflow

1. **Clarify article type** with the user (case study, opinion, tutorial, career guide, or other)
2. **Read the relevant template** from `references/TEMPLATES.md`
3. **Read voice examples** from `references/STYLE_GUIDE.md`
4. **Draft the article** in Markdown following all rules above
5. **Run the checklist** from `references/CHECKLIST.md` against the draft
6. **Present the final .md file** to the user with recommended topic tags and a note about the Gist import workflow

## Output format

Always produce a complete `.md` file. Include:
- Title as `# Heading`
- Subtitle as `*italicized line*` immediately below
- All H2 sections
- Image placeholders with alt text and Fig.N captions where relevant
- Recommended topic tags at the end as a comment: `<!-- Tags: Tag1, Tag2, Tag3, Tag4, Tag5 -->`
