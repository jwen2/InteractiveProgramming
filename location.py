def location(x,y):
    x1 = x - 20
    x2 = x + 20
    y1 = y - 20
    y2 = y + 20

    indication = ImageDraw.Draw(img)
    indication.ellipse((x1, y1, x2, y2))
    img.save('newimage2.jpg')
