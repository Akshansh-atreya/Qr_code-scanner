import PIL
import qrcode
from PIL import Image


qr = qrcode.QRCode(version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_H,
                    box_size=10,border=4,)
qr.add_data("https://www.youtube.com/watch?v=OKuiyX5k6zg&ab_channel=WsCubeTech")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="blue")
img.save("Wscube_youtube2.png")