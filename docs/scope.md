# Scheme Navigator: Scope

## 1. Problem
Government welfare schemes exist for farmers, students, women and the
elderly, but the information is spread across many portals, PDFs and
local-language notices. Eligibility rules are hard to read, change often,
and differ between central and Karnataka schemes. Many people miss benefits
they qualify for, or waste trips to offices for schemes they don't.

## 2. Personas
### Ramesh
- Situation: farmer, Tumakuru, 1.5 ha of land, age 45
- Language: Kannada
- Typical question: "Which schemes can I get for my farm?"
- What a good answer looks like: a short list of schemes he qualifies for
  (for example PM-KISAN and crop insurance), why each applies, documents
  needed, and a link to the official page. Asks about land ownership only if
  he hasn't said.

### Priya
- Situation: engineering student, family income about 3 lakh per year
- Language: English mixed with Kannada
- Typical question: "Any scholarships for me?"
- What a good answer looks like: scholarships matching her course, income
  and category, with deadlines and the portal to apply. Asks for category
  and course if missing.

### Lakshmamma
- Situation: widow, age 58, no income, lives in a village
- Language: Kannada
- Typical question: "Can I get a pension?"
- What a good answer looks like: pension schemes she may qualify for,
  stated simply, with the office or portal to visit. Says "please verify at
  the taluk office" when rules are unclear.

## 3. Scope
- Coverage: central schemes plus Karnataka schemes, extensible to other states
- Categories: agriculture, education, health, women and child (housing later)
- Start with about 5 schemes per category, grow to about 10
- Languages: English, Kannada, Hindi
- Sources: official government websites and documents only

## 4. Success metrics
- Eligibility decision correct on at least 90% of 100 hand-written test cases
- Every factual claim in an answer has a citation that actually supports it
  (target: 95% of claims on the test set)
- On test questions the system should not answer (out of scope, or missing
  information), it declines or says "I'm not sure" at least 90% of the time
- Kannada answers judged correct by me (and ideally a native-speaker friend)
  on at least 80% of a Kannada test set
- Every answer states which scheme document it came from and when that
  document was last fetched

## 5. Non-goals
- Does not fill or submit application forms
- Does not collect Aadhaar numbers or other ID numbers
- Does not store personal details beyond the current conversation
- Does not give legal advice or guarantee that someone will be approved
- Does not use non-official sources (blogs, lookalike sites) as evidence
- Does not cover all states or all schemes in this version

## 6. Known risks
- Free LLMs answered in Marathi when asked for Kannada (my own test, Nov 2026)
- Scheme rules change, and data may be outdated
- Official pages can be incomplete or inconsistent (the PM-KISAN page
  summarizes rules, while full rules sit in separate guideline PDFs)
- Karnataka schemes may be renamed, merged or paused
- Lookalike non-government sites rank high in search and could pollute
  the data if I'm careless
- Extracted eligibility rules may contain errors, so I will spot-check them
  by hand