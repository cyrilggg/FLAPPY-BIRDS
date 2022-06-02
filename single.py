# encoding=gbk
import pygame
import random

######################################## �������
MAP_WIDTH = 288  # ��ͼ��С
MAP_HEIGHT = 512
FPS = 30  # ˢ����
PIPE_GAPS = [90, 100, 110, 120, 130, 140]  # ȱ�ڵľ��� ����6���������
# PIPE_GAPS1 = []
PIPE_HEIGHT_RANGE = [int(MAP_HEIGHT * 0.5), int(MAP_HEIGHT * 0.7)]  # �ܵ����ȷ�Χ
PIPE_DISTANCE = 120  # �ܵ�֮�����

######################################## ��Ϸ��������
pygame.init()  # ���г�ʼ��
SCREEN = pygame.display.set_mode((MAP_WIDTH, MAP_HEIGHT))  # ���ô���������Ļ��С
pygame.display.set_caption('FLAPPY BIRD')  # ����
CLOCK = pygame.time.Clock()  # ����ʱ��

######################################## �����ز�
SPRITE_FILE = '.\images\\'
# �б��Ƶ�ʽ ������ֲ�ͬ���������״̬
BIRDS = [[f'{SPRITE_FILE}{bird}bird-{move}flap.png' for move in ['up', 'mid', 'down']] for bird in ['red', 'blue', 'yellow']]
BGPICS = [SPRITE_FILE + 'background-day.png', SPRITE_FILE + 'background-night.png']
PIPES = [SPRITE_FILE + 'pipe-green.png', SPRITE_FILE + 'pipe-red.png']
NUMBERS = [f'{SPRITE_FILE}{n}.png' for n in range(10)]

# ��ͼƬ���ó�һ�����ֵ� ����ͨ��key-value�治ͬ�ĳ���ͼ
IMAGES = {}
IMAGES['numbers'] = [pygame.image.load(number) for number in NUMBERS]  # �����ز���10�� ��˱���
IMAGES['guide'] = pygame.image.load(SPRITE_FILE + 'message.png')
IMAGES['gameover'] = pygame.image.load(SPRITE_FILE + 'gameover.png')
IMAGES['floor'] = pygame.image.load(SPRITE_FILE + 'base.png')

# �ذ�ĸ���һ���ܳ��õı��� �������ר���ó���
FLOOR_H = MAP_HEIGHT - IMAGES['floor'].get_height()  # ��Ļ�߼�ȥfloorͼƬ�ĸ� ����������Ļ���λ��

# ִ�к���
def main():
    while True:
        IMAGES['bgpic'] = pygame.image.load(random.choice(BGPICS))  # random��choice��������������б��ﷵ��һ��Ԫ�� ������ߺ�ҹ
        IMAGES['bird'] = [pygame.image.load(frame) for frame in random.choice(BIRDS)]  # �б��Ƶ�ʽ ��Ҳ�����
        pipe = pygame.image.load(random.choice(PIPES))
        IMAGES['pipe'] = [pipe, pygame.transform.flip(pipe, False, True)]  # flip�Ƿ�ת ���ܵ������������ Flaseˮƽ������True���·�ת
        menu_window()
        result = game_window()
        end_window(result)


def menu_window():
    floor_gap = IMAGES['floor'].get_width() - MAP_WIDTH  # �ذ��϶ 336 - 288 = 48
    floor_x = 0

    # ����λ��
    guide_x = (MAP_WIDTH - IMAGES['guide'].get_width()) / 2
    guide_y = MAP_HEIGHT * 0.12

    # С��λ��
    bird_x = MAP_WIDTH * 0.2
    bird_y = MAP_HEIGHT * 0.5 - IMAGES['bird'][0].get_height() / 2
    bird_y_vel = 1  # С����е����� ��y��������
    max_y_shift = 50  # С����е�������
    y_shift = 0  # С����ʼ����Ϊ0

    idx = 0  # С����ɿ��Ƶ��
    frame_seq = [0] * 5 + [1] * 5 + [2] * 5 + [1] * 5  # ����С�����˶�������

    while True:
        for event in pygame.event.get():  # �����Ϊ
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return

        if floor_x <= -floor_gap:  # ���ذ��ܵ��������ʱ��
            floor_x = floor_x + floor_gap  # ˢ�µذ��x��
        else:
            floor_x -= 4  # �ذ� x����ƶ��ٶ�

        if abs(y_shift) == max_y_shift:  # ���y_shift�ľ���ֵ = ������
            bird_y_vel *= -1  # ��ת����� ͬʱ�����ٶ�Ϊ1
        else:
            bird_y += bird_y_vel
        y_shift += bird_y_vel  # С��y���������� ���·�

        # С����
        idx += 1  # ���ɿ��Ƶ��
        idx %= len(frame_seq)  # ͨ��ȡ��õ� 0 1 2
        frame_index = frame_seq[idx]  # С��ͼƬ���±� ���ǳ���״̬

        SCREEN.blit(IMAGES['bgpic'], (0, 0))
        SCREEN.blit(IMAGES['floor'], (floor_x, FLOOR_H))
        SCREEN.blit(IMAGES['guide'], (guide_x, guide_y))
        SCREEN.blit(IMAGES['bird'][frame_index], (bird_x, bird_y))

        pygame.display.update()
        CLOCK.tick(FPS)  # ��ÿ��30֡ˢ����Ļ


