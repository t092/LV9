---
name: add-quiz-question
description: 在章節中新增測驗選擇題 (Quiz Question) 的標準流程
---

# 新增測驗題 (Add Quiz Question)

根據本專案的 `AGENTS.md` 規範，要在歷史關卡中新增一個選擇題，請遵循以下步驟：

1. **新增 HTML 結構**:
   - 在章節 HTML 檔案對應關卡的 `.challenge-section` 區塊中，加入新的題目 HTML 結構。
   - 複製且沿用現有的 `.quiz-card` 結構模版。
   - 給定唯一的題目 ID，格式應依循 `{關卡號}-{題號}` 的慣例 (例如 `id="l2-q3"`)。

2. **設定選項與互動事件 (`onclick`)**:
   - 在選擇題的每一個選項 (`.quiz-option`) 中加入行內的點擊事件： `onclick="checkAnswer(this, [true或false], '此題的解釋區塊ID')"`。
   - 確保正確的選項中參數帶入 `true`，錯誤的選項中帶入 `false`。

3. **設定解答與提示區塊**:
   - 在每個題目的下方加入解說區塊： `<div class="quiz-explanation" id="{題目ID}-exp" style="display: none;">`。
   - **務必** 確保解答區塊的 ID 使用 `{quiz-id}-exp` 這個命名慣例 (否則 `checkAnswer` 中的引數會找不到元素)。

4. **註冊至系統進度追蹤 (`app.js`)**:
   - 打開 `app.js`，找到對應的 `levelChallenges` 設定物件。
   - 在該階層的 `quizzes` 屬性陣列中把新的題目 ID 加進去，這樣系統在結算關卡進度與計算最終分數時，遊戲進度條才會正確推展。
