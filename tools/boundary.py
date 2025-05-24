from config import llm

def generate_boundary_test_cases(state: dict) -> dict:
    functional = state["functional"]
    result = llm.invoke(f"基于以下功能用例，添加边界值测试用例：{functional}")
    return {"boundary": result}
