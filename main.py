import research_question_generator
import keyword_generator
import scopus_api_handler
import gui_handler
import data_processor
import claude_handler

def main():
    # 1. Generate and select research questions
    initial_question = input("Enter your initial research question: ")
    questions = research_question_generator.generate_questions(initial_question)
    selected_question = gui_handler.select_question(questions)

    # 2. Generate and select keywords
    keywords = keyword_generator.generate_keywords(selected_question)
    selected_keywords = gui_handler.select_keywords(keywords)

    # 3. Search ASJC areas and select articles
    articles = scopus_api_handler.search_articles(selected_keywords)
    selected_articles = gui_handler.select_articles(articles)

    # 4. Retrieve journals and descriptions
    journals = scopus_api_handler.get_q1_q2_journals(selected_articles)
    journal_descriptions = scopus_api_handler.get_journal_descriptions(journals)

    # 5. Retrieve article metadata and abstracts
    article_data = scopus_api_handler.get_article_data(journals)

    # 6. Generate PRISMA review
    review_data = data_processor.prepare_review_data(
        selected_question, 
        selected_keywords, 
        selected_articles, 
        journal_descriptions, 
        article_data
    )
    prisma_review = claude_handler.generate_prisma_review(review_data)

    print(prisma_review)

if __name__ == "__main__":
    main()
