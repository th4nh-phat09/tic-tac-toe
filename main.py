import pygame, sys
from pygame.locals import *

pygame.init()

manHinh = pygame.display.set_mode((900, 800))
pygame.display.set_caption("Cờ chéo")

BAN = pygame.image.load("./assets/Board.png")
hinhX = pygame.image.load("./assets/X.png")
hinhO = pygame.image.load("./assets/O.png")

mauNen = (214, 201, 227)
bang = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
trangThaiGame = False
khoiTao=[[[None,None],[None,None],[None,None]],[[None,None],[None,None],[None,None]],[[None, None],[None,None],[None,None]]]
boardImage = khoiTao


luot_di = 'X'

manHinh.fill(mauNen)
manHinh.blit(BAN, (64, 64))
pygame.display.update()


def themToaDo(bang, boardImage, luotDi):
    
    vTriHTai = pygame.mouse.get_pos()
    column = vTriHTai[0] // 300
    row = vTriHTai[1] // 300
    
    
    if bang[row][column] != 'O' and bang[row][column] != 'X':
        bang[row][column] = luotDi
        luotDi = 'O' if luotDi == 'X' else 'X'
    
    veBang(bang, hinhX, hinhO)

    for h in range(3):
        for c in range(3):
            if boardImage[h][c][0] is not None:
                manHinh.blit(boardImage[h][c][0], boardImage[h][c][1])
    
    return bang, luotDi

def veBang(bang, hinhX, hinhO):
    global boardImage
    for h in range(3):
        for c in range(3):
            if bang[h][c]=='O':
                boardImage[h][c][0]=hinhO
                boardImage[h][c][1]=hinhO.get_rect(center=(c * 300 + 150, h * 300 + 150))
            elif bang[h][c]=='X':
                boardImage[h][c][0] = hinhX
                boardImage[h][c][1] = hinhX.get_rect(center=(c * 300 + 150, h * 300 + 150))
            

def kiemTraThang(bang):
    nguoiThang = None
    for hang in range(3):
        if bang[hang][0] == bang[hang][2] == bang[hang][1]  and bang[hang][0] is not None:
            nguoiThang = bang[hang][0]
            return nguoiThang

    for cot in range(3):
        if bang[0][cot] == bang[1][cot] == bang[2][cot] and bang[0][cot] is not None:
            nguoiThang = bang[0][cot]
            return nguoiThang

    if bang[0][0] == bang[1][1] == bang[2][2] and bang[0][0] is not None:
        nguoiThang = bang[0][0]
        return nguoiThang

    if bang[0][2] == bang[1][1] == bang[2][0] and bang[0][2] is not None:
        nguoiThang = bang[0][2]
        return nguoiThang
    
    if nguoiThang is None:
        for hang in bang:
            for o in hang:
                if isinstance(o, int):
                    return None
        return "HÒA"

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            bang, luot_di = themToaDo(bang, boardImage, luot_di)
            if trangThaiGame:
                boardImage = khoiTao
                bang = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
                luot_di = 'X'
                manHinh.fill(mauNen)
                manHinh.blit(BAN, (64, 64))
                trangThaiGame = False
                pygame.display.update()

            if kiemTraThang(bang) is not None:
                trangThaiGame = True

            pygame.display.update()
