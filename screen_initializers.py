
class ScreenConfig:
    def __init__(self, width: int = 1020, height: int = 768,
                 title: str = "4D cube",
                 rotate_speed: float = 0.02,
                 stroke_color: tuple[int, int, int] = (255, 255, 255),
                 scale: float = 200,
                 min_scale: float = 100,
                 max_scale: float = 300,
                 angle_x: float = 0,
                 angle_y: float = 0,
                 angle_z: float = 0,
                 angle_w: float = 0,
                 fps: int = 60,
                 distance: int = 2.5) -> None:
        '''
        Screen configuration
        '''
        self.stroke_color = stroke_color
        self.rotate_speed = rotate_speed
        self.red = (255, 100, 0, 100)
        self.black = (43, 43, 43)
        self.width = width
        self.height = height
        self.title = title
        self.scale = scale
        self.angle_x = angle_x
        self.angle_y = angle_y
        self.angle_z = angle_z
        self.angle_w = angle_w
        self.fps = fps
        self.distance = distance
        self.max_scale = max_scale
        self.min_scale = min_scale

    @property
    def screen_size(self) -> tuple[int, int]:
        return (self.width, self.height)

    @property
    def center(self) -> tuple[int, int]:
        return (self.width // 2, self.height // 2)

    def refresh(self):
        self.angle_x = 0
        self.angle_y = 0
        self.angle_z = 0
        self.angle_w = 0

    def inc_angle_x(self):
        self.angle_x += self.rotate_speed

    def inc_angle_y(self):
        self.angle_y += self.rotate_speed

    def inc_angle_z(self):
        self.angle_z += self.rotate_speed

    def inc_angle_w(self) -> None:
        self.angle_w += self.rotate_speed

    def dec_angle_x(self):
        self.angle_x -= self.rotate_speed

    def dec_angle_y(self):
        self.angle_y -= self.rotate_speed

    def dec_angle_z(self):
        self.angle_z -= self.rotate_speed

    def dec_angle_w(self) -> None:
        self.angle_w -= self.rotate_speed

    def inc_scale(self):
        self.scale += 1
        if self.scale > self.max_scale:
            self.scale = self.max_scale

    def dec_scale(self):
        self.scale -= 1
        if self.scale < self.min_scale:
            self.scale = self.min_scale

    @property
    def angles(self) -> tuple[float, float, float, float]:
        return (self.angle_x, self.angle_y, self.angle_z, self.angle_w)
