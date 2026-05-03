Workflow:

1. parse_document(input)
2. extract_entities(parsed_doc)   # LLM (non-deterministic)
3. enrich_entities(entities)      # external API (can fail)
4. generate_output(enriched)

Problems:

- no state persistence
- no checkpointing
- non-deterministic outputs
- failures stop entire workflow
- no replay or resume capability
- no visibility into intermediate steps