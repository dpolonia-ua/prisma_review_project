from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT

anthropic = Anthropic()

def generate_keywords(research_question):
    prompt = f"{HUMAN_PROMPT}Generate 10 relevant keywords for this research question: '{research_question}'{AI_PROMPT}"
    
    completion = anthropic.completions.create(
        model="claude-3-sonnet-20240229",
        max_tokens_to_sample=500,
        prompt=prompt
    )
    
    # Parse the completion to extract the keywords
    keywords = completion.completion.strip().split('\n')
    return keywords[:10]  # Ensure we only return 10 keywords
