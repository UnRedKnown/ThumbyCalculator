# Idk why this doesn't work I'll fix it later TM

delta = (Num2 ** 2) - (4 * Num1 * Num3)
        p = -Num2 / (Num1 * 2)
        q = -delta / (Num1 * 4)
        if Num1 != 0:
            if delta < 0:
                printd('Delta = ' + str(delta) + "\n x doesn't exist" + '\nP = ' + str(p) + '\nQ = ' + str(q))
            elif delta == 0:
                printd('Delta = ' + str(-Num2 / (Num1 * 2)) + '\nP = ' + str(p) + '\nQ = ' + str(q))
            elif delta > 0:
                printd('Delta = ' + str(delta) + '\nx1 = ' + str(((-Num2) - math.sqrt(delta)) / (Num1 * 2)) + '\nx2 = ' + str(((-Num2) + math.sqrt(delta)) / (Num1 * 2)) + '\nP = ' + str(p) + '\nQ = ' + str(q))
        elif Num1 == 0:
            printd("a mustsn't be 0")
    
    if buttons.buttonB.justPressed():
        machine.reset()
    elif buttons.buttonA.justPressed() and selMode == 2:
        menu = 'drawQuadFun'
        display.fill(0)
        
while menu == 'drawQuadFun':
    display.drawLine(0, 19, 71, 19, 1)
    display.drawLine(35, 0, 35, 39, 1)
    display.update()
    x_start = -36
    x_end = 36
    prev_x = x_start
    prev_y = (Num1 * (prev_x ** 2)) + (Num2 * prev_x) + (Num3)
    prev_scaled_y = 19 - int(prev_y / 10)
    for i in range (-36, 36 + 1):
        x = i
        y = (Num1 * (x ** 2)) + (Num2 * x) + (Num3)
        scaled_y = 19 - int(y / 10)
        screen_x = x + 35
        screen_y = scaled_y
        if 0 <= screen_x < 72 and 0 <= screen_y < 40:
            display.setPixel(screen_x, screen_y, 1)
            if 0 <= prev_x + 36 < 72 and 0 <= prev_scaled_y < 40:
                display.drawLine(prev_x + 36, prev_scaled_y, screen_x, screen_y, 1)
        prev_x = x
        prev_scaled_y = scaled_y


            
    display.update()
