import codecs
import re

with codecs.open("app.js", "r", "utf-8") as f:
    content = f.read()

# 1. Replace the data block
old_data_block = re.search(r'const stepState = \{\};\nconst levelStepCounts = \{ 1: 5, 2: 5, 3: 5, 4: 4, 5: 6 \};\n\n// ===== SORTING DATA ====\n// 排序項目：label = 不含年份的事件名稱, year = 揭示用的年份\nconst sortData = \{[\s\S]*?const completedChallenges = new Set\(\);', content).group(0)

new_data_block = """const stepState = {};
let levelStepCounts = {};
let sortData = {};
let dragFillData = {};
let levelChallenges = {};
let currentChapter = '1';

const allLevelStepCounts = {
  '1': { 1: 5, 2: 5, 3: 5, 4: 4, 5: 6 },
  '2': { 1: 5, 2: 3, 3: 4, 4: 5, 5: 5 }
};

// ===== SORTING DATA =====
const allSortData = {
  '1': {
    l1: {
      items: [
        { id: 1, label: '波士頓茶葉事件', year: '1773 年', order: 1 },
        { id: 2, label: '發表獨立宣言', year: '1776 年', order: 2 },
        { id: 3, label: '英國承認美國獨立', year: '1783 年', order: 3 },
        { id: 4, label: '召開制憲會議', year: '1787 年', order: 4 },
        { id: 5, label: '華盛頓就任首任總統', year: '1789 年', order: 5 },
      ]
    },
    l2: {
      items: [
        { id: 1, label: '攻陷巴士底監獄', year: '1789 年', order: 1 },
        { id: 2, label: '發表人權宣言', year: '1789 年', order: 2 },
        { id: 3, label: '處死路易十六', year: '1793 年', order: 3 },
        { id: 4, label: '拿破崙稱帝', year: '1804 年', order: 4 },
        { id: 5, label: '維也納會議召開', year: '1814 年', order: 5 },
        { id: 6, label: '滑鐵盧之役，拿破崙戰敗', year: '1815 年', order: 6 },
      ]
    },
    l5combined: {
      items: [
        { id: 1, label: '日耳曼邦聯成立', year: '1815 年', order: 1 },
        { id: 2, label: '關稅同盟成立', year: '1834 年', order: 2 },
        { id: 3, label: '義大利王國成立', year: '1861 年', order: 3 },
        { id: 4, label: '普魯士戰勝奧國', year: '1866 年', order: 4 },
        { id: 5, label: '德法戰爭爆發', year: '1870 年', order: 5 },
        { id: 6, label: '收復羅馬，義大利統一完成', year: '1870 年', order: 6 },
        { id: 7, label: '德意志帝國成立', year: '1871 年', order: 7 },
      ]
    }
  },
  '2': {
    'c2-l4': {
      items: [
        { id: 1, label: '塞拉耶佛事件', year: '1914 年', order: 1 },
        { id: 2, label: '大戰全面爆發', year: '1914 年', order: 2 },
        { id: 3, label: '西線陷入壕溝戰僵持', year: '1914-1918 年', order: 3 },
        { id: 4, label: '美國參戰與俄國退出', year: '1917 年', order: 4 },
        { id: 5, label: '德國投降，大戰結束', year: '1918 年', order: 5 }
      ]
    }
  }
};

// ===== DRAG-DROP FILL DATA =====
const allDragFillData = {
  '1': {
    l3: {
      options: ['門羅', '玻利瓦', '華盛頓', '拿破崙'],
      blanks: [
        { id: 'l3-drop-1', answer: '門羅' },
        { id: 'l3-drop-2', answer: '玻利瓦' },
      ]
    }
  },
  '2': {}
};

// ===== LEVEL CHALLENGE TRACKING =====
const allLevelChallenges = {
  '1': {
    1: { quizzes: ['l1-q1', 'l1-q2', 'l1-q3'], sort: 'l1', dragfill: null, match: null, map: null, categorize: null },
    2: { quizzes: ['l2-q1', 'l2-q2', 'l2-q3'], sort: 'l2', dragfill: null, match: null, map: null, categorize: null },
    3: { quizzes: ['l3-q1', 'l3-q2', 'l3-q3'], sort: null, dragfill: 'l3', match: null, map: null, categorize: null },
    4: { quizzes: ['l4-q1', 'l4-q2', 'l4-q3'], sort: null, dragfill: null, match: null, map: null, categorize: null },
    5: { quizzes: ['l5-q1', 'l5-q2', 'l5-q3'], sort: 'l5combined', dragfill: null, match: 'l5', map: null, categorize: null },
  },
  '2': {
    1: { quizzes: ['c2-l1-q1', 'c2-l1-q2', 'c2-l1-q3'], sort: null, dragfill: null, match: null, map: 'c2-l1', categorize: null },
    2: { quizzes: ['c2-l2-q1'], sort: null, dragfill: null, match: null, map: null, categorize: 'c2-l2' },
    3: { quizzes: ['c2-l3-q1', 'c2-l3-q2', 'c2-l3-q3'], sort: null, dragfill: null, match: null, map: null, categorize: null },
    4: { quizzes: ['c2-l4-q1', 'c2-l4-q2', 'c2-l4-q3'], sort: 'c2-l4', dragfill: null, match: null, map: null, categorize: null },
    5: { quizzes: ['c2-l5-q1', 'c2-l5-q2', 'c2-l5-q3'], sort: null, dragfill: null, match: 'c2-l5', map: null, categorize: null },
  }
};

const completedChallenges = new Set();"""

