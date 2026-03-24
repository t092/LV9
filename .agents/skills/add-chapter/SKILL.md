---
name: add-chapter
description: 新增章節 (Chapter) 的標準流程
---

# 新增章節 (Add Chapter)

當需要在「Modern Nation Building」歷史教學遊戲中新增一個章節時，請遵循以下步驟：

1. **建立 HTML 檔案**: 
   - 複製現有的 `ch01.html` 或 `ch02.html` 作為基礎，命名為新的章節名稱 (例如 `ch03.html` 等)。
   - 更新檔案中的 `<title>`、各頁面標題 (`<h1>`、`<h2>`) 等文字與中介資料。
   - 將所有 HTML 結構內的 ID 與關卡卡片更新為新章節的對應層級 (例如將所有 `l2-` 開頭的 ID 替換為 `l3-`)。

2. **更新主導覽頁主選單**:
   - 在首頁 `index.html` 中新增連結至新章節的選單按鈕或章節卡片。

3. **配置圖檔資源**:
   - 將新章節所需的所有圖片放入 `images/` 資料夾中。
   - 確保圖片檔名明確且能在 `<img>` 及 Lightbox 屬性中正確參照。

4. **更新遊戲與互動邏輯 (`app.js`)**:
   - 在 `app.js` 全域的 `levelChallenges` 物件中新增該章節的陣列與設定。
   - 如果有拖曳填空 (Drag and Drop)、排序 (Sort) 或配對 (Match) 遊戲，請同步在 `app.js` 裡的 `sortData` 和 `dragFillData` 常數物件中加入新章節對應的新內容。
