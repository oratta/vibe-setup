import os
import re
from pathlib import Path

# --- 定数 ---
BASE_RULES_DIR = Path(".vibe-setup/rules")
OUTPUT_RULES_DIR = Path("rules")
# 出力ファイル名を変更 (ツール名を含むファイル名に)
# OUTPUT_FILE_NAME = "base.md"

# Markdownのセクションヘッダー (## から始まる行) を検出するための正規表現
# これを使ってファイルをセクションに分割します
SECTION_HEADER_PATTERN_FOR_SPLIT = r'(^## .*$)'
FILE_HEADER_KEY = "___FILE_HEADER___" # ファイル先頭のヘッダーなし部分を示す内部キー

# --- ヘルパー関数 ---

def get_available_tools(rules_dir: Path) -> list[str]:
    """
    指定されたディレクトリから利用可能なAIツールのリストを取得します。
    ツール名は base<ツール名>.md の <ツール名> の部分から抽出されます。
    """
    tool_files = rules_dir.glob("base*.md")
    tools = []
    for f_path in tool_files:
        if f_path.name == "base.md":  # 基本ファイルは除外
            continue
        # ファイル名 "base" と拡張子 ".md" を除いた部分をツール名とする
        tool_name = f_path.name[len("base"):-len(".md")]
        if tool_name:  # ツール名が空でないことを確認
            tools.append(tool_name)
    return sorted(list(set(tools)))  # 重複を除きアルファベット順にソート

def select_tools(available_tools: list[str]) -> list[str]:
    """
    ユーザーに利用可能なAIツールのリストを提示し、使用するツールを選択させます。
    """
    if not available_tools:
        print("利用可能なAIツール設定ファイルが見つかりませんでした。")
        return []

    print("\n利用可能なAIツール:")
    for i, tool in enumerate(available_tools):
        print(f"  {i + 1}. {tool}")

    selected_tools = []
    while True:
        try:
            choices_str = input(
                "使用するツールの番号をカンマ区切りで入力してください (例: 1,3)。\n選択しない場合はそのままEnterキーを押してください: "
            )
            if not choices_str.strip():
                print("ツールは選択されませんでした。")
                break
            
            choices_indices = [int(c.strip()) - 1 for c in choices_str.split(',')]
            
            valid_choices = True
            temp_selected_tools = []
            for index in choices_indices:
                if 0 <= index < len(available_tools):
                    temp_selected_tools.append(available_tools[index])
                else:
                    print(f"無効な番号です: {index + 1}")
                    valid_choices = False
                    break
            
            if valid_choices:
                selected_tools = sorted(list(set(temp_selected_tools))) # 重複を排除しソート
                print(f"選択されたツール: {', '.join(selected_tools)}")
                break
        except ValueError:
            print("無効な入力です。番号をカンマ区切りで、半角数字で入力してください。")
    return selected_tools

def parse_markdown_into_sections_ordered(content: str) -> tuple[list[str], dict[str, str]]:
    """
    Markdownコンテンツをセクションごとの辞書に分割し、ヘッダーの出現順序も返します。
    セクションは "## 見出し" で区切られます。
    "## 見出し" より前の部分は FILE_HEADER_KEY (___FILE_HEADER___) というキーで扱われます。
    """
    sections_dict = {}
    ordered_headers = [] # ヘッダーの出現順を保持

    # re.split で "## 見出し" を区切り文字として分割（区切り文字自体もリストに含まれる）
    parts = re.split(SECTION_HEADER_PATTERN_FOR_SPLIT, content, flags=re.MULTILINE)

    # 最初の部分は "## 見出し" より前のコンテンツ
    first_part = parts[0].strip()
    if first_part:
        sections_dict[FILE_HEADER_KEY] = first_part
        ordered_headers.append(FILE_HEADER_KEY)
    
    # "## 見出し" とその内容を処理
    i = 1
    while i < len(parts):
        header = parts[i].strip()  # "## 見出し"
        i += 1
        section_content_parts = []
        if i < len(parts):
            section_content_parts.append(parts[i].strip()) # 見出しに続く内容
            i += 1
        
        current_content = "\n".join(section_content_parts).strip()

        if header not in sections_dict : # 初めて見るヘッダーの場合
            ordered_headers.append(header)
            sections_dict[header] = current_content
        else: # まれに同じファイル内に重複ヘッダーがある場合、内容を追記
            sections_dict[header] = (sections_dict[header] + "\n\n" + current_content).strip()
            
    return ordered_headers, sections_dict

