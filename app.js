// ===========================
// 時間旅行者 — 互動式歷史教學遊戲
// ===========================

// ===== GAME STATE =====
const state = {
  currentLevel: 0,
  totalScore: 0,
  correctAnswers: 0,
  totalStars: 0,
  levelScores: [0, 0, 0, 0, 0],
  levelCompleted: [false, false, false, false, false],
  answeredQuestions: new Set(),
  userName: '',
};

const stepState = {};
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

const completedChallenges = new Set();

// ===== PARTICLES =====
function initParticles() {
  const canvas = document.getElementById('particles-canvas');
  const ctx = canvas.getContext('2d');
  let particles = [];

  function resize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }
  resize();
  window.addEventListener('resize', resize);

  class Particle {
    constructor() {
      this.reset();
    }
    reset() {
      this.x = Math.random() * canvas.width;
      this.y = Math.random() * canvas.height;
      this.size = Math.random() * 2 + 0.5;
      this.speedX = (Math.random() - 0.5) * 0.3;
      this.speedY = (Math.random() - 0.5) * 0.3;
      this.opacity = Math.random() * 0.4 + 0.1;
    }
    update() {
      this.x += this.speedX;
      this.y += this.speedY;
      if (this.x < 0 || this.x > canvas.width) this.speedX *= -1;
      if (this.y < 0 || this.y > canvas.height) this.speedY *= -1;
    }
    draw() {
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(255, 192, 64, ${this.opacity})`;
      ctx.fill();
    }
  }

  for (let i = 0; i < 60; i++) {
    particles.push(new Particle());
  }

  function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    particles.forEach(p => { p.update(); p.draw(); });
    requestAnimationFrame(animate);
  }
  animate();
}

// ===== INIT =====
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
});

function initStepIndicator(level) {
  const el = document.getElementById(`step-indicator-${level}`);
  if (!el) return;
  const total = levelStepCounts[level];
  let html = '';
  for (let i = 1; i <= total; i++) {
    html += `<span class="step-dot${i === 1 ? ' active' : ''}" data-step="${i}"></span>`;
  }
  el.innerHTML = html;
}

function updateStepIndicator(level) {
  const el = document.getElementById(`step-indicator-${level}`);
  if (!el) return;
  el.querySelectorAll('.step-dot').forEach(dot => {
    const s = parseInt(dot.dataset.step);
    dot.classList.toggle('active', s === stepState[level]);
    dot.classList.toggle('done', s < stepState[level]);
  });
}

function nextStep(level) {
  const current = stepState[level];
  const total = levelStepCounts[level];
  if (current >= total) return;
  const screen = document.getElementById(`screen-level-${level}`);
  if (!screen) return;
  const steps = screen.querySelectorAll('.level-step');
  steps.forEach(s => s.classList.remove('active'));
  stepState[level] = current + 1;
  const nextEl = screen.querySelector(`.level-step[data-step="${stepState[level]}"]`);
  if (nextEl) {
    nextEl.classList.add('active');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
  updateStepIndicator(level);
}

// ===== NAVIGATION =====
function showScreen(screenId) {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  const screen = document.getElementById(screenId);
  if (screen) {
    screen.classList.add('active');
    window.scrollTo({ top: 0, behavior: 'smooth' });
    const levelMatch = screenId.match(/screen-level-(\d+)/);
    if (levelMatch) {
      const lv = parseInt(levelMatch[1]);
      stepState[lv] = 1;
      const steps = screen.querySelectorAll('.level-step');
      steps.forEach(s => s.classList.remove('active'));
      const first = screen.querySelector('.level-step[data-step="1"]');
      if (first) first.classList.add('active');
      initStepIndicator(lv);
    }
  }
}

function goToLevel(level) {
  showLevelComplete(level - 1, () => {
    state.currentLevel = level;
    showScreen(`screen-level-${level}`);
    updateProgress();
  });
}

function showFinalScreen() {
  showLevelComplete(5, () => {
    showScreen('screen-final');
    document.getElementById('final-score').textContent = state.totalScore;
    document.getElementById('final-correct').textContent = state.correctAnswers;
    document.getElementById('final-stars').textContent = state.totalStars;
    document.getElementById('final-username').textContent = state.userName;
    document.getElementById('navbar').style.display = 'none';
    spawnConfetti();
  });
}

function goToPortal() {
  window.location.href = 'index.html';
}

function restartGame() {
  state.currentLevel = 1;
  state.totalScore = 0;
  state.correctAnswers = 0;
  state.totalStars = 0;
  state.levelScores = [0, 0, 0, 0, 0];
  state.levelCompleted = [false, false, false, false, false];
  state.answeredQuestions.clear();
  completedChallenges.clear();

  document.querySelectorAll('.quiz-option').forEach(btn => {
    btn.classList.remove('correct', 'wrong');
    btn.disabled = false;
  });
  document.querySelectorAll('.quiz-explanation').forEach(el => el.classList.remove('show'));
  document.querySelectorAll('.btn-next-level').forEach(btn => btn.classList.remove('show'));

  document.querySelectorAll('.sort-item').forEach(item => {
    item.classList.remove('correct-pos', 'wrong-pos');
  });

  document.querySelectorAll('.match-item').forEach(item => {
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
  initAllCategorizeChallenges();
  document.getElementById('total-score').textContent = '0';
  document.getElementById('progress-fill').style.width = '0%';
  document.getElementById('navbar').style.display = 'flex';
  showScreen('screen-level-1');
}

function updateProgress() {
  const completed = state.levelCompleted.filter(Boolean).length;
  const pct = (completed / 5) * 100;
  document.getElementById('progress-fill').style.width = pct + '%';
  document.getElementById('total-score').textContent = state.totalScore;
}

// ===== QUIZ LOGIC =====
function checkAnswer(button, isCorrect, explanationId) {
  const card = button.closest('.quiz-card');
  const cardId = card.id;

  if (state.answeredQuestions.has(cardId)) return;
  state.answeredQuestions.add(cardId);

  const allOptions = card.querySelectorAll('.quiz-option');
  allOptions.forEach(opt => opt.disabled = true);

  if (isCorrect) {
    button.classList.add('correct');
    addScore(20, button);
    state.correctAnswers++;
  } else {
    button.classList.add('wrong');
    // Find and highlight correct answer
    const correctBtn = Array.from(allOptions).find(opt => {
      const onclickStr = opt.getAttribute('onclick');
      return onclickStr && onclickStr.includes('true');
    });
    if (correctBtn) {
      setTimeout(() => correctBtn.classList.add('correct'), 500);
    }
  }

  // Show explanation
  const exp = document.getElementById(explanationId);
  if (exp) {
    setTimeout(() => exp.classList.add('show'), 300);
  }

  // Mark challenge complete
  completedChallenges.add(cardId);

  // Check if level is complete
  checkLevelComplete();
}

// ===== SORTING LOGIC (不顯示年份，確認後再揭示) =====
function initAllSortItems() {
  Object.keys(sortData).forEach(key => {
    initSortItems(key);
  });
}

function initSortItems(levelKey) {
  const container = document.getElementById(`${levelKey}-sort-items`);
  if (!container) return;

  container.innerHTML = '';

  // Shuffle items
  const items = [...sortData[levelKey].items];
  shuffleArray(items);

  items.forEach(item => {
    const div = document.createElement('div');
    div.className = 'sort-item';
    div.setAttribute('data-order', item.order);
    div.setAttribute('data-year', item.year);
    div.setAttribute('draggable', 'true');
    // 只顯示事件名稱，不顯示年份
    div.innerHTML = `<span class="drag-handle">☰</span> <span class="sort-label">${item.label}</span><span class="sort-year" style="display:none;"> (${item.year})</span>`;

    // Drag events
    div.addEventListener('dragstart', handleDragStart);
    div.addEventListener('dragover', handleDragOver);
    div.addEventListener('drop', handleDrop);
    div.addEventListener('dragend', handleDragEnd);

    // Touch events for mobile
    div.addEventListener('touchstart', handleTouchStart, { passive: false });
    div.addEventListener('touchmove', handleTouchMove, { passive: false });
    div.addEventListener('touchend', handleTouchEnd);

    container.appendChild(div);
  });
}

let dragSrcEl = null;

function handleDragStart(e) {
  dragSrcEl = this;
  this.classList.add('dragging');
  e.dataTransfer.effectAllowed = 'move';
}

function handleDragOver(e) {
  e.preventDefault();
  e.dataTransfer.dropEffect = 'move';
  const container = this.parentNode;
  const siblings = [...container.querySelectorAll('.sort-item:not(.dragging)')];
  const nextSibling = siblings.find(sibling => {
    const rect = sibling.getBoundingClientRect();
    return e.clientY < rect.top + rect.height / 2;
  });
  container.insertBefore(dragSrcEl, nextSibling || null);
}

function handleDrop(e) {
  e.preventDefault();
}

function handleDragEnd() {
  this.classList.remove('dragging');
}

// Touch support
let touchStartY = 0;
let touchCurrentItem = null;

function handleTouchStart(e) {
  touchCurrentItem = this;
  touchStartY = e.touches[0].clientY;
  this.classList.add('dragging');
}

function handleTouchMove(e) {
  e.preventDefault();
  const touchY = e.touches[0].clientY;
  const container = this.parentNode;
  const siblings = [...container.querySelectorAll('.sort-item:not(.dragging)')];
  const nextSibling = siblings.find(sibling => {
    const rect = sibling.getBoundingClientRect();
    return touchY < rect.top + rect.height / 2;
  });
  container.insertBefore(this, nextSibling || null);
}

function handleTouchEnd() {
  this.classList.remove('dragging');
  touchCurrentItem = null;
}

function checkSort(levelKey) {
  const container = document.getElementById(`${levelKey}-sort-items`);
  const items = container.querySelectorAll('.sort-item');
  let allCorrect = true;

  items.forEach((item, index) => {
    const correctOrder = parseInt(item.getAttribute('data-order'));
    // 揭示年份
    const yearSpan = item.querySelector('.sort-year');
    if (yearSpan) yearSpan.style.display = 'inline';

    if (correctOrder === index + 1) {
      item.classList.remove('wrong-pos');
      item.classList.add('correct-pos');
    } else {
      item.classList.remove('correct-pos');
      item.classList.add('wrong-pos');
      allCorrect = false;
    }
  });

  const challengeId = `${levelKey}-sort`;
  if (allCorrect && !completedChallenges.has(challengeId)) {
    completedChallenges.add(challengeId);
    addScore(30, container);
    state.correctAnswers++;
    checkLevelComplete();
  }
}

// ===== DRAG-DROP FILL-IN-BLANK LOGIC =====
function initAllDragFills() {
  Object.keys(dragFillData).forEach(key => {
    initDragFill(key);
  });
}

function initDragFill(levelKey) {
  const data = dragFillData[levelKey];
  if (!data) return;

  const optionsContainer = document.getElementById(`${levelKey}-drag-options`);
  if (!optionsContainer) return;

  optionsContainer.innerHTML = '';

  // Shuffle options
  const options = [...data.options];
  shuffleArray(options);

  options.forEach(opt => {
    const chip = document.createElement('div');
    chip.className = 'drag-chip';
    chip.textContent = opt;
    chip.setAttribute('draggable', 'true');
    chip.setAttribute('data-value', opt);

    chip.addEventListener('dragstart', (e) => {
      e.dataTransfer.setData('text/plain', opt);
      chip.classList.add('dragging');
    });
    chip.addEventListener('dragend', () => {
      chip.classList.remove('dragging');
    });

    // Click to select (for mobile / easier interaction)
    chip.addEventListener('click', () => {
      // Toggle selection
      const wasSelected = chip.classList.contains('chip-selected');
      optionsContainer.querySelectorAll('.drag-chip').forEach(c => c.classList.remove('chip-selected'));
      if (!wasSelected) {
        chip.classList.add('chip-selected');
      }
    });

    optionsContainer.appendChild(chip);
  });

  // Setup drop zones
  data.blanks.forEach(blank => {
    const dropZone = document.getElementById(blank.id);
    if (!dropZone) return;

    dropZone.textContent = '？';
    dropZone.classList.remove('correct-drop', 'wrong-drop', 'filled');
    dropZone.setAttribute('data-answer', blank.answer);
    dropZone.setAttribute('data-filled', '');

    dropZone.addEventListener('dragover', (e) => {
      e.preventDefault();
      dropZone.classList.add('drop-hover');
    });

    dropZone.addEventListener('dragleave', () => {
      dropZone.classList.remove('drop-hover');
    });

    dropZone.addEventListener('drop', (e) => {
      e.preventDefault();
      dropZone.classList.remove('drop-hover');
      const value = e.dataTransfer.getData('text/plain');
      placeFillValue(levelKey, dropZone, value);
    });

    // Click to place selected chip
    dropZone.addEventListener('click', () => {
      const selectedChip = optionsContainer.querySelector('.chip-selected');
      if (selectedChip) {
        const value = selectedChip.getAttribute('data-value');
        placeFillValue(levelKey, dropZone, value);
        selectedChip.classList.remove('chip-selected');
      }
    });
  });
}

function placeFillValue(levelKey, dropZone, value) {
  if (dropZone.classList.contains('correct-drop')) return;

  // Return previous chip if any
  const prevValue = dropZone.getAttribute('data-filled');
  if (prevValue) {
    restoreDragChip(levelKey, prevValue);
  }

  dropZone.textContent = value;
  dropZone.setAttribute('data-filled', value);
  dropZone.classList.add('filled');

  // Hide the used chip
  const optionsContainer = document.getElementById(`${levelKey}-drag-options`);
  const chips = optionsContainer.querySelectorAll('.drag-chip');
  chips.forEach(chip => {
    if (chip.getAttribute('data-value') === value) {
      chip.classList.add('chip-used');
    }
  });
}

function restoreDragChip(levelKey, value) {
  const optionsContainer = document.getElementById(`${levelKey}-drag-options`);
  const chips = optionsContainer.querySelectorAll('.drag-chip');
  chips.forEach(chip => {
    if (chip.getAttribute('data-value') === value) {
      chip.classList.remove('chip-used');
    }
  });
}

function checkDragFill(levelKey) {
  const data = dragFillData[levelKey];
  if (!data) return;

  let allCorrect = true;

  data.blanks.forEach(blank => {
    const dropZone = document.getElementById(blank.id);
    const filled = dropZone.getAttribute('data-filled');

    if (filled === blank.answer) {
      dropZone.classList.remove('wrong-drop');
      dropZone.classList.add('correct-drop');
    } else {
      dropZone.classList.remove('correct-drop');
      dropZone.classList.add('wrong-drop');
      allCorrect = false;
      // Reset wrong answer after delay
      setTimeout(() => {
        dropZone.classList.remove('wrong-drop', 'filled');
        const prevValue = dropZone.getAttribute('data-filled');
        if (prevValue) restoreDragChip(levelKey, prevValue);
        dropZone.textContent = '？';
        dropZone.setAttribute('data-filled', '');
      }, 1200);
    }
  });

  const challengeId = `${levelKey}-dragfill`;
  if (allCorrect && !completedChallenges.has(challengeId)) {
    completedChallenges.add(challengeId);
    addScore(25, document.getElementById(`${levelKey}-fill`));
    state.correctAnswers++;
    checkLevelComplete();
  }
}

// ===== MATCHING LOGIC =====
const matchState = {};

function selectMatch(item, levelKey) {
  if (item.classList.contains('matched')) return;

  if (!matchState[levelKey]) {
    matchState[levelKey] = { selected: null, matchCount: 0, totalPairs: 3 };
  }

  const ms = matchState[levelKey];

  if (!ms.selected) {
    ms.selected = item;
    item.classList.add('selected');
  } else {
    const firstParent = ms.selected.parentNode.id;
    const secondParent = item.parentNode.id;

    if (firstParent === secondParent) {
      ms.selected.classList.remove('selected');
      ms.selected = item;
      item.classList.add('selected');
      return;
    }

    const firstMatch = ms.selected.getAttribute('data-match');
    const secondMatch = item.getAttribute('data-match');

    if (firstMatch === secondMatch) {
      ms.selected.classList.remove('selected');
      ms.selected.classList.add('matched');
      item.classList.add('matched');
      ms.matchCount++;
      ms.selected = null;

      if (ms.matchCount === ms.totalPairs) {
        const challengeId = `${levelKey}-match`;
        if (!completedChallenges.has(challengeId)) {
          completedChallenges.add(challengeId);
          addScore(30, item);
          state.correctAnswers++;
          checkLevelComplete();
        }
      }
    } else {
      ms.selected.classList.add('wrong-match');
      item.classList.add('wrong-match');
      const prevSelected = ms.selected;
      setTimeout(() => {
        prevSelected.classList.remove('selected', 'wrong-match');
        item.classList.remove('wrong-match');
      }, 600);
      ms.selected = null;
    }
  }
}

// ===== SCORE SYSTEM =====
function addScore(points, element) {
  state.totalScore += points;
  const levelIdx = state.currentLevel - 1;
  state.levelScores[levelIdx] += points;
  document.getElementById('total-score').textContent = state.totalScore;

  showScorePopup(points, element);
}

function showScorePopup(points, element) {
  const popup = document.createElement('div');
  popup.className = 'score-popup';
  popup.textContent = `+${points}`;

  const rect = element.getBoundingClientRect();
  popup.style.left = (rect.left + rect.width / 2) + 'px';
  popup.style.top = rect.top + 'px';

  document.body.appendChild(popup);
  setTimeout(() => popup.remove(), 1200);
}

// ===== LEVEL COMPLETION =====
function checkLevelComplete() {
  const level = state.currentLevel;
  const challenges = levelChallenges[level];
  if (!challenges) return;

  let allDone = true;

  challenges.quizzes.forEach(qId => {
    if (!completedChallenges.has(qId)) allDone = false;
  });

  if (challenges.sort && !completedChallenges.has(`${challenges.sort}-sort`)) allDone = false;
  if (challenges.dragfill && !completedChallenges.has(`${challenges.dragfill}-dragfill`)) allDone = false;
  if (challenges.match && !completedChallenges.has(`${challenges.match}-match`)) allDone = false;
  if (challenges.map && !completedChallenges.has(`${challenges.map}-map`)) allDone = false;
  if (challenges.categorize && !completedChallenges.has(`${challenges.categorize}-categorize`)) allDone = false;

  if (allDone) {
    const btn = document.getElementById(`btn-next-${level}`);
    if (btn) btn.classList.add('show');
  }
}

function showLevelComplete(level, callback) {
  if (state.levelCompleted[level - 1]) {
    callback();
    return;
  }

  state.levelCompleted[level - 1] = true;
  updateProgress();

  const overlay = document.getElementById('level-complete-overlay');
  const titleEl = document.getElementById('complete-title');
  const scoreEl = document.getElementById('complete-score');
  const iconEl = document.getElementById('complete-icon');
  const starsContainer = document.getElementById('stars-earned');

  const levelScore = state.levelScores[level - 1];
  const stars = levelScore >= 80 ? 3 : levelScore >= 50 ? 2 : 1;
  state.totalStars += stars;

  const allLevelNames = {
    '1': ['美國獨立', '法國大革命', '拉丁美洲獨立', '德國統一', '義大利統一'],
    '2': ['新帝國主義', '戰雲密布', '第一槍與戰火蔓延', '戰局轉折與結束', '巴黎和會與國際聯盟']
  };
  const levelNames = allLevelNames[currentChapter] || allLevelNames['1'];
  titleEl.textContent = `${levelNames[level - 1]} — 完成！`;
  scoreEl.textContent = `本關得分：${levelScore} 分`;
  iconEl.textContent = level === 5 ? '🏆' : '🎉';

  starsContainer.innerHTML = '';
  for (let i = 0; i < 3; i++) {
    const star = document.createElement('span');
    star.className = 'star';
    star.textContent = i < stars ? '⭐' : '☆';
    star.style.opacity = i < stars ? '1' : '0.3';
    starsContainer.appendChild(star);
  }

  overlay.classList.add('show');

  const btn = document.getElementById('btn-complete-continue');
  btn.onclick = () => {
    overlay.classList.remove('show');
    callback();
  };
}

// ===== LIGHTBOX =====
function openLightbox(src, caption) {
  const lightbox = document.getElementById('lightbox');
  document.getElementById('lightbox-img').src = src;
  document.getElementById('lightbox-caption').textContent = caption;
  lightbox.classList.add('show');
}

function closeLightbox() {
  document.getElementById('lightbox').classList.remove('show');
}

// ===== CONFETTI =====
function spawnConfetti() {
  const colors = ['#ffd060', '#ff9f1c', '#06d6a0', '#118ab2', '#e63946', '#f1faee'];
  for (let i = 0; i < 50; i++) {
    setTimeout(() => {
      const piece = document.createElement('div');
      piece.className = 'confetti-piece';
      piece.style.left = Math.random() * 100 + 'vw';
      piece.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
      piece.style.width = Math.random() * 10 + 5 + 'px';
      piece.style.height = Math.random() * 10 + 5 + 'px';
      piece.style.borderRadius = Math.random() > 0.5 ? '50%' : '2px';
      piece.style.animationDuration = (Math.random() * 2 + 2) + 's';
      piece.style.animationDelay = Math.random() * 0.5 + 's';
      document.body.appendChild(piece);
      setTimeout(() => piece.remove(), 4000);
    }, i * 60);
  }
}

// ===== UTILITIES =====
function shuffleArray(arr) {
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

// ===== MAP DRAG-DROP LOGIC =====
function initAllMapChallenges() {
  const optionsContainers = document.querySelectorAll('.map-challenge-card .drag-options');
  optionsContainers.forEach(container => {
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
