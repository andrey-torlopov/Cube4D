
class ScreenConfig:
    def __init__(self, width: int = 800, height: int = 640,
                 title: str = "4D cube", rotate_speed: float = 0.02, background: tuple[int, int, int] = (255, 255, 255),
                 scale: float = 50, angle_x: float = 0, angle_y: float = 0, angle_z: float = 0, fps: int = 60,
                 distance: int = 2) -> None:
        '''
        Screen configuration
        '''
        self.background = background
        self.rotate_speed = rotate_speed
        self.red = (255, 100, 0, 100)
        self.black = (0, 0, 0)
        self.width = width
        self.height = height
        self.title = title
        self.scale = scale
        self.angle_x = angle_x
        self.angle_y = angle_y
        self.angle_z = angle_z
        self.fps = fps
        self.distance = distance

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

    def inc_angle_x(self):
        self.angle_x += self.rotate_speed

    def inc_angle_y(self):
        self.angle_y += self.rotate_speed

    def inc_angle_z(self):
        self.angle_z += self.rotate_speed

    def dec_angle_x(self):
        self.angle_x -= self.rotate_speed

    def dec_angle_y(self):
        self.angle_y -= self.rotate_speed

    def dec_angle_z(self):
        self.angle_z -= self.rotate_speed

    @property
    def anglesXYZ(self) -> tuple[float, float, float]:
        return (self.angle_x, self.angle_y, self.angle_z)
