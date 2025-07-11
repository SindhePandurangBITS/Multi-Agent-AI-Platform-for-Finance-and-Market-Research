question1 = "List the top five financial performance highlights from this report as bullet points."
print("=== TESTING WITH YOUR CUSTOM PROMPT ===")
answer1 = qa_chain.run(question1)
print("\nQ1:", question1, "\nA1:\n", answer1)

question2 = "Provide a 100-word executive summary emphasizing the report’s financial implications."
print("=== TESTING WITH YOUR CUSTOM PROMPT ===")
answer2 = qa_chain.run(question2)
print("\nQ1:", question1, "\nA1:\n", answer1)

