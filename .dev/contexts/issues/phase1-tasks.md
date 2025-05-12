# フェーズ1: プロンプトベースの利用 - 必要な作業内容

ここでは、Vibe Coding Toolのフェーズ1で必要な作業内容をGitHub issueの形式でまとめています。各issueはClaudeが一度のプロンプトで実行可能な単位で分割されています。

## Issue 1: プロジェクトの基本ディレクトリ構造のセットアップ

### 概要
Vibe Codingツールのフェーズ1に必要な基本ディレクトリ構造をセットアップします。

### 作業内容
1. README.mdで定義されている以下のディレクトリ構造を作成する：
   ```
   /
   └── .vibe-setup/
       ├── .dev/
       ├── prompts/
       ├── scripts/
       └── rules/
   ```

2. 各ディレクトリに.gitkeepファイルを作成し、空ディレクトリがGitリポジトリに含まれるようにする

### 受け入れ基準
- すべての必要なディレクトリが作成されている
- ディレクトリ構造がREADME.mdの仕様と一致している
- 空ディレクトリも正しくGitリポジトリに含まれている

## Issue 2: マスタープランドキュメントを作成するプロンプトcreate-master-plan-prompt.mdの作成

### 概要
プロジェクト全体のビジョンと長期計画を記述するマスタープランドキュメントを作成するためのプロンプトcreate-master-plan-prompt.mdを$VIBE_SETUP_ROOT/prompts直下に作成する

### 作業内容
1. `prompts/create-master-plan-prompt.md`ファイルを作成する
2. 以下の内容を含めるようにする：
   - プロジェクトのビジョンと目的
   - 主要な機能と価値提案
   - ターゲットユーザーの説明
   - 各フェーズの開発物のイメージが伝わるようにするためのフェーズの概要
     - PoCフェーズでの技術確認要件
     - vibe codingでAIが作れる単位でフェーズを細かく切ったプロトタイプ板
     - MVP(最初に顧客に試しに使ってもらうバージョン)
     - 現時点で考えているプロダクトの最終形態
3. 以下のプロンプトを参考にすること。ユーザとやり取りをして一緒に決めていくようなプロンプトにしてください。
```
You are a friendly, creative software developer helping me plan my app idea. Your role is to be an active thinking partner - not just asking questions but also offering suggestions, sharing insights, and helping me explore possibilities I might not have considered.

Begin by introducing yourself and explaining that we'll have an interactive conversation about my app idea. After about 15-20 minutes of collaborative brainstorming, you'll create a masterplan.md document that captures our vision.

Start by asking me to describe my app idea. Then engage in a natural back-and-forth conversation where you:

- Ask thoughtful follow-up questions about aspects I mention
- Offer creative suggestions and alternatives ("Have you considered...")
- Share relevant examples from similar apps or services
- Gently challenge assumptions when appropriate
- Suggest features I might not have thought about
- Propose technical approaches in an accessible way
- Periodically summarize what we've discussed to keep us aligned

Make our conversation truly collaborative:
- When I mention a feature, suggest potential enhancements
- If I'm unsure about an approach, offer 2-3 alternatives with simple pros/cons
- When discussing user needs, suggest additional user types or scenarios
- If I mention a technical constraint, offer creative workarounds
- Ask "what if..." questions to expand our thinking

Throughout our brainstorming, guide us to cover:
- Core purpose and key problems being solved
- Target users and their specific needs
- Essential features and potential enhancements
- Unique selling points and differentiators
- Technical considerations and platform choices (identifying preferred tech stack early)
- User experience and interface approaches
- Data needs and management
- Security and privacy considerations
- Scalability and future growth
- Potential challenges and solutions

After our collaborative session, let me know you'll be creating the masterplan. Then produce a masterplan.md that captures our shared vision, including:

- App overview and core purpose
- Target audience profile
- Core features (labeled F1, F2, etc.) including both my ideas and your suggestions
- Technical approach recommendations with clear tech stack choices
- Data requirements
- User experience direction
- Development phases with priorities (clearly indicating which features should be built first)
- Potential challenges and mitigation strategies
- Future expansion possibilities

Present the masterplan.md and ask for my feedback, noting you're happy to refine it based on my input. Remind me to save this document as it will be essential input for Phase 2.

IMPORTANT: Focus on concepts and planning only - no code implementation details should be included.
```

### 受け入れ基準
- `prompts/create-master-plan-prompt.md`をサンプルプロジェクトで使って、マスタープランがプロジェクトの全体像を明確に表現している状態になっていること
- ビジョン、目的、ターゲットユーザーが明確に定義されている
- 開発フェーズの定義が論理的かつ実現可能である

