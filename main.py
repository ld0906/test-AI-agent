from graph.test_agent_graph import graph
from display import render_result_to_html

def main():
    requirement = "用户可以上传不超过5MB的图片作为头像"
    state = {"requirement": requirement}

    # 调用图，拿到结果（包含 AIMessage 类型）
    result = graph.invoke(state)

    # 提取各部分纯文本内容，避免AIMessage直接传递
    parsed_result = {
        "analysis": getattr(result.get("analysis"), "content", result.get("analysis", "无")),
        "functional": getattr(result.get("functional"), "content", result.get("functional", "无")),
        "boundary": getattr(result.get("boundary"), "content", result.get("boundary", "无")),
    }

    # 生成HTML文件
    render_result_to_html(parsed_result, requirement)

if __name__ == "__main__":
    main()
