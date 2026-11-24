# Primeiros 14 dias — comece 24/11/2026

Não tente completar todo o cronograma no primeiro dia. Execute o passo de hoje e avance quando souber explicar o que aconteceu.

| Data | Tarefa | Entrega |
|---|---|---|
| 24/11 terça | Criar conta GitHub pessoal, conferir Git/Python/VS Code, descompactar kit, executar app | Programa rodando e 6 testes verdes |
| 25/11 quarta | Aprender commit e push, publicar repo pessoal seguindo guia | Link público do GitHub |
| 26/11 quinta | Ler o código Python e anotar função de cada parte | Notas docs/diario.md |
| 27/11 sexta | Estudar CSV, loops, funções e dicionários; criar 1 job extra fictício | Output correto com novo registro |
| 28/11 sábado | Revisão opcional ou descanso conforme compromissos | Descanso legítimo |
| 29/11 domingo | Descanso e balanço de dúvidas | Planejar próxima semana |
| 30/11 segunda | AZ-104: Entra ID, RBAC, scopes | Resumo RBAC vs Entra Roles |
| 01/12 terça | Python: criar nova regra para jobs RUNNING atrasados | Regra + teste novo |
| 02/12 quarta | AZ-104: resource groups, subscriptions, policies, locks | Mapa visual de governança |
| 03/12 quinta | Git: branch e pull request para a nova regra | Pull request no GitHub |
| 04/12 sexta | Responder 10 questões AZ-104 sobre identidade e governança | Planilha/manual de erros e motivos |
| 05/12 sábado | Revisar README e testar do zero seguindo as instruções | README replicável |
| 06/12 domingo | Descansar | Sem obrigação |
| 07/12 segunda | Planejar laboratório de rede e storage AZ-104 | Issue de projeto e escopo |

## Dia 1 — tutorial completo (60–90 minutos)

1. Entre em https://github.com e crie/confirme sua conta pessoal.
2. Instale VS Code (https://code.visualstudio.com/), Git (https://git-scm.com/downloads) e Python 3.11+ (https://www.python.org/downloads/), se ainda não tiver.
3. Extraia o ZIP para `Documentos\EstudosCloud\` e abra a pasta `azure-ai-cloud-starter` no VS Code.
4. No VS Code selecione `Terminal > New Terminal`.
5. No PowerShell rode `py -3 --version`, `git --version`, depois `py -3 main.py --file samples/execucoes.csv`.
6. Resultado esperado: **5 jobs, 2 normais, 3 alertas**.
7. Rode `py -3 -m unittest discover -s tests -v`. Resultado esperado: **6 testes OK**.
8. Crie `docs/diario.md` com três coisas que aprendeu e duas dúvidas; não precisa postar no LinkedIn já.
9. Se sobrar tempo, faça a introdução ao Git do Microsoft Learn.

Se `py -3` não existir, tente `python`. Não execute comandos em servidores de trabalho.

## Dia 2 — publicar no GitHub

1. Siga `docs/GITHUB_PASSO_A_PASSO.md`.
2. Prefira GitHub Desktop se for a primeira vez com Git.
3. Primeiro confira que os dados são fictícios.
4. Faça commit e publique o repositório.
5. Abra no navegador e confirme se o README está visível.

## Regra de segurança

Nunca publique logs de produção, dados de clientes, credenciais, identificadores de acesso ou scripts corporativos.
