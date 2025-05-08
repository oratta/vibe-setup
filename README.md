# Vibe Coding Documentation Setup Tool

## 名前
vibe-setup

## 概要
vibe-setupは、AI Codingを効率的に行うために必要なドキュメントを自動的にセットアップするためのものです。適切なドキュメントを整備することで、AIがプロジェクトのコンテキストを深く理解し、より効果的なコード生成や問題解決を実現します。
vibe-setupを使うことでAIコーディングツールを使ったコーディングに必要なdocumentを自動生成したり、メンテナンスすることができます。

## Vibe Codingとは
Vibe Codingとは、AIを使ったコーディングの中でも、大きなタスクを自動でLLM（大規模言語モデル）が行うアプローチを指します。単なるコード補完などのペアプログラミングツールとしてのAI Codingではなく、与えられたタスクをLLMが自動でアクションに分解し、動作確認を行いながらタスクを完了まで自動で処理する手法です。

## 主な機能
- プロジェクトのコードベースを自動探索し、必要な情報を収集
- 不足情報がある場合はLLMによるユーザーへのインタラクティブなヒアリングを実施
- AI Codingに最適化されたドキュメント構造の自動生成
- 各種AIコーディングツール(Cursor, windserf, cline, roocode, Claude Code, Claude Desktop等)に対応したルールファイルの生成

## 使い方
1. AI Codingをこれから行うプロジェクト内にvibe-setupをgit cloneします
2. status-check.mdを実行します。

## ディレクトリ構造

```
/
├── plans/
│   ├── master-plan.md
│   ├── phases-overview.md
│   ├── phase3-description.md
│   └── archives/
│       ├── phase1-description.md
│       ├── phase1-implementation-plan.md
│       ├── phase2-description.md
│       └── phase2-implementation-plan.md
├── specs/
│   ├── phase3-implementation-plan.md
│   ├── tech-stack.md
│   ├── stack-knowledge-xx.md
│   ├── stack-knowledge-yy.md
│   ├── directory-structure.md
│   └── in-progress-task.md
└── .vibe-setup/
    ├── prompts/
    │   ├── create-master-plan-prompt.md
    │   ├── create-phases-overview-prompt.md
    │   ├── create-target-phase-prompt.md
    │   ├── create-target-phase-implementation-plan-prompt.md
    │   ├── create-stack-knowledge-prompt.md
    │   └── maintenance-documents-prompt.md
    └── rules/
        ├── global.md
        └── task-management-github.md
```

## 使い方

### フェーズ1：プロンプトベースの利用（現在）
1. `.vibe-setup/prompts/` ディレクトリから目的に合ったプロンプトファイルを選択
2. プロンプトの内容をAIツール（Claude, ChatGPT, Cursor等）にコピー＆ペースト
3. 生成されたドキュメントを適切なディレクトリに配置

### フェーズ2：CLIツールの利用（開発中）
※ 今後実装予定です
1. CLIコマンドを実行してプロジェクト分析を開始
2. 対話式のヒアリングに回答
3. 必要なドキュメントが自動生成される

## ドキュメント構成の詳細

### plans/ ディレクトリ
プロジェクト全体の計画と各フェーズの詳細を記述します。
vibe-setupツールによって作成される
- `master-plan.md`: プロジェクト全体のビジョンと長期計画
- `phases-overview.md`: 開発フェーズの概要と各フェーズの目標
- `phase*-description.md`: 特定のフェーズの詳細説明
- `archives/`: 完了したフェーズの計画書のアーカイブ

### specs/ ディレクトリ
技術仕様と実装計画を管理します。
- `phase*-implementation-plan.md`: 現在のフェーズの実装計画（タスクはGitHub IssuesやLinearで管理）
- `tech-stack.md`: プロジェクトで使用する技術スタックの一覧
- `stack-knowledge-*.md`: 特定の技術スタックに関する詳細情報
- `directory-structure.md`: プロジェクトのディレクトリ構造と各ディレクトリの役割
- `in-progress-task.md`: 現在進行中のタスクの状況と作業メモ

### .vibe-tool/ ディレクトリ
ツール自体の設定とプロンプトを管理します。
- `prompts/`: ドキュメント生成・メンテナンス用のプロンプト
- `rules/`: 各種AIコーディングツールに対応したルールファイル


## ライセンス
現時点では非公開プロジェクトとして管理しています。
