import pygame
import os
from random import *
import time
###############################################################
# 기본 초기화(반드시 해야 하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 880
screen_height = 880
screen = pygame.display.set_mode((screen_width, screen_height)) # 화면 크기

# 화면 타이틀 설정
pygame.display.set_caption("구룡투")

# FPS
clock = pygame.time.Clock()
###############################################################
# 1. 사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 속도, 폰트)
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "image") # 이미지 폴더 위치 반환

# 배경
menu_bg = pygame.image.load(os.path.join(image_path, "menu_bg.png"))
menu_bg = pygame.transform.scale(menu_bg, (screen_width, screen_height))
background = pygame.image.load(os.path.join(image_path, "background.png"))
background = pygame.transform.scale(background, (screen_width, screen_height))
background_size = background.get_rect().size
background_width = background_size[0]
background_height = background_size[1]

gametable = pygame.image.load(os.path.join(image_path, "gametable.png"))
gametable = pygame.transform.scale(gametable, (600, 450))
gametable_size = gametable.get_rect().size
gametable_width = gametable_size[0]
gametable_height = gametable_size[1]

green_cover = pygame.transform.scale(background, (880, 100))
small_green_cover = pygame.transform.scale(background, (100, 100))

# [게임 이미지(카드, 승리 표시등)]
# 1. 승리 표시등
red_light = pygame.image.load(os.path.join(image_path, "red.png"))
red_light = pygame.transform.scale(red_light, (27, 4))
blue_light = pygame.image.load(os.path.join(image_path, "blue.png"))
blue_light = pygame.transform.scale(blue_light, (27, 4))

# 2. 게임 중 사용되는 카드 이미지
# 컴퓨터 덱의 카드
red_black = pygame.image.load(os.path.join(image_path, "red_black.png"))
red_black_on = pygame.transform.scale(red_black, (50, 67))
red_black_off = pygame.transform.scale(red_black, (75, 100))
red_white = pygame.image.load(os.path.join(image_path, "red_white.png"))
red_white_on = pygame.transform.scale(red_white, (50, 67))
red_white_off = pygame.transform.scale(red_white, (75, 100))

off_size = red_black_off.get_rect().size
off_width = off_size[0]
off_height = off_size[1]

# 플레이어 카드

# 판 위에 가려진 상태로 올라간 플레이어 카드
blue_black_on = pygame.image.load(os.path.join(image_path, "blue_black.png"))
blue_black_on = pygame.transform.scale(blue_black_on, (50, 67))
blue_white_on = pygame.image.load(os.path.join(image_path, "blue_white.png"))
blue_white_on = pygame.transform.scale(blue_white_on, (50, 67))

blue_1 = pygame.image.load(os.path.join(image_path, "blue_1.png"))
blue_2 = pygame.image.load(os.path.join(image_path, "blue_2.png"))
blue_3 = pygame.image.load(os.path.join(image_path, "blue_3.png"))
blue_4 = pygame.image.load(os.path.join(image_path, "blue_4.png"))
blue_5 = pygame.image.load(os.path.join(image_path, "blue_5.png"))
blue_6 = pygame.image.load(os.path.join(image_path, "blue_6.png"))
blue_7 = pygame.image.load(os.path.join(image_path, "blue_7.png"))
blue_8 = pygame.image.load(os.path.join(image_path, "blue_8.png"))
blue_9 = pygame.image.load(os.path.join(image_path, "blue_9.png"))

# 플레이어 덱 내의 보이는 카드
blue_1_off = pygame.transform.scale(blue_1, (75, 100))
blue_2_off = pygame.transform.scale(blue_2, (75, 100))
blue_3_off = pygame.transform.scale(blue_3, (75, 100))
blue_4_off = pygame.transform.scale(blue_4, (75, 100))
blue_5_off = pygame.transform.scale(blue_5, (75, 100))
blue_6_off = pygame.transform.scale(blue_6, (75, 100))
blue_7_off = pygame.transform.scale(blue_7, (75, 100))
blue_8_off = pygame.transform.scale(blue_8, (75, 100))
blue_9_off = pygame.transform.scale(blue_9, (75, 100))
blues_off = [blue_1_off, blue_2_off, blue_3_off, blue_4_off,
             blue_5_off, blue_6_off, blue_7_off, blue_8_off, blue_9_off]

