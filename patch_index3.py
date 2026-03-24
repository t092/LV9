with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

ch03_card = """      </div>
    </a>

    <a class="chapter-card chapter-available" id="ch03-card" href="#" onclick="enterChapter('ch03.html')">
      <div class="chapter-badge">L11</div>
      <div class="chapter-cover">
        <span class="chapter-emoji">🕊️</span>
      </div>
      <div class="chapter-info">
        <h3 class="chapter-name">戰間期與二戰</h3>
        <p class="chapter-desc">俄國革命、經濟大恐慌、極權崛起、二戰進程、雅爾達會議與戰後秩序</p>
        <div class="chapter-meta">
          <span class="chapter-levels">4 個關卡</span>
          <span class="chapter-status-tag">✅ 可遊玩</span>
        </div>
      </div>
    </a>"""

content = content.replace("      </div>\n    </a>\n\n    <div class=\"chapter-card chapter-locked\">", ch03_card + "\n\n    <div class=\"chapter-card chapter-locked\">")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("index.html patched")
