from selenium import webdriver
import time

#Abrir o navegador de internet
navegador = webdriver.Chrome()

#Acessa a URL do site que você quer testar
navegador.get("https://www.jjconsulting.com.br/pt-br") 

#colocando o navegador em tela Cheia
navegador.maximize_window()


#selecionar elemento na tela
botao_exemplo = navegador.find_element("class name", "nav-link") # pega o primeiro elemento que aparece dessa classe 

#clickar no elemento pego
botao_exemplo.click() #esse .click simula um click com o botao esquerdo do mouse


lista_exemplo = navegador.find_elements("class name", "nav-link") 
#aqui usamos find_element!s!

for botao in lista_exemplo:
    texto = botao.text.strip()  # remove espaços extras
    print("Achei:", texto)      # printa todos os textos com a classe nav-link assim vou saber o texto que eu queria
    if "FAÇA PARTE" in texto: # aqui eu coloco o texto que eu quero que a automação clique
        botao.click() # se achar entao ela clicka e encerra o loop
        break


abas = navegador.window_handles # gerencia a abas e as coloca em um array -retorna um array de paginas-
navegador.switch_to.window(abas[1]) # muda a aba que os proximos comandos serao feitos

lista_vagas = navegador.find_elements("class name", "btn-primary")

lista_vagas[4].click() # clicka no item 5 dos elementos da classe btn-primary
enviarCandidatura = navegador.find_element("class name", "btn-success") 
#enviarCandidatura.click() clickar aqui ele bloqueia e testa mensagem de erro no formulario

time.sleep(1)

#preenchendo candidatura
navegador.find_element("id", "Candidato_Nome").send_keys("Vitaooo")
navegador.find_element("id", "Candidato_Email").send_keys("vitorzada@gmail.com") # escreve no campo com o id passado para o parametro
navegador.find_element("id", "Candidato_Celular").send_keys("11999999999")
botaoCV =navegador.find_element("id", "cv-file")
botaoCV.send_keys(r"C:\Users\Windows 10\Desktop\teste\CurriculoVitorGM.docx") # ja envia o arquivo direto!
navegador.find_element("id", "Candidato_Mensagem").send_keys("Sou muito legal e estou aprendendo selenium (Isso é uma automação)")

#Dar scroll na tela 
navegador.execute_script('window.scrollBy(0,320)') # o segundo paramentro do scroll é o vertical, negativo pra cima e positiva pra baixo

#tem um captcha que estou acionando manualmente por isso dou 5 segundos para isso
time.sleep(5)

enviarCandidatura.click() # enfim, envio a candidatura

time.sleep(10)