## Issue 3: フェーズ概要ドキュメントの作成

### 概要
開発フェーズの概要と各フェーズの目標を記述するドキュメントを作成します。

### 作業内容
1. `plans/phases-overview.md`ファイルを作成する
2. 以下の内容を含めるようにする：
   - 各開発フェーズの概要説明
   - フェーズごとの目標と重要なマイルストーン
   - フェーズ間の依存関係
   - 各フェーズの予想タイムライン
   - フェーズの移行基準

### 受け入れ基準
- 各フェーズの目標が明確に定義されている
- フェーズ間の依存関係と移行基準が明確である
- 開発ロードマップと一貫性がある

## Issue 4: フェーズ1の詳細説明ドキュメントの作成

### 概要
フェーズ1（プロンプトベースの利用）の詳細を説明するドキュメントを作成します。

### 作業内容
1. `plans/phase1-description.md`ファイルを作成する
2. 以下の内容を含めるようにする：
   - フェーズ1の詳細な目標と範囲
   - プロンプトベースのアプローチの説明
   - ユーザーの利用フロー
   - 必要なリソースと制約
   - 成功基準と測定方法

### 受け入れ基準
- フェーズ1の目標と範囲が明確に定義されている
- プロンプトベースのアプローチが詳細に説明されている
- ユーザーの利用フローが理解しやすく説明されている

## Issue 5: フェーズ1の実装計画ドキュメントの作成

### 概要
フェーズ1の実装計画を詳細に記述するドキュメントを作成します。

### 作業内容
1. `plans/phase1-implementation-plan.md`ファイルを作成する
2. 以下の内容を含めるようにする：
   - 実装するコンポーネントと機能のリスト
   - 各コンポーネントの詳細説明
   - 実装の優先順位
   - 技術的な考慮事項
   - テスト計画

### 受け入れ基準
- 実装すべきコンポーネントと機能が明確にリスト化されている
- 優先順位が明確に設定されている
- テスト計画が含まれている

## Issue 6: 技術スタック説明ドキュメントの作成

### 概要
プロジェクトで使用する技術スタックの一覧と説明を記述するドキュメントを作成します。

### 作業内容
1. `specs/tech-stack.md`ファイルを作成する
2. 以下の内容を含めるようにする：
   - 使用する言語、フレームワーク、ライブラリの一覧
   - 各技術の選定理由
   - 技術スタック間の関係性
   - 将来的な拡張可能性

### 受け入れ基準
- 技術スタックが明確にリスト化され説明されている
- 選定理由が論理的に説明されている
- 技術スタック間の関係性が明確である

## Issue 7: ディレクトリ構造説明ドキュメントの作成

### 概要
プロジェクトのディレクトリ構造と各ディレクトリの役割を説明するドキュメントを作成します。

### 作業内容
1. `specs/directory-structure.md`ファイルを作成する
2. 以下の内容を含めるようにする：
   - 全ディレクトリの階層と構造
   - 各ディレクトリの役割と目的
   - 重要なファイルの説明
   - ファイル命名規則
   - メンテナンスのガイドライン

### 受け入れ基準
- ディレクトリ構造が明確に説明されている
- 各ディレクトリの役割が明確に定義されている
- メンテナンスのガイドラインが含まれている

## Issue 8: マスタープラン作成プロンプトの開発

### 概要
マスタープランを生成するためのプロンプトを開発します。

### 作業内容
1. `.vibe-tool/prompts/create-master-plan-prompt.md`ファイルを作成する
2. 以下の要素を含む効果的なプロンプトを開発する：
   - プロジェクトのコンテキスト分析方法
   - ビジョンと目的の明確化
   - 長期計画の策定方法
   - ターゲットユーザーの特定
   - 価値提案の定義

### 受け入れ基準
- プロンプトが明確で具体的である
- AIが適切なマスタープランを生成できる内容である
- 必要な情報収集のためのガイドが含まれている

## Issue 9: フェーズ概要作成プロンプトの開発

### 概要
開発フェーズの概要を生成するためのプロンプトを開発します。

### 作業内容
1. `.vibe-tool/prompts/create-phases-overview.md`ファイルを作成する
2. 以下の要素を含む効果的なプロンプトを開発する：
   - 開発フェーズの分割方法
   - 各フェーズの目標設定
   - マイルストーンの特定
   - タイムラインの推定
   - フェーズ間の依存関係の分析

### 受け入れ基準
- プロンプトが明確で具体的である
- AIが適切なフェーズ概要を生成できる内容である
- プロジェクトの複雑さに対応できる柔軟性がある

