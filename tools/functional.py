from config import llm

def generate_functional_test_cases(state: dict) -> dict:
    analysis = state["analysis"]
    result = llm.invoke(f"基于以下测试点，生成功能测试用例：{analysis}")
    return {"functional": result}