def game_window():
    score = 0

    floor_gap = IMAGES['floor'].get_width() - MAP_WIDTH  # �ذ��϶ 336 - 288 = 48
    floor_x = 0

    # С��λ��
    bird_x = MAP_WIDTH * 0.2
    bird_y = MAP_HEIGHT * 0.5 - IMAGES['bird'][0].get_height() / 2
    bird = Bird(bird_x, bird_y)

    n_pair = round(MAP_WIDTH / PIPE_DISTANCE)  # ��������ȡ���� ��Ļ���/�����ܵ�֮��ľ��� �������ʱ��ˢ�µڶ����ܵ�  2.4
    pipe_group = pygame.sprite.Group()  # ��һ������

    # ����ǰ��Ĺܵ�
    pipe_x = MAP_WIDTH
    pipe_y = random.randint(PIPE_HEIGHT_RANGE[0], PIPE_HEIGHT_RANGE[1])  # �ܵ����������153.6 �� 358.4
    pipe1 = Pipe(pipe_x, pipe_y, upwards=True)  # ����һ���ܵ�����
    pipe_group.add(pipe1)  # ��������ӵ�������鼯������
    pipe2 = Pipe(pipe_x, pipe_y - random.choice(PIPE_GAPS), upwards=False)  # ��ת�Ĺܵ�
    pipe_group.add(pipe2)


    while True:
        flap = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # �ո��ĳ��
                flap = True

        bird.update(flap)

        if floor_x <= -floor_gap:  # ���ذ��ܵ��������ʱ��
            floor_x = floor_x + floor_gap  # ˢ�µذ��x��
        else:
            floor_x -= 4  # �ذ� x����ƶ��ٶ�

        # �������һ���ܵ�
        if len(pipe_group) / 2 < n_pair:  # ���ܵ��鳤��<2.4 ʱ ��˼����������ܵ���ʱ��
            # sprites()���ܵ��鷵�س��б�
            last_pipe = pipe_group.sprites()[-1]
            pipe_x = last_pipe.rect.right + PIPE_DISTANCE
            pipe_y = random.randint(PIPE_HEIGHT_RANGE[0], PIPE_HEIGHT_RANGE[1])
            pipe1 = Pipe(pipe_x, pipe_y, upwards=True)
            pipe_group.add(pipe1)
            pipe2 = Pipe(pipe_x, pipe_y - random.choice(PIPE_GAPS), upwards=False)
            pipe_group.add(pipe2)

        pipe_group.update()
        # ��ľ���y����������ڵذ�ĸ߶� ������
        # pygame.sprite.spritecollideany ��ײ���� ���bird��pipe_group��ײ�� ������
        if bird.rect.y > FLOOR_H or bird.rect.y < 0 or pygame.sprite.spritecollideany(bird, pipe_group):
            # ��������ʱ����� ���� �ܵ� ������ʾ�ڽ�������
            result = {'bird': bird, 'score': score, 'pipe_group': pipe_group}
            return result

        # ��С����ߴ��� �ܵ��ұ߾͵÷�
        if pipe_group.sprites()[0].rect.left == 0:
            score += 1

        SCREEN.blit(IMAGES['bgpic'], (0, 0))
        pipe_group.draw(SCREEN)
        SCREEN.blit(IMAGES['floor'], (floor_x, FLOOR_H))
        SCREEN.blit(bird.image, bird.rect)
        show_score(score)
        pygame.display.update()
        CLOCK.tick(FPS)


