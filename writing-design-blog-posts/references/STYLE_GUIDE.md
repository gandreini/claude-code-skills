# Style guide: voice and tone

This file contains the detailed voice patterns and concrete transformation examples that show how to convert generic writing into the target practitioner voice.

## Core voice identity

The author is a **product designer who learned development on the side**, working at the intersection of design and technology. The voice is that of someone who has shipped real work and wants to save others the trouble of learning the hard way.

Key traits:
- **Generous**: Shares templates, spreadsheets, tools, resources — often for free
- **Self-aware**: Honest about limitations and mistakes ("I've been working on short-term projects where the design process is made on autopilot")
- **Practical**: Names specific tools (Figma, Miro, Google Spreadsheets, Notion) rather than abstract categories
- **Internationally minded**: Writes in English for a global audience, references European and international projects naturally
- **Connected**: Links to own previous articles, building a body of work

## Voice transformation examples

These before/after pairs show how to convert generic AI-style writing into the target voice.

### Example 1: Opening paragraph

**❌ Generic (AI-sounding):**
> User testing is a critical component of the UX design process. It allows designers to validate their assumptions and gather valuable feedback from real users. In this article, we will explore a practical approach to conducting user testing sessions that can be applied to various project contexts.

**✅ Target voice:**
> At the beginning of 2018, I joined a research project where we needed to test a digital archive with real users — but we had no dedicated UX lab, a tiny budget, and participants scattered across three Italian universities. What we built instead was a portable testing setup that fit in a backpack. Here's the method we used, and the template I still carry with me today.

**Why it works:** Names a year, a real situation, a constraint. Shows vulnerability (tiny budget). Promises something concrete (a template). The reader trusts a person who was there.

### Example 2: Introducing a methodology

**❌ Generic:**
> A retrospective analysis of previous design decisions is an important first step in any design project. It helps teams identify areas for improvement and avoid repeating past mistakes. Consider reviewing the outcomes of your last project before starting a new one.

**✅ Target voice:**
> The first thing we did was disable autopilot. We sat down and ran a retrospective on the previous version of the archive — the one that, honestly, nobody used. What did we do wrong? The interface was cluttered, the search was broken, and we'd designed the whole thing without talking to a single researcher. So we started from scratch.

**Why it works:** Uses metaphor ("disable autopilot"). Admits failure openly. Uses a rhetorical question to transition. Shows the messy reality of design work.

### Example 3: Bullet list formatting

**❌ Generic:**
> - Use a simple layout
> - Choose readable fonts
> - Maintain consistent spacing
> - Use a limited color palette

**✅ Target voice:**
> - **Simple layout:** don't reinvent the wheel. Use established grid patterns and let the content breathe
> - **Readable fonts:** pick two max — one for headings, one for body. If in doubt, go with system fonts
> - **Consistent spacing:** define a spacing scale (4px, 8px, 16px, 24px, 32px) and stick with it across every component
> - **Limited palette:** 2–3 colors plus neutrals. Every additional color needs to earn its place

**Why it works:** Bold lead-in phrase pattern. Each bullet has a rationale, not just a rule. Practical specifics (4px, 8px...) instead of vague guidance.

### Example 4: Closing paragraph

**❌ Generic:**
> In conclusion, following these guidelines will help you create a more effective resume. Remember to tailor your resume to each position and continuously update it as you gain new experience. Good luck with your job search!

**✅ Target voice:**
> I hope this collection of tips and resources helps you land your next design role. If you want to dig deeper, I'd recommend checking out Hung Nguyen's portfolio tips on Bestfolios — his advice on case study structure is excellent. And if you want to chat about any of this, feel free to reach out on LinkedIn. Good luck out there 🚀

**Why it works:** "I hope" language. Names a specific person and resource. Invites connection. Emoji only in career/lighter content. Warm without being saccharine.

### Example 5: Explaining a UX concept

**❌ Generic:**
> Information architecture refers to the structural design of shared information environments. It encompasses the organization, labeling, and navigation systems that enable users to find and manage information effectively.

**✅ Target voice:**
> The hardest part of the whole project was the information architecture. We had 8,000+ text fragments, each connected to sources, authors, and commentary — and all of it needed to be searchable by scholars who think in very different ways from each other. We mapped the relationships using a spreadsheet first (I'll share the template below), then translated that into a site structure that could handle both the "I know exactly what I want" searcher and the "I'm just browsing" explorer.

**Why it works:** Shows the concept through a real problem. Names the scale (8,000+ fragments). Promises a deliverable. Acknowledges user diversity without textbook language.

## Tone adaptation matrix

| Signal | Response |
|---|---|
| User says "case study" | Narrative mode. Past tense. "We discovered..." "The team decided..." |
| User says "opinion piece" or "essay" | Thesis-driven mode. Present tense. Strong claims with evidence. |
| User says "tutorial" or "how-to" | Teaching mode. "You" address. Step-by-step. Encouraging. |
| User says "career" or "guidelines" | Peer advice mode. Casual. "I" stories. Can use emojis sparingly. |
| User mentions UX Collective | Highest editorial bar. No emojis. Deep analysis. Must pass the "would ChatGPT produce this?" test. |
| User mentions Bootcamp | Slightly broader scope. Still high quality. Career and tutorial content accepted. |

## Phrases to use and avoid

### Use freely
- "I hope this helps"
- "Here's what worked for us"
- "The template is available [here]"
- "(where I work)"
- "(remember the F-shape pattern?)"
- "What did we do wrong?"
- "Great! It looks like you have everything you need:"
- "If you want to dig deeper, I'd recommend..."

### Never use
- "In this article, we will explore..."
- "Let's dive in"
- "Without further ado"
- "It's important to note that..."
- "In today's fast-paced world..."
- "This is a game-changer"
- "In conclusion"
- "The landscape of [X] is evolving rapidly"
- "As designers, we must..."
- "Leverage" (use "use")
- "Utilize" (use "use")
- "Streamline" (say what actually happens)

## Image caption format

For case studies and technical articles, use numbered figure captions:

```
![Alt text: Screenshot of the Galassia Ariosto homepage showing the search interface and navigation](image-placeholder.png)
*Fig.1 — The homepage of the digital archive Galassia Ariosto*
```

For tutorials and career articles, simpler captions are fine:

```
![Alt text: Photo of the portable user testing setup on a desk](image-placeholder.png)
*Our portable testing setup — everything fits in a backpack*
```
