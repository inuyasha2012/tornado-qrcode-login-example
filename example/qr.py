# coding=utf-8
import qrcode
import qrcode.image.svg
from StringIO import StringIO


def get_qrcode(url):

    """
    依据url生成二维码
    :param url:url,例如http://www.sina.com.cn
    :return:svg格式的二维码
    """

    qr = qrcode.QRCode(
        version=4,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image()
    output = StringIO()
    img.save(output)
    qr_data = output.getvalue()
    output.close()
    return qr_data