# 2. Replace init block
old_init_block = """// ===== INIT =====
document.addEventListener('DOMContentLoaded', () => {
  initParticles();
  initAllSortItems();
  initAllDragFills();
  state.userName = sessionStorage.getItem('userName') || '時間旅行者';
  state.currentLevel = 1;
  for (let lv = 1; lv <= 5; lv++) {
    stepState[lv] = 1;
    initStepIndicator(lv);
  }
  updateProgress();
});"""

new_init_block = """// ===== INIT =====
document.addEventListener('DOMContentLoaded', () => {
  currentChapter = document.body.getAttribute('data-chapter') || '1';
  levelStepCounts = allLevelStepCounts[currentChapter] || allLevelStepCounts['1'];
  sortData = allSortData[currentChapter] || {};
  dragFillData = allDragFillData[currentChapter] || {};
  levelChallenges = allLevelChallenges[currentChapter] || {};

  initParticles();
  initAllSortItems();
  initAllDragFills();
  initAllMapChallenges();
  initAllCategorizeChallenges();
  
  state.userName = sessionStorage.getItem('userName') || '時間旅行者';
  state.currentLevel = 1;
  for (let lv = 1; lv <= 5; lv++) {
    stepState[lv] = 1;
    initStepIndicator(lv);
  }
  updateProgress();
});"""

# 3. Replace verify Level Complete block
old_check_complete = """  if (challenges.sort && !completedChallenges.has(`${challenges.sort}-sort`)) allDone = false;
  if (challenges.dragfill && !completedChallenges.has(`${challenges.dragfill}-dragfill`)) allDone = false;
  if (challenges.match && !completedChallenges.has(`${challenges.match}-match`)) allDone = false;

  if (allDone) {"""

new_check_complete = """  if (challenges.sort && !completedChallenges.has(`${challenges.sort}-sort`)) allDone = false;
  if (challenges.dragfill && !completedChallenges.has(`${challenges.dragfill}-dragfill`)) allDone = false;
  if (challenges.match && !completedChallenges.has(`${challenges.match}-match`)) allDone = false;
  if (challenges.map && !completedChallenges.has(`${challenges.map}-map`)) allDone = false;
  if (challenges.categorize && !completedChallenges.has(`${challenges.categorize}-categorize`)) allDone = false;

  if (allDone) {"""

# 4. Restart game map reset
old_restart = """  document.querySelectorAll('.match-item').forEach(item => {
    item.classList.remove('matched', 'selected', 'wrong-match');
  });

  Object.keys(matchState).forEach(k => delete matchState[k]);

  initAllSortItems();
  initAllDragFills();"""

