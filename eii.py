"""
Encryption In Image 文本加密
开源接口

本接口完全开源，使用GPL3.0 开源许可证
"""
import random
import numpy
from PIL import Image

__version__ = version = "0.6.0"


def _to10base(array128):
    """
    内部函数：将128进制转换为10进制

    :param array128: numpy.ndarray
    :return: int
    """
    return array128[0] * 16384 + array128[1] * 128 + array128[2]


def _to128base(int10):
    """
    内部函数：将10进制转换为128进制

    :param int10: int
    :return: numpy.ndarray
    """
    n1 = int10 // 16384
    n2 = (int10 - n1 * 16384) // 128
    n3 = (int10 - n1 * 16384 - n2 * 128)

    return numpy.array([n1, n2, n3])


def _get_pixel(eii, clean, length):
    """
    内部函数：获取某个像素的10进制值
    """

    return _to10base(numpy.array(
        [abs(int(eii[length][0]) - int(clean[length][0])),
         abs(int(eii[length][1]) - int(clean[length][1])),
         abs(int(eii[length][2]) - int(clean[length][2]))
         ]))


def image_open(path):
    """
    打开图像并转换为numpy数组

    :param path: str
    :return: numpy.ndarray
    """
    return numpy.array(Image.open(path))  # noqa


def image_save(image, path):
    """
    保存图像

    :param image: numpy.ndarray
    :param path: str
    :return: None
    """
    img = image.copy()
    img = img.astype(numpy.uint8)
    pimg = Image.fromarray(img)
    pimg.save(path)


def encode_text(image: numpy.ndarray, text, key=None, des_image=False):
    """
    源于EII - Beta算法的文本加密方法

    :param key: int
    :param image: numpy.ndarray
    使用 eii.image_open 以读取numpy图片数组
    :param text: str
    :return: numpy.ndarray
    """
    image = image.copy()

    # 加密字符串
    if key:
        text = _string_enc(text, key)

    # 记录数据维度
    shape = image.shape

    # 初始化数据
    image = image.flatten()
    length = len(text)

    # 将字符串转换为unicode数组
    u_array = numpy.array([])

    for char in text:
        u_array = numpy.append(u_array, ord(char))

    # 获取图像的正负值
    image_pn = numpy.where(image > 127, -1, 1)[0:length * 3 + 6]
    image_des = image[0:length * 3 + 6]

    # 破坏原图
    a = numpy.where(image > 127, -1, 1) * numpy.random.randint(0, 27, image.shape)
    image = image + a

    # 更改原图
    re_array = numpy.array([])

    # 图像第一像素：0x01 (Beta算法文本加密)
    re_array = numpy.append(re_array, [0, 0, 1])

    # 填入长度
    re_array = numpy.append(re_array, _to128base(length))

    # 填入数组
    for x in u_array:
        re_array = numpy.append(re_array, _to128base(x))

    image[0:length * 3 + 6] = image_pn * re_array + image_des

    return numpy.reshape(image, shape)


def decode_text(eii_image: numpy.ndarray, clean_image: numpy.ndarray, key=None):
    """
    源于EII - Beta算法的文本解密方法

    :param key: int
    :param eii_image: numpy.ndarray
    :param clean_image: numpy.ndarray
    :return: str
    """

    eii_image: numpy.ndarray = eii_image.copy()
    clean_image: numpy.ndarray = clean_image.copy()

    # 初始化数据
    eii_image = numpy.reshape(eii_image, (eii_image.size // 3, 3))
    clean_image = numpy.reshape(clean_image, (clean_image.size // 3, 3))

    # 读取文本长度
    length = _get_pixel(eii_image, clean_image, 1)

    text = ''
    # 获取文本
    for i in range(length):
        text += chr(_get_pixel(eii_image, clean_image, i + 2))

    # 解密字符串
    # 加密字符串
    if key:
        text = _string_dec(text, key)

    return text


def _string_enc(text: str, key: int):
    """
    内置函数：EII Sigma算法 字符串加密系统
    注：此加密系统为对称加密，
    适用于Beta算法的内置二次加密方式

    :param text: str
    :param key: int
    :return:
    """

    enc_text = ''
    key = str(key)
    i = 0

    length = int(key)
    if len(key) >= 3:
        length = 1024

    for x in text:
        random.seed(int(key[i % (len(key)) - 1]))
        enc_text += chr(ord(x) + random.randint(1, length))

        i += 1

    return enc_text


def _string_dec(enc: str, key: int):
    dec_text = ''
    key = str(key)
    i = 0

    length = int(key)
    if len(key) >= 3:
        length = 1024

    for x in enc:
        random.seed(int(key[i % (len(key)) - 1]))
        dec_text += chr(ord(x) - random.randint(1, length))

        i += 1

    return dec_text
