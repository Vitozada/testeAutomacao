# Teste automação com Selenium!
### A Automação tem como objetivo se candidatar para a vaga de Estagiario na JJ consulting ###

#### Tudo começa com um comando no prompt após criar seu arquivo.py (python)

`pip install selenium`
E pronto, *selenium* Instalado
***
#### Imports
<img width="400" height="400" alt="code1" src="https://github.com/user-attachments/assets/b1714228-8f9e-409a-bc6e-c1643196e043" />

Importação do *WebDriver* e *time* 

**WebDriver:** Para podermos usar o navegador de preferrencia 

**Time:** Permite usar comando para parar a automação por alguns segundos
***
#### Primeiros passos
<img width="400" height="400" alt="code2" src="https://github.com/user-attachments/assets/299795c6-fb9f-48f0-aec4-a009b1028865" />

Comandos iniciais para abrir o google chrome, ir para a URL destacada e deixar o navegador em tela cheia
***
#### Criando uma varivel de um elemento
<img width="2200" height="562" alt="code3" src="https://github.com/user-attachments/assets/66fe6369-4b42-46eb-a6d1-f3528b04ad39" />

Criamos uma variavel **botao_exemplo** para armazenar um elemento da pagina com o nome de classe "nav-link" no site que irei automatizar tem varios elementos com essa classe entao o Selenium clicka na primeira aparição de algum elemento dessa classe

Logo a baixo clickamos no elemento com a função ` .click() `

***
#### Criando um array de elementos web
<img width="600" height="400" alt="code4 elements" src="https://github.com/user-attachments/assets/9297f558-e2fa-42b6-b520-3203e98a0a7a" />

Com o comando ` lista_exemplo = navegador.find_elements("class name", "nav-link") ` Criamos um array que é populado pelo nome de todos os elementos que sejam da classe **nav-link**
***
#### Laço de repetição para exibição dos textos dos elementos 
<img width="2000" height="616" alt="code5 for each" src="https://github.com/user-attachments/assets/2afe3313-de95-4858-a26f-c192e411b3ca" />

Esse **foreach** representa um laço simples, retornando os valores das posições do meu Array assim podendo ver o conteudo que esta no elemento que quero selecionar da pagina

***
#### Trocando guias do navegador
<img width="2000" height="400" alt="code6 guias" src="https://github.com/user-attachments/assets/d9a68af1-8926-410b-937e-ceeda2e48130" />

`abas = navegador.window_handles` Cria um array com o tamanho igual a quantidade de guias abertas 

`navegador.switch_to.window(abas[1])` Executa uma troca de janela nesse caso indo para a segunda posição do Array [1] se houver mais abas você pode trocar facilmente apenas especificando a posição da guia
***
#### Exemplo de teste para submit do formulario
<img width="2304" height="562" alt="code botao candidatar" src="https://github.com/user-attachments/assets/1138d875-65e5-4762-93c2-d3bd86646261" />

Na linha 1 crio um array que representa os botoões de candidatar-se chamado `lista_vagas`

Logo crio uma varivel com o elemento que faz o submit do formulario e chamei de `EnviarCandidatura`

legal citar que na linha 5 eu optei por colocar um `enviarCandidatura.click()` para poder testar as mensagem de requerimento de preenchimento dos campos do formulario
***
#### Preenchendo o Formulario de candidatura
<img width="3228" height="724" alt="preenchendo as parada" src="https://github.com/user-attachments/assets/c8386fad-0bba-4059-8b0e-e14e962db849" />

Usando o `send_keys()` podemos enviar valores para o elemento web registrado, assim podendo preencher formularios e outros inputs...

#### Enviar arquivos para input do tipo FILE

Nesse bloco do algoritmo uso os codigos aprendidos anteriormente para chegar nessa etapa e acabo aprendendo algo novo:
```
botaoCV =navegador.find_element("id", "cv-file")
botaoCV.send_keys(r"C:\Users\Windows 10\Desktop\teste\CurriculoVitorGM.docx") # ja envia o arquivo direto!
```

Enviar um arquivo indicando o caminho do meu diretorio de pastas onde se encontra o arquivo que quero enviar, importante citar que o python precisa colocar um "r" antes do diretorio de pastas para aceitar o caminho tranquilamente, ele entende as \ como uma referencia pra colocar uma variavel no texto.

***

#### Dando Scroll na tela com Javascript
<img width="3294" height="454" alt="injetando script" src="https://github.com/user-attachments/assets/5ceed294-21f2-450d-8385-5f35431b5f48" />

Após me alertar um erro dizendo que nao encontrava o elemento na pagina, Achei na documentação do Selenium possiveis soluções para o erro e lá ele me entregou a solução mostrando que podemos injetar no Selenium um codigo javaScrpit que me permite dar Scroll na tela assim fazendo o elemento que eu estava buscando aparecer na tela e ser identificado pelo Selenium
***

#### Completando o objetivo da automação

<img width="2084" height="616" alt="Enviando o formulario e resolvendo o captcha manualmente" src="https://github.com/user-attachments/assets/a03a70a2-b4c3-466d-ac19-19e62b30dcf7" />

Primeiramente coloco um `time.Sleep(5)` para poder resolver o captcha manualmente pois essa é a finalidade de um CAPTCHA

logo depois eu ultilizo a variavel do botão de submit da candidatura com `.click()` assim finalmente enviado-a
