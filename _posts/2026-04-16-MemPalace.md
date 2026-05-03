
## [MemPalace](https://github.com/MemPalace/mempalace) 

1. **Reference**
2. https://mempalaceofficial.com/concepts/the-palace.html
3. It organizes memories using a spatial hierarchy (Wings, Rooms, Drawers) based on the "Method of Loci" to structure data, 
4. though core retrieval relies heavily on ChromaDB’s semantic search capabilities.
5. MCP server for **semantic search** and **knowledge graph**
6. MemPalace stores your conversation history as verbatim text and retrieves it with semantic search. 
7. It does not summarize, extract, or paraphrase. 
8. The index is structured — 
   1. people and projects become wings, 
   2. topics become rooms, and 
   3. original content lives in drawers — so searches can be scoped rather than run against a flat corpus.
9. The retrieval layer is pluggable. 
10. The current default is ChromaDB; the interface is defined in mempalace/backends/base.py and 
11. alternative backends can be dropped in without touching the rest of the system.
12. Nothing leaves your machine unless you opt in.

## What is structure inside MemPalace

1.  **Palace** is the overall structure.
2.  **Wings** : Wings are the top-level organizational unit.
3.  A person or project. As many as you need.
4.  Every project, person, or topic gets its own wing in the palace. 
5.  **Rooms** : Rooms are named ideas. 
6.  They're auto-detected from your folder structure during mempalace init, and you can create additional rooms manually.
7.  Specific topics within a wing. 
8.  Examples: auth-migration, graphql-switch, ci-pipeline.
9.  **Halls** : Halls are the conceptual categories that describe how related memories connect within a wing:
    1.  hall_facts — decisions made, choices locked in
    2.  hall_events — sessions, milestones, debugging
    3.  hall_discoveries — breakthroughs, new insights
    4.  hall_preferences — habits, likes, opinions
    5.  hall_advice — recommendations and solutions
10. **Tunnels** : Connections between wings. 
11. When the same room appears in different wings, the graph layer can treat that as a cross-wing connection.
12. Same room. Three wings. The graph can use that shared room name as a bridge.
13. **Closets** : compact notes that point back to the original content. A compressed summary.
14. The main persisted storage path is still the underlying drawer text plus metadata.
15. These use the AAAK compression dialect to create 30x-smaller representations that point back to the original drawers.
16. **Drawers**
17. The original stored text chunks. This is the primary retrieval layer used by the current search and benchmark flows.

```
wing_kai       / hall_events / auth-migration  → "Kai debugged the OAuth token refresh"
wing_driftwood / hall_facts  / auth-migration  → "team decided to migrate auth to Clerk"
wing_priya     / hall_advice / auth-migration  → "Priya approved Clerk over Auth0"
```

1. Wing and room identifiers become metadata filters at query time. 
2. Narrowing a search to a specific wing (or wing + room) means the vector store only scores candidates inside that scope, 
3. which is useful when you have many unrelated projects or people filed in the same palace.
4. This is standard metadata filtering in the underlying vector store, not a novel retrieval mechanism. 
5. The useful property here is operational — clear scoping rules that a human or an agent can apply predictably — not a magic retrieval boost.


1. https://www.linkedin.com/pulse/unexpected-entry-ai-memory-milla-jovovichs-mempalace-alexey-grigorev-diz3f/
2. What sets the MemPalace project apart is its approach to AI assistant memory. 
3. Unlike most AI memory systems that tend to rely on increased model calls, extensive infrastructure, and layers of abstraction, 
4. MemPalace shows that long-term assistant memory can be local, deterministic, and cost-effective.
5. According to the project’s GitHub, MemPalace runs entirely on your local machine with just two dependencies: 
6. **ChromaDB** and **PyYAML**, and 
7. it achieves an impressive 96.6% recall@5 on the **LongMemEval** benchmark.


1. The memory layer itself doesn’t use any LLM API calls 
1. all classification, chunking, room detection, and compression run on regex heuristics and keyword scoring. 
1. The LLM is still there for the actual conversation (answering questions, generating responses), but 
1. the memory infrastructure that decides 
1. what to store, where to put it, and what to retrieve is 
1. completely deterministic and free to run.


1. **Why Do AI Agents Need Memory?**
1. LLMs are stateless. 
1. Every conversation starts from scratch - the model doesn’t have any context. 
1. The context window (the text the model can “see” at once) is its only memory, and it resets with each new session.
1. That’s fine for one-off questions. But it breaks down for anything that needs continuity:
1. A coding assistant that should remember your project’s architecture across sessions
1. A personal assistant that knows your preferences and ongoing tasks
1. A research agent that builds on previous findings over days or weeks
1. The naive solution - stuff everything into the context window - hits limits fast. 
1. Context windows are finite (even large ones degrade past ~150k tokens), and 
2. including irrelevant information hurts reasoning. **Hallucination(?)**, **ContextDilution(?)**
3. **Costly** : You pay for every token, and the model’s attention gets diluted.

4. **How Traditional RAG Helps?**
5. Traditionally, this problem is solved with **RAG - Retrieval Augmented Generation**. 
6. Instead of stuffing everything into the context, you keep your documents in a searchable index and 
7. only pull in what’s relevant to the current question.
8. The search step can use 
   1. keyword matching (like Elasticsearch), 
   2. vector similarity (like Qdrant with embeddings), or 
   3. both. 
9. You chunk your documents into smaller pieces, index them, and retrieve at query time - so the model only sees what’s relevant, not the entire knowledge base.
   
10. This works well for question-answering over static document collections - FAQs, documentation, books, video transcripts. 
11. The pattern is straightforward: 
   1. a search() method to find relevant chunks, 
   2. a build_prompt() to format the context, 
   3. an llm() to get the answer, and a 
   4. rag() that orchestrates the flow.

**RAG failure**
1. All documents are treated equally - there’s no concept of “more important” or “less important” memories
2. Everything goes into one flat index, and you rely entirely on search quality to find the right thing
3. No temporal awareness - a fact stored six months ago looks the same as one stored today, even if the old one is outdated
4. No token budget management - every query does a full search, with no progressive loading based on what the conversation actually needs
5. No cross-domain discovery - if related information lives in different topics, traditional RAG won’t surface those connections
   



## PyYAML

## LongMemEval







