import pygame, sys
from pygame.locals import *

pygame.init()

MANH_HINH = pygame.display.set_mode((900, 800))
pygame.display.set_caption("Cờ chéo")

BAN = pygame.image.load("./assets/Board.png")
HINH_X = pygame.image.load("./assets/X.png")
HINH_O = pygame.image.load("./assets/O.png")


Mau_Nen = (214, 201, 227)
trang_thai_game = False

bang_hinh = [[[None, None], [None, None], [None, None]], [[None, None], [None, None], [None, None]],[[None, None], [None, None], [None, None]]]
bang = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


luot_di = 'X'

MANH_HINH.fill(Mau_Nen)
MANH_HINH.blit(BAN, (64, 64))
pygame.display.update()


def them_toado(bang, bang_hinh, luot_di):
    vi_tri_hien_tai = pygame.mouse.get_pos()
    hang = vi_tri_hien_tai[1] // 300
    cot = vi_tri_hien_tai[0] // 300
    
    if bang[hang][cot] != 'O' and bang[hang][cot] != 'X':
        bang[hang][cot] = luot_di
        luot_di = 'O' if luot_di == 'X' else 'X'
    
    ve_bang(bang, HINH_X, HINH_O)

    for i in range(3):
        for j in range(3):
            if bang_hinh[i][j][0] is not None:
                MANH_HINH.blit(bang_hinh[i][j][0], bang_hinh[i][j][1])
    
    return bang, luot_di

def ve_bang(bang, hinh_x, hinh_o):
    global bang_hinh
    for i in range(3):
        for j in range(3):
            if bang[i][j] == 'O':
                bang_hinh[i][j][0] = hinh_o
                bang_hinh[i][j][1] = hinh_o.get_rect(center=(j * 300 + 150, i * 300 + 150))
            elif bang[i][j] == 'X':
                bang_hinh[i][j][0] = hinh_x
                bang_hinh[i][j][1] = hinh_x.get_rect(center=(j * 300 + 150, i * 300 + 150))
            

def kiem_tra_thang(bang):
    nguoi_thang = None
    for hang in range(3):
        if bang[hang][0] == bang[hang][1] == bang[hang][2] and bang[hang][0] is not None:
            nguoi_thang = bang[hang][0]
            return nguoi_thang

    for cot in range(3):
        if bang[0][cot] == bang[1][cot] == bang[2][cot] and bang[0][cot] is not None:
            nguoi_thang = bang[0][cot]
            return nguoi_thang

    if bang[0][0] == bang[1][1] == bang[2][2] and bang[0][0] is not None:
        nguoi_thang = bang[0][0]
        return nguoi_thang

    if bang[0][2] == bang[1][1] == bang[2][0] and bang[0][2] is not None:
        nguoi_thang = bang[0][2]
        return nguoi_thang
    
    if nguoi_thang is None:
        for hang in bang:
            for o in hang:
                if isinstance(o, int):
                    return None
        return "HÒA"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            bang, luot_di = them_toado(bang, bang_hinh, luot_di)
            if trang_thai_game:
                bang_hinh = [[[None, None], [None, None], [None, None]],[[None, None], [None, None], [None, None]], [[None, None], [None, None], [None, None]]]
                bang = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
                luot_di = 'X'
                MANH_HINH.fill(Mau_Nen)
                MANH_HINH.blit(BAN, (64, 64))
                trang_thai_game = False
                pygame.display.update()

            if kiem_tra_thang(bang) is not None:
                trang_thai_game = True

            pygame.display.update()
