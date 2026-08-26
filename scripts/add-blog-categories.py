#!/usr/bin/env python3
"""Add category filter system to blog/index.html:
1. Tag each article card with data-category
2. Add category tabs (全部 + 8 categories) below header
3. Add vanilla JS filter logic (no Alpine dependency)
"""
import json, re

INDEX = "/mnt/c/Users/hongk/Desktop/esgov/blog/index.html"
CAT_FILE = "/mnt/c/Users/hongk/Desktop/esgov/scripts/blog-categories.json"

cats = json.load(open(CAT_FILE, encoding="utf-8"))
raw = open(INDEX, encoding="utf-8").read()
orig = raw

# Map folder → category
# Card href pattern: /blog/{folder}/
folder_by_href = {}
for folder, info in cats.items():
    folder_by_href[f"/blog/{folder}/"] = info["category"]

# 1. Add data-category to each card <a href="/blog/XXX/">
def add_category(m):
    href = m.group(1)
    cat = folder_by_href.get(href)
    if cat:
        return f'<a href="{href}" data-category="{cat}"'
    return m.group(0)

# Match card open tags: <a href="/blog/中文名/" class="block bg-white rounded-xl...
card_pattern = re.compile(r'<a href="(/blog/[^"]*/)" class="block bg-white rounded-xl(?: border-2 border-gold/30 p-5 hover:shadow-lg hover:border-gold transition-all duration-300 group bg-gold/\[0\.02\]| border border-gray-200 p-5 hover:shadow-lg hover:border-gold/30 transition-all duration-300 group)"')
raw = card_pattern.sub(add_category, raw)

# 2. Count tagged
tagged = len(re.findall(r'<a href="/blog/[^"]*/" data-category="[^"]*"', raw))
print(f"Cards tagged with data-category: {tagged}")

# 3. Insert category tabs + filter JS after <div id="article-list" class="space-y-3">
CATEGORY_TABS = '''
      <!-- ═══ Category Filter ═══ -->
      <div id="category-filter" class="flex flex-wrap gap-2 mb-6">
        <button data-filter="all" class="cat-btn px-4 py-2 rounded-full text-sm font-semibold transition-all duration-200 bg-navy text-white">全部（99）</button>
        <button data-filter="開公司" class="cat-btn px-4 py-2 rounded-full text-sm font-medium transition-all duration-200 bg-white border border-gray-200 text-gray-600 hover:border-gold hover:text-gold">開公司（14）</button>
        <button data-filter="股份" class="cat-btn px-4 py-2 rounded-full text-sm font-medium transition-all duration-200 bg-white border border-gray-200 text-gray-600 hover:border-gold hover:text-gold">股份（10）</button>
        <button data-filter="合規" class="cat-btn px-4 py-2 rounded-full text-sm font-medium transition-all duration-200 bg-white border border-gray-200 text-gray-600 hover:border-gold hover:text-gold">合規（12）</button>
        <button data-filter="董事股東" class="cat-btn px-4 py-2 rounded-full text-sm font-medium transition-all duration-200 bg-white border border-gray-200 text-gray-600 hover:border-gold hover:text-gold">董事股東（13）</button>
        <button data-filter="報稅審計" class="cat-btn px-4 py-2 rounded-full text-sm font-medium transition-all duration-200 bg-white border border-gray-200 text-gray-600 hover:border-gold hover:text-gold">報稅審計（9）</button>
        <button data-filter="人事" class="cat-btn px-4 py-2 rounded-full text-sm font-medium transition-all duration-200 bg-white border border-gray-200 text-gray-600 hover:border-gold hover:text-gold">人事（7）</button>
        <button data-filter="財務保險" class="cat-btn px-4 py-2 rounded-full text-sm font-medium transition-all duration-200 bg-white border border-gray-200 text-gray-600 hover:border-gold hover:text-gold">財務保險（7）</button>
        <button data-filter="公司文件" class="cat-btn px-4 py-2 rounded-full text-sm font-medium transition-all duration-200 bg-white border border-gray-200 text-gray-600 hover:border-gold hover:text-gold">公司文件（27）</button>
      </div>

      <p id="cat-count" class="text-sm text-gray-400 mb-4"></p>

'''

# Insert tabs right after article-list opening
marker = '<div id="article-list" class="space-y-3">'
if marker in raw:
    raw = raw.replace(marker, marker + "\n" + CATEGORY_TABS, 1)
else:
    print("WARN: article-list marker not found")

# 4. Add filter JS before </body>
FILTER_JS = '''
  <script>
    (function() {
      var buttons = document.querySelectorAll('.cat-btn');
      var cards = document.querySelectorAll('#article-list > a[data-category]');
      var countEl = document.getElementById('cat-count');

      function applyFilter(cat) {
        var visible = 0;
        cards.forEach(function(card) {
          var show = (cat === 'all') || (card.getAttribute('data-category') === cat);
          card.style.display = show ? '' : 'none';
          if (show) visible++;
        });
        buttons.forEach(function(b) {
          var active = (b.getAttribute('data-filter') === cat);
          b.className = active
            ? 'cat-btn px-4 py-2 rounded-full text-sm font-semibold transition-all duration-200 bg-navy text-white shadow'
            : 'cat-btn px-4 py-2 rounded-full text-sm font-medium transition-all duration-200 bg-white border border-gray-200 text-gray-600 hover:border-gold hover:text-gold';
        });
        if (countEl) {
          countEl.textContent = cat === 'all'
            ? '顯示全部 ' + visible + ' 篇文章'
            : '「' + cat + '」分類 — ' + visible + ' 篇文章';
        }
      }

      buttons.forEach(function(btn) {
        btn.addEventListener('click', function() {
          applyFilter(btn.getAttribute('data-filter'));
        });
      });

      // Keep the 精選 hub card visible in all views (it has no data-category)
    })();
  </script>
'''

if "</body>" in raw:
    raw = raw.replace("</body>", FILTER_JS + "\n</body>", 1)
else:
    print("WARN: </body> not found")

open(INDEX, "w", encoding="utf-8").write(raw)

# Verify
raw2 = open(INDEX, encoding="utf-8").read()
print(f"Tabs inserted: {'category-filter' in raw2}")
print(f"JS inserted: {'applyFilter' in raw2}")
print(f"Total data-category tags: {len(re.findall(r'data-category=', raw2))}")