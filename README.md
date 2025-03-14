# calendario-je
Criação de CSV para google calendar a partir das resoluções eleitorais

# Objetivo
Criar um calendário acessável a partir de aplicativos de calendário para facilitar a identificação dos eventos da Justiça Eleitoral.

# Calendário do Google
Usei minha conta particular do Google, para disponibização pública dos eventos. 
* [Calendário Navegável](https://calendar.google.com/calendar/u/0/embed?src=fabf9fd7b70e772e1b1790e9a71dd386fd8d58bb4c6e75b0fb5eaeb0c538fc3c@group.calendar.google.com&ctz=America/Sao_Paulo)
* [Calendário ICS](https://calendar.google.com/calendar/ical/fabf9fd7b70e772e1b1790e9a71dd386fd8d58bb4c6e75b0fb5eaeb0c538fc3c%40group.calendar.google.com/public/basic.ics)

# Calendários Carregados

## [RESOLUÇÃO Nº 23.737, DE 27 DE FEVEREIRO DE 2024](https://www.tse.jus.br/legislacao/compilada/res/2024/resolucao-no-23-737-de-27-de-fevereiro-de-2024)
Dispõe sobre o cronograma operacional do Cadastro Eleitoral para as Eleições 2024.

Esse foi o mais fácil, pois já tem uma tabela internamente.

Criei a pasta [dados-cronogramas-2024.xlsx] e colei a tabela diretamente numa planilha. Removi as linhas exclusivas para mês e nomeei as colunas conforme o padrão do [Google Calendar](https://support.google.com/calendar/answer/37118?hl=pt-BR&co=GENIE.Platform%3DDesktop#zippy=%2Ccriar-ou-editar-um-arquivo-csv).

Depois foi necessário converter o formato do CSV que no excel em português usa ";" ao invés de ",". Tentei mudar isso de várias formas sugeridas pelo Copilot mas não funcionou. Então parti para a solução usando script python [csv-converter.py] (sugerida pelo Copilot).

Após algumas tentativas e ajuste no formato da planilha e do CSV, deu certo.

## [RESOLUÇÃO Nº 23.736, DE 27 DE FEVEREIRO DE 2024](https://www.tse.jus.br/legislacao/compilada/res/2024/resolucao-no-23-736-de-27-de-fevereiro-de-2024)
Dispõe sobre os atos gerais do processo eleitoral para as eleições municipais de 2024.

Esse eu só consegui importar imprindo um PDF e submentendo ao [Deepseek](chat.deepseek.com).


