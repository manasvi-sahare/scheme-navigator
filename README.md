# Scheme Navigator

Scheme Navigator is an AI assistant that helps people in Karnataka find
government welfare schemes they are eligible for. Citizens describe their
situation in plain language (English, Kannada, or Hindi), and the assistant
asks only the follow-up questions it needs, then recommends relevant central
and state schemes with the documents required and links to official sources.

**Design principle: the LLM explains, code decides.** Scheme information is
retrieved and explained using retrieval-augmented generation (RAG) with
citations. Eligibility is decided by a deterministic rules engine built from
structured criteria extracted from official documents, so a model can't
guess whether someone qualifies. When the system is unsure or information
may be outdated, it says so and directs the user to verify at the official
office.