# 3. 게임 종료 후 카드 확인 시 사용하는 이미지

# 컴퓨터 카드
red_1 = pygame.image.load(os.path.join(image_path, "red_1.png"))
red_2 = pygame.image.load(os.path.join(image_path, "red_2.png"))
red_3 = pygame.image.load(os.path.join(image_path, "red_3.png"))
red_4 = pygame.image.load(os.path.join(image_path, "red_4.png"))
red_5 = pygame.image.load(os.path.join(image_path, "red_5.png"))
red_6 = pygame.image.load(os.path.join(image_path, "red_6.png"))
red_7 = pygame.image.load(os.path.join(image_path, "red_7.png"))
red_8 = pygame.image.load(os.path.join(image_path, "red_8.png"))
red_9 = pygame.image.load(os.path.join(image_path, "red_9.png"))

red_1_on = pygame.transform.scale(red_1, (50, 67))
red_2_on = pygame.transform.scale(red_2, (50, 67))
red_3_on = pygame.transform.scale(red_3, (50, 67))
red_4_on = pygame.transform.scale(red_4, (50, 67))
red_5_on = pygame.transform.scale(red_5, (50, 67))
red_6_on = pygame.transform.scale(red_6, (50, 67))
red_7_on = pygame.transform.scale(red_7, (50, 67))
red_8_on = pygame.transform.scale(red_8, (50, 67))
red_9_on = pygame.transform.scale(red_9, (50, 67))
reds_on = [red_1_on, red_2_on, red_3_on, red_4_on,
           red_5_on, red_6_on, red_7_on, red_8_on, red_9_on]

# 플레이어 카드
blue_1_on = pygame.transform.scale(blue_1, (50, 67))
blue_2_on = pygame.transform.scale(blue_2, (50, 67))
blue_3_on = pygame.transform.scale(blue_3, (50, 67))
blue_4_on = pygame.transform.scale(blue_4, (50, 67))
blue_5_on = pygame.transform.scale(blue_5, (50, 67))
blue_6_on = pygame.transform.scale(blue_6, (50, 67))
blue_7_on = pygame.transform.scale(blue_7, (50, 67))
blue_8_on = pygame.transform.scale(blue_8, (50, 67))
blue_9_on = pygame.transform.scale(blue_9, (50, 67))
blues_on = [blue_1_on, blue_2_on, blue_3_on, blue_4_on,
            blue_5_on, blue_6_on, blue_7_on, blue_8_on, blue_9_on]

# 순서 표시
red_turn = pygame.image.load(os.path.join(image_path, "red_turn.png"))
red_turn = pygame.transform.scale(red_turn, (50, 50))
blue_turn = pygame.image.load(os.path.join(image_path, "blue_turn.png"))
blue_turn = pygame.transform.scale(blue_turn, (50, 50))

# 게임 팁
white_bar = pygame.image.load(os.path.join(image_path, "white_bar.png"))
white_bar = pygame.transform.scale(white_bar, (880, 30))
white_bar_height = white_bar.get_rect().size[1]

# 기본 설정
main_menu = True
how_to = False
clicked = False
start_clicked = False
how_to_clicked = False
in_how_clicked = False
replay_clicked = False
home_clicked = False
playing_clicked = False
running = True  # 게임이 진행 중인가?
playing = False
choosing = False
player_first = False
round_on = False
ended = False
retire = False

com_deck = list(range(9))
player_deck = list(range(9))
player_win_round = []
com_win_round = []
com_card = []  # 컴퓨터가 필드에 낸 카드
player_card = []  # 플레이어가 필드에 낸 카드
round_x_pos = 0
speed = 13.75
round = 1
tip_y_pos = screen_height - white_bar_height
tip_speed = 0.2

