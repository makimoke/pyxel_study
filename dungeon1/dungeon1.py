import pyxel

TRANSPARENT_COLOR = 2
TILE_WALL = (0, 8)
TILE_STAIRS = (1, 9)

def get_tile(tile_x, tile_y):
    return pyxel.tilemaps[0].pget(tile_x, tile_y)

def is_wall(x, y):
    tile = get_tile(x // 8, y // 8)
    # print("x={0} y={1} tile={2}".format(x,y,tile))
    return tile == TILE_WALL

def is_stairs(x,y):
    tile = get_tile(x // 8, y // 8)
    return tile == TILE_STAIRS

def is_btn_left():
    return pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT) or pyxel.btn(pyxel.KEY_S)

def is_btn_right():
    return pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT) or pyxel.btn(pyxel.KEY_F)

def is_btn_up():
    return pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP) or pyxel.btn(pyxel.KEY_E)

def is_btn_down():
    return pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN) or pyxel.btn(pyxel.KEY_D)


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = self.dy = 0

    def update(self):
        last_x = self.x
        last_y = self.y
        dx = 0
        dy = 0
        if is_btn_left():
            dx -= 1
        if is_btn_right():
            dx += 1
        if is_btn_up():
            dy -= 1
        if is_btn_down():
            dy += 1
        
        if not is_wall(self.x+dx,self.y+dy) and not is_wall(self.x+dx+7,self.y+dy+7):
            self.x = self.x + dx
            self.y = self.y + dy
        else:
            dx = 0
            dy = 0
        
        self.dx = dx
        self.dy = dy

    def draw(self):
        u = 0 if self.dx == 0 and self.dy == 0 else (pyxel.frame_count // 3 % 2 + 1) * 8
        pyxel.blt(self.x, self.y, 0, u, 8, 8, 8, TRANSPARENT_COLOR)

class App:
    def __init__(self):
        pyxel.init(128, 128, title="Dugenon1")
        #pyxel.images[0].load(0, 0, "assets/pyxel_logo_38x16.png")
        pyxel.load("assets/dungeon1.pyxres")

        global player
        player = Player(3*8, 12*8)

        pyxel.run(self.update, self.draw)

    def restart(self):
        player.x = 3*8
        player.y = 12*8

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        player.update()

        if is_stairs(player.x+4,player.y+4):
            self.restart()

    def draw(self):
        pyxel.cls(0)
        #pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count % 16)
        #pyxel.blt(61, 66, 0, 0, 0, 38, 16)
        pyxel.bltm(0, 0, 0, 0, 0, 128, 128)

        player.draw()


App()
