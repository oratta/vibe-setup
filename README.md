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
1. AI Codingをこれから行うプロジェクト内にvibe-setupを.vibe-setupという名前でgit cloneします
2. PROJECT_ROOT/.vibe-setup/prompts/status-check-prompt.mdをAI Codingツールで実行して、その後出力される指示に従うことでAI Codingに必要なドキュメントが作成されます。
3. 必要に応じてPROJECT_ROOT/.vibe-setup/prompts/maintenance-documents-prompt.md AI Codingツールで実行することでドキュメントを最新の状態に保ちます。

### フェーズ2：CLIツールの利用（開発中）
※ 今後実装予定です
1. CLIコマンドを実行してプロジェクト分析を開始
2. 対話式のヒアリングに回答
3. 必要なドキュメントが自動生成される


## vibe-setupが作成するファイルと、ディレクトリ構造

```
/ vibe-setupでドキュメントを作成するプロジェクトルート
├── plans/ : コンテキストを作成するためのプロジェクトの計画
│   ├── master-plan.md: プロジェクト全体のビジョンと長期計画
│   ├── phases-overview.md: 開発フェーズの概要と各フェーズの目標
│   ├── phase3-description.md: 特定のフェーズの詳細説明。現在作業中のフェーズのみplansディレクトリに置く
│   └── archives/: 作業完了済みのフェーズのドキュメントを置く場所
│       ├── phase1-description.md
│       ├── phase1-implementation-plan.md
│       ├── phase2-description.md
│       └── phase2-implementation-plan.md
├── contexts/ : LLMがプロジェクトのコンテキストを把握するために必要なファイルを入れる
│   ├── phase3-implementation-plan.md: 現在のフェーズの実装計画（タスクはGitHub IssuesやLinearで管理）
│   ├── tech-stack.md: プロジェクト全体の技術スタック
│   ├── stack-knowledge-xx.md: 特定の技術スタックに関する情報
│   ├── stack-knowledge-yy.md: 特定の技術スタックに関する情報
│   ├── directory-structure.md: プロジェクトのディレクトリ構成
│   └── in-progress-task.md: 現在進行中のタスクの状況と作業メモ
└── .vibe-setup/: vide-setupディレクトリ
```


## vibe-setupのディレクトリ構造

```
/  (https://github.com/oratta/vibe-setup.git)
├── prompts/
│   ├── status-check-prompt.md
│   ├── create-master-plan-prompt.md
│   ├── create-phases-overview-prompt.md
│   ├── create-target-phase-description-prompt.md
│   ├── create-target-phase-implementation-plan-prompt.md
│   ├── create-stack-knowledge-prompt.md
│   └── maintenance-documents-prompt.md
├── rules/
│   ├── global.md
│   └── task-management-github.md 
│── scripts/
└── .dev/
    ├── prompts/
    └── contexts/

```

### prompt ディレクトリ
ドキュメント生成・メンテナンス用のプロンプトを入れるディレクトリ。
vibeセットアップがドキュメント生成をする対象のプロジェクトルート以下に必要なドキュメントを作成するために使うプロンプト集
- create-master-plan-prompt.md: plans/master-plan.mdを作成するためのプロンプト
- create-phases-overview-prompt.md: plans/phases-overview.md
- create-target-phase-description-prompt.md: plans/phase*-description.mdを作成するためのプロンプト
- create-target-phase-implementation-plan-prompt.md: contexts/phase*-implementation-plan.mdを作成するためのプロンプト
- create-stack-knowledges-prompt.md: stack-knowledge-*.mdを作成するためのプロンプト
- maintenance-documents-prompt.md: ドキュメントをメンテナンスする際に使うプロンプト

### rules ディレクトリ
各種AIコーディングツールのルールファイルに変換される元ファイル。
scripts内のスクリプトで各ツール用のルールファイルに自動で変換される
- global.md: ルール全般
- task-management-github.md: タスク管理に関するルールを記載

### scripts ディレクトリ
各種スクリプトを置くためのディレクトリ


## ライセンス
現時点では非公開プロジェクトとして管理しています。
