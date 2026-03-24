import re

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Step counts
content = content.replace(
    "'2': { 1: 5, 2: 3, 3: 4, 4: 5, 5: 5 }\n};",
    "'2': { 1: 5, 2: 3, 3: 4, 4: 5, 5: 5 },\n  '3': { 1: 3, 2: 3, 3: 3, 4: 4 }\n};"
)

# 2. Sort Data
sort_data_insert = """    }
  },
  '3': {
    'c3-l1': {
      items: [
        { id: 1, label: '二月革命 (推翻沙皇)', year: '1917年3月', order: 1 },
        { id: 2, label: '十月革命 (建立政權)', year: '1917年11月', order: 2 },
        { id: 3, label: '蘇聯正式成立', year: '1922年', order: 3 },
        { id: 4, label: '實施計畫經濟', year: '1928年起', order: 4 }
      ]
    },
    'c3-l2': {
      items: [
        { id: 1, label: '一戰後歐洲衰弱', year: '1', order: 1 },
        { id: 2, label: '美國成為經濟強權', year: '2', order: 2 },
        { id: 3, label: '歐洲逐漸復甦', year: '3', order: 3 },
        { id: 4, label: '美國農工產品面臨供過於求', year: '4', order: 4 },
        { id: 5, label: '美國開啟關稅保護', year: '5', order: 5 },
        { id: 6, label: '各國仿效，形成關稅壁壘', year: '6', order: 6 },
        { id: 7, label: '自由市場不再流動，經濟成一攤死水', year: '7', order: 7 },
        { id: 8, label: '股市崩盤並蔓延全球', year: '8', order: 8 }
      ]
    },
    'c3-l3': {
      items: [
        { id: 1, label: '盧溝橋事變', year: '1937年', order: 1 },
        { id: 2, label: '慕尼黑會議', year: '1938年', order: 2 },
        { id: 3, label: '德國併吞捷克', year: '1939年', order: 3 },
        { id: 4, label: '德蘇互不侵犯條約', year: '1939年', order: 4 },
        { id: 5, label: '德國入侵波蘭', year: '1939年', order: 5 },
        { id: 6, label: '珍珠港事件', year: '1941年', order: 6 },
        { id: 7, label: '開羅會議', year: '1943年', order: 7 },
        { id: 8, label: '諾曼第登陸', year: '1944年', order: 8 },
        { id: 9, label: '雅爾達會議', year: '1945年', order: 9 },
        { id: 10, label: '日本投降', year: '1945年', order: 10 }
      ]
    }
  }
};"""
content = content.replace("    }\n  }\n};", sort_data_insert, 1)

# 3. DragFill Data
drag_fill_insert = """  '2': {},
  '3': {
    'c3-l4': {
      options: ['1914年', '1939年', '1918年', '1945年', '塞拉耶佛事件', '德國入侵波蘭', '同盟國 vs 協約國', '軸心國 vs 同盟國', '國際聯盟', '聯合國'],
      blanks: [
        { id: 'c3-l4-drop-1', answer: '1914年' },
        { id: 'c3-l4-drop-2', answer: '塞拉耶佛事件' },
        { id: 'c3-l4-drop-3', answer: '同盟國 vs 協約國' },
        { id: 'c3-l4-drop-4', answer: '1918年' },
        { id: 'c3-l4-drop-5', answer: '國際聯盟' },
        { id: 'c3-l4-drop-6', answer: '1939年' },
        { id: 'c3-l4-drop-7', answer: '德國入侵波蘭' },
        { id: 'c3-l4-drop-8', answer: '軸心國 vs 同盟國' },
        { id: 'c3-l4-drop-9', answer: '1945年' },
        { id: 'c3-l4-drop-10', answer: '聯合國' }
      ]
    }
  }
};"""
content = content.replace("  '2': {}\n};", drag_fill_insert)

# 4. Level Challenges
level_callenges_insert = """    5: { quizzes: ['c2-l5-q1', 'c2-l5-q2', 'c2-l5-q3'], sort: null, dragfill: null, match: 'c2-l5', map: null, categorize: null },
  },
  '3': {
    1: { quizzes: [], sort: 'c3-l1', dragfill: null, match: 'c3-l1', map: null, categorize: null, multiselect: [] },
    2: { quizzes: [], sort: 'c3-l2', dragfill: null, match: 'c3-l2', map: null, categorize: null, multiselect: [] },
    3: { quizzes: [], sort: 'c3-l3', dragfill: null, match: 'c3-l3', map: null, categorize: null, multiselect: [] },
    4: { quizzes: [], sort: null, dragfill: 'c3-l4', match: 'c3-l4', map: null, categorize: null, multiselect: ['c3-l4-multi1'] }
  }
};"""
content = content.replace("    5: { quizzes: ['c2-l5-q1', 'c2-l5-q2', 'c2-l5-q3'], sort: null, dragfill: null, match: 'c2-l5', map: null, categorize: null },\n  }\n};", level_callenges_insert)