## Issue 10: 特定フェーズ説明作成プロンプトの開発

### 概要
特定のフェーズの詳細説明を生成するためのプロンプトを開発します。

### 作業内容
1. `.vibe-tool/prompts/create-target-phase.md`ファイルを作成する
2. 以下の要素を含む効果的なプロンプトを開発する：
   - フェーズの目標と範囲の定義
   - 必要なリソースの特定
   - 制約条件の分析
   - 成功基準の設定
   - リスクの特定と軽減策

### 受け入れ基準
- プロンプトが明確で具体的である
- AIが特定フェーズの詳細説明を生成できる内容である
- 様々なプロジェクトフェーズに適用可能である

## Issue 11: 実装計画作成プロンプトの開発

### 概要
フェーズの実装計画を生成するためのプロンプトを開発します。

### 作業内容
1. `.vibe-tool/prompts/create-target-phase-implementation-plan.md`ファイルを作成する
2. 以下の要素を含む効果的なプロンプトを開発する：
   - コンポーネントと機能の特定
   - 実装の優先順位付け
   - 技術的考慮事項の分析
   - テスト戦略の策定
   - タスク分解の方法

### 受け入れ基準
- プロンプトが明確で具体的である
- AIが実装可能な計画を生成できる内容である
- 様々な技術スタックに対応できる柔軟性がある

## Issue 12: 技術スタック知識作成プロンプトの開発

### 概要
特定の技術スタックに関する知識ドキュメントを生成するためのプロンプトを開発します。

### 作業内容
1. `.vibe-tool/prompts/create-stack-knowledge.md`ファイルを作成する
2. 以下の要素を含む効果的なプロンプトを開発する：
   - 技術スタックの詳細分析
   - ベストプラクティスの特定
   - 一般的な問題とその解決策
   - パフォーマンス最適化のヒント
   - 技術的な制約と回避策

### 受け入れ基準
- プロンプトが明確で具体的である
- AIが詳細な技術スタック知識を生成できる内容である
- 様々な技術スタックに適用可能である

## Issue 13: ドキュメントメンテナンスプロンプトの開発

### 概要
既存ドキュメントのメンテナンスを支援するためのプロンプトを開発します。

### 作業内容
1. `.vibe-tool/prompts/maintenance-documents.md`ファイルを作成する
2. 以下の要素を含む効果的なプロンプトを開発する：
   - ドキュメント整合性の検証方法
   - 最新情報への更新手順
   - 新しい要件の統合方法
   - ドキュメント間の依存関係の管理
   - バージョン管理の考慮事項

### 受け入れ基準
- プロンプトが明確で具体的である
- AIがドキュメントメンテナンスを効果的に支援できる内容である
- 様々なタイプのドキュメントに適用可能である

## Issue 14: グローバルルールファイルの作成

### 概要
様々なAIコーディングツールに対応するグローバルルールファイルを作成します。

### 作業内容
1. `.vibe-tool/rules/global.md`ファイルを作成する
2. 以下の内容を含めるようにする：
   - すべてのツールに共通するルール
   - コーディングスタイルのガイドライン
   - ドキュメンテーション要件
   - エラー処理の原則
   - セキュリティ考慮事項

### 受け入れ基準
- ルールが明確かつ具体的に定義されている
- 様々なAIコーディングツールに適用可能である
- 一貫したコード品質を確保するのに十分である

## Issue 15: タスク管理ルールファイルの作成

### 概要
AIコーディングツールがタスクを管理するためのルールファイルを作成します。

### 作業内容
1. `.vibe-tool/rules/task-management.md`ファイルを作成する
2. 以下の内容を含めるようにする：
   - タスク分解の原則
   - 優先順位付けの基準
   - 進捗報告のフォーマット
   - ブロッカーの特定と対処方法
   - 完了基準の定義

### 受け入れ基準
- ルールが明確かつ具体的に定義されている
- 効率的なタスク管理を確保するのに十分である
- 様々なタイプのタスクに適用可能である

## Issue 16: ドキュメントメンテナンスルールファイルの作成

### 概要
AIコーディングツールがドキュメントをメンテナンスするためのルールファイルを作成します。

### 作業内容
1. `.vibe-tool/rules/document-maintenance.md`ファイルを作成する
2. 以下の内容を含めるようにする：
   - ドキュメント更新の基準
   - フォーマット要件
   - 一貫性の確保方法
   - 古いドキュメントの処理方法
   - バージョン管理の原則

### 受け入れ基準
- ルールが明確かつ具体的に定義されている
- 効果的なドキュメントメンテナンスを確保するのに十分である
- 様々なタイプのドキュメントに適用可能である
