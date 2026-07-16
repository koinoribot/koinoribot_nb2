from typing import Any, Tuple, Optional, Union, List, Literal
from io import BytesIO
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
import asyncio
import base64
from matplotlib import pyplot as plt

# https://www.osgeo.cn/pillow

FONT_PATH = os.path.join(os.path.dirname(__file__), "src/fonts")
_CENTER_TYPE_ERROR = "center_type must be 'center', 'by_width' or 'by_height'"
_LEGACY_MARK_IMAGE_ATTRIBUTE = "mark" + "Img"
_BUILD_IMAGE_OPTION_NAMES = (
    "paste_image_width",
    "paste_image_height",
    "color",
    "image_mode",
    "font_size",
    "background",
    "font",
    "ratio",
    "is_alpha",
    "plain_text",
    "multiline_text",
    "font_color",
    "stroke_width",
    "stroke_fill",
)
_BUILD_IMAGE_OPTION_DEFAULTS = {
    "paste_image_width": 0,
    "paste_image_height": 0,
    "color": None,
    "image_mode": "RGBA",
    "font_size": 10,
    "background": None,
    "font": "yz.ttf",
    "ratio": 1,
    "is_alpha": False,
    "plain_text": None,
    "multiline_text": None,
    "font_color": None,
    "stroke_width": 0,
    "stroke_fill": (0, 0, 0, 0),
}


def _resolve_build_image_options(
    positional_options: tuple[Any, ...],
    keyword_options: dict[str, Any],
) -> dict[str, Any]:
    if len(positional_options) > len(_BUILD_IMAGE_OPTION_NAMES):
        expected = len(_BUILD_IMAGE_OPTION_NAMES) + 2
        received = len(positional_options) + 2
        raise TypeError(
            f"BuildImage expected at most {expected} positional arguments, "
            f"got {received}"
        )

    positional = dict(zip(_BUILD_IMAGE_OPTION_NAMES, positional_options))
    duplicates = positional.keys() & keyword_options.keys()
    if duplicates:
        duplicate = sorted(duplicates)[0]
        raise TypeError(f"BuildImage got multiple values for argument '{duplicate}'")

    unknown = keyword_options.keys() - _BUILD_IMAGE_OPTION_DEFAULTS.keys()
    if unknown:
        option = sorted(unknown)[0]
        raise TypeError(f"BuildImage got an unexpected keyword argument '{option}'")

    return _BUILD_IMAGE_OPTION_DEFAULTS | positional | keyword_options

def alpha2white_pil(pic: Image) -> Image:
    """
    说明：
        将图片透明背景转化为白色
    参数：
        :param pic: 通过PIL打开的图片文件
    """
    img = pic.convert("RGBA")
    width, height = img.size
    for yh in range(height):
        for xw in range(width):
            dot = (xw, yh)
            color_d = img.getpixel(dot)
            if color_d[3] == 0:
                color_d = (255, 255, 255, 255)
                img.putpixel(dot, color_d)
    return img


def pic2b64(pic: Image) -> str:
    """
    说明：
        PIL图片转base64
    参数：
        :param pic: 通过PIL打开的图片文件
    """
    buf = BytesIO()
    pic.save(buf, format="PNG")
    base64_str = base64.b64encode(buf.getvalue()).decode()
    return "base64://" + base64_str


def fig2b64(plt_: plt) -> str:
    """
    说明：
        matplotlib图片转base64
    参数：
        :param plt_: matplotlib生成的图片
    """
    buf = BytesIO()
    plt_.savefig(buf, format="PNG", dpi=100)
    base64_str = base64.b64encode(buf.getvalue()).decode()
    return "base64://" + base64_str


def is_valid(file: str) -> bool:
    """
    说明：
        判断图片是否损坏
    参数：
        :param file: 图片文件路径
    """
    valid = True
    try:
        Image.open(file).load()
    except OSError:
        valid = False
    return valid


