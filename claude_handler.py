from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT

anthropic = Anthropic()

def generate_prisma_review(review_data):
    prompt = f"{HUMAN_PROMPT}Generate a PRISMA systematic literature review based on the following data:\n\n"
    prompt += f"Research Question: {review_data['research_question']}\n"
    prompt += f"Keywords: {', '.join(review_data['keywords'])}\n"
    prompt += f"Number of Articles: {len(review_data['articles'])}\n"
    prompt += f"Number of Journals: {len(review_data['journal_descriptions'])}\n"
    prompt += f"{AI_PROMPT}"

    completion = anthropic.completions.create(
        model="claude-3-sonnet-20240229",
        max_tokens_to_sample=2000,
        prompt=prompt
    )

    return completion.completion