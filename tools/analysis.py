from config import llm

def analyze_requirement_for_testing(requirement: str) -> dict:
    result = llm.invoke(f"请分析这个需求的测试点：{requirement}")
    return {"analysis": result}