# 폰트
title_font = pygame.font.Font("독립체.TTF", 120)
main_font = pygame.font.Font("양재본목각체.TTF", 40)
how_to_font = pygame.font.Font("함초롬돋움.TTF", 22)
how_to_menu_font = pygame.font.Font("함초롬돋움.TTF", 30)
round_font = pygame.font.Font("양재본목각체.TTF", 60)
round_win_font = round_font
turn_font = pygame.font.Font("함초롬돋움.ttf", 20)
game_win_font = pygame.font.Font("독립체.ttf", 80)
game_tip_font = pygame.font.Font("함초롬돋움.ttf", 20)
score_font = pygame.font.Font("함초롬돋움.ttf", 40)

# 텍스트
title = title_font.render("구 룡 투", True, (0, 0, 0))
start_menu = main_font.render("게임시작", True, (0, 0, 0))
how_to_menu = main_font.render("게임방법", True, (0, 0, 0))
game_win = game_win_font.render("<  승  리  >", True, (0, 0, 0))
game_lose = game_win_font.render("<  패  배  >", True, (0, 0, 0))
game_draw = game_win_font.render("<  무  승  부  >", True, (50, 50, 50))
tip_texts = ["알고 계셨나요? 이 게임은 실제 보드게임 구룡투를 원작으로 한 게임입니다.",
            "알고 계셨나요? 이 게임에는 여전히 잔 버그가 많지만 더는 못 고치겠습니다.",
            "알고 계셨나요? 게임 내 AI는 플레이어의 패를 예측하여 최적의 수를 냅니다.",
            "알고 계셨나요? 제작자는 버그를 수정하다가 머리가 4번 터졌습니다.",
            "알고 계셨나요? 구룡투의 업데이트 계획은 없습니다.",
            "알고 계셨나요? 이 게임의 제작 기간은 총 7일이었습니다.",
            "알고 계셨나요? 제한시간 내에 카드를 고르지 않으면 자동으로 아무 카드나 내집니다.",
            "알고 계셨나요? AI는 심리전에 걸려들지 않습니다.",
            "알고 계셨나요? 보드게임 구룡투의 플레이타임은 15분 내외입니다.",
            "알고 계셨나요? 실제 보드게임 구룡투의 가격은 3만원 선입니다.(건전지 별도)",
            "알고 계셨나요? 구룡투는 더 지니어스의 흑과 백을 모티브로 만들어진 게임입니다.",
            "알고 계셨나요? 9는 아끼다 똥됩니다.",
            "4번 연달아 졌다고 실망하지 마세요! 상대는 이제 작은 수밖에 없습니다."]
how_to_texts = ["아홉 개의 용석에는 각각 1부터 9까지 숫자가 쓰여 있습니다.",
                "각 플레이어는 라운드마다 하나의 용석을 내고",
                "더 큰 숫자를 지닌 용석을 낸 사람이 라운드를 승리합니다.",
                "단, 가장 작은 수 1은 9를 이깁니다.",
                "",
                "라운드를 승리하면 다음 라운드의 선공 플레이어가 됩니다.",
                "무승부가 되었다면 선공 플레이어가 바뀌지 않습니다.",
                "",
                "게임은 총 9라운드로 이루어져 있습니다.",
                "9라운드가 모두 끝나거나 한 플레이어의 승리가 확정되면 게임이 종료됩니다.",
                "",
                "큰 수를 언제 내는 게 좋을까요?",
                "먼저 네 번을 지더라도 뒤에 다섯 번을 연속으로 이기는 전략은 어떨까요?",
                "",
                "큰 그림을 그리고, 이에 맞는 전략을 짜보세요!"]



def print_round():
    speed = 100
    round_x_pos = 0
    round_x_pos += speed
    screen.blit(round_text, round_text.get_rect(center=(round_x_pos, screen_height / 2)))
    pygame.display.update()


# 플레이어가 카드를 고르는 함수
def player_choose():
    global off_width, clicked, player_num, player_deck, choosing, playing, start_ticks, running, main_menu,\
    playing_clicked, retire, round_on, player_deck_color
    time_limit = 20

    while player_num == None and choosing:
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
        time_left = int(time_limit - elapsed_time)
        timer = score_font.render(str(time_left), True, (0, 0, 0))

        screen.blit(small_green_cover, small_green_cover.get_rect(center=(screen_width - 50, screen_height / 2)))
        screen.blit(timer, timer.get_rect(center=(screen_width - 50, screen_height / 2)))
        pygame.display.update()

        if time_left < 0:
            screen.blit(small_green_cover, small_green_cover.get_rect(center=(screen_width - 50, screen_height / 2)))
            player_num = player_deck[randint(1, len(player_deck)) - 1]
            player_deck.remove(player_num)
            player_card.append(player_num)
            pygame.display.update()
            choosing = False
        #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                choosing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu = True
                    playing = False
                    reset_setting()

            ####
            if event.type == pygame.MOUSEBUTTONDOWN and playing_clicked == False:
                down_position = pygame.mouse.get_pos()
                if 15 <= down_position[0] <= 135 and 9 <= down_position[1] <= 49:
                    playing_clicked = True
                if 803 <= down_position[0] <= 855 and 9 <= down_position[1] <= 49:
                    playing_clicked = True
            if event.type == pygame.MOUSEBUTTONUP and playing_clicked:
                up_position = pygame.mouse.get_pos()
                if 15 <= up_position[0] <= 135 and 9 <= up_position[1] <= 49:
                    playing_clicked = False
                    reset_setting()
                    main_menu = True
                    playing = False
                if 803 <= up_position[0] <= 855 and 9 <= up_position[1] <= 49:
                    round_on = False
                    choosing = False
                    playing_clicked = False
                    retire = True
                    playing = False
            ####

            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                pos = pygame.mouse.get_pos()
                for i in range(len(player_deck)):
                    if ((45 + (off_width + 15) * i) <= pos[0] <= (45 + (off_width + 15) * (i + 1) - 15)) \
                            and (700 <= pos[1] <= 800) and (len(player_card) == (round - 1)):
                        clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked:
                pos = pygame.mouse.get_pos()
                for i in range(len(player_deck)):
                    if ((45 + (off_width + 15) * i) <= pos[0] <= (45 + (off_width + 15) * (i + 1) - 15)) \
                            and (700 <= pos[1] <= 800) and (len(player_card) == (round - 1)):
                        clicked = False
                        player_num = player_deck_color[i]
                        player_deck.remove(player_num)
                        player_card.append(player_num)
                        pygame.display.update()
                        choosing = False


def computer_choose():
    global com_deck, com_card, com_num, player_num

    while com_num == None:
        rand_idx = randint(1, len(com_deck)) - 1
        com_num = com_deck[rand_idx]
        if player_num != None:
            if player_num % 2 == 1 and com_num == 0:
                com_num = com_deck[rand_idx - 1]
        com_deck.remove(com_num)  # com_deck : 컴퓨터의 덱에 남은 카드 리스트
        com_card.append(com_num)  # com_card : 컴퓨터가 낸 카드의 리스트
        pygame.display.update()


def check_round_winner():
    global player_num, com_num, player_first, round
    if player_num == 0 and com_num == 8:
        player_first = True
        player_win_round.append(round)
    elif player_num == 8 and com_num == 0:
        player_first = False
        com_win_round.append(round)
    elif player_num > com_num:
        player_first = True
        player_win_round.append(round)
    elif player_num < com_num:
        player_first = False
        com_win_round.append(round)
    elif player_num == com_num:
        player_win_round.append(round)
        com_win_round.append(round)
        pass


def print_com_card():
    for idx, card in enumerate(com_card):
        if card % 2 == 0:
            screen.blit(red_white_on, ((204 + 53.5 * idx), 338))
        else:
            screen.blit(red_black_on, ((204 + 53.5 * idx), 338))


def print_player_card():
    for idx, card in enumerate(player_card):
        if card % 2 == 0:
            screen.blit(blue_white_on, ((204 + 53.5 * idx), 470))
        else:
            screen.blit(blue_black_on, ((204 + 53.5 * idx), 470))

