import random

def parse_document(doc):
    return {"text": doc}

def extract_entities(parsed):
    # Simulate non-deterministic LLM behavior
    if random.random() < 0.2:
        return {"entities": None}
    return {"entities": ["contract_id", "date"]}

def enrich_entities(entities):
    # Simulate dependency on previous step
    if entities["entities"] is None:
        raise Exception("No entities to enrich")
    return {"enriched": {e: "value" for e in entities["entities"]}}

def generate_output(enriched):
    return {"result": enriched}

def run_pipeline(doc):
    parsed = parse_document(doc)
    extracted = extract_entities(parsed)
    enriched = enrich_entities(extracted)
    output = generate_output(enriched)
    return output

if __name__ == "__main__":
    doc = "Sample contract"
    print(run_pipeline(doc))