def merge_rules_by_section_ordered(
    base_ordered_headers: list[str], 
    base_sections: dict[str, str], 
    selected_tools: list[str], 
    rules_dir: Path
) -> str:
    """
    ルールファイルをセクションごとにマージします。
    基本ファイル (base.md) のセクション構造と順序を尊重し、
    ツール固有ファイルの内容を対応するセクションに追記します。
    ツール固有ファイルにしかないセクションは、末尾に新しいセクションとして追加されます。
    """
    merged_sections = {k: v for k, v in base_sections.items()}  # 基本セクションをコピー
    final_ordered_headers = list(base_ordered_headers)  # 最終的なヘッダー順序

    for tool in selected_tools:
        tool_file_path = rules_dir / f"base{tool}.md"
        if tool_file_path.exists():
            print(f"ツール '{tool}' のルールファイル ({tool_file_path.name}) を処理中...")
            with open(tool_file_path, "r", encoding="utf-8") as f:
                tool_content_raw = f.read()
            
            # ツール固有ファイルもセクションに分割
            _tool_ord_headers, tool_sections_map = parse_markdown_into_sections_ordered(tool_content_raw)

            for header_key_from_tool, content_from_tool in tool_sections_map.items():
                if not content_from_tool.strip():  # 空のコンテンツはスキップ
                    continue

                if header_key_from_tool in merged_sections:
                    # 既存セクションに内容を追記（空行を挟んで）
                    merged_sections[header_key_from_tool] = (merged_sections[header_key_from_tool] + "\n\n" + content_from_tool).strip()
                else:
                    # 新しいセクションとして追加
                    merged_sections[header_key_from_tool] = content_from_tool.strip()
                    if header_key_from_tool not in final_ordered_headers: 
                        final_ordered_headers.append(header_key_from_tool)
        else:
            print(f"警告: ツール '{tool}' のルールファイル ({tool_file_path}) が見つかりませんでした。")

    # 最終的な順序に基づいてMarkdown文字列を組み立て
    output_lines = []
    for header_key in final_ordered_headers:
        if header_key in merged_sections and merged_sections[header_key].strip():
            section_content = merged_sections[header_key].strip()
            if header_key == FILE_HEADER_KEY:
                output_lines.append(section_content)
            else:
                # 前のブロックとの間に空行を確保
                if output_lines and output_lines[-1].strip():
                    output_lines.append("") 
                output_lines.append(header_key)  # "## 見出し"
                output_lines.append(section_content) # 見出しの内容
    
    # 各ブロックを2つの改行（1つの空行）で結合し、最後に改行1つを追加
    return "\n\n".join(output_lines).strip() + "\n"


def process_placeholders(content: str) -> str:
    """
    コンテンツ内のプレースホルダー {{placeholder}} を検出し、
    ユーザーに入力を促して置換します。
    """
    # \{\{(.*?)\}\} という正規表現で {{placeholder_name}} 形式のプレースホルダーを全て見つける
    placeholders = sorted(list(set(re.findall(r"\{\{(.*?)\}\}", content)))) 
    
    if not placeholders:
        return content # プレースホルダーがなければ何もしない

    print("\n以下のプレースホルダーの値を入力してください:")
    placeholder_values = {}
    for ph_name in placeholders:
        # 同じプレースホルダー名が複数あっても、質問は一度だけ
        if ph_name in placeholder_values: 
            continue
        
        user_value = ""
        while not user_value.strip(): # 空の入力は許可しない
            user_value = input(f"  {ph_name}: ")
            if not user_value.strip():
                print("値を入力してください。")
        placeholder_values[ph_name] = user_value

    new_content = content
    for ph_name, value in placeholder_values.items():
        new_content = new_content.replace(f"{{{{{ph_name}}}}}", value)
    return new_content

# --- メイン処理 ---
def main():
    print("ルールファイル生成スクリプトを開始します。")

    # 0. スクリプトの実行場所の簡易チェック (ルートディレクトリで実行されているか)
    if not Path(".vibe-setup").is_dir() or not BASE_RULES_DIR.is_dir():
        print(f"エラー: このスクリプトはプロジェクトのルートディレクトリで実行してください。")
        print(f"       必要なディレクトリ (.vibe-setup や {BASE_RULES_DIR}) が見つかりません。")
        return

    # 1. 出力ディレクトリの作成 (存在しない場合)
    try:
        OUTPUT_RULES_DIR.mkdir(parents=True, exist_ok=True)
        print(f"ルールは {OUTPUT_RULES_DIR.resolve()} に出力されます。")
    except OSError as e:
        print(f"エラー: 出力ディレクトリ ({OUTPUT_RULES_DIR}) の作成に失敗しました: {e}")
        return


    # 2. 基本ルールファイル (base.md) の読み込みとセクション分割
    base_md_path = BASE_RULES_DIR / "base.md"
    if not base_md_path.exists():
        print(f"エラー: 基本ルールファイル ({base_md_path}) が見つかりません。")
        return
    
    print(f"基本ルールファイル ({base_md_path.name}) を読み込み中...")
    with open(base_md_path, "r", encoding="utf-8") as f:
        base_content_raw = f.read()
    
    base_ordered_headers, base_sections = parse_markdown_into_sections_ordered(base_content_raw)

    # 3. 利用可能なAIツールの取得とユーザー選択
    available_tools = get_available_tools(BASE_RULES_DIR)
    selected_tools = select_tools(available_tools)

    # 4. ルールのマージ (セクションごと)
    print("\nルールのマージ処理を開始します...")
    merged_content_str = merge_rules_by_section_ordered(
        base_ordered_headers, base_sections, selected_tools, BASE_RULES_DIR
    )

    # 5. プレースホルダーの処理
    final_content = process_placeholders(merged_content_str)

    # 6. マージ・置換された内容を出力ファイルに書き出し
    # 選択されたツール名を結合して出力ファイル名を生成
    if selected_tools:
        # ツールが選択された場合、ツール名を結合したファイル名を使用
        tool_name_combined = "".join(selected_tools)
        output_file_name = f"base{tool_name_combined}.md"
    else:
        # ツールが選択されなかった場合は base.md を使用
        output_file_name = "base.md"
        
    output_file_path = OUTPUT_RULES_DIR / output_file_name
    try:
        with open(output_file_path, "w", encoding="utf-8") as f:
            f.write(final_content)
        print(f"\nルールファイルが正常に生成されました: {output_file_path.resolve()}")
    except IOError as e:
        print(f"エラー: ファイル ({output_file_path}) の書き出しに失敗しました: {e}")


if __name__ == "__main__":
    main() 