class BuildImage:
    """
    快捷生成图片与操作图片的工具类
    """

    def __getattr__(self, name: str):
        if name == _LEGACY_MARK_IMAGE_ATTRIBUTE:
            return self.mark_img
        raise AttributeError(name)

    def __setattr__(self, name: str, value):
        if name == _LEGACY_MARK_IMAGE_ATTRIBUTE:
            name = "mark_img"
        object.__setattr__(self, name, value)

    def __init__(
        self,
        w: int,
        h: int,
        *positional_options: Any,
        **keyword_options: Any,
    ):
        """
        参数：
            :param w: 自定义图片的宽度，w=0时为图片原本宽度
            :param h: 自定义图片的高度，h=0时为图片原本高度
            :param paste_image_width: 当图片做为背景图时，设置贴图的宽度，用于贴图自动换行
            :param paste_image_height: 当图片做为背景图时，设置贴图的高度，用于贴图自动换行
            :param color: 生成图片的颜色
            :param image_mode: 图片的类型
            :param font_size: 文字大小
            :param background: 打开图片的路径
            :param font: 字体，默认在 resource/ttf/ 路径下
            :param ratio: 倍率压缩
            :param is_alpha: 是否背景透明
            :param plain_text: 纯文字文字
            :param multiline_text: 多行文字
            :param stroke_width: 为文字描边 (魔改)
            :param stroke_fill: 描边的颜色填充 (魔改)
        """
        options = _resolve_build_image_options(
            positional_options,
            keyword_options,
        )
        paste_image_width = options["paste_image_width"]
        paste_image_height = options["paste_image_height"]
        color = options["color"]
        image_mode = options["image_mode"]
        font_size = options["font_size"]
        background = options["background"]
        font = options["font"]
        ratio = options["ratio"]
        is_alpha = options["is_alpha"]
        plain_text = options["plain_text"]
        multiline_text = options["multiline_text"]
        font_color = options["font_color"]
        stroke_width = options["stroke_width"]
        stroke_fill = options["stroke_fill"]

        self.multi_textsize = None  # 测量多行文本得到的长宽
        self.w = int(w)
        self.h = int(h)
        self.paste_image_width = int(paste_image_width)
        self.paste_image_height = int(paste_image_height)
        self.current_w = 0
        self.current_h = 0
        self.font = ImageFont.truetype(str(os.path.join(FONT_PATH, font)), int(font_size))
        if not plain_text and not color:
            color = (255, 255, 255)
        self.background = background
        if background:
            w, h = self._open_background(background, w, h, ratio)
        else:
            self._create_blank_image(
                color,
                image_mode,
                plain_text,
                multiline_text,
                stroke_width,
            )
        if is_alpha:
            self._make_near_white_transparent(w, h)
        self.draw = ImageDraw.Draw(self.mark_img)
        self.size = self.w, self.h
        self._draw_initial_text(
            plain_text,
            multiline_text,
            font_color,
            stroke_width,
            stroke_fill,
        )
        self.loop = self._get_event_loop()

    def _create_blank_image(
        self,
        color,
        image_mode: str,
        plain_text: Optional[str],
        multiline_text: Optional[str],
        stroke_width: int,
    ) -> None:
        if plain_text:
            color = color or (255, 255, 255, 0)
            self._expand_for_text(self.getsize(plain_text), stroke_width)
        elif multiline_text:
            color = color or (255, 255, 255, 0)
            self._expand_for_text(
                self.getsize_multiline(multiline_text),
                stroke_width,
            )
            self.h += 4
        self.mark_img = Image.new(image_mode, (self.w, self.h), color)
        self.mark_img.convert(image_mode)

    def _expand_for_text(
        self,
        text_size: Tuple[int, int],
        stroke_width: int,
    ) -> None:
        text_width, text_height = text_size
        self.w = max(self.w, text_width)
        self.h = max(self.h, text_height)
        if stroke_width:
            self.w += stroke_width * 2
            self.h += stroke_width * 2

    def _open_background(
        self,
        background: Union[str, BytesIO, Path],
        requested_w: int,
        requested_h: int,
        ratio: float,
    ) -> Tuple[int, int]:
        if requested_w or requested_h:
            self.mark_img = Image.open(background).resize(
                (self.w, self.h),
                Image.LANCZOS,
            )
            return requested_w, requested_h

        self.mark_img = Image.open(background)
        image_w, image_h = self.mark_img.size
        if ratio and ratio > 0 and ratio != 1:
            self.w = int(ratio * image_w)
            self.h = int(ratio * image_h)
            self.mark_img = self.mark_img.resize(
                (self.w, self.h),
                Image.LANCZOS,
            )
        else:
            self.w = image_w
            self.h = image_h
        return image_w, image_h

    def _make_near_white_transparent(self, width: int, height: int) -> None:
        pixels = self.mark_img.load()
        for x in range(width):
            for y in range(height):
                pixel = pixels[x, y]
                try:
                    is_near_white = all(channel > 240 for channel in pixel[:3])
                except TypeError:
                    is_near_white = False
                if is_near_white:
                    pixels[x, y] = (255, 255, 255, 0)

    def _draw_initial_text(
        self,
        plain_text: Optional[str],
        multiline_text: Optional[str],
        font_color,
        stroke_width: int,
        stroke_fill,
    ) -> None:
        fill = font_color or (0, 0, 0)
        if plain_text:
            self.text(
                (stroke_width, 0),
                plain_text,
                fill,
                stroke_fill=stroke_fill,
                stroke_width=stroke_width,
            )
        elif multiline_text:
            self.multiline_text((0, 0), multiline_text, fill)

    @staticmethod
    def _get_event_loop() -> asyncio.AbstractEventLoop:
        try:
            return asyncio.get_event_loop()
        except RuntimeError:
            new_loop = asyncio.new_event_loop()
            asyncio.set_event_loop(new_loop)
            return asyncio.get_event_loop()

    async def apaste(
        self,
        img: Union["BuildImage", Image.Image],
        pos: Tuple[int, int] = None,
        alpha: bool = False,
        center_type: Optional[Literal["center", "by_height", "by_width"]] = None,
    ):
        """
        说明：
            异步 贴图
        参数：
            :param img: 已打开的图片文件，可以为 BuildImage 或 Image
            :param pos: 贴图位置（左上角）
            :param alpha: 图片背景是否为透明
            :param center_type: 居中类型，可能的值 center: 完全居中，by_width: 水平居中，by_height: 垂直居中
        """
        await self.loop.run_in_executor(None, self.paste, img, pos, alpha, center_type)

    def paste(
        self,
        img: Union["BuildImage", Image.Image],
        pos: Tuple[int, int] = None,
        alpha: bool = False,
        center_type: Optional[Literal["center", "by_height", "by_width"]] = None,
    ):
        """
        说明：
            贴图
        参数：
            :param img: 已打开的图片文件，可以为 BuildImage 或 Image
            :param pos: 贴图位置（左上角）
            :param alpha: 图片背景是否为透明
            :param center_type: 居中类型，可能的值 center: 完全居中，by_width: 水平居中，by_height: 垂直居中
        """
        if center_type:
            pos = self._centered_position(img, pos, center_type)
        if isinstance(img, BuildImage):
            img = img.mark_img
        if self.current_w == self.w:
            self.current_w = 0
            self.current_h += self.paste_image_height
        if not pos:
            pos = (self.current_w, self.current_h)
        self._paste_image(img, pos, alpha)
        self.current_w += self.paste_image_width

    def _centered_position(
        self,
        img: Union["BuildImage", Image.Image],
        pos: Optional[Tuple[int, int]],
        center_type: Literal["center", "by_height", "by_width"],
    ) -> Tuple[int, int]:
        if center_type not in {"center", "by_height", "by_width"}:
            raise ValueError(_CENTER_TYPE_ERROR)

        base_x, base_y = pos or (0, 0)
        image_w, image_h = (
            (img.w, img.h)
            if isinstance(img, BuildImage)
            else img.size
        )
        centered_x = int((self.w - image_w) / 2)
        centered_y = int((self.h - image_h) / 2)
        if center_type == "center":
            return centered_x, centered_y
        if center_type == "by_width":
            return centered_x, base_y
        return base_x, centered_y

    def _paste_image(
        self,
        img: Image.Image,
        pos: Tuple[int, int],
        alpha: bool,
    ) -> None:
        if not alpha:
            self.mark_img.paste(img, pos)
            return
        try:
            self.mark_img.paste(img, pos, img)
        except ValueError:
            rgba_image = img.convert("RGBA")
            self.mark_img.paste(rgba_image, pos, rgba_image)

    def getsize(self, msg: str) -> Tuple[int, int]:
        """
        说明：
            获取文字在该图片 font_size 下所需要的空间
        参数：
            :param msg: 文字内容
        """
        ascent, descent = self.font.getmetrics()
        return (int(self.font.getlength(msg)), ascent + descent)


    def getsize_multiline(self, msg: str) -> Tuple[int, int]:
        """
        说明：
            获取多行文本在该图片 font_size 下需要的空间
        参数：
            :param msg: 文字内容
        """
        lines = msg.split("\n")
        ascent, descent = self.font.getmetrics()
        line_height = ascent + descent
        spacing = 4
        max_width = max((int(self.font.getlength(line)) for line in lines), default=0)
        return (max_width, line_height * len(lines) + spacing * (len(lines) - 1))


    async def apoint(
        self, pos: Tuple[int, int], fill: Optional[Tuple[int, int, int]] = None
    ):
        """
        说明：
            异步 绘制多个或单独的像素
        参数：
            :param pos: 坐标
            :param fill: 填错颜色
        """
        await self.loop.run_in_executor(None, self.point, pos, fill)

    def point(self, pos: Tuple[int, int], fill: Optional[Tuple[int, int, int]] = None):
        """
        说明：
            绘制多个或单独的像素
        参数：
            :param pos: 坐标
            :param fill: 填错颜色
        """
        self.draw.point(pos, fill=fill)

    async def aellipse(
        self,
        pos: Tuple[int, int, int, int],
        fill: Optional[Tuple[int, int, int]] = None,
        outline: Optional[Tuple[int, int, int]] = None,
        width: int = 1,
    ):
        """
        说明：
            异步 绘制圆
        参数：
            :param pos: 坐标范围
            :param fill: 填充颜色
            :param outline: 描线颜色
            :param width: 描线宽度
        """
        await self.loop.run_in_executor(None, self.ellipse, pos, fill, outline, width)

    def ellipse(
        self,
        pos: Tuple[int, int, int, int],
        fill: Optional[Tuple[int, int, int]] = None,
        outline: Optional[Tuple[int, int, int]] = None,
        width: int = 1,
    ):
        """
        说明：
            绘制圆
        参数：
            :param pos: 坐标范围
            :param fill: 填充颜色
            :param outline: 描线颜色
            :param width: 描线宽度
        """
        self.draw.ellipse(pos, fill, outline, width)

    async def atext(
        self,
        pos: Union[Tuple[int, int], Tuple[float, float]],
        text: str,
        fill: Union[str, Tuple[int, int, int]] = (0, 0, 0),
        center_type: Optional[Literal["center", "by_height", "by_width"]] = None,
    ):
        """
        说明：
            异步 在图片上添加文字
        参数：
            :param pos: 文字位置
            :param text: 文字内容
            :param fill: 文字颜色
            :param center_type: 居中类型，可能的值 center: 完全居中，by_width: 水平居中，by_height: 垂直居中
        """
        await self.loop.run_in_executor(None, self.text, pos, text, fill, center_type)

    def text(
        self,
        pos: Union[Tuple[int, int], Tuple[float, float]],
        text: str,
        fill: Union[str, Tuple[int, int, int]] = (0, 0, 0),
        center_type: Optional[Literal["center", "by_height", "by_width"]] = None,

        stroke_width: int = 0,
        stroke_fill: Union[Tuple[int, int, int, int], Tuple[int, int, int]] = (0, 0, 0, 0),
        align: Literal["left", "center", "right"] = 'left',
        anchor: str = None,

    ):
        """
        说明：
            在图片上添加文字(单行)
        参数：
            :param pos: 文字位置
            :param text: 文字内容
            :param fill: 文字颜色
            :param anchor: 文字对齐方式，详见：https://pillow.readthedocs.io/en/stable/handbook/text-anchors.html#text-anchors
            :param center_type: 居中类型，可能的值 center: 完全居中，by_width: 水平居中，by_height: 垂直居中
            :param stroke_width: 描边粗细
            :param stroke_fill: 描边填充
            :param align: 对齐方式
        """
        if center_type:
            if center_type not in ["center", "by_height", "by_width"]:
                raise ValueError(_CENTER_TYPE_ERROR)
            w, h = self.w, self.h
            ttf_w, ttf_h = self.getsize(text)
            if center_type == "center":
                w = int((w - ttf_w) / 2)
                h = int((h - ttf_h) / 2)
            elif center_type == "by_width":
                w = int((w - ttf_w) / 2)
                h = pos[1]
            elif center_type == "by_height":
                h = int((h - ttf_h) / 2)
                w = pos[0]
            pos = (w, h)
        self.draw.text(pos, text, fill=fill, font=self.font, stroke_fill=stroke_fill, stroke_width=stroke_width, align=align, anchor=anchor)


    def multiline_text(
        self,
        pos: Union[Tuple[int, int], Tuple[float, float]],
        text: str,
        fill: Union[str, Tuple[int, int, int]] = (0, 0, 0),
        center_type: Optional[Literal["center", "by_height", "by_width"]] = None,

        stroke_width: int = 0,
        stroke_fill: Union[Tuple[int, int, int, int], Tuple[int, int, int]] = (0, 0, 0, 0),
        align: Literal["left", "center", "right"] = 'left',
        anchor: str = None,

    ):
        """
        说明：
            在图片上添加文字(多行)
        参数：
            :param pos: 文字位置
            :param text: 文字内容
            :param fill: 文字颜色
            :param anchor: 文字对齐方式，详见：https://pillow.readthedocs.io/en/stable/handbook/text-anchors.html#text-anchors
            :param center_type: 居中类型，可能的值 center: 完全居中，by_width: 水平居中，by_height: 垂直居中
            :param stroke_width: 描边粗细
            :param stroke_fill: 描边填充
            :param align: 对齐方式
        """
        if center_type:
            if center_type not in ["center", "by_height", "by_width"]:
                raise ValueError(_CENTER_TYPE_ERROR)
            w, h = self.w, self.h
            ttf_w, ttf_h = self.getsize_multiline(text)
            if center_type == "center":
                w = int((w - ttf_w) / 2)
                h = int((h - ttf_h) / 2)
            elif center_type == "by_width":
                w = int((w - ttf_w) / 2)
                h = pos[1]
            elif center_type == "by_height":
                h = int((h - ttf_h) / 2)
                w = pos[0]
            pos = (w, h)
        self.draw.multiline_text(pos, text, fill=fill, font=self.font, stroke_fill=stroke_fill, stroke_width=stroke_width, align=align, anchor=anchor)


    def get_multi_size(
        self,
        pos: Union[Tuple[int, int], Tuple[float, float]],
        text: str,
        stroke_width: int = 0,
        align: Literal["left", "center", "right"] = 'left',
        anchor: str = None,
        spacing: int = 4,
    ):
        """
            pos -- 文本的锚点坐标。
            text -- 要测量的文本。
            font -- A FreeTypeFont 实例。
            anchor -- 文本锚点对齐方式。确定锚点相对于文本的相对位置。默认对齐方式为左上角。看见 文本锚点 有效值。对于非TrueType字体，此参数将被忽略。
            spacing -- 行与行之间的像素数。
            align -- "left" ， "center" 或 "right" 。确定线条的相对对齐方式。使用 anchor 参数指定对齐方式。 xy 。
            direction -- 文本的方向。它可以 "rtl" （从右到左）， "ltr" （从左到右）或 "ttb" （从上到下）。需要QMLibra。【无】
            features -- 文本布局期间使用的OpenType字体功能的列表。例如，这通常用于打开默认情况下未启用的可选字体功能 "dlig" 或 "ss01" ，但也可以用于关闭默认字体功能，例如 "-liga" 禁用连字或 "-kern" 禁用字距调整。要获取所有支持的功能，请参阅 OpenType docs . 需要QMLibra。【无】
            language -- 文本的语言。不同的语言可以使用不同的字形或连字。此参数告诉文本使用哪种语言的字体，并根据需要应用正确的替换（如果可用）。应该是一个 BCP 47 language code . 需要QMLibra。【无】
            stroke_width -- 文本笔划的宽度。
            embedded_color -- 是否使用字体嵌入颜色字形(COLR、CBDT、SBIX)。【无】
        """
        text_bbox = self.draw.multiline_textbbox(pos, text, font=self.font, stroke_width=stroke_width, align=align, anchor=anchor, spacing=spacing)
        self.multi_textsize = (text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1])
        return self.multi_textsize

    async def asave(self, path: Optional[Union[str, Path]] = None):
        """
        说明：
            异步 保存图片
        参数：
            :param path: 图片路径
        """
        await self.loop.run_in_executor(None, self.save, path)

    def save(self, path: Optional[Union[str, Path]] = None):
        """
        说明：
            保存图片
        参数：
            :param path: 图片路径
        """
        if not path:
            path = self.background
        self.mark_img.save(path)

    def show(self):
        """
        说明：
            显示图片
        """
        self.mark_img.show(self.mark_img)

    async def aresize(self, ratio: float = 0, w: int = 0, h: int = 0):
        """
        说明：
            异步 压缩图片
        参数：
            :param ratio: 压缩倍率
            :param w: 压缩图片宽度至 w
            :param h: 压缩图片高度至 h
        """
        await self.loop.run_in_executor(None, self.resize, ratio, w, h)

    def resize(self, ratio: float = 0, w: int = 0, h: int = 0):
        """
        说明：
            压缩图片
        参数：
            :param ratio: 压缩倍率
            :param w: 压缩图片宽度至 w
            :param h: 压缩图片高度至 h
        """
        if not w and not h and not ratio:
            raise ValueError("缺少参数...")
        if not w and not h and ratio:
            w = int(self.w * ratio)
            h = int(self.h * ratio)
        self.mark_img = self.mark_img.resize((w, h), Image.LANCZOS)
        self.w, self.h = self.mark_img.size
        self.size = self.w, self.h
        self.draw = ImageDraw.Draw(self.mark_img)

    async def acrop(self, box: Tuple[int, int, int, int]):
        """
        说明：
            异步 裁剪图片
        参数：
            :param box: 左上角坐标，右下角坐标 (left, upper, right, lower)
        """
        await self.loop.run_in_executor(None, self.crop, box)

    def crop(self, box: Tuple[int, int, int, int]):
        """
        说明：
            裁剪图片
        参数：
            :param box: 左上角坐标，右下角坐标 (left, upper, right, lower)
        """
        self.mark_img = self.mark_img.crop(box)
        self.w, self.h = self.mark_img.size
        self.size = self.w, self.h
        self.draw = ImageDraw.Draw(self.mark_img)

    def check_font_size(self, word: str) -> bool:
        """
        说明：
            检查文本所需宽度是否大于图片宽度
        参数：
            :param word: 文本内容
        """
        return self.font.getlength(word) > self.w

    async def atransparent(self, alpha_ratio: float = 1, n: int = 0):
        """
        说明：
            异步 图片透明化
        参数：
            :param alpha_ratio: 透明化程度
            :param n: 透明化大小内边距
        """
        await self.loop.run_in_executor(None, self.transparent, alpha_ratio, n)

    def transparent(self, alpha_ratio: float = 1, n: int = 0):
        """
        说明：
            图片透明化
        参数：
            :param alpha_ratio: 透明化程度
            :param n: 透明化大小内边距
        """
        self.mark_img = self.mark_img.convert("RGBA")
        x, y = self.mark_img.size
        for i in range(n, x - n):
            for k in range(n, y - n):
                color = self.mark_img.getpixel((i, k))
                color = color[:-1] + (int(100 * alpha_ratio),)
                self.mark_img.putpixel((i, k), color)
        self.draw = ImageDraw.Draw(self.mark_img)

    def pic2bs4(self) -> str:
        """
        说明：
            BuildImage 转 base64
        """
        buf = BytesIO()
        self.mark_img.save(buf, format="PNG")
        base64_str = base64.b64encode(buf.getvalue()).decode()
        return base64_str

    def convert(self, type_: str):
        """
        说明：
            修改图片类型
        参数：
            :param type_: 类型
        """
        self.mark_img = self.mark_img.convert(type_)

    async def arectangle(
        self,
        xy: Tuple[int, int, int, int],
        fill: Optional[Tuple[int, int, int]] = None,
        outline: str = None,
        width: int = 1,
    ):
        """
        说明：
            异步 画框
        参数：
            :param xy: 坐标
            :param fill: 填充颜色
            :param outline: 轮廓颜色
            :param width: 线宽
        """
        await self.loop.run_in_executor(None, self.rectangle, xy, fill, outline, width)

    def rectangle(
        self,
        xy: Tuple[int, int, int, int],
        fill: Optional[Tuple[int, int, int]] = None,
        outline: str = None,
        width: int = 1,
    ):
        """
        说明：
            画框
        参数：
            :param xy: 坐标
            :param fill: 填充颜色
            :param outline: 轮廓颜色
            :param width: 线宽
        """
        self.draw.rectangle(xy, fill, outline, width)

    async def apolygon(
        self,
        xy: List[Tuple[int, int]],
        fill: Tuple[int, int, int] = (0, 0, 0),
        outline: int = 1,
    ):
        """
        说明:
            异步 画多边形
        参数：
            :param xy: 坐标
            :param fill: 颜色
            :param outline: 线宽
        """
        await self.loop.run_in_executor(None, self.polygon, xy, fill, outline)

    def polygon(
        self,
        xy: List[Tuple[int, int]],
        fill: Tuple[int, int, int] = (0, 0, 0),
        outline: int = 1,
    ):
        """
        说明:
            画多边形
        参数：
            :param xy: 坐标
            :param fill: 颜色
            :param outline: 线宽
        """
        self.draw.polygon(xy, fill, outline)

    async def aline(
        self,
        xy: Tuple[int, int, int, int],
        fill: Optional[Union[str, Tuple[int, int, int]]] = None,
        width: int = 1,
    ):
        """
        说明：
            异步 画线
        参数：
            :param xy: 坐标
            :param fill: 填充
            :param width: 线宽
        """
        await self.loop.run_in_executor(None, self.line, xy, fill, width)

    def line(
        self,
        xy: Tuple[int, int, int, int],
        fill: Optional[Union[Tuple[int, int, int], str]] = None,
        width: int = 1,
    ):
        """
        说明：
            画线
        参数：
            :param xy: 坐标
            :param fill: 填充
            :param width: 线宽
        """
        self.draw.line(xy, fill, width)

    async def acircle(self):
        """
        说明：
            异步 将 BuildImage 图片变为圆形
        """
        await self.loop.run_in_executor(None, self.circle)

    def circle(self):
        """
        说明：
            使图像变圆
        """
        self.mark_img.convert("RGBA")
        size = self.mark_img.size
        r2 = min(size[0], size[1])
        if size[0] != size[1]:
            self.mark_img = self.mark_img.resize((r2, r2), Image.LANCZOS)
        width = 1
        antialias = 4
        ellipse_box = [0, 0, r2 - 2, r2 - 2]
        mask = Image.new(
            size=[int(dim * antialias) for dim in self.mark_img.size],
            mode='L', color='black')
        draw = ImageDraw.Draw(mask)
        for offset, fill in (width / -2.0, 'black'), (width / 2.0, 'white'):
            left, top = [(value + offset) * antialias for value in ellipse_box[:2]]
            right, bottom = [(value - offset) * antialias for value in ellipse_box[2:]]
            draw.ellipse([left, top, right, bottom], fill=fill)
        mask = mask.resize(self.mark_img.size, Image.LANCZOS)
        self.mark_img.putalpha(mask)

    async def acircle_corner(self, radii: int = 30):
        """
        说明：
            异步 矩形四角变圆
        参数：
            :param radii: 半径
        """
        await self.loop.run_in_executor(None, self.circle_corner, radii)

    def circle_corner(self, radii: int = 30):
        """
        说明：
            矩形四角变圆
        参数：
            :param radii: 半径
        """
        # 画圆（用于分离4个角）
        circle = Image.new("L", (radii * 2, radii * 2), 0)
        draw = ImageDraw.Draw(circle)
        draw.ellipse((0, 0, radii * 2, radii * 2), fill=255)
        self.mark_img = self.mark_img.convert("RGBA")
        w, h = self.mark_img.size
        alpha = Image.new("L", self.mark_img.size, 255)
        alpha.paste(circle.crop((0, 0, radii, radii)), (0, 0))
        alpha.paste(circle.crop((radii, 0, radii * 2, radii)), (w - radii, 0))
        alpha.paste(
            circle.crop((radii, radii, radii * 2, radii * 2)), (w - radii, h - radii)
        )
        alpha.paste(circle.crop((0, radii, radii, radii * 2)), (0, h - radii))
        self.mark_img.putalpha(alpha)

    async def arotate(self, angle: int, expand: bool = False):
        """
        说明：
            异步 旋转图片
        参数：
            :param angle: 角度
            :param expand: 放大图片适应角度
        """
        await self.loop.run_in_executor(None, self.rotate, angle, expand)

    def rotate(self, angle: int, expand: bool = False):
        """
        说明：
            旋转图片
        参数：
            :param angle: 角度
            :param expand: 放大图片适应角度
        """
        self.mark_img = self.mark_img.rotate(angle, expand=expand)

    async def atranspose(self, angle: int):
        """
        说明：
            异步 旋转图片(包括边框)
        参数：
            :param angle: 角度
        """
        await self.loop.run_in_executor(None, self.transpose, angle)

    def transpose(self, angle: int):
        """
        说明：
            旋转图片(包括边框)
        参数：
            :param angle: 角度
        """
        self.mark_img.transpose(angle)

    async def afilter(self, filter_: str, aud: int = None):
        """
        说明：
            异步 图片变化
        参数：
            :param filter_: 变化效果
            :param aud: 利率
        """
        await self.loop.run_in_executor(None, self.filter, filter_, aud)

    def filter(self, filter_: str, aud: int = None):
        """
        说明：
            图片变化
        参数：
            :param filter_: 变化效果
            :param aud: 利率
        """
        _x = None
        if filter_ == "GaussianBlur":  # 高斯模糊
            _x = ImageFilter.GaussianBlur
        elif filter_ == "EDGE_ENHANCE":  # 锐化效果
            _x = ImageFilter.EDGE_ENHANCE
        elif filter_ == "BLUR":  # 模糊效果
            _x = ImageFilter.BLUR
        elif filter_ == "CONTOUR":  # 铅笔滤镜
            _x = ImageFilter.CONTOUR
        elif filter_ == "FIND_EDGES":  # 边缘检测
            _x = ImageFilter.FIND_EDGES
        if _x:
            if aud:
                self.mark_img = self.mark_img.filter(_x(aud))
            else:
                self.mark_img = self.mark_img.filter(_x)
        self.draw = ImageDraw.Draw(self.mark_img)

    async def areplace_color_tran(
        self,
        src_color: Union[
            Tuple[int, int, int], Tuple[Tuple[int, int, int], Tuple[int, int, int]]
        ],
        replace_color: Tuple[int, int, int],
    ):
        """
        说明：
            异步 颜色替换
        参数：
            :param src_color: 目标颜色，或者使用列表，设置阈值
            :param replace_color: 替换颜色
        """
        await self.loop.run_in_executor(
            None, self.replace_color_tran, src_color, replace_color
        )

    def replace_color_tran(
        self,
        src_color: Union[
            Tuple[int, int, int], Tuple[Tuple[int, int, int], Tuple[int, int, int]]
        ],
        replace_color: Tuple[int, int, int],
    ):
        """
        说明：
            颜色替换
        参数：
            :param src_color: 目标颜色，或者使用元祖，设置阈值
            :param replace_color: 替换颜色
        """
        start_color, end_color = self._color_range(src_color)
        for x in range(self.w):
            for y in range(self.h):
                pixel = self.mark_img.getpixel((x, y))
                if self._color_matches(pixel, start_color, end_color):
                    self.mark_img.putpixel((x, y), replace_color)

    @staticmethod
    def _color_range(
        src_color: Union[
            Tuple[int, int, int],
            Tuple[Tuple[int, int, int], Tuple[int, int, int]],
        ],
    ) -> Tuple[Tuple[int, int, int], Optional[Tuple[int, int, int]]]:
        if isinstance(src_color[0], tuple):
            return src_color
        return src_color, None

    @staticmethod
    def _color_matches(
        pixel,
        start_color: Tuple[int, int, int],
        end_color: Optional[Tuple[int, int, int]],
    ) -> bool:
        rgb = pixel[:3]
        if end_color is None:
            return rgb == start_color
        return all(
            start <= channel <= end
            for channel, start, end in zip(rgb, start_color, end_color)
        )

    #
    def getchannel(self, type_):
        self.mark_img = self.mark_img.getchannel(type_)