def print_com_deck():
    global green_cover

    screen.blit(green_cover, (0, 80))
    com_whites = []
    com_blacks = []
    for idx, card in enumerate(com_deck):
        if card % 2 == 0:
            com_whites.append(card)
        else:
            com_blacks.append(card)
    com_deck_color = com_whites + com_blacks
    for idx, card in enumerate(com_deck_color):
        if card % 2 == 0:
            screen.blit(red_white_off, (45 + (off_width + 15) * idx, 80))
        else:
            screen.blit(red_black_off, (45 + (off_width + 15) * idx, 80))


def print_player_deck():
    global player_deck_color

    screen.blit(green_cover, (0, 700))
    player_whites = []
    player_blacks = []

    for idx, card in enumerate(player_deck):
        if card % 2 == 0:
            player_whites.append(card)
        else:
            player_blacks.append(card)
    player_deck_color = player_whites + player_blacks
    for idx, card in enumerate(player_deck_color):
        if card % 2 == 0:
            screen.blit(blues_off[card], (45 + (off_width + 15) * idx, 700))
        else:
            screen.blit(blues_off[card], (45 + (off_width + 15) * idx, 700))

def print_com_fight():
    if com_num % 2 == 0:
        screen.blit(red_white_on, (screen_width / 2 - 22, screen_height / 2 - gametable_height / 2 + 3))
    else:
        screen.blit(red_black_on, (screen_width / 2 - 22, screen_height / 2 - gametable_height / 2 + 3))


def print_player_fight():
    if player_num % 2 == 0:
        screen.blit(blue_white_on, (screen_width / 2 - 22, screen_height / 2 + gametable_height / 2 - 70))
    else:
        screen.blit(blue_black_on, (screen_width / 2 - 22, screen_height / 2 + gametable_height / 2 - 70))


def winner_light():
    for i in com_win_round:
        screen.blit(red_light, ((216 + 53.4 * (i - 1)), 428))
    for i in player_win_round:
        screen.blit(blue_light, ((216 + 53.4 * (i - 1)), 445))


def open_card():
    for idx, card in enumerate(player_card):
        screen.blit(blues_on[card], ((204 + 53.5 * idx), 470))
    for idx, card in enumerate(com_card):
        screen.blit(reds_on[card], ((204 + 53.5 * idx), 338))


def print_winner():
    if len(com_win_round) > len(player_win_round) or retire:
        screen.blit(game_lose, game_lose.get_rect(center=(screen_width/2, 100)))
    elif len(com_win_round) < len(player_win_round):
        screen.blit(game_win, game_win.get_rect(center=(screen_width / 2, 100)))
    else:
        screen.blit(game_draw, game_draw.get_rect(center=(screen_width / 2, 100)))

    # 원래 center의 y좌표는 (screen_height / 2 - 8) 이었다.


def cover_turn():
    screen.blit(small_green_cover,
                small_green_cover.get_rect(center=((screen_width - gametable_width) / 4, screen_height / 2 + 100)))
    screen.blit(small_green_cover,
                small_green_cover.get_rect(center=((screen_width - gametable_width) / 4, screen_height / 2 - 100)))


def reset_setting():
    global clicked, replay_clicked, home_clicked, running, choosing,\
    round_on, com_deck, player_deck, player_win_round, com_win_round, player_num,\
    com_card, player_card, round_x_pos, round, playing, round_x_pos, retire

    clicked = False
    replay_clicked = False
    home_clicked = False
    choosing = False
    round_on = False
    retire = False
    player_num = None

    com_deck = list(range(9))
    player_deck = list(range(9))
    player_win_round = []
    com_win_round = []
    com_card = []  # 컴퓨터가 필드에 낸 카드
    player_card = []  # 플레이어가 필드에 낸 카드
    round_x_pos = 0
    round = 1


def create_box(x, y, width, height):
    pygame.draw.lines(screen, (0, 0, 0), True,
                      [(x, y), (x + width, y), (x + width, y + height), (x, y + height)])


