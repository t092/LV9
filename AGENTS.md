# AGENTS.md

This document provides guidelines for AI coding agents working in this codebase.

## Project Overview

This is a static educational game ("Time Traveler - Modern Nation Building") built with vanilla HTML, CSS, and JavaScript. It's an interactive history learning game covering American Independence, French Revolution, Latin American Independence, German Unification, and Italian Unification.

**Tech Stack:** Vanilla HTML5, CSS3, JavaScript (ES6+) - No build tools or frameworks.

## Build/Lint/Test Commands

This project has no build system, package manager, or automated tests. To run:

```bash
# Simply open index.html in a browser
# On Windows:
start index.html

# Or use a simple HTTP server:
npx serve .
# or
python -m http.server 8000
```

No linting or type-checking tools are configured. Manual testing is required by opening the game in a browser and verifying functionality.

## Project Structure

```
/
├── index.html      # Main HTML file with all game screens
├── style.css       # All styles using CSS custom properties
├── app.js          # Game logic, state management, interactions
├── images/         # JPEG images for historical content
└── L01.pdf - L04.pdf  # Reference PDF materials (read-only)
```

## Code Style Guidelines

### JavaScript (app.js)

**State Management:**
- Use the global `state` object pattern for game state
- State object at the top of file contains all mutable game data
- Use `const` for immutable configuration objects (sortData, dragFillData, levelChallenges)

**Function Naming:**
- Use camelCase for all function names
- Event handlers: `checkAnswer()`, `checkSort()`, `checkDragFill()`, `selectMatch()`
- Navigation: `showScreen()`, `goToLevel()`, `startGame()`
- Utilities: `shuffleArray()`, `addScore()`

**Event Handling:**
- Use inline `onclick` attributes in HTML for simplicity (e.g., `onclick="checkAnswer(this, true, 'l1-q1-exp')"`)
- For drag-and-drop, use `addEventListener()` with named handler functions

**DOM Queries:**
- Use `document.getElementById()` for single elements
- Use `document.querySelectorAll()` with `.forEach()` for multiple elements
- Cache DOM references when used repeatedly

**Code Organization:**
- Group related functions with comment headers (e.g., `// ===== QUIZ LOGIC =====`)
- Place initialization code inside `DOMContentLoaded` event
- Keep functions focused and single-purpose

**No Comments in Code:**
- Do not add comments to the code unless explicitly requested

### CSS (style.css)

**Design System:**
- CSS custom properties defined in `:root` for colors, typography, spacing, radius, shadows
- Use semantic color names: `--gold-100` through `--gold-600`, `--emerald`, `--crimson`, etc.
- Font variables: `--font-display` (Noto Serif TC), `--font-ui` (Outfit)

**Selectors:**
- Use BEM-inspired naming: `.quiz-card`, `.quiz-option`, `.quiz-explanation`
- State classes: `.active`, `.show`, `.correct`, `.wrong`, `.matched`, `.dragging`
- Component prefixes: `.btn-`, `.level-`, `.story-`, `.match-`, `.sort-`

**Responsive Design:**
- Mobile-first approach
- Single media query breakpoint at 768px
- Use `clamp()` for fluid typography
- Use CSS Grid and Flexbox for layouts

**Animations:**
- Define `@keyframes` at the end of relevant section
- Use CSS transitions for micro-interactions (0.25s - 0.4s)
- Keep animations subtle and purposeful

### HTML (index.html)

**Document Structure:**
- Use semantic HTML5 elements (`<nav>`, `<section>`, `<button>`)
- Chinese (zh-TW) language attribute on `<html>`
- Include meta description for SEO

**Screen Pattern:**
- Each game screen is a `<div class="screen">` with unique ID (e.g., `id="screen-level-1"`)
- Active screen has `.active` class
- Welcome screen starts as active

**Component IDs:**
- Quiz cards: `l1-q1`, `l1-q2` (level-question format)
- Explanation divs: `l1-q1-exp`
- Sort containers: `l1-sort`, `l1-sort-items`
- Drop zones: `l3-drop-1`, `l3-drop-2`

**Interactive Elements:**
- Quiz options use inline onclick with boolean for correct answer
- Images have `onclick="openLightbox('path', 'caption')"` for lightbox
- Use emoji icons for visual appeal (consistent with existing pattern)

## Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| Functions | camelCase | `checkAnswer`, `goToLevel` |
| CSS classes | kebab-case | `.quiz-card`, `.btn-next-level` |
| IDs | kebab-case with level prefix | `l1-q1`, `l3-drop-1` |
| State properties | camelCase | `totalScore`, `currentLevel` |
| CSS variables | kebab-case with `--` prefix | `--gold-300`, `--space-md` |
| Constants | camelCase | `sortData`, `dragFillData` |

## Error Handling

This is a client-side educational game with minimal error handling needs:
- Functions check for null/undefined before DOM manipulation
- `if (!container) return;` pattern for optional elements
- State tracking prevents duplicate answers (Set-based tracking)
- Wrong answers show visual feedback, correct answer highlighted after delay

## Adding New Content

To add a new quiz question:
1. Add HTML in the appropriate level's `.challenge-section`
2. Follow existing `quiz-card` structure with unique ID
3. Ensure explanation ID matches the pattern `{quiz-id}-exp`
4. Add quiz ID to `levelChallenges` object in app.js

To add new sorting/matching challenges:
1. Add data to `sortData` or `dragFillData` objects
2. Create HTML container with proper IDs
3. Update `levelChallenges` configuration

## Browser Support

Target modern browsers (Chrome, Firefox, Safari, Edge). Uses:
- ES6+ features (const/let, arrow functions, template literals)
- CSS custom properties
- Drag and Drop API
- Touch events for mobile
- No transpilation required

## Testing Checklist

When making changes, manually verify:
1. Game starts correctly from welcome screen
2. Navigation between levels works
3. Quiz questions accept answers and show explanations
4. Sorting games are draggable (desktop and mobile)
5. Drag-fill challenges work correctly
6. Matching games connect properly
7. Progress bar updates
8. Score popups appear
9. Level completion overlay shows
10. Final screen displays correct statistics
11. Lightbox opens/closes for images
