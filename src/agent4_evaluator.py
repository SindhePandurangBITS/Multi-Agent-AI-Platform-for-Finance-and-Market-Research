temparature: 0
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from textwrap import dedent

persona = """
You are a senior RAG evaluator with expertise in:
- Assessing factual accuracy
- Verifying source attribution
- Gauging relevance of retrieved context
- Checking completeness of answers
- Ensuring coherent, well-structured responses
"""

scoring_guide = """
Rate the response on a scale of 1–5 for each:

1. **Accuracy**  
   - Are all statements supported by the source documents?  
   - Note any hallucinations or factual errors.

2. **Relevance**  
   - Do the retrieved passages directly address the query?  
   - Identify missing or extraneous information.

3. **Completeness**  
   - Does the answer fully cover the question’s requirements?  
   - Highlight any gaps in coverage.

4. **Citation Quality**  
   - Are sources clearly cited and traceable?  
   - Point out any missing attributions.

5. **Clarity & Flow**  
   - Is the answer logically organized and easy to follow?  
   - Suggest improvements to structure or phrasing.
"""

output_template = """
# RAG Assessment Report

**Query:** {query}  
**Response Length:** {{length}} chars

## Scores

- **Accuracy:** {{accuracy}}/5  
  _Justification:_ {{accuracy_notes}}

- **Relevance:** {{relevance}}/5  
  _Justification:_ {{relevance_notes}}

- **Completeness:** {{completeness}}/5  
  _Justification:_ {{completeness_notes}}

- **Citation Quality:** {{citations}}/5  
  _Justification:_ {{citations_notes}}

- **Clarity & Flow:** {{coherence}}/5  
  _Justification:_ {{coherence_notes}}

**Total Score:** {{total}}/25

## Recommendations
1. {{rec1}}  
2. {{rec2}}  
3. {{rec3}}

**Summary:**  
{{summary}}
"""

review_prompt = PromptTemplate(
    input_variables=["query", "answer", "contexts"],
    template=(
        persona
        + "\n\n"
        + scoring_guide
        + "\n\n"
        + "You will receive a user question, retrieved source passages, and the answer. "
        + "Produce a review report using the markdown template below.\n\n"
        + "----\n"
        + "User Query: {query}\n\n"
        + "Retrieved Passages:\n{contexts}\n\n"
        + "Generated Answer:\n{answer}\n\n"
        + "----\n"
        + "Here is the template for your output:\n\n"
        + output_template
    )
)

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
class RAGReview:
    """A helper to assess RAG outputs against defined quality metrics."""
    def __init__(self, llm, prompt):
        self.llm = llm
        self.prompt = prompt

    def assess_response(self, query, answer, contexts, stream=False):
        prompt_text = self.prompt.format(
            query=query,
            answer=answer,
            contexts="\n".join(contexts)
        )
        response = self.llm.invoke(prompt_text)
        if stream:
            print(response)
        return response

# ---- Example usage ----
reviewer = RAGReview(llm, review_prompt)
print("RAG/LLM evaluator is ready!")

user_query = (
    "How is Goldman Sachs using AI in the BFSI sector to enhance its wealth "
    "management and trading operations?"
)

retrieved_passages = [
    "Goldman Sachs has deployed AI-driven portfolio optimization engines that adjust asset allocations in real-time based on market signals and individual risk profiles.",
    "The bank employs NLP models to analyze financial news and social media sentiment, integrating those insights directly into its risk management frameworks."
]
model_answer = (
    "Goldman Sachs leverages machine learning-based portfolio optimization to continuously rebalance client portfolios "
    "according to shifting market conditions and personalized risk targets. They also use natural language processing "
    "to monitor news and social media sentiment, feeding those signals into trading algorithms and risk models. "
    "Additionally, AI-powered chatbots deliver personalized client support within their digital wealth platform, and "
    "NLP-driven compliance tools automatically flag regulatory issues, improving operational efficiency and reducing risk."
)
review_report = reviewer.assess_response(
    user_query,
    model_answer,
    retrieved_passages,
    stream=True  
)
