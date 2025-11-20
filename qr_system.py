import qrcode_terminal

def create_qr(data):
    qrcode_terminal.draw(data)

def read_qr(data):
    return data
