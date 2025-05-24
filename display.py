import markdown
import webbrowser
import os
import tempfile

def render_result_to_html(result: dict, requirement: str):
    def render_markdown(text):
        # text 可能是字符串，直接转markdown
        return markdown.markdown(text or "无内容")

    html_content = f"""
    <html>
    <head>
        <meta charset="utf-8">
        <title>AI 测试分析结果</title>
        <style>
            body {{ font-family: 'Arial', sans-serif; padding: 30px; line-height: 1.6; background-color: #f9f9f9; }}
            h1, h2 {{ color: #2c3e50; }}
            h2 {{ border-bottom: 2px solid #eee; padding-bottom: 5px; margin-top: 40px; }}
            .section {{ background-color: #fff; padding: 20px; margin: 20px 0; border-radius: 10px; box-shadow: 0 0 5px rgba(0,0,0,0.1); }}
            pre, code {{ background: #f4f4f4; padding: 8px; border-radius: 4px; display: block; white-space: pre-wrap; }}
            ul {{ padding-left: 20px; }}
        </style>
    </head>
    <body>
        <h1>AI 测试需求分析结果</h1>
        <div class="section">
            <h2>📝 测试需求</h2>
            <p>{requirement}</p>
        </div>
        <div class="section">
            <h2>📊 分析结果</h2>
            {render_markdown(result.get('analysis'))}
        </div>
        <div class="section">
            <h2>✅ 功能测试用例</h2>
            {render_markdown(result.get('functional'))}
        </div>
        <div class="section">
            <h2>🧪 边界值测试用例</h2>
            {render_markdown(result.get('boundary'))}
        </div>
    </body>
    </html>
    """

    # 写临时文件并打开浏览器
    with tempfile.NamedTemporaryFile('w', delete=False, suffix='.html', encoding='utf-8') as f:
        f.write(html_content)
        temp_path = f.name

    webbrowser.open(f"file://{temp_path}")
