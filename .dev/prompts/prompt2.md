このプロジェクトで行うことをまとめてREADMEにしたいです。いかにやりたいことを箇条書きにするので、READMEを作る上で不足している情報があれば繰り返し質問を行い必要なすべての情報を聞き出してください。
十分な情報が与えられたと感じた場合にのみREADMEの作成を開始してください。

## プロジェクトでやりたいこと
- AI Codingを行うために必要なドキュメントをセットアップするツールを作成する
- AI Codingを実行するツールはCursor, windserf, cline, roocode, Claude Code, Claude Desktop(desktop commander mcpを利用)を想定している
- ツールを実行すると現在のコードベースを探索して、ドキュメントのセットアップに必要な情報を調べる
- LLMを活用:コードベースをチェックしてもドキュメントのセットアップに必要な情報が足りない場合にユーザへのヒアリングを行いAI Codingに必要なドキュメントを自動作成する
- LLMを活用:ドキュメントを生成したりメンテナンスするためのプロンプトが用意されていて、必要に応じてツールがプロンプトを利用する

## 開発フェーズのイメージ
- 最初は洗練されたプロンプトを作る
- ユーザは与えられたプロンプトをコピペしてドキュメントのセットアップを行う
- ツールの開発初期ではユーザが与えられたプロンプトをコピペして実行することで代替する

## ディレクトリ構造のイメージ
plans/
		- master–plan.md
		- phases-overview.md
		- phase3-description.md
		- archives/
			- phase1-description.md
			- phase1-implementation-plan.md
			- phase2-description.md
			- phase2-implementation-plan.md
	- specs/
		- phase3-implementation-plan.md
			- ここのタスクをすべてlinearかgithub issueで管理する
		- tech-stack.md
		- stask-knowledge-xx.md: 技術スタック毎の最新バージョンの情報
		- stask-knowledge-yy.md
		- directory-structure.md
		- in-progress-task.md
			- 今実行中のタスクの管理
			- linearやgithub issueと同連携するか
			- タスクの作業メモにすればいいんじゃないかな
	- .vibe-tool/
		- prompts/ : ドキュメント整理において実行するプロンプト
			- create-master-plan-prompt.md
			- create-phases-overview.md
			- create-target-phase.md
			- create-target-phase-implementation-plan.md
			- create-stack-knowledge.md
			- maintenance-documents.md
		- rules/: 作業中にCoding Agentが活用するルール
			- global.md
			- task-management.md
				- mcp serverの
			- document-mentenance.md

## QA
1. このツールの主なターゲットユーザーは誰を想定していますか？（例：個人開発者、チーム開発、特定の言語/フレームワークを使う開発者など）
あらゆる開発時にドキュメントを整備することを想定している。IDEを開いて最初にツールを実行してドキュメントを揃える。その後はAI Codingを行う際に、AIはドキュメントのおかげで適切にプロジェクトのコンテキストやタスクの進行状況を把握できるようになる。
要件定義前でも使えるし、要件定義後のプランニングフェーズでも使えるし、開発後でも、メンテナンス作業でも使える。

2. vibe codingという概念について、もう少し詳しく教えていただけますか？AI Codingとの関係性や具体的なメリットなど。
ここいうVibe CodingとはAIを使ったコーディングの中でも大きなタスクを自動でLLMが行うことを指す。
コード保管などのペアプロツールとしてのAI Codingではなくて与えられたタスクをLLMが自動でアクションに分解して、動作確認をしてタスクの完了までやり遂げるようなCoding作業をVibe Codingと呼びます。

3. サポートする言語やフレームワークに制限はありますか？
すべての言語に対応するような汎用的な作りにします。
あくまでAIがプロジェクトのコンテキストを理解するためのドキュメンテーションを行うツールなので、プロジェクトの技術要素がなんであろうと関係なく動作します。

4. ツールの実行方法（CLIツール、GUIアプリ、VSCode拡張など）はどのように考えていますか？
最初はプロンプトのmdファイルがあるだけでユーザがプロンプトを実行してドキュメントをそろえます。
次のフェーズではCLIツールでコマンドを実行するとドキュメントを整理してくれるようにします。この段階ではユーザへのヒアリングや現在のコードベースの探索などが必要なので、LLMを活用したスクリプトを作る必要があります。
このツールを個人利用して有用なものと判断した場合、その次のフェーズでビジネス化します。GUIやMCPサーバーを用意して、ユーザがトークンを購入して使えるようにします。

5.vibe-tool/rules/ の下にあるルールファイルの具体的な内容や目的について、もう少し詳しく教えていただけますか？
vibe-tool/rulesディレクトリは、Cursor, windserf, cline, roocode, Claude Code, Claude Desktop(desktop commander mcpを利用)などのツールに渡すルールファイルを入れます。
ユーザが使うツールに合わせてツールのルールファイルの仕様に応じて、vibe-tool/rulesの下のファイルをコンパイルすることで、どのツールでも同じように動作するようにします。

6. 開発のタイムラインやマイルストーンなどは考えていますか？
最初はプロンプトのmdファイルがあるだけでユーザがプロンプトを実行してドキュメントをそろえます。
次のフェーズではCLIツールでコマンドを実行するとドキュメントを整理してくれるようにします。この段階ではユーザへのヒアリングや現在のコードベースの探索などが必要なので、LLMを活用したスクリプトを作る必要があります。
ここまでをREADMEに記載してください。その後のビジネス展開に関しては記載不要です。