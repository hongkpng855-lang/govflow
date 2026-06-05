#!/bin/bash
# GovFlow Asset Uploader
# 用法：bash upload-asset.sh
# 幫你 upload 文件模板或示範圖片，自動放啱位置 + 更新 processes.json + deploy

set -e

cd "$(dirname "$0")"
PROJECT_DIR="$(pwd)"

echo "╔══════════════════════════════════════╗"
echo "║   GovFlow 資產上傳工具              ║"
echo "║   幫你放好文件 + 自動更新 + 上線     ║"
echo "╚══════════════════════════════════════╝"
echo ""

# ── 選擇類型 ──
echo "你想上傳咩類型嘅文件？"
echo "  1) 📄 Word 模板（.docx）→ templates/"
echo "  2) 🖼️ 示範圖片（.svg/.png/.jpg）→ assets/demo/"
echo "  3) 📂 兩個一齊上傳"
echo ""
read -p "輸入選項 (1/2/3): " TYPE

case "$TYPE" in
  1) UPLOAD_TYPE="template" ;;
  2) UPLOAD_TYPE="demo" ;;
  3) UPLOAD_TYPE="both" ;;
  *) echo "❌ 無效選項"; exit 1 ;;
esac

# ── 選擇步驟 ──
echo ""
echo "邊個步驟嘅文件？"
echo "  1) Step 1 - Sold Note"
echo "  2) Step 2 - Letter of Transferee"
echo "  3) Step 3 - Instrument of Transfer"
echo "  4) Step 4 - Audit Report"
echo "  5) Step 5 - NAR1"
echo "  其他) 自訂名稱"
echo ""
read -p "輸入步驟編號 (1-5) 或按其他鍵自訂: " STEP_NUM

case "$STEP_NUM" in
  1) STEP_NAME="step1-soldnote" ;;
  2) STEP_NAME="step2-transferee-letter" ;;
  3) STEP_NAME="step3-instrument" ;;
  4) STEP_NAME="step4-audit" ;;
  5) STEP_NAME="step5-nar1" ;;
  *)
    read -p "輸入自訂文件名稱（無空格，e.g. annual-return）: " CUSTOM_NAME
    STEP_NAME="$CUSTOM_NAME"
    ;;
esac

# ── 上傳 Template ──
upload_template() {
  echo ""
  read -p "📄 Word 模板檔案路徑（拖放檔案到呢度）: " FILE_PATH
  FILE_PATH="${FILE_PATH#\'}"
  FILE_PATH="${FILE_PATH%\'}"

  if [ ! -f "$FILE_PATH" ]; then
    echo "❌ 檔案唔存在: $FILE_PATH"
    return 1
  fi

  # Get extension
  EXT="${FILE_PATH##*.}"
  DEST="$PROJECT_DIR/templates/${STEP_NAME}.${EXT}"

  cp "$FILE_PATH" "$DEST"
  echo "✅ 已複製到 templates/${STEP_NAME}.${EXT}"

  # Update processes.json if needed
  if command -v python3 &>/dev/null; then
    python3 -c "
import json
with open('$PROJECT_DIR/processes.json') as f:
    d = json.load(f)
updated = False
for s in d.get('steps', []):
    for doc in s.get('documents', []):
        if 'templateFile' in doc and '${STEP_NAME}' in doc['templateFile']:
            doc['templateFile'] = 'templates/${STEP_NAME}.${EXT}'
            updated = True
if updated:
    with open('$PROJECT_DIR/processes.json', 'w') as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    print('✅ processes.json 已更新 template 路徑')
else:
    print('ℹ️ 冇對應嘅步驟，請手動更新 processes.json')
"
  fi
}

# ── 上傳 Demo 圖片 ──
upload_demo() {
  echo ""
  read -p "🖼️ 示範圖片檔案路徑（拖放檔案到呢度）: " FILE_PATH
  FILE_PATH="${FILE_PATH#\'}"
  FILE_PATH="${FILE_PATH%\'}"

  if [ ! -f "$FILE_PATH" ]; then
    echo "❌ 檔案唔存在: $FILE_PATH"
    return 1
  fi

  EXT="${FILE_PATH##*.}"
  DEST="$PROJECT_DIR/assets/demo/${STEP_NAME}.${EXT}"

  cp "$FILE_PATH" "$DEST"
  echo "✅ 已複製到 assets/demo/${STEP_NAME}.${EXT}"

  # Update processes.json
  if command -v python3 &>/dev/null; then
    python3 -c "
import json
with open('$PROJECT_DIR/processes.json') as f:
    d = json.load(f)
updated = False
for s in d.get('steps', []):
    for doc in s.get('documents', []):
        if 'demoImage' in doc and '${STEP_NAME}' in doc['demoImage']:
            doc['demoImage'] = 'assets/demo/${STEP_NAME}.${EXT}'
            updated = True
if updated:
    with open('$PROJECT_DIR/processes.json', 'w') as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    print('✅ processes.json 已更新 demo 路徑')
else:
    print('ℹ️ 冇對應嘅步驟，請手動更新 processes.json')
"
  fi
}

# ── 執行 ──
case "$UPLOAD_TYPE" in
  "template")
    upload_template
    ;;
  "demo")
    upload_demo
    ;;
  "both")
    upload_template
    upload_demo
    ;;
esac

# ── Deploy? ──
echo ""
read -p "🚀 而家 deploy 上線？(y/n): " DEPLOY_NOW
if [ "$DEPLOY_NOW" = "y" ] || [ "$DEPLOY_NOW" = "Y" ]; then
  read -p "Commit message（預設: 更新資產）: " COMMIT_MSG
  COMMIT_MSG="${COMMIT_MSG:-更新資產}"
  bash "$PROJECT_DIR/deploy.sh" "$COMMIT_MSG"
fi

echo ""
echo "✅ 完成！"
