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

Crie uma tabela com TODAS as datas desse documento numa tabela de eventos, 
com uma coluna para um número sequencial da linha, uma coluna para a data no formato "mm/dd/yyyy", outra para o título do assunto, outra coluna com descrição resumida do evento e uma coluna para a hora do evento, se existir.

Aqui está uma tabela com todas as datas e eventos mencionados no documento, organizados em colunas para número sequencial, data, título do assunto, descrição resumida e hora do evento, quando disponível:

| Nº  | Data       | Título do Assunto                                                                 | Descrição Resumida                                                                                     | Hora  |
|-----|------------|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|-------|
| 1   | 10/06/2023 | Acesso antecipado aos sistemas eleitorais                                        | Entidades fiscalizadoras têm acesso antecipado aos sistemas eleitorais para fiscalização e auditoria.   | -     |
| 2   | 11/27/2023 | Início do Teste Público de Segurança da Urna 2023 (TPS)                          | Início do teste de segurança do sistema eletrônico de votação no TSE.                                   | -     |
| 3   | 12/01/2023 | Término do Teste Público de Segurança da Urna 2023 (TPS)                         | Término do teste de segurança do sistema eletrônico de votação no TSE.                                  | -     |
| 4   | 12/15/2023 | Divulgação do resultado do Teste Público de Segurança da Urna 2023 (TPS)         | Divulgação dos resultados do teste de segurança do sistema eletrônico de votação.                       | -     |
| 5   | 12/19/2023 | Designação de juízos eleitorais                                                  | Último dia para designar juízos eleitorais responsáveis por registros de candidaturas e fiscalização.   | -     |
| 6   | 01/01/2024 | Início do registro de pesquisas eleitorais                                       | Início do registro obrigatório de pesquisas eleitorais no sistema PesqEle.                              | -     |
| 7   | 01/01/2024 | Proibição de distribuição gratuita de bens pela Administração Pública            | Proibição de distribuição gratuita de bens, exceto em casos de calamidade pública.                      | -     |
| 8   | 01/01/2024 | Proibição de execução de programas sociais vinculados a candidatos               | Proibição de execução de programas sociais vinculados a candidatos.                                     | -     |
| 9   | 01/01/2024 | Limitação de gastos com publicidade pelos órgãos públicos                        | Limitação de gastos com publicidade pelos órgãos públicos.                                              | -     |
| 10  | 03/05/2024 | Instruções relativas às eleições municipais de 2024                              | Data-limite para o TSE expedir instruções relativas às eleições municipais de 2024.                     | -     |
| 11  | 03/07/2024 | Justa causa para desfiliação partidária                                          | Mudança de partido para concorrer a cargo de prefeito ou vereador é considerada justa causa.           | -     |
| 12  | 04/01/2024 | Propaganda institucional para incentivar participação política                   | Início da propaganda institucional para incentivar participação feminina, jovem e negra na política.    | -     |
| 13  | 04/05/2024 | Término do período de justa causa para desfiliação partidária                    | Término do período em que mudança de partido é considerada justa causa.                                | -     |
| 14  | 04/06/2024 | Data-limite para registro de estatutos de partidos políticos                     | Último dia para registro de estatutos de partidos políticos e federações para as eleições de 2024.      | -     |
| 15  | 04/06/2024 | Data-limite para filiação partidária e domicílio eleitoral                       | Último dia para candidatos estarem filiados e com domicílio eleitoral no município onde desejam concorrer. | -     |
| 16  | 04/06/2024 | Data-limite para renúncia de mandatos                                            | Último dia para presidentes, governadores e prefeitos renunciarem aos mandatos para concorrer a outros cargos. | -     |
| 17  | 04/08/2024 | Último dia para solicitação de operações eleitorais via autoatendimento          | Último dia para solicitação de alistamento, transferência e revisão eleitoral via internet.             | -     |
| 18  | 04/09/2024 | Último dia para publicação de normas partidárias                                 | Último dia para partidos publicarem normas para escolha de candidatos e formação de coligações.         | -     |
| 19  | 04/09/2024 | Proibição de revisão geral de remuneração de servidores públicos                 | Proibição de revisão geral de remuneração de servidores públicos durante o período eleitoral.           | -     |
| 20  | 05/08/2024 | Último dia para recebimento de solicitações eleitorais                           | Último dia para recebimento de solicitações de alistamento, transferência e revisão eleitoral.          | -     |
| 21  | 05/09/2024 | Suspensão de solicitações eleitorais                                             | Suspensão de solicitações de alistamento, transferência e revisão eleitoral até 5 de novembro de 2024.  | -     |
| 22  | 05/15/2024 | Teste de Confirmação das correções do TPS                                        | Realização do teste de confirmação das correções aplicadas após o TPS.                                 | -     |
| 23  | 05/15/2024 | Início da arrecadação prévia de recursos via financiamento coletivo              | Início da arrecadação prévia de recursos via financiamento coletivo para campanhas eleitorais.          | -     |
| 24  | 05/17/2024 | Término do Teste de Confirmação das correções do TPS                             | Término do teste de confirmação das correções aplicadas após o TPS.                                     | -     |
| 25  | 06/03/2024 | Início do período de prioridade postal para propaganda eleitoral                  | Início do período de prioridade postal para envio de material de propaganda eleitoral.                   | -     |
| 26  | 07/08/2024 | Último dia para publicação de edital de mesários e apoio logístico               | Último dia para publicação de edital com nomes de mesários e apoio logístico para as eleições.          | -     |
| 27  | 07/12/2024 | Início do prazo para cadastramento de agregação de seções eleitorais             | Início do prazo para cadastramento de agregação de seções eleitorais.                                   | -     |
| 28  | 07/16/2024 | Divulgação de comunicados e instruções ao eleitorado                             | Início da divulgação de comunicados e instruções ao eleitorado via rádio e TV.                          | -     |
| 29  | 07/19/2024 | Data-limite para criação de novos locais de votação                              | Data-limite para criação de novos locais de votação em estabelecimentos penais e unidades de internação. | -     |
| 30  | 07/20/2024 | Início das convenções partidárias para escolha de candidatos                     | Início das convenções partidárias para escolha de candidatos a prefeito, vice-prefeito e vereador.      | -     |
| 31  | 07/26/2024 | Último dia para publicação de edital de juntas eleitorais                        | Último dia para publicação de edital com nomes de integrantes das juntas eleitorais.                    | -     |
| 32  | 07/30/2024 | Término da propaganda institucional                                              | Término da propaganda institucional para incentivar participação política.                              | -     |
| 33  | 08/04/2024 | Término da propaganda intrapartidária                                            | Término da propaganda intrapartidária para indicação de nomes para candidaturas.                        | -     |
| 34  | 08/05/2024 | Último dia para realização de convenções partidárias                             | Último dia para realização de convenções partidárias para escolha de candidatos.                        | -     |
| 35  | 08/06/2024 | Proibição de transmissão de pesquisas eleitorais                                 | Proibição de transmissão de pesquisas eleitorais em rádio e TV.                                         | -     |
| 36  | 08/07/2024 | Último dia para publicação de edital de mesários e apoio logístico               | Último dia para publicação de edital com nomes de mesários e apoio logístico para as eleições.          | -     |
| 37  | 08/13/2024 | Publicação da tabela de representação partidária                                 | Publicação da tabela de representação partidária para divisão do tempo de propaganda eleitoral.         | -     |
| 38  | 08/15/2024 | Último dia para registro de candidaturas                                         | Último dia para registro de candidaturas a prefeito, vice-prefeito e vereador.                          | -     |
| 39  | 08/15/2024 | Último dia para envio de relação de contas rejeitadas                            | Último dia para envio de relação de contas rejeitadas por irregularidades.                              | -     |
| 40  | 08/15/2024 | Abertura de cartórios eleitorais aos sábados, domingos e feriados                | Abertura de cartórios eleitorais aos sábados, domingos e feriados durante o período eleitoral.          | -     |
| 41  | 08/16/2024 | Início da propaganda eleitoral                                                   | Início da propaganda eleitoral, inclusive na internet.                                                  | -     |
| 42  | 08/17/2024 | Data-limite para informar veículos para transporte de eleitores                  | Data-limite para informar veículos disponíveis para transporte de eleitores.                            | -     |
| 43  | 08/20/2024 | Divulgação de percentuais de candidaturas femininas e negras                     | Divulgação de percentuais de candidaturas femininas e negras por partido político.                      | -     |
| 44  | 08/22/2024 | Último dia para habilitação de eleitores para votar em seção distinta            | Último dia para habilitação de eleitores para votar em seção distinta dentro do mesmo município.        | -     |
| 45  | 08/23/2024 | Último dia para distribuição de atribuições entre emissoras                      | Último dia para distribuição de atribuições entre emissoras para propaganda eleitoral.                  | -     |
| 46  | 08/25/2024 | Data-limite para elaboração de plano de mídia                                    | Data-limite para elaboração de plano de mídia para uso do horário eleitoral gratuito.                   | -     |
| 47  | 08/27/2024 | Último dia para indicação de membros da Comissão de Transporte                   | Último dia para indicação de membros da Comissão Especial de Transporte para as eleições.               | -     |
| 48  | 08/28/2024 | Último dia para indicação de pessoas autorizadas a entregar mapas e mídias       | Último dia para indicação de pessoas autorizadas a entregar mapas e mídias para propaganda eleitoral.   | -     |
| 49  | 08/29/2024 | Último dia para agregação de seções eleitorais                                   | Último dia para agregação de seções eleitorais pelas zonas eleitorais.                                  | -     |
| 50  | 08/30/2024 | Último dia para publicação de edital de mesários                                 | Último dia para publicação de edital com nomes de mesários para as eleições.                            | -     |
| 51  | 08/30/2024 | Início da propaganda eleitoral gratuita no rádio e TV                            | Início da propaganda eleitoral gratuita no rádio e TV para o primeiro turno.                            | -     |
| 52  | 09/01/2024 | Homologação de programas de verificação de sistemas eleitorais                   | Homologação de programas de verificação de sistemas eleitorais pelas entidades fiscalizadoras.          | -     |
| 53  | 09/02/2024 | Último dia para agregação de seções pelos TREs                                   | Último dia para agregação de seções eleitorais pelos tribunais regionais eleitorais.                    | -     |
| 54  | 09/03/2024 | Disponibilização de consulta à seção de votação                                  | Disponibilização de consulta à seção de votação atualizada no e-Título ou na internet.                  | -     |
| 55  | 09/06/2024 | Último dia para preenchimento de vagas remanescentes para vereador               | Último dia para preenchimento de vagas remanescentes para candidaturas a vereador.                      | -     |
| 56  | 09/06/2024 | Último dia para designação de escrutinadores e auxiliares                        | Último dia para designação de escrutinadores e auxiliares para as eleições.                             | -     |
| 57  | 09/06/2024 | Último dia para instalação da Comissão de Transporte                             | Último dia para instalação da Comissão Especial de Transporte para as eleições.                         | -     |
| 58  | 09/06/2024 | Último dia para planejamento de transporte de eleitores                          | Último dia para planejamento de transporte de eleitores para as eleições.                               | -     |
| 59  | 09/06/2024 | Convocação de entidades fiscalizadoras para assinatura digital                   | Convocação de entidades fiscalizadoras para assinatura digital dos programas eleitorais.                | -     |
| 60  | 09/09/2024 | Início do envio de prestação parcial de contas                                   | Início do envio de prestação parcial de contas das campanhas eleitorais.                                | -     |
| 61  | 09/11/2024 | Último dia para apresentação de certificado digital                              | Último dia para apresentação de certificado digital por entidades fiscalizadoras.                       | -     |
| 62  | 09/13/2024 | Último dia para envio de prestação parcial de contas                             | Último dia para envio de prestação parcial de contas das campanhas eleitorais.                          | -     |
| 63  | 09/14/2024 | Último dia para comunicação de anulações de deliberações                         | Último dia para comunicação de anulações de deliberações de convenções partidárias.                    | -     |
| 64  | 09/15/2024 | Divulgação de prestação parcial de contas                                        | Divulgação de prestação parcial de contas das campanhas eleitorais na internet.                         | -     |
| 65  | 09/16/2024 | Data-limite para julgamento de pedidos de registro de candidaturas               | Data-limite para julgamento de pedidos de registro de candidaturas pelas instâncias ordinárias.         | -     |
| 66  | 09/16/2024 | Último dia para substituição de candidatos                                       | Último dia para substituição de candidatos, exceto em caso de falecimento.                              | -     |
| 67  | 09/16/2024 | Último dia para escolha ou sorteio de seções para auditoria                      | Último dia para escolha ou sorteio de seções para auditoria da votação eletrônica.                      | -     |
| 68  | 09/16/2024 | Lacração dos sistemas eleitorais                                                 | Lacração dos sistemas eleitorais e programas de verificação pelas entidades fiscalizadoras.             | -     |
| 69  | 09/21/2024 | Proibição de detenção de candidatos                                              | Proibição de detenção de candidatos, exceto em flagrante delito.                                        | -     |
| 70  | 09/21/2024 | Requisição de servidores e instalações para transporte de eleitores              | Requisição de servidores e instalações para transporte de eleitores para as eleições.                   | -     |
| 71  | 09/21/2024 | Divulgação de quadro geral de percursos e horários de transporte                 | Divulgação de quadro geral de percursos e horários de transporte de eleitores.                          | -     |
| 72  | 09/26/2024 | Ações de esclarecimento sobre o voto                                             | Realização de ações para esclarecer a população sobre o voto.                                           | -     |
| 73  | 09/26/2024 | Definição de locais para Testes de Integridade com Biometria                     | Definição de locais para realização de Testes de Integridade com Biometria.                             | -     |
| 74  | 09/30/2024 | Último dia para registro de pesquisas eleitorais                                 | Último dia para registro de pesquisas eleitorais realizadas antes do dia das eleições.                 | -     |
| 75  | 10/01/2024 | Proibição de detenção de eleitores                                               | Proibição de detenção de eleitores, exceto em flagrante delito.                                         | -     |
| 76  | 10/01/2024 | Designação de horário e local para verificação de sistemas                       | Designação de horário e local para verificação de sistemas Transportador e JE-Connect.                 | -     |
| 77  | 10/03/2024 | Término da propaganda eleitoral gratuita no rádio e TV                           | Término da propaganda eleitoral gratuita no rádio e TV para o primeiro turno.                          | -     |
| 78  | 10/03/2024 | Término de comícios e uso de sonorização fixa                                    | Término de comícios e uso de sonorização fixa, exceto comício de encerramento.                         | -     |
| 79  | 10/03/2024 | Término de debates no rádio e TV                                                 | Término de debates no rádio e TV, admitida extensão até 7h do dia 4 de outubro.                        | -     |
| 80  | 10/03/2024 | Expedição de salvo-conduto para eleitores                                        | Expedição de salvo-conduto para eleitores que sofrerem violência moral ou física.                       | -     |
| 81  | 10/03/2024 | Divulgação de comunicados e instruções ao eleitorado                             | Divulgação de comunicados e instruções ao eleitorado via rádio e TV.                                    | -     |
| 82  | 10/03/2024 | Término de circulação paga de propaganda eleitoral na internet                   | Término de circulação paga de propaganda eleitoral na internet.                                         | -     |
| 83  | 10/04/2024 | Término de divulgação paga de propaganda na imprensa escrita                     | Término de divulgação paga de propaganda na imprensa escrita e reprodução na internet.                 | -     |
| 84  | 10/04/2024 | Audiência para verificação de sistemas                                           | Audiência para verificação de integridade e autenticidade dos sistemas Transportador e JE-Connect.     | -     |
| 85  | 10/04/2024 | Comunicação de nomes de fiscais e delegados                                      | Comunicação de nomes de fiscais e delegados habilitados a fiscalizar as eleições.                      | -     |
| 86  | 10/05/2024 | Término de uso de alto-falantes e amplificadores de som                          | Término de uso de alto-falantes e amplificadores de som para campanhas eleitorais.                     | -     |
| 87  | 10/05/2024 | Término de distribuição de material gráfico e passeatas                          | Término de distribuição de material gráfico e realização de passeatas.                                  | -     |
| 88  | 10/05/2024 | Escolha ou sorteio de seções para auditoria                                      | Escolha ou sorteio de seções para auditoria da votação eletrônica.                                      | -     |
| 89  | 10/05/2024 | Verificação de sistemas de totalização                                           | Verificação de sistemas de totalização (SISTOT, RecBU, InfoArquivos e Transportador WEB).              | -     |
| 90  | 10/05/2024 | Divulgação de comunicados e instruções ao eleitorado                             | Divulgação de comunicados e instruções ao eleitorado via rádio e TV.                                    | -     |
| 91  | 10/05/2024 | Proibição de transporte de armas e munições                                      | Proibição de transporte de armas e munições por colecionadores, atiradores e caçadores.                | -     |
| 92  | 10/06/2024 | Dia das Eleições (1º turno)                                                      | Realização da votação do primeiro turno das eleições.                                                   | 7:00  |
| 93  | 10/06/2024 | Instalação da seção eleitoral                                                    | Instalação da seção eleitoral e emissão dos Relatórios Zerésima e Resumo da Zerésima.                  | 7:00  |
| 94  | 10/06/2024 | Início da votação                                                                | Início da votação no primeiro turno das eleições.                                                       | 8:00  |
| 95  | 10/06/2024 | Encerramento da votação                                                          | Encerramento da votação no primeiro turno das eleições.                                                 | 17:00 |
| 96  | 10/06/2024 | Emissão dos boletins de urna                                                     | Emissão dos boletins de urna após o encerramento da votação.                                            | 17:00 |
| 97  | 10/06/2024 | Funcionamento das Mesas Receptoras de Justificativa                              | Funcionamento das Mesas Receptoras de Justificativa.                                                    | 8:00-17:00 |
| 98  | 10/06/2024 | Teste de Integridade das Urnas Eletrônicas                                       | Realização do Teste de Integridade das Urnas Eletrônicas em ambiente controlado.                       | -     |
| 99  | 10/06/2024 | Verificação de autenticidade e integridade dos sistemas                          | Verificação de autenticidade e integridade dos sistemas instalados nas urnas.                          | 7:00  |
| 100 | 10/06/2024 | Atualização de arquivos de correspondências e logs                               | Atualização de arquivos de correspondências e logs do sistema GEDAI-UE.                                | 16:00 |
| 101 | 10/06/2024 | Divulgação dos resultados da votação                                             | Divulgação dos resultados da votação, incluindo votos em branco, nulos e abstenções.                   | 17:00 |
| 102 | 10/07/2024 | Reinício de uso de alto-falantes e amplificadores de som                         | Reinício de uso de alto-falantes e amplificadores de som para campanhas eleitorais.                    | -     |
| 103 | 10/07/2024 | Reinício de comícios e uso de sonorização fixa                                   | Reinício de comícios e uso de sonorização fixa, exceto comício de encerramento.                        | -     |
| 104 | 10/07/2024 | Reinício de distribuição de material gráfico e passeatas                         | Reinício de distribuição de material gráfico e realização de passeatas.                                | -     |
| 105 | 10/07/2024 | Reinício de divulgação paga de propaganda na imprensa escrita                    | Reinício de divulgação paga de propaganda na imprensa escrita e reprodução na internet.                | -     |
| 106 | 10/07/2024 | Reinício de circulação paga de propaganda eleitoral na internet                  | Reinício de circulação paga de propaganda eleitoral na internet.                                        | -     |
| 107 | 10/07/2024 | Requerimento de veiculação de propaganda em rede                                 | Requerimento de veiculação de propaganda em rede por partidos políticos.                               | -     |
| 108 | 10/07/2024 | Informação de locais para auditorias de urnas                                    | Informação de locais para auditorias de funcionamento das urnas no segundo turno.                      | -     |
| 109 | 10/07/2024 | Comunicação sobre escolha ou sorteio de seções para auditoria                    | Comunicação sobre escolha ou sorteio de seções para auditoria no segundo turno.                        | -     |
| 110 | 10/07/2024 | Solicitação de arquivos de log e dados para auditoria                            | Solicitação de arquivos de log e dados para auditoria pelas entidades fiscalizadoras.                  | -     |
| 111 | 10/07/2024 | Proibição de transporte de armas e munições                                      | Proibição de transporte de armas e munições por colecionadores, atiradores e caçadores.                | -     |
| 112 | 10/08/2024 | Término da validade de salvo-conduto                                             | Término da validade de salvo-conduto expedido para eleitores.                                           | -     |
| 113 | 10/08/2024 | Término do período de proibição de detenção de eleitores                         | Término do período de proibição de detenção de eleitores.                                               | -     |
| 114 | 10/09/2024 | Último dia para justificativa de mesários                                        | Último dia para mesários que abandonaram os trabalhos apresentarem justificativa.                      | -     |
| 115 | 10/11/2024 | Início da propaganda eleitoral gratuita no rádio e TV (2º turno)                 | Início da propaganda eleitoral gratuita no rádio e TV para o segundo turno.                            | -     |
| 116 | 10/11/2024 | Envio de relatório conclusivo de auditoria                                       | Envio de relatório conclusivo de auditoria de funcionamento das urnas no primeiro turno.               | -     |
| 117 | 10/12/2024 | Funcionamento de cartórios eleitorais                                            | Funcionamento de cartórios eleitorais em municípios sem segundo turno.                                 | -     |
| 118 | 10/12/2024 | Proibição de detenção de candidatos                                              | Proibição de detenção de candidatos, exceto em flagrante delito.                                        | -     |
| 119 | 10/14/2024 | Reinício da emissão de certidão de quitação eleitoral                            | Reinício da emissão de certidão de quitação eleitoral pela internet.                                    | -     |
| 120 | 10/15/2024 | Envio de notas fiscais eletrônicas                                               | Envio de notas fiscais eletrônicas relativas a campanhas eleitorais.                                   | -     |
| 121 | 10/15/2024 | Envio de identificação de permissionários de serviço público                    | Envio de identificação de permissionários de serviço público.                                          | -     |
| 122 | 10/17/2024 | Definição de locais para Testes de Integridade com Biometria (2º turno)          | Definição de locais para realização de Testes de Integridade com Biometria no segundo turno.            | -     |
| 123 | 10/19/2024 | Término da disponibilidade de dados de resultados                                | Término da disponibilidade de dados de resultados do primeiro turno.                                   | -     |
| 124 | 10/21/2024 | Último dia para registro de pesquisas eleitorais (2º turno)                      | Último dia para registro de pesquisas eleitorais realizadas antes do segundo turno.                    | -     |
| 125 | 10/22/2024 | Proibição de detenção de eleitores (2º turno)                                    | Proibição de detenção de eleitores, exceto em flagrante delito.                                         | -     |
| 126 | 10/22/2024 | Designação de horário e local para verificação de sistemas (2º turno)            | Designação de horário e local para verificação de sistemas Transportador e JE-Connect no segundo turno. | -     |
| 127 | 10/24/2024 | Término de comícios e uso de sonorização fixa (2º turno)                         | Término de comícios e uso de sonorização fixa, exceto comício de encerramento.                         | -     |
| 128 | 10/24/2024 | Término de debates no rádio e TV (2º turno)                                      | Término de debates no rádio e TV, admitida extensão até 24h.                                            | -     |
| 129 | 10/24/2024 | Expedição de salvo-conduto para eleitores (2º turno)                             | Expedição de salvo-conduto para eleitores que sofrerem violência moral ou física.                       | -     |
| 130 | 10/24/2024 | Término de circulação paga de propaganda eleitoral na internet (2º turno)        | Término de circulação paga de propaganda eleitoral na internet.                                         | -     |
| 131 | 10/25/2024 | Término da propaganda eleitoral gratuita no rádio e TV (2º turno)                | Término da propaganda eleitoral gratuita no rádio e TV para o segundo turno.                            | -     |
| 132 | 10/25/2024 | Término de divulgação paga de propaganda na imprensa escrita (2º turno)          | Término de divulgação paga de propaganda na imprensa escrita e reprodução na internet.                 | -     |
| 133 | 10/25/2024 | Audiência para verificação de sistemas (2º turno)                                | Audiência para verificação de integridade e autenticidade dos sistemas Transportador e JE-Connect.      | -     |
| 134 | 10/25/2024 | Comunicação de nomes de fiscais e delegados (2º turno)                           | Comunicação de nomes de fiscais e delegados habilitados a fiscalizar as eleições.                       | -     |
| 135 | 10/26/2024 | Término de uso de alto-falantes e amplificadores de som (2º turno)               | Término de uso de alto-falantes e amplificadores de som para campanhas eleitorais.                     | -     |
| 136 | 10/26/2024 | Término de distribuição de material gráfico e passeatas (2º turno)               | Término de distribuição de material gráfico e realização de passeatas.                                  | -     |
| 137 | 10/26/2024 | Escolha ou sorteio de seções para auditoria (2º turno)                           | Escolha ou sorteio de seções para auditoria da votação eletrônica.                                      | -     |
| 138 | 10/26/2024 | Verificação de sistemas de totalização (2º turno)                                | Verificação de sistemas de totalização (SISTOT, RecBU, InfoArquivos e Transportador WEB).              | -     |
| 139 | 10/26/2024 | Divulgação de comunicados e instruções ao eleitorado (2º turno)                  | Divulgação de comunicados e instruções ao eleitorado via rádio e TV.                                    | -     |
| 140 | 10/26/2024 | Proibição de transporte de armas e munições (2º turno)                           | Proibição de transporte de armas e munições por colecionadores, atiradores e caçadores.                | -     |
| 141 | 10/27/2024 | Dia das Eleições (2º turno)                                                      | Realização da votação do segundo turno das eleições.                                                    | 7:00  |
| 142 | 10/27/2024 | Instalação da seção eleitoral (2º turno)                                         | Instalação da seção eleitoral e emissão dos Relatórios Zerésima e Resumo da Zerésima.                  | 7:00  |
| 143 | 10/27/2024 | Início da votação (2º turno)                                                     | Início da votação no segundo turno das eleições.                                                        | 8:00  |
| 144 | 10/27/2024 | Encerramento da votação (2º turno)                                               | Encerramento da votação no segundo turno das eleições.                                                  | 17:00 |
| 145 | 10/27/2024 | Emissão dos boletins de urna (2º turno)                                          | Emissão dos boletins de urna após o encerramento da votação.                                            | 17:00 |
| 146 | 10/27/2024 | Funcionamento das Mesas Receptoras de Justificativa (2º turno)                   | Funcionamento das Mesas Receptoras de Justificativa.                                                    | 8:00-17:00 |
| 147 | 10/27/2024 | Teste de Integridade das Urnas Eletrônicas (2º turno)                            | Realização do Teste de Integridade das Urnas Eletrônicas em ambiente controlado.                       | -     |
| 148 | 10/27/2024 | Verificação de autenticidade e integridade dos sistemas (2º turno)               | Verificação de autenticidade e integridade dos sistemas instalados nas urnas.                          | 7:00  |
| 149 | 10/27/2024 | Atualização de arquivos de correspondências e logs (2º turno)                    | Atualização de arquivos de correspondências e logs do sistema GEDAI-UE.                                | 16:00 |
| 150 | 10/27/2024 | Divulgação dos resultados da votação (2º turno)                                  | Divulgação dos resultados da votação, incluindo votos em branco, nulos e abstenções.                   | 17:00 |
| 151 | 10/28/2024 | Solicitação de arquivos de log e dados para auditoria (2º turno)                 | Solicitação de arquivos de log e dados para auditoria pelas entidades fiscalizadoras.                  | -     |
| 152 | 10/28/2024 | Proibição de transporte de armas e munições (2º turno)                           | Proibição de transporte de armas e munições por colecionadores, atiradores e caçadores.                | -     |
| 153 | 10/28/2024 | Suspensão de fornecimento de certidão de quitação eleitoral                      | Suspensão de fornecimento de certidão de quitação eleitoral pela internet.                              | -     |
| 154 | 10/28/2024 | Publicação de relatórios finais de pesquisas eleitorais                          | Publicação de relatórios finais de pesquisas eleitorais, salvo determinação da Justiça Eleitoral.      | -     |
| 155 | 10/29/2024 | Término da validade de salvo-conduto (2º turno)                                  | Término da validade de salvo-conduto expedido para eleitores.                                           | -     |
| 156 | 10/29/2024 | Término do período de proibição de detenção de eleitores (2º turno)              | Término do período de proibição de detenção de eleitores.                                               | -     |
| 157 | 10/30/2024 | Último dia para justificativa de mesários (2º turno)                             | Último dia para mesários que abandonaram os trabalhos apresentarem justificativa.                      | -     |
| 158 | 11/01/2024 | Envio de relatório conclusivo de auditoria (2º turno)                            | Envio de relatório conclusivo de auditoria de funcionamento das urnas no segundo turno.                | -     |
| 159 | 11/01/2024 | Término de prioridade para processos eleitorais                                  | Término de prioridade para processos eleitorais, exceto habeas corpus e mandado de segurança.          | -     |
| 160 | 11/01/2024 | Término de auxílio de órgãos públicos na apuração de delitos eleitorais          | Término de auxílio de órgãos públicos na apuração de delitos eleitorais.                                | -     |
| 161 | 11/05/2024 | Envio de prestações de contas referentes ao primeiro turno                       | Envio de prestações de contas referentes ao primeiro turno das eleições.                                | -     |
| 162 | 11/05/2024 | Transferência de sobras de campanha                                              | Transferência de sobras de campanha ao órgão partidário.                                                | -     |
| 163 | 11/05/2024 | Transferência de valores não utilizados do FEFC                                  | Transferência de valores não utilizados do Fundo Especial de Financiamento de Campanha ao Tesouro Nacional. | -     |
| 164 | 11/05/2024 | Remoção de propagandas do primeiro turno                                         | Remoção de propagandas do primeiro turno e restauração de bens afixados.                               | -     |
| 165 | 11/05/2024 | Justificativa de mesários que não compareceram                                   | Justificativa de mesários que não compareceram aos trabalhos no primeiro turno.                        | -     |
| 166 | 11/05/2024 | Reinício da emissão de certidão de quitação eleitoral                            | Reinício da emissão de certidão de quitação eleitoral pela internet.                                    | -     |
| 167 | 11/05/2024 | Reinício do atendimento nas unidades da Justiça Eleitoral                        | Reinício do atendimento nas unidades da Justiça Eleitoral.                                              | -     |
| 168 | 11/05/2024 | Reativação do serviço de pré-atendimento                                         | Reativação do serviço de pré-atendimento para alistamento, transferência e revisão eleitoral.          | -     |
| 169 | 11/08/2024 | Identificação de candidatos e partidos que omitiram prestação de contas          | Identificação de candidatos e partidos que omitiram prestação de contas no primeiro turno.             | -     |
| 170 | 11/08/2024 | Término da disponibilidade de dados de resultados (2º turno)                     | Término da disponibilidade de dados de resultados do segundo turno.                                     | -     |
| 171 | 11/10/2024 | Envio de notas fiscais eletrônicas complementares                                | Envio de notas fiscais eletrônicas complementares relativas a campanhas eleitorais.                    | -     |
| 172 | 11/10/2024 | Envio de identificação de permissionários de serviço público complementar        | Envio de identificação de permissionários de serviço público complementar.                             | -     |
| 173 | 11/11/2024 | Funcionamento de cartórios eleitorais (2º turno)                                 | Funcionamento de cartórios eleitorais em municípios com segundo turno.                                 | -     |
| 174 | 11/11/2024 | Término de publicação de decisões em representações                              | Término de publicação de decisões em representações sobre propaganda eleitoral e direito de resposta.  | -     |
| 175 | 11/16/2024 | Envio de prestações de contas referentes ao segundo turno                        | Envio de prestações de contas referentes ao segundo turno das eleições.                                | -     |
| 176 | 11/16/2024 | Transferência de sobras de campanha (2º turno)                                   | Transferência de sobras de campanha ao órgão partidário no segundo turno.                              | -     |
| 177 | 11/16/2024 | Transferência de valores não utilizados do FEFC (2º turno)                       | Transferência de valores não utilizados do Fundo Especial de Financiamento de Campanha ao Tesouro Nacional. | -     |
| 178 | 11/19/2024 | Identificação de candidatos e partidos que omitiram prestação de contas (2º turno)| Identificação de candidatos e partidos que omitiram prestação de contas no segundo turno.              | -     |
| 179 | 11/26/2024 | Remoção de propagandas do segundo turno                                          | Remoção de propagandas do segundo turno e restauração de bens afixados.                                | -     |
| 180 | 11/26/2024 | Justificativa de mesários que não compareceram (2º turno)                        | Justificativa de mesários que não compareceram aos trabalhos no segundo turno.                         | -     |
| 181 | 12/05/2024 | Último dia para justificativa de falta ao primeiro turno                         | Último dia para eleitores justificarem falta ao primeiro turno.                                         | -     |
| 182 | 12/11/2024 | Lançamento de informações de justificativa no Cadastro Eleitoral                 | Lançamento de informações de justificativa no Cadastro Eleitoral.                                       | -     |
| 183 | 12/16/2024 | Publicação de decisões sobre contas de candidatos eleitos                        | Publicação de decisões sobre contas de candidatos eleitos.                                              | -     |
| 184 | 12/19/2024 | Diplomação das eleitas e eleitos                                                | Último dia para diplomação das eleitas e eleitos.                                                      | -     |
| 185 | 12/19/2024 | Término de abertura de cartórios eleitorais aos sábados, domingos e feriados     | Término de abertura de cartórios eleitorais aos sábados, domingos e feriados.                          | -     |
| 186 | 12/19/2024 | Término de atuação de juízes auxiliares                                          | Término de atuação de juízes auxiliares nos tribunais eleitorais.                                      | -     |
| 187 | 12/19/2024 | Término de contagem contínua de prazos processuais                               | Término de contagem contínua de prazos processuais relativos às eleições de 2024.                      | -     |
| 188 | 12/19/2024 | Término de uso de mural eletrônico e mensagens eletrônicas                       | Término de uso de mural eletrônico e mensagens eletrônicas para comunicações da Justiça Eleitoral.     | -     |
| 189 | 12/19/2024 | Término de intimação eletrônica do Ministério Público                            | Término de intimação eletrônica do Ministério Público em processos eleitorais.                         | -     |
| 190 | 12/19/2024 | Término de publicação de acórdãos em sessão de julgamento                        | Término de publicação de acórdãos em sessão de julgamento.                                              | -     |
| 191 | 12/31/2024 | Encerramento de contas bancárias de campanha                                     | Encerramento de contas bancárias de campanha e transferência de saldos.                                | -     |
| 192 | 12/31/2024 | Cancelamento de inscrições de candidatos na Receita Federal                      | Cancelamento de inscrições de candidatos na Receita Federal.                                            | -     |
| 193 | 01/06/2025 | Término de cessão de funcionários à Justiça Eleitoral                            | Término de cessão de funcionários à Justiça Eleitoral em unidades que realizaram apenas o primeiro turno. | -     |
| 194 | 01/07/2025 | Último dia para justificativa de falta ao segundo turno                          | Último dia para eleitores justificarem falta ao segundo turno.                                          | -     |
| 195 | 01/09/2025 | Último dia para solicitação de verificação de sistemas eleitorais                | Último dia para entidades fiscalizadoras solicitarem verificação de sistemas eleitorais.               | -     |
| 196 | 01/14/2025 | Manutenção de meios de armazenamento de dados                                    | Manutenção de meios de armazenamento de dados utilizados nas eleições.                                 | -     |
| 197 | 01/14/2025 | Envio de ata de encerramento dos testes de integridade                           | Envio de ata de encerramento dos testes de integridade das urnas eletrônicas ao TSE.                   | -     |
| 198 | 01/14/2025 | Solicitação de relatórios e cópias de arquivos para auditoria                    | Solicitação de relatórios e cópias de arquivos para auditoria pelas entidades fiscalizadoras.          | -     |
| 199 | 01/15/2025 | Remoção de lacres e formatação de mídias de votação                              | Remoção de lacres e formatação de mídias de votação das urnas eletrônicas.                             | -     |
| 200 | 01/15/2025 | Inutilização de cédulas e deslacramento de urnas de lona                         | Inutilização de cédulas e deslacramento de urnas de lona utilizadas nas eleições.                      | -     |
| 201 | 01/15/2025 | Formatação de meios de armazenamento de dados                                    | Formatação de meios de armazenamento de dados e descarte de cópias de segurança.                       | -     |
| 202 | 01/27/2025 | Término de cessão de funcionários à Justiça Eleitoral (2º turno)                 | Término de cessão de funcionários à Justiça Eleitoral em unidades que realizaram segundo turno.        | -     |
| 203 | 03/05/2025 | Afixação de edital com relação de faltosos                                       | Afixação de edital com relação de eleitores faltosos às três últimas eleições.                         | -     |
| 204 | 06/16/2025 | Conservação de documentação de contas                                            | Conservação de documentação de contas por candidatos e partidos políticos.                             | -     |
| 205 | 07/30/2025 | Envio de consolidação de informações sobre doações                               | Envio de consolidação de informações sobre doações à Receita Federal.                                  | -     |
| 206 | 07/30/2025 | Comunicação de indícios de excessos de doações                                   | Comunicação de indícios de excessos de doações ao Ministério Público.                                  | -     |
| 207 | 12/31/2025 | Ajuizamento de representação por doações acima do limite                         | Ajuizamento de representação por doações acima do limite legal nas eleições de 2024.                   | -     |

Esta tabela resume todos os eventos e datas mencionados no documento, com uma breve descrição de cada um e a hora do evento, quando disponível.
