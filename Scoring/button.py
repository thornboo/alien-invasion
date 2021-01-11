import pygame.font


class Button():
    def __init__(self, ai_settings, screen, msg):
        """初始化按钮的属性"""
        self.screen = screen
        self.ai_settings = ai_settings
        self.screen_rect = screen.get_rect()

        # 设置按钮的尺寸和其他属性
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)  # 按钮颜色(亮绿色)
        self.text_color = (255, 255, 255)  # 文本颜色(白色)
        self.font = pygame.font.SysFont(None, 48)  # 设置字体和字号(None表示使用pygame默认字体)

        # 创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 按钮的标签只创建一次
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """将msg渲染为图像，并使其在按钮上剧中"""
        # font.render()可以将文本转换成图像,第二个形参为抗锯齿,余下两个分别是文本颜色和背景色,若没有指定背景色将使用透明背景。
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """绘制一个用颜色填充的按钮，再绘制文本"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
