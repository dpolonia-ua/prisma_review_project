from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT

anthropic = Anthropic()

def generate_questions(initial_question):
    prompt = f"{HUMAN_PROMPT}Generate 10 alternative research questions based on this initial question: '{initial_question}'{AI_PROMPT}"
    
    completion = anthropic.completions.create(
        model="claude-3-sonnet-20240229",
        max_tokens_to_sample=1000,
        prompt=prompt
    )
    
    # Parse the completion to extract the questions
    questions = completion.completion.strip().split('\n')
    return questions[:10]  # Ensure we only return 10 questions
