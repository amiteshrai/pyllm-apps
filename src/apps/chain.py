"""Example Using Language Chains"""

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain_openai.llms import OpenAI

from configs.env_configs import OPENAI_API_KEY

if __name__ == "__main__":
    llm = OpenAI(api_key=OPENAI_API_KEY)

    generator_promt = PromptTemplate(
        template="Write a very short `{language}` function that will `{task}`.",
        input_variables=['language', 'task']
    )

    # This is deprecated and will be removed in the future
    generator_chain = LLMChain(
        llm=llm,
        prompt=generator_promt,
        output_key="code"
    )

    generator_result = generator_chain.invoke({
        "language": "Python",
        "task": "Return the sum of two numbers."
    })
    # print(generator_result)

    tester_promt = PromptTemplate(
        template="Write test cases for the function below in `{language}` code:\n\n{code}",
        input_variables=['language', 'code']
    )

    tester_chain = LLMChain(
        llm=llm,
        prompt=tester_promt,
        output_key="test_cases"
    )

    # Create chains
    chains = SequentialChain(
        chains=[generator_chain, tester_chain],
        input_variables=['language', 'task'],
        output_variables=['code', 'test_cases']
    )

    result = chains.invoke({
        "language": "Python",
        "task": "Return the sum of two numbers."
    })

    for output in ['code', 'test_cases']:
        print(result[output])