# 5. CheckLevelComplete multiselect check
ch_check = """  if (challenges.match && !completedChallenges.has(`${challenges.match}-match`)) allDone = false;
  if (challenges.map && !completedChallenges.has(`${challenges.map}-map`)) allDone = false;
  if (challenges.categorize && !completedChallenges.has(`${challenges.categorize}-categorize`)) allDone = false;
  if (challenges.multiselect) {
    challenges.multiselect.forEach(mId => {
      if (!completedChallenges.has(mId)) allDone = false;
    });
  }

  if (allDone) {"""
content = content.replace("  if (challenges.match && !completedChallenges.has(`${challenges.match}-match`)) allDone = false;\n  if (challenges.map && !completedChallenges.has(`${challenges.map}-map`)) allDone = false;\n  if (challenges.categorize && !completedChallenges.has(`${challenges.categorize}-categorize`)) allDone = false;\n\n  if (allDone) {", ch_check)

# 6. Init loops and restart
content = content.replace(
    "  for (let lv = 1; lv <= 5; lv++) {",
    "  const numLevels = Object.keys(levelChallenges).length || 5;\n  for (let lv = 1; lv <= numLevels; lv++) {"
)
content = content.replace(
    "const pct = (completed / 5) * 100;",
    "const numLevels = Object.keys(levelChallenges).length || 5;\n  const pct = (completed / numLevels) * 100;"
)

# 7. Level Names
names_replace = """  const allLevelNames = {
    '1': ['美國獨立', '法國大革命', '拉丁美洲獨立', '德國統一', '義大利統一'],
    '2': ['新帝國主義', '戰雲密布', '第一槍與戰火蔓延', '戰局轉折與結束', '巴黎和會與國際聯盟'],
    '3': ['俄國革命與共產政權', '戰間期經濟波動與極權崛起', '二戰的爆發與進程', '大戰終局與全球新秩序']
  };"""
content = content.replace("  const allLevelNames = {\n    '1': ['美國獨立', '法國大革命', '拉丁美洲獨立', '德國統一', '義大利統一'],\n    '2': ['新帝國主義', '戰雲密布', '第一槍與戰火蔓延', '戰局轉折與結束', '巴黎和會與國際聯盟']\n  };", names_replace)

# 8. Add checkMultiSelect function
ms_func = """  checkLevelComplete();
}

// ===== MULTI-SELECT LOGIC =====
function checkMultiSelect(cardId, expectedCorrect) {
  const card = document.getElementById(cardId);
  if (!card) return;
  
  if (state.answeredQuestions.has(cardId)) return;
  
  const checkboxes = card.querySelectorAll('input[type="checkbox"]');
  let userCorrect = [];
  let userWrong = [];
  
  checkboxes.forEach(cb => {
    const parent = cb.closest('.ms-option');
    if (cb.checked) {
      if (expectedCorrect.includes(cb.value)) {
        userCorrect.push(cb);
        parent.classList.add('selected-correct');
      } else {
        userWrong.push(cb);
        parent.classList.add('selected-wrong');
      }
    } else {
      if (expectedCorrect.includes(cb.value)) {
        parent.style.border = "2px dashed var(--gold-400)"; 
      }
    }
    cb.disabled = true;
  });

  const isAllCorrect = (userCorrect.length === expectedCorrect.length && userWrong.length === 0);
  
  if (isAllCorrect) {
    addScore(30, card);
    state.correctAnswers++;
  }
  
  state.answeredQuestions.add(cardId);
  completedChallenges.add(cardId);
  
  const exp = document.getElementById(`${cardId}-exp`);
  if (exp) {
    exp.classList.add('show');
    if (!isAllCorrect) {
      exp.innerHTML = "❌ 答錯囉！黃色虛線框體是這次遺漏的正確項目，紅色則是您多選的項目。";
      exp.style.color = "var(--crimson)";
    } else {
      exp.style.color = "var(--emerald)";
    }
  }
  
  const nextBtn = card.nextElementSibling;
  if (nextBtn && nextBtn.classList.contains('btn-step-next')) {
    nextBtn.style.display = 'inline-block';
  }
  
  checkLevelComplete();
}

// ===== SORTING LOGIC (不顯示年份，確認後再揭示) ====="""
content = content.replace("  checkLevelComplete();\n}\n\n// ===== SORTING LOGIC (不顯示年份，確認後再揭示) =====", ms_func)

# 9. In showLevelComplete, replace iconEl.textContent
content = content.replace("iconEl.textContent = level === 5 ? '🏆' : '🎉';", "iconEl.textContent = (level === allLevelNames[currentChapter].length) ? '🏆' : '🎉';")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(content)
print("app.js patched successfully")
