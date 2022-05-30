import qrcode as qr
img = qr.make("https://www.youtube.com/watch?v=OKuiyX5k6zg&ab_channel=WsCubeTech")
img.save("wscube_youtube.png")