def end_window(result):
    # ��ʾgameover��ͼƬ
    gameover_x = MAP_WIDTH * 0.5 - IMAGES['gameover'].get_width() / 2
    gameover_y = MAP_HEIGHT * 0.4
    bird = result['bird']
    pipe_group = result['pipe_group']

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and bird.rect.y > FLOOR_H:
                return

        # ʹ����go_die���� ���ײǽ�� ��ת����
        bird.go_die()
        SCREEN.blit(IMAGES['bgpic'], (0, 0))
        pipe_group.draw(SCREEN)
        SCREEN.blit(IMAGES['floor'], (0, FLOOR_H))
        SCREEN.blit(IMAGES['gameover'], (gameover_x, gameover_y))
        show_score(result['score'])
        SCREEN.blit(bird.image, bird.rect)
        pygame.display.update()
        CLOCK.tick(FPS)


# ��ʾ�÷�
def show_score(score):
    score_str = str(score)
    w = IMAGES['numbers'][0].get_width()
    x = MAP_WIDTH / 2 - 2 * w / 2
    y = MAP_HEIGHT * 0.1
    for number in score_str:  # IMAGES['numbers'] = [pygame.image.load(number) for number in NUMBERS]
        SCREEN.blit(IMAGES['numbers'][int(number)], (x, y))
        x += w


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # super(Bird, self).__init__(x, y)
        pygame.sprite.Sprite.__init__(self)
        self.gameover = 0
        self.score = 0
        self.frames = IMAGES['bird']  # ������
        self.frame_list = [0] * 5 + [1] * 5 + [2] * 5 + [1] * 5  # ����С�����˶�������
        self.frame_index = 0
        self.image = self.frames[self.frame_list[self.frame_index]]  # �Ͳ˵�����С���ȳ��һ��ԭ��
        self.rect = self.image.get_rect()  # ����ľ���
        self.rect.x = x
        self.rect.y = y
        self.gravity = 1  # ����
        self.flap_acc = -10  # ����Ĵ����Ϸ� y����-10
        self.y_vel = -10  # y������ٶ�
        self.max_y_vel = 15  # y����������ٶ�
        self.rotate = 0  # �Դ�����
        self.rotate_vel = -3  # ת���ٶ�
        self.max_rotate = -30  # ���ת���ٶ�
        self.flap_rotate = 45  # ���˿ո�ֻ���Դ�������30��

    def update(self, flap=False):
        if flap:
            self.y_vel = self.flap_acc  # �Ĵ��� ��y�ٶ�-10����
            self.rotate = self.flap_rotate
        else:
            self.rotate = self.rotate + self.rotate_vel

        self.y_vel = min(self.y_vel + self.gravity, self.max_y_vel)
        self.rect.y += self.y_vel  # С�������ƶ��ľ���
        self.rorate = max(self.rotate + self.rotate_vel, self.max_rotate)

        self.frame_index += 1  # �ȳ�������
        self.frame_index %= len(self.frame_list)  # 0~20
        self.image = self.frames[self.frame_list[self.frame_index]]
        self.image = pygame.transform.rotate(self.image, self.rotate)  # transform���η��� ��ת

    def go_die(self):
        if self.rect.y < FLOOR_H:
            self.y_vel = self.max_y_vel
            self.rect.y += self.y_vel
            self.rotate = -90
            self.image = self.frames[self.frame_list[self.frame_index]]
            self.image = pygame.transform.rotate(self.image, self.rotate)


# �ܵ���
class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, upwards=True):
        pygame.sprite.Sprite.__init__(self)
        self.x_vel = -4  # �ܵ��ƶ��ٶ�
        # Ĭ������Ϊ�� ��������ܵ�
        if upwards:
            self.image = IMAGES['pipe'][0]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.top = y
        # ����flip���� ��ת�ܵ���Ϊ����ܵ�
        else:
            self.image = IMAGES['pipe'][1]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.bottom = y

    def update(self):
        self.rect.x += self.x_vel  # �ܵ�x����ƶ��ٶ�
        if self.rect.right < 0:
            self.kill()

if __name__ == '__main__':
    main()