new_restart = """  document.querySelectorAll('.match-item').forEach(item => {
    item.classList.remove('matched', 'selected', 'wrong-match');
  });
  
  document.querySelectorAll('.map-drop-zone').forEach(item => {
    item.classList.remove('correct-drop', 'wrong-drop', 'filled');
    let label = '';
    if (item.id === 'map-drop-india') label = '印度';
    if (item.id === 'map-drop-vietnam') label = '越南';
    if (item.id === 'map-drop-indonesia') label = '印尼';
    if (item.id === 'map-drop-philippines') label = '菲律賓';
    item.textContent = label;
    item.setAttribute('data-filled', '');
  });
  
  document.querySelectorAll('.cat-slot').forEach(item => {
    item.classList.remove('filled', 'wrong-drop', 'correct-drop');
    item.textContent = '';
    item.setAttribute('data-filled', '');
  });

  Object.keys(matchState).forEach(k => delete matchState[k]);

  initAllSortItems();
  initAllDragFills();
  initAllMapChallenges();
  initAllCategorizeChallenges();"""

content = content.replace(old_data_block, new_data_block)
content = content.replace(old_init_block, new_init_block)
content = content.replace(old_check_complete, new_check_complete)
content = content.replace(old_restart, new_restart)

# 5. Append new logic for Map and Categorize at EOF
new_logic = """

// ===== MAP DRAG-DROP LOGIC =====
function initAllMapChallenges() {
  const optionsContainers = document.querySelectorAll('.map-challenge-card .drag-options');
  optionsContainers.forEach(container => {
    // Only init if belonging to current chapter
    const levelKey = container.id.replace('-map-options', '');
    if (Object.values(levelChallenges).some(l => l.map === levelKey)) {
      initMapChallenge(levelKey);
    }
  });
}

function initMapChallenge(levelKey) {
  const optionsContainer = document.getElementById(`${levelKey}-map-options`);
  if (!optionsContainer) return;
  optionsContainer.innerHTML = '';
  
  // Custom options for c2-l1
  let options = [];
  if (levelKey === 'c2-l1') {
    options = ['英國', '法國', '荷蘭', '美國'];
  }
  shuffleArray(options);
  
  options.forEach(opt => {
    const chip = document.createElement('div');
    chip.className = 'drag-chip map-chip';
    chip.textContent = opt;
    chip.setAttribute('draggable', 'true');
    chip.setAttribute('data-value', opt);
    
    chip.addEventListener('dragstart', (e) => {
      e.dataTransfer.setData('text/plain', opt);
      chip.classList.add('dragging');
    });
    chip.addEventListener('dragend', () => shipEndDrag(chip));
    chip.addEventListener('click', () => {
      const wasSelected = chip.classList.contains('chip-selected');
      optionsContainer.querySelectorAll('.drag-chip').forEach(c => c.classList.remove('chip-selected'));
      if (!wasSelected) chip.classList.add('chip-selected');
    });
    optionsContainer.appendChild(chip);
  });

  const challengeCard = document.getElementById(`${levelKey}-map`);
  const dropZones = challengeCard.querySelectorAll('.map-drop-zone');
  
  dropZones.forEach(zone => {
    zone.setAttribute('data-filled', '');
    zone.addEventListener('dragover', (e) => {
      e.preventDefault();
      zone.classList.add('drop-hover');
    });
    zone.addEventListener('dragleave', () => {
      zone.classList.remove('drop-hover');
    });
    zone.addEventListener('drop', (e) => {
      e.preventDefault();
      zone.classList.remove('drop-hover');
      const value = e.dataTransfer.getData('text/plain');
      placeMapValue(levelKey, zone, value);
    });
    zone.addEventListener('click', () => {
      const selectedChip = optionsContainer.querySelector('.chip-selected');
      if (selectedChip) {
        placeMapValue(levelKey, zone, selectedChip.getAttribute('data-value'));
        selectedChip.classList.remove('chip-selected');
      } else if (zone.classList.contains('filled')) {
         restoreMapDragChip(levelKey, zone.getAttribute('data-filled'));
         zone.classList.remove('filled', 'correct-drop', 'wrong-drop');
         let label = '';
         if (zone.id === 'map-drop-india') label = '印度';
         if (zone.id === 'map-drop-vietnam') label = '越南';
         if (zone.id === 'map-drop-indonesia') label = '印尼';
         if (zone.id === 'map-drop-philippines') label = '菲律賓';
         zone.textContent = label;
         zone.setAttribute('data-filled', '');
      }
    });
  });
}

function shipEndDrag(chip) {
    chip.classList.remove('dragging');
}

function placeMapValue(levelKey, dropZone, value) {
  if (dropZone.classList.contains('correct-drop')) return;
  const prevValue = dropZone.getAttribute('data-filled');
  if (prevValue) restoreMapDragChip(levelKey, prevValue);
  
  dropZone.textContent = value;
  dropZone.setAttribute('data-filled', value);
  dropZone.classList.add('filled');
  dropZone.classList.remove('wrong-drop');
  
  const chips = document.getElementById(`${levelKey}-map-options`).querySelectorAll('.drag-chip');
  chips.forEach(chip => {
    if (chip.getAttribute('data-value') === value) chip.classList.add('chip-used');
  });
}

function restoreMapDragChip(levelKey, value) {
  const chips = document.getElementById(`${levelKey}-map-options`).querySelectorAll('.drag-chip');
  chips.forEach(chip => {
    if (chip.getAttribute('data-value') === value) chip.classList.remove('chip-used');
  });
}

function checkMapDrag(levelKey) {
  const challengeCard = document.getElementById(`${levelKey}-map`);
  const dropZones = challengeCard.querySelectorAll('.map-drop-zone');
  let allCorrect = true;
  
  dropZones.forEach(zone => {
    const filled = zone.getAttribute('data-filled');
    const answer = zone.getAttribute('data-answer');
    
    if (filled === answer) {
      zone.classList.remove('wrong-drop');
      zone.classList.add('correct-drop');
    } else {
      zone.classList.remove('correct-drop');
      zone.classList.add('wrong-drop');
      allCorrect = false;
      setTimeout(() => {
        zone.classList.remove('wrong-drop', 'filled');
        const prevValue = zone.getAttribute('data-filled');
        if (prevValue) restoreMapDragChip(levelKey, prevValue);
        let label = '';
        if (zone.id === 'map-drop-india') label = '印度';
        if (zone.id === 'map-drop-vietnam') label = '越南';
        if (zone.id === 'map-drop-indonesia') label = '印尼';
        if (zone.id === 'map-drop-philippines') label = '菲律賓';
        zone.textContent = label; 
        zone.setAttribute('data-filled', '');
      }, 1200);
    }
  });

  const challengeId = `${levelKey}-map`;
  if (allCorrect && !completedChallenges.has(challengeId)) {
    completedChallenges.add(challengeId);
    addScore(25, challengeCard);
    state.correctAnswers++;
    checkLevelComplete();
  }
}

// ===== CATEGORIZE DRAG-DROP LOGIC =====
function initAllCategorizeChallenges() {
  const optionsContainers = document.querySelectorAll('.categorize-card .drag-options');
  optionsContainers.forEach(container => {
    const levelKey = container.id.replace('-cat-options', '');
    if (Object.values(levelChallenges).some(l => l.categorize === levelKey)) {
      initCategorizeChallenge(levelKey);
    }
  });
}

function initCategorizeChallenge(levelKey) {
  const optionsContainer = document.getElementById(`${levelKey}-cat-options`);
  if (!optionsContainer) return;
  optionsContainer.innerHTML = '';
  
  let options = [];
  if (levelKey === 'c2-l2') {
    options = ['德國', '英國', '法國', '俄國', '奧匈帝國', '義大利'];
  }
  shuffleArray(options);
  
  options.forEach(opt => {
    const chip = document.createElement('div');
    chip.className = 'drag-chip cat-chip';
    chip.textContent = opt;
    chip.setAttribute('draggable', 'true');
    chip.setAttribute('data-value', opt);
    
    chip.addEventListener('dragstart', (e) => {
      e.dataTransfer.setData('text/plain', opt);
      chip.classList.add('dragging');
    });
    chip.addEventListener('dragend', () => shipEndDrag(chip));
    chip.addEventListener('click', () => {
      const wasSelected = chip.classList.contains('chip-selected');
      optionsContainer.querySelectorAll('.drag-chip').forEach(c => c.classList.remove('chip-selected'));
      if (!wasSelected) chip.classList.add('chip-selected');
    });
    optionsContainer.appendChild(chip);
  });

  const challengeCard = document.getElementById(`${levelKey}-categorize`);
  const dropZones = challengeCard.querySelectorAll('.cat-slot');
  
  dropZones.forEach(zone => {
    zone.setAttribute('data-filled', '');
    zone.addEventListener('dragover', (e) => {
      e.preventDefault();
      if (!zone.classList.contains('filled')) zone.classList.add('drop-hover');
    });
    zone.addEventListener('dragleave', () => {
      zone.classList.remove('drop-hover');
    });
    zone.addEventListener('drop', (e) => {
      e.preventDefault();
      zone.classList.remove('drop-hover');
      const value = e.dataTransfer.getData('text/plain');
      placeCatValue(levelKey, zone, value);
    });
    zone.addEventListener('click', () => {
      const selectedChip = optionsContainer.querySelector('.chip-selected');
      if (selectedChip) {
        placeCatValue(levelKey, zone, selectedChip.getAttribute('data-value'));
        selectedChip.classList.remove('chip-selected');
      } else if (zone.classList.contains('filled')) {
         restoreCatDragChip(levelKey, zone.getAttribute('data-filled'));
         zone.classList.remove('filled', 'correct-drop', 'wrong-drop');
         zone.textContent = '';
         zone.setAttribute('data-filled', '');
      }
    });
  });
}

function placeCatValue(levelKey, zone, value) {
  if (zone.classList.contains('correct-drop')) return;
  if (zone.classList.contains('filled')) return; // Clear first
  
  zone.textContent = value;
  zone.setAttribute('data-filled', value);
  zone.classList.add('filled');
  zone.classList.remove('wrong-drop');
  
  const chips = document.getElementById(`${levelKey}-cat-options`).querySelectorAll('.drag-chip');
  chips.forEach(chip => {
    if (chip.getAttribute('data-value') === value) chip.classList.add('chip-used');
  });
}

function restoreCatDragChip(levelKey, value) {
  const chips = document.getElementById(`${levelKey}-cat-options`).querySelectorAll('.drag-chip');
  chips.forEach(chip => {
    if (chip.getAttribute('data-value') === value) chip.classList.remove('chip-used');
  });
}

function checkCategorization(levelKey) {
  const challengeCard = document.getElementById(`${levelKey}-categorize`);
  const allianceSlots = challengeCard.querySelectorAll('.category-slots[data-type="alliance"] .cat-slot');
  const ententeSlots = challengeCard.querySelectorAll('.category-slots[data-type="entente"] .cat-slot');
  
  let allCorrect = true;
  
  const answers = {
    'alliance': ['德國', '奧匈帝國', '義大利'],
    'entente': ['英國', '法國', '俄國']
  };

  const validateSlots = (slots, correctList) => {
    slots.forEach(slot => {
      const filled = slot.getAttribute('data-filled');
      if (!filled) {
        allCorrect = false;
        slot.classList.add('wrong-drop');
        setTimeout(() => slot.classList.remove('wrong-drop'), 1000);
        return;
      }
      if (correctList.includes(filled)) {
        slot.classList.remove('wrong-drop');
        slot.classList.add('correct-drop');
      } else {
        slot.classList.remove('correct-drop');
        slot.classList.add('wrong-drop');
        allCorrect = false;
        setTimeout(() => {
          slot.classList.remove('wrong-drop', 'filled');
          restoreCatDragChip(levelKey, filled);
          slot.textContent = '';
          slot.setAttribute('data-filled', '');
        }, 1200);
      }
    });
  };

  validateSlots(allianceSlots, answers['alliance']);
  validateSlots(ententeSlots, answers['entente']);

  const challengeId = `${levelKey}-categorize`;
  if (allCorrect && !completedChallenges.has(challengeId)) {
    completedChallenges.add(challengeId);
    addScore(30, challengeCard);
    state.correctAnswers++;
    checkLevelComplete();
  }
}
"""
content += new_logic

with codecs.open("app.js", "w", "utf-8") as f:
    f.write(content)
