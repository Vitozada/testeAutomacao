# Teste automação com Selenium!
### A Automação tem como objetivo se candidatar para a vaga de Estagiario na JJ consulting ###

#### Tudo começa com um comando no prompt após criar seu arquivo.py (python)

`pip install selenium`
E pronto, *selenium* Instalado
***

<img width="400" height="400" alt="code1" src="https://github.com/user-attachments/assets/b1714228-8f9e-409a-bc6e-c1643196e043" />

Importação do *WebDriver* e *time* 

**WebDriver:** Para podermos usar o navegador de preferrencia 

**Time:** Permite usar comando para parar a automação por alguns segundos
***

<img width="400" height="400" alt="code2" src="https://github.com/user-attachments/assets/299795c6-fb9f-48f0-aec4-a009b1028865" />

Comandos iniciais para abrir o google chrome, ir para a URL destacada e deixar o navegador em tela cheia
***

<img width="2200" height="562" alt="code3" src="https://github.com/user-attachments/assets/66fe6369-4b42-46eb-a6d1-f3528b04ad39" />

Criamos uma variavel **botao_exemplo** para armazenar um elemento da pagina com o nome de classe "nav-link" no site que irei automatizar tem varios elementos com essa classe entao o Selenium clicka na primeira aparição de algum elemento dessa classe

Logo a baixo clickamos no elemento com a função ` .click() `

***

<img width="600" height="400" alt="code4 elements" src="https://github.com/user-attachments/assets/9297f558-e2fa-42b6-b520-3203e98a0a7a" />

Com o comando ` lista_exemplo = navegador.find_elements("class name", "nav-link") ` Criamos um array que é populado pelo nome de todos os elementos que sejam da classe **nav-link**
***

<img width="2000" height="616" alt="code5 for each" src="https://github.com/user-attachments/assets/2afe3313-de95-4858-a26f-c192e411b3ca" />

Esse **foreach** representa um laço simples, retornando os valores das posições do meu Array assim podendo ver o conteudo que esta no elemento que quero selecionar da pagina

***
<img width="2000" height="400" alt="code6 guias" src="https://github.com/user-attachments/assets/d9a68af1-8926-410b-937e-ceeda2e48130" />

`abas = navegador.window_handles` Cria um array com o tamanho igual a quantidade de guias abertas 

`navegador.switch_to.window(abas[1])` Executa uma troca de janela nesse caso indo para a segunda posição do Array [1] se houver mais abas você pode trocar facilmente apenas especificando a posição da guia
***



