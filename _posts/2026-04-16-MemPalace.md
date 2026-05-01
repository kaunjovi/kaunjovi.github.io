
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
13. **Closets** : compact notes that point back to the original content. 
14. The main persisted storage path is still the underlying drawer text plus metadata.
15. **Drawers**
16. The original stored text chunks. This is the primary retrieval layer used by the current search and benchmark flows.

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