while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                main_menu = True
                playing = False

    while main_menu:
        start_button = (340, 460, 200, 80)
        how_to_button = (340, 560, 200, 80)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                main_menu = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    running = False
                    main_menu = False
                if e.key == pygame.K_SPACE:
                    pygame.time.delay(800)
                    playing = True
                    main_menu = False

            menu_pos = pygame.mouse.get_pos()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if start_button[0] <= menu_pos[0] <= start_button[0] + start_button[2] \
                        and start_button[1] <= menu_pos[1] <= start_button[1] + start_button[3]:
                    start_clicked = True
                if how_to_button[0] <= menu_pos[0] <= how_to_button[0] + how_to_button[2] \
                        and how_to_button[1] <= menu_pos[1] <= how_to_button[1] + how_to_button[3]:
                    how_to_clicked = True
            if e.type == pygame.MOUSEBUTTONUP and (start_clicked or how_to_clicked):
                if start_button[0] <= menu_pos[0] <= start_button[0] + start_button[2] \
                        and start_button[1] <= menu_pos[1] <= start_button[1] + start_button[3]:
                    pygame.time.delay(800)
                    playing = True
                    start_clicked = False
                    main_menu = False
                if how_to_button[0] <= menu_pos[0] <= how_to_button[0] + how_to_button[2] \
                        and how_to_button[1] <= menu_pos[1] <= how_to_button[1] + how_to_button[3]:
                    how_to = True
                    how_to_clicked = False
                    main_menu = False


        screen.blit(menu_bg, (0, 0))
        screen.blit(title, title.get_rect(center=(screen_width / 2, 300)))
        screen.blit(start_menu, start_menu.get_rect(center=(screen_width / 2, 500)))
        screen.blit(how_to_menu, how_to_menu.get_rect(center=(screen_width / 2, 600)))

        create_box(340, 460, 200, 80)
        create_box(340, 560, 200, 80)

        pygame.display.update()

    while how_to:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                how_to = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    main_menu = True
                    how_to = False
                if e.key == pygame.K_SPACE:
                    pygame.time.delay(800)
                    playing = True
                    how_to = False
            if e.type == pygame.MOUSEBUTTONDOWN and in_how_clicked == False:
                in_how_pos1 = pygame.mouse.get_pos()
                if 27 <= in_how_pos1[0] <= 177 and 55 <= in_how_pos1[1] <= 91:
                    in_how_clicked = True
                if 695 <= in_how_pos1[0] <= 845 and 785 <= in_how_pos1[1] <= 821:
                    in_how_clicked = True
            if e.type == pygame.MOUSEBUTTONUP and in_how_clicked:
                in_how_pos2 = pygame.mouse.get_pos()
                if 27 <= in_how_pos2[0] <= 177 and 55 <= in_how_pos2[1] <= 91:
                    in_how_clicked = False
                    main_menu = True
                    how_to = False
                if 695 <= in_how_pos2[0] <= 845 and 785 <= in_how_pos2[1] <= 821:
                    in_how_clicked = False
                    playing = True
                    how_to = False


        screen.blit(menu_bg, (0, 0))
        screen.blit(how_to_menu, how_to_menu.get_rect(center=(screen_width / 2, 85)))
        for idx, how_to_text in enumerate(how_to_texts):
            how_to_text_render = how_to_font.render(how_to_text, True, (0, 0, 0))
            screen.blit(how_to_text_render, (50, 180 + 40 * idx))

        to_main = how_to_menu_font.render("< 메인으로", True, (0, 0, 0))
        letsplay = how_to_menu_font.render("게임시작 >", True, (0, 0, 0))
        screen.blit(to_main, (30, 50))
        screen.blit(letsplay, (700, 780))
        # create_box(27, 55, 150, 36)  # 메인으로 box
        # create_box(695, 785, 150, 36)  # 게임시작 box
        pygame.display.update()

    while playing:
        dt = clock.tick(60)
        # 이벤트 처리(키보드, 마우스 등)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    reset_setting()
                    main_menu = True
                    playing = False
            if e.type == pygame.MOUSEBUTTONDOWN and playing_clicked == False:
                mouse_pos1 = pygame.mouse.get_pos()
                if 15 <= mouse_pos1[0] <= 135 and 9 <= mouse_pos1[1] <= 49:
                    playing_clicked = True
                if 803 <= mouse_pos1[0] <= 855 and 9 <= mouse_pos1[1] <= 49:
                    playing_clicked = True
            if e.type == pygame.MOUSEBUTTONUP and playing_clicked:
                mouse_pos2 = pygame.mouse.get_pos()
                if 15 <= mouse_pos2[0] <= 135 and 9 <= mouse_pos2[1] <= 49:
                    playing_clicked = False
                    reset_setting()
                    main_menu = True
                    playing = False
                if 803 <= mouse_pos2[0] <= 855 and 9 <= mouse_pos2[1] <= 49:
                    playing_clicked = False
                    retire = True
                    playing = False

        # 초기 화면에 그리기
        screen.blit(background, (0, 0))
        screen.blit(gametable, ((background_width - gametable_width) / 2, (background_height - gametable_height) / 2))
        screen.blit(white_bar, (0, screen_height - white_bar_height))
        minute = time.localtime().tm_min
        tip = tip_texts[minute % len(tip_texts)]
        game_tip = game_tip_font.render(tip, True, (0, 0, 0))
        screen.blit(game_tip, (5, screen_height - white_bar_height))
        to_main = how_to_font.render("< 메인으로", True, (0, 0, 0))
        retire_text = how_to_font.render("항복", True, (0, 0, 0))
        screen.blit(to_main, to_main.get_rect(center=(75, 27)))
        screen.blit(retire_text, retire_text.get_rect(center=(835, 27)))
        create_box(15, 9, 120, 40)
        create_box(803, 9, 63, 40)

        if player_first:
            screen.blit(blue_turn,
                        blue_turn.get_rect(center=((screen_width - gametable_width) / 4, screen_height / 2 + 100)))
        elif player_first == False:
            screen.blit(red_turn,
                        blue_turn.get_rect(center=((screen_width - gametable_width) / 4, screen_height / 2 - 100)))

        com_score = score_font.render("{}승".format(len(com_win_round)), True, (0, 0, 0))
        player_score = score_font.render("{}승".format(len(player_win_round)), True, (0, 0, 0))
        screen.blit(com_score, com_score.get_rect(center=(screen_width - 50, screen_height / 2 - 200)))
        screen.blit(player_score, player_score.get_rect(center=(screen_width - 50, screen_height / 2 + 200)))

        winner_light()
        print_com_card()
        print_player_card()

        print_com_deck()

        # for idx, card in enumerate(player_deck):
        #     screen.blit(blues_off[card], (45 + (off_width + 15) * idx, 700))

        print_player_deck()

        round_x_pos += speed

        round_text = main_font.render(f"{round}라운드", True, (255, 255, 255))
        screen.blit(round_text, round_text.get_rect(center=(round_x_pos, screen_height / 2)))
        pygame.display.update()

        if round_x_pos == screen_width / 2:
            pygame.time.delay(1000)

        if round_x_pos == screen_width + speed * 10:
            round_on = True

        while round_on:
            # 카드 덱 출력을 위한 가림막
            pygame.display.update()

            pygame.time.delay(1000)
            player_num = None
            com_num = None

            if player_first == False:  # 컴퓨터가 선인 상황
                computer_choose()

                print_com_deck()  # 컴퓨터 카드 덱 업데이트
                print_com_fight()  # 컴퓨터가 낸 카드 올리기

                cover_turn()
                screen.blit(blue_turn,
                            blue_turn.get_rect(center=((screen_width - gametable_width) / 4, screen_height / 2 + 100)))

                pygame.display.update()

                choosing = True
                start_ticks = pygame.time.get_ticks()

                player_choose()

                print_player_deck()  # 플레이어 카드 덱 업데이트

                if playing:
                    print_player_fight()  # 플레이어가 낸 카드 올리기

                pygame.display.update()

            elif player_first:
                choosing = True
                start_ticks = pygame.time.get_ticks()
                player_choose()

                print_player_deck()

                if playing:
                    print_player_fight()

                    pygame.display.update()

                    cover_turn()
                    screen.blit(red_turn,
                                blue_turn.get_rect(center=((screen_width - gametable_width) / 4, screen_height / 2 - 100)))
                    pygame.display.update()

                    computer_choose()
                    pygame.time.delay(1000)

                    print_com_deck()
                    print_com_fight()

                    pygame.display.update()
            # ---------------------------------- 각자 카드 제시 완료 ------------------------------------
            if playing:
                pygame.time.delay(1000)
                # 라운드 승패 학인
                check_round_winner()
                # 컴퓨터가 낸 카드
                print_com_card()
                # 플레이어가 낸 카드
                print_player_card()

            # 승리 표시등
                winner_light()

                pygame.display.update()

                round += 1
                round_x_pos = 0

                pygame.time.delay(1000)

                round_on = False

            if abs(len(com_win_round) - len(player_win_round)) > 10 - round or round > 9:
                ended = True
                playing = False

    while ended or retire:
        screen.blit(background, (0, 0))
        screen.blit(gametable, ((background_width - gametable_width) / 2, (background_height - gametable_height) / 2))
        screen.blit(white_bar, (0, screen_height - white_bar_height))
        minute = time.localtime().tm_min
        tip = tip_texts[minute % len(tip_texts)]
        game_tip = game_tip_font.render(tip, True, (0, 0, 0))
        screen.blit(game_tip, (5, screen_height - white_bar_height))

        com_score = score_font.render("{}승".format(len(com_win_round)), True, (0, 0, 0))
        player_score = score_font.render("{}승".format(len(player_win_round)), True, (0, 0, 0))

        screen.blit(com_score, com_score.get_rect(center=(screen_width - 50, screen_height / 2 - 200)))
        screen.blit(player_score, player_score.get_rect(center=(screen_width - 50, screen_height / 2 + 200)))

        winner_light()
        print_winner()
        open_card()

        replay_button = (100, 700, 200, 100)
        home_button = (580, 700, 200, 100)

        create_box(100, 700, 200, 100)
        create_box(580, 700, 200, 100)
        replay_text = main_font.render("다시하기", True, (0, 0, 0))
        home_text = main_font.render("메인으로", True, (0, 0, 0))
        screen.blit(replay_text, replay_text.get_rect(center=(200, 750)))
        screen.blit(home_text, home_text.get_rect(center=(680, 750)))

        pygame.display.update()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                ended = False
                retire = False
                running = False

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    reset_setting()
                    main_menu = True
                    ended = False

            end_pos = pygame.mouse.get_pos()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if replay_button[0] <= end_pos[0] <= replay_button[0] + replay_button[2] \
                        and replay_button[1] <= end_pos[1] <= replay_button[1] + replay_button[3]:
                    replay_clicked = True
                if home_button[0] <= end_pos[0] <= home_button[0] + home_button[2] \
                        and home_button[1] <= end_pos[1] <= home_button[1] + home_button[3]:
                    home_clicked = True
            if e.type == pygame.MOUSEBUTTONUP and (replay_clicked or home_clicked):
                if replay_button[0] <= end_pos[0] <= replay_button[0] + replay_button[2] \
                        and replay_button[1] <= end_pos[1] <= replay_button[1] + replay_button[3]:
                    reset_setting()
                    pygame.time.delay(800)
                    playing = True
                    ended = False
                if home_button[0] <= end_pos[0] <= home_button[0] + home_button[2] \
                        and home_button[1] <= end_pos[1] <= home_button[1] + home_button[3]:
                    reset_setting()
                    main_menu = True
                    ended = False

        pygame.display.update() # 게임화면 계속 그리기

# 6. 게임 종료
pygame.quit()


# 보완점
# 2. 라운드별 승패 표시
# 3. 홀짝 따로 정렬 / 크기 순으로 정렬
# 4. 정렬 방식 선택 가능
