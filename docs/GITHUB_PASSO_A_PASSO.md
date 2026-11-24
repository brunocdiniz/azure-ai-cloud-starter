# GitHub: do zero à primeira publicação

## Entenda as palavras

- **Git:** controla versões do seu projeto.
- **GitHub:** serviço onde pode publicar seus repositórios Git.
- **Repositório:** conjunto de arquivos e seu histórico.
- **Commit:** fotografia de uma alteração.
- **Push:** envio de commits locais para GitHub.
- **Branch:** desenvolvimento isolado de mudanças.
- **Pull Request:** proposta de mudança para revisão.
- **README:** primeira página que apresenta seu projeto.

## Método recomendado: GitHub Desktop (interface gráfica)

1. Crie uma conta pessoal em https://github.com e instale https://desktop.github.com/.
2. Descompacte este kit e escolha no GitHub Desktop **File > Add Local Repository** apontando para a pasta `azure-ai-cloud-starter`.
3. Caso avise que não há repositório Git, siga a opção para criar repositório local com os arquivos existentes.
4. No painel Changes, confira que **não há credenciais nem dados empresariais**.
5. Crie o commit `Initial project - Cloud Ops Log Analyzer`.
6. Escolha **Publish repository**, dê o nome `cloud-ops-log-analyzer`; publique como público apenas após conferência de privacidade.
7. Abra o repositório no navegador: confira README, código, dados fictícios e testes.

## Alternativa: publicar pelo terminal do VS Code

Dentro da pasta do projeto, no PowerShell:

```powershell
git --version
git config --global user.name "Seu Nome"
git config --global user.email "seu-email-noreply-ou-profissional"
git init
git add .
git commit -m "Initial project - Cloud Ops Log Analyzer"
git branch -M main
```

Depois crie um repositório **vazio** em https://github.com/new com o nome `cloud-ops-log-analyzer`. Não selecione README, `.gitignore` ou licença — já estão no projeto local (exceto licença).

```powershell
git remote add origin https://github.com/SEU_USUARIO/cloud-ops-log-analyzer.git
git push -u origin main
```

Substitua `SEU_USUARIO` pelo usuário real do GitHub. Autentique-se por um método oficial do Git/Git Credential Manager. Não forneça senha de conta em páginas suspeitas.

## Atualizações semanais

```powershell
git status
git add .
git commit -m "Add AZ-104 learning notes"
git push
```

Importante: não faça commits de `.env`, chaves de API, segredos, screenshots corporativas, logs reais ou dados de clientes. `gitignore` ajuda, mas **não substitui revisão**.

Guias oficiais: https://docs.github.com/en/get-started/using-git ; https://docs.github.com/en/get-started/start-your-journey/creating-a-repository-for-your-project-on-github
