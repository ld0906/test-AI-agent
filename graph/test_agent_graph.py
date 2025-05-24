from langgraph.graph import StateGraph
from langchain_core.runnables import RunnableLambda
from tools.analysis import analyze_requirement_for_testing
from tools.functional import generate_functional_test_cases
from tools.boundary import generate_boundary_test_cases
from typing import TypedDict

# 定义状态结构
class TestAgentState(TypedDict):
    requirement: str
    analysis: str
    functional: str
    boundary: str

# 创建 LangGraph 流程
workflow = StateGraph(state_schema=TestAgentState)

# 添加节点
workflow.add_node("analyze_node", RunnableLambda(analyze_requirement_for_testing))
workflow.add_node("functional_node", RunnableLambda(generate_functional_test_cases))
workflow.add_node("boundary_node", RunnableLambda(generate_boundary_test_cases))

# 连接节点
workflow.set_entry_point("analyze_node")
workflow.add_edge("analyze_node", "functional_node")
workflow.add_edge("functional_node", "boundary_node")
workflow.set_finish_point("boundary_node")

# 编译 graph
graph = workflow.compile()
