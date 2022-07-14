#Primeiramente importei o módulo do pygame, e inicializei o mesmo.
from ast import Sub
from cmath import rect
from turtle import clear
import pygame
from pygame import mixer
pygame.init()
pygame.font.init()

#Defini variáveis com os números das cores (em RGB), de modo que fique mais fácil trabalhar com elas em meu código.
branco = (255, 255, 255)
preto = (0, 0, 0)
azul = (0, 0, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
amarelo = (255, 255, 0)
rosa = (255, 0, 127)
cinza_escuro = (46, 46, 46)
cinza_barra =(97, 100, 105)
cinza =  (130, 128, 128)
roxo = (148, 0, 211)

#Defini a resolução de minha janela do programa, além de dar um nome ao mesmo e também a taxa de quadros por segundo. Também adicionei uma varivável som, que será o
#efeito sonoro do programa.
largura = 1000
altura = 800
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("iPaint")
frame = pygame.time.Clock()
icone = pygame.image.load('icone.png')
pygame.display.set_icon(icone)
som = mixer.Sound('som_clique.wav')

#Esta é a função da barra de ferramentas (interface) do aplicativo.
def menu(cor_pincel, tamanho_pincel):

    class Interface:
        def interface_base(self):
            pygame.draw.rect(janela, cinza,[0, 680, largura, 120])
        def botao1(self):
            pygame.draw.rect(janela, preto,[900, 700, 70, 70])
        def botao2(self):
            pygame.draw.rect(janela, preto,[820, 700, 70, 70])
        def botao3(self):
            pygame.draw.rect(janela, preto,[740, 700, 70, 70])
        def botao4(self):
            pygame.draw.rect(janela, preto,[660, 700, 70, 70])
        def linha1(self):
            pygame.draw.line(janela, preto, [0, 680], [largura, 680], 3)
        def linha2(self):
            pygame.draw.line(janela, preto, [0, 800], [largura, 800], 8)
        def linha3(self):
            pygame.draw.line(janela, preto, [0, 800], [0, 680], 5)
        def linha4(self):
            pygame.draw.line(janela, preto, [1000, 800], [1000, 680], 8)

    interface = Interface()

    #Este é o modelo da barra de ferramentas, juntamente com os quadrados dos botões de tamanho do pincel.
    interface.interface_base()
    interface.botao1()
    interface.botao2()
    interface.botao3()
    interface.botao4()

    #Linhas barra de ferramentas.
    interface.linha1()
    interface.linha2()
    interface.linha3()
    interface.linha4()

    pygame.draw.line(janela, cinza_barra, [540, 690], [540, 790], 4)
    pygame.draw.line(janela, cinza_barra, [320, 690], [320, 790], 4)

    #Quadrado que mostra o tamnho do pincel selecionado.
    if tamanho_pincel == 20:
        pygame.draw.rect(janela, azul,[900, 700, 70, 70], 3)
    elif tamanho_pincel == 15:
        pygame.draw.rect(janela, azul,[820, 700, 70, 70], 3)
    elif tamanho_pincel == 10:
        pygame.draw.rect(janela, azul,[740, 700, 70, 70], 3)
    elif tamanho_pincel == 5:
        pygame.draw.rect(janela, azul,[660, 700, 70, 70], 3)

    #Círculo que mostra a cor selecionada.
    pygame.draw.circle(janela, cor_pincel, (270, 740), 35)
    pygame.draw.circle(janela, cinza_escuro, (270, 740), 35, 5)

    #Esta é a função preencher, que preenche a tela com a cor escolhida.
    preencher = pygame.draw.rect(janela, preto,[575, 700, 70, 70])
    pygame.draw.line(janela, branco, [590, 710], [590,760], 7)
    pygame.draw.line(janela, branco, [630, 710], [630,760], 7)
    pygame.draw.line(janela, branco, [590, 756], [630,756], 8)

    #Esta é a função clear, que limpa toda a tela do programa.
    clear = pygame.draw.rect(janela, preto,[350, 700, 70, 70])
    pygame.draw.line(janela, branco, [360, 710], [410,760], 8)
    pygame.draw.line(janela, branco, [410, 710], [360,760], 8)

    #Estes sãos os tamanhos dos pinceis.
    pincelG = pygame.draw.circle(janela, branco, (935, 735), 20)
    pincelM = pygame.draw.circle(janela, branco, (855, 735), 15)
    pincelP = pygame.draw.circle(janela, branco, (775, 735), 10)
    pincelPP = pygame.draw.circle(janela, branco, (695, 735), 5)

    #Estas são as cores disponíveis para uso.
    Bpreto = pygame.draw.rect(janela, preto,[20, 700, 40, 40])
    Bbranco =pygame.draw.rect(janela, branco,[70, 700, 40, 40])
    Bazul = pygame.draw.rect(janela, azul,[120, 700, 40, 40])
    Bvermelho = pygame.draw.rect(janela, vermelho,[170, 700, 40, 40])
    Bverde = pygame.draw.rect(janela, verde,[20, 750, 40, 40])
    Bamarelo = pygame.draw.rect(janela, amarelo,[70, 750, 40, 40])
    Brosa = pygame.draw.rect(janela, rosa,[120, 750, 40, 40])
    Broxo = pygame.draw.rect(janela, roxo,[170, 750, 40, 40])

    #Função save, que salva a imagem.
    save = pygame.draw.rect(janela, preto,[430, 700, 70, 70])
    pygame.draw.line(janela, branco, [440, 739], [460, 755], 8)
    pygame.draw.line(janela, branco, [460, 758], [485, 710], 8)

    #Aqui estão as listas de todas as ferramentas. 
    bpreencher = [preencher]
    saves = [save]
    pinceis = [pincelPP, pincelP, pincelM, pincelG]
    Bcores = [Bpreto, Bbranco, Bazul, Bvermelho, Bverde, Bamarelo, Brosa, Broxo]
    cores = [(0, 0, 0), (255, 255, 255), (0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (255, 0, 127), (148, 0, 211)]
    Lclear = [clear]
    pygame.display.update()

    return pinceis, Bcores, cores, Lclear, saves, bpreencher

#Este é o comando que determina qual parte da tela será salva.
rect = pygame.Rect(0, 0, 1000, 680)
sub = janela.subsurface(rect)

#Este é o código principal do programa. Aqui é onde são utilizadas as listas das ferramentas e onde o código de funcionamento do programa se encontra.
def main():
    rodar = True
    tamanho_pincel = 5
    cor_pincel = branco
    janela.fill(branco)
    pygame.display.update()

    class Pincel:
        def desenhar(self):
            pygame.draw.circle(janela, cor_pincel, mouse, tamanho_pincel)
        
    pincel_principal = Pincel()

    class Janela:
        def salvar(self):
            pygame.image.save(sub, "screenshot.jpg")
        def clear(self):
            janela.fill(branco)
        def preencher (self):
            janela.fill(cor_pincel)
        
    tela = Janela() 

#Este é o loop que mantém o programa funcionando, até que o usuário feche a janela do aplicativo.
    while rodar:
        #Estas são as listas definidas na função anterior, trouxe elas para a função principal para poder utilizá-las no código.
        pinceis, Bcores, cores, Lclear, saves, bpreencher = menu(cor_pincel, tamanho_pincel)
        frame.tick(1000)
        clique = pygame.mouse.get_pressed()[0]
        mouse = pygame.mouse.get_pos()

        #Este é a função que verifica todos os eventos que ocorrem no aplicativo.
        for event in pygame.event.get():

            #Este é o evento QUIT, se ele ocorrer, o programa fecha (run = False)
            if event.type == pygame.QUIT:
                rodar = False

            #Caso o mouse seja pressionado nas coordenadas do botão de preencher, a ferramenta será utilizada e a tela será preenchida com a cor atual.
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(bpreencher)):
                    if bpreencher[i].collidepoint(event.pos):
                        som.play()
                        tela.preencher()
                        pygame.display.update()
            
            #Caso o mouse seja pressionado nas coordenadas do botão de clear, a ferramenta será utilizada e a tela será preenchida com a cor branca.
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(Lclear)):
                    if Lclear[i].collidepoint(event.pos):
                        som.play()
                        tela.clear()

            #Caso o mouse seja pressionado nas coordenadas do botão de save, a ferramenta será utilizada e a tela será salva em uma imagem jpg, 
            #intitulada "screenshot" na mesma pasta do arquivo.
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(saves)):
                    if saves[i].collidepoint(event.pos):
                        som.play()
                        tela.salvar()
                        
            #Caso o mouse seja pressionado nas coordenadas de qualquer botão de tamanho de pincel, a ferramenta será utilizada e o pincel assumirá o tamanho selecionado.
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(pinceis)):
                    if pinceis[i].collidepoint(event.pos):
                        som.play()
                        tamanho_pincel = 5 + 5 * i
            
            #Caso o mouse seja pressionado nas coordenadas de qualquer botão de cor, a ferramenta será utilizada e o pincel assumirá a cor selecionada.
                for i in range(len(Bcores)):
                    if Bcores[i].collidepoint(event.pos):
                        som.play()
                        cor_pincel = cores[i]
                        
        #Este condicional serve para que o pincel desenhe na tela. Ele também garante que a barra de ferramentas não seja afetada pelo pincel.
        if mouse[1] < 680 and clique:
            pincel_principal.desenhar()
            
        pygame.display.flip()

    pygame.quit()
if __name__ == "__main__":
    main()