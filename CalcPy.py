from thumbyGraphics import display
import thumbyButton as buttons
import machine
import math
import time

menu = 'main'
Num1 = 0
Num1Deci = 0
Num2 = 0
Num2Deci = 0
Num3 = 0
Num3Deci = 0
selMode = 0
Num1DeciMode = 0
Num2DeciMode = 0
Num3DeciMode = 0
numMode = 0
selNum = 1
operator = 0
operatorTXT = '+'
operator1 = 0
operator2 = 0
operator1TXT = '+'
operator2TXT = '+'
delta = 0
p = 0
q = 0
prev_x = 1 - 36
prev_y = (Num1 * (prev_x ** 2)) + (Num2 * prev_x) + (Num3)
prev_scaled_y = 19 - int(prev_y / 10)
manualPage = 0
secMode = 0
measuringUnit = 0
measuringUnitTXT = 'mm^2'
volMode = 'surface'
volOrSurf = '^2'

def printd(message):
      message = str(message)
      display.fill(0)
      txt = [""]
      for line in message.split("\n"):
          for word in line.split(" "):
              next_len = len(txt[-1]) + len(word) + 1
              if next_len*display.textWidth + (next_len-1) > display.width:
                  txt += [""]
              txt[-1] += (" " if txt[-1] else "") + word
          txt += [""]
      for ln, line in enumerate(txt):
          display.drawText(line, 0, (display.textHeight+1)*ln, 1)
      display.display.show()

while menu == 'main':
    if selMode == 0:
        printd('A to select \n B for menu\n SIMPLE \n sqrt, pwr \n fun^2')
    elif selMode == 1:
        printd('A to select \n B for menu\n simple \n SQRT, PWR \n fun^2')
    elif selMode == 2:
        printd('A to select \n B for menu\n simple \n sqrt, pwr \n FUN^2')
    elif selMode == 3:
        printd('SURF,VOL')
    elif selMode < 0:
        selMode = 3
    elif selMode > 3:
        selMode = 0
        
    if buttons.buttonU.justPressed():
        selMode = selMode - 1
    elif buttons.buttonD.justPressed():
        selMode = selMode + 1
        
    if buttons.buttonA.justPressed():
        if selMode == 0:
            menu = 'simple'
        elif selMode == 1:
            menu = 'sqrt'
        elif selMode == 2:
            menu = 'quadfun'
        elif selMode == 3:
            menu = 'vol'
    elif buttons.buttonB.justPressed():
        menu = 'secondary'

while menu == 'secondary':
    if secMode == 0:
        printd('MANUAL')
    elif secMode < 0:
        secMode = 0
    elif secMode > 0:
        secMode = 0
        
    if buttons.buttonA.justPressed():
        if secMode == 0:
            menu = 'manual'
    elif buttons.buttonB.justPressed():
        machine.reset()
        

while menu == 'manual':
    
    if buttons.buttonU.justPressed():
        manualPage = manualPage - 1
    elif buttons.buttonD.justPressed():
        manualPage = manualPage + 1
        
    if manualPage > 0:
        if manualPage < 11:
            display.drawText(str(manualPage - 1), 67, 33, 1)
            display.update()
        elif manualPage >= 11:
            display.drawText(str(manualPage - 1), 61, 33, 1)
            display.update()
        
    if manualPage == 0:
        printd('Controls   1\nTop num    2\nBottom num 4\nOperator   7\nSpecial   11')
    elif manualPage == 1:
        printd('\n\n\n\nCurrent pg:')
    elif manualPage == 2:
        printd('A to confirm, B to exit.')
    elif manualPage == 3:
        printd('The top number is the number you will input after')
    elif manualPage == 4:
        printd('pressing A. Change it with up and down.')
    elif manualPage == 5:
        printd('The bottom number is the modifying number.')
    elif manualPage == 6:
        printd("This is how much you'll add or subtract from the")
    elif manualPage == 7:
        printd('top number. Change it with left and right.')
    elif manualPage == 8:
        printd('After inputting a number, you will be asked about')
    elif manualPage == 9:
        printd("it's operator. Operators that only take a")
    elif manualPage == 10:
        printd('single value will take the first number as the value.')
    elif manualPage == 11:
        printd('Change the operator with up and down.')
    elif manualPage == 12:
        printd('Nothing special so far')
    elif manualPage > 12:
        manualPage = 12
    elif manualPage < 0:
        manualPage = 0
        
while menu == 'simple' and numMode == 0:
    
    if Num1Deci > 99:
        Num1Deci = 0
    elif Num1Deci < 0 and selNum != 1:
        Num1Deci = 90
    elif Num1Deci < 0 and selNum == 1:
        Num1Deci = 99
        
    if selNum < 1:
        selNum = 1000000000
    elif selNum > 1000000000:
        selNum = 1
    
    if buttons.buttonL.justPressed():
        selNum = (selNum // 10)
    elif buttons.buttonR.justPressed():
        selNum = (selNum * 10)
    
    if buttons.buttonB.justPressed():
        Num1DeciMode = 1 if Num1DeciMode == 0 else 0

    if Num1DeciMode == 0:
        printd(str(Num1) + '\n\n\n\n' + str(selNum))
        if buttons.buttonU.justPressed():
            Num1 = Num1 + selNum
        elif buttons.buttonD.justPressed():
            Num1 = Num1 - selNum
    elif Num1DeciMode == 1:
        printd(str(Num1) + '.' + f"{Num1Deci:02}" + '\n\n\n\n' + str(selNum))
        if buttons.buttonU.justPressed():
            Num1Deci = Num1Deci + selNum
        elif buttons.buttonD.justPressed():
            Num1Deci = Num1Deci - selNum
    
    if buttons.buttonA.justPressed():
        numMode = 1
            
while menu == 'simple' and numMode == 1:
    if Num1DeciMode == 0:
        printd(str(Num1) + ' ' + operatorTXT)
    elif  Num1DeciMode == 1:
        printd(str(Num1) + '.' + str(Num1Deci) + ' ' + operatorTXT)
        
    if operator < 0:
        operator = 3
    elif operator > 3:
        operator = 0
        
    if operator == 0:
        operatorTXT = '+'
    elif operator == 1:
        operatorTXT = '-'
    elif operator == 2:
        operatorTXT = 'x'
    elif operator == 3:
        operatorTXT = '/'
        
    if buttons.buttonU.justPressed():
        operator = operator + 1
    elif buttons.buttonD.justPressed():
        operator = operator - 1
        
    if buttons.buttonA.justPressed():
        numMode = 2
        
while menu == 'simple' and numMode == 2:
    
    if Num2Deci > 99:
        Num2Deci = 0
    elif Num2Deci < 0 and selNum != 1:
        Num2Deci = 90
    elif Num2Deci < 0 and selNum == 1:
        Num2Deci = 99
        
    if selNum < 1:
        selNum = 1000000000
    elif selNum > 1000000000:
        selNum = 1
        
    if buttons.buttonL.justPressed():
        selNum = (selNum // 10)
    elif buttons.buttonR.justPressed():
        selNum = (selNum * 10)
    
    if buttons.buttonB.justPressed():
        Num2DeciMode = 1 if Num2DeciMode == 0 else 0
        
    if Num1DeciMode == 0 and Num2Deci == 0:
        printd(str(Num1) + ' ' + operatorTXT + ' ' + str(Num2) + '\n\n\n\n' + str(selNum))
        if buttons.buttonU.justPressed():
            Num2 = Num2 + selNum
        elif buttons.buttonD.justPressed():
            Num2 = Num2 - selNum
    elif Num1DeciMode == 0 and Num2DeciMode == 1:
        printd(str(Num1) + ' ' + operatorTXT + ' ' + str(Num2) + '.' + f"{Num2Deci:02}" + '\n\n\n\n' + str(selNum))
        if buttons.buttonU.justPressed():
            Num2Deci = Num2Deci + selNum
        elif buttons.buttonD.justPressed():
            Num2Deci = Num2Deci - selNum
    elif Num1DeciMode == 1 and Num2DeciMode == 1:
        printd(str(Num1) + '.' + f"{Num1Deci:02}" + ' ' + operatorTXT + ' ' + str(Num2) + '.' + f"{Num2Deci:02}" + '\n\n\n\n' + str(selNum))
        if buttons.buttonU.justPressed():
            Num2Deci = Num2Deci + selNum
        elif buttons.buttonD.justPressed():
            Num2Deci = Num2Deci - selNum
    elif Num1DeciMode == 1 and Num2DeciMode == 0:
        printd(str(Num1) + '.' + f"{Num1Deci:02}" + ' ' + operatorTXT + ' ' + str(Num2) + '\n\n\n\n' + str(selNum))
        if buttons.buttonU.justPressed():
            Num2 = Num2 + selNum
        elif buttons.buttonD.justPressed():
            Num2 = Num2 - selNum
            
    if buttons.buttonA.justPressed():
        menu = 'equals'

while menu == 'sqrt' and numMode == 0:
    
    operator = 4
    
    if Num1Deci > 99:
        Num1Deci = 0
    elif Num1Deci < 0 and selNum != 1:
        Num1Deci = 90
    elif Num1Deci < 0 and selNum == 1:
        Num1Deci = 99
        
    if selNum < 1:
        selNum = 1000000000
    elif selNum > 1000000000:
        selNum = 1
        
    if buttons.buttonL.justPressed():
        selNum = (selNum // 10)
    elif buttons.buttonR.justPressed():
        selNum = (selNum * 10)
    
    if buttons.buttonB.justPressed():
        Num1DeciMode = 1 if Num1DeciMode == 0 else 0
    
    if Num1DeciMode == 0:
        printd(str(Num1) + '\n\n\n\n' + str(selNum))
        if buttons.buttonU.justPressed():
            Num1 = Num1 + selNum
        elif buttons.buttonD.justPressed():
            Num1 = Num1 - selNum
    elif Num1DeciMode == 1:
        printd(str(Num1) + '.' + f"{Num1Deci:02}" + '\n\n\n\n' + str(selNum))
        if buttons.buttonU.justPressed():
            Num1Deci = Num1Deci + selNum
        elif buttons.buttonD.justPressed():
            Num1Deci = Num1Deci - selNum
            
    if buttons.buttonA.justPressed():
        numMode = 1
        
while menu == 'sqrt' and numMode == 1:
    
    if Num1DeciMode == 0:
        printd(str(Num1) + ' ' + operatorTXT)
    elif  Num1DeciMode == 1:
        printd(str(Num1) + '.' + str(Num1Deci) + ' ' + operatorTXT)
        
    if operator < 4:
        operator = 6
    elif operator > 6:
        operator = 4
        
    if operator == 4:
        operatorTXT = '^'
    elif operator == 5:
        operatorTXT = 'sqrt'
    elif operator == 6:
        operatorTXT = 'cbrt'
        
    if buttons.buttonU.justPressed():
        operator = operator + 1
    elif buttons.buttonD.justPressed():
        operator = operator - 1
        
    if buttons.buttonA.justPressed():
        if (operator == 5 or operator == 6) and (Num1 + (Num1Deci / 100)) < 0:
            printd("Number mustn't be lesser than 0")
            time.sleep(5)
            machine.reset()
        else:
            if operator == 4:
                numMode = 2
            else:
                menu = 'equals'
            
while menu == 'sqrt' and numMode == 2:
    
    if Num2Deci > 99:
        Num2Deci = 0
    elif Num2Deci < 0 and selNum != 1:
        Num2Deci = 90
    elif Num2Deci < 0 and selNum == 1:
        Num2Deci = 99
        
    if selNum < 1:
        selNum = 1000000000
    elif selNum > 1000000000:
        selNum = 1
        
    if buttons.buttonL.justPressed():
        selNum = (selNum // 10)
    elif buttons.buttonR.justPressed():
        selNum = (selNum * 10)
        
    if Num1DeciMode == 0:
        printd(str(Num1) + ' ' + operatorTXT + ' ' + str(Num2) + '\n\n\n\n' + str(selNum))
        if buttons.buttonU.justPressed():
            Num2 = Num2 + selNum
        elif buttons.buttonD.justPressed():
            Num2 = Num2 - selNum
    elif Num1DeciMode == 1:
        printd(str(Num1) + '.' + f"{Num1Deci:02}" + ' ' + operatorTXT + ' ' + str(Num2) + '\n\n\n\n' + str(selNum))
        if buttons.buttonU.justPressed():
            Num2 = Num2 + selNum
        elif buttons.buttonD.justPressed():
            Num2 = Num2 - selNum
            
    if buttons.buttonA.justPressed():
        menu = 'equals'

while menu == 'quadfun' and numMode == 0:
    
    if selNum < 1:
        selNum = 1000000000
    elif selNum > 1000000000:
        selNum = 1
        
    if buttons.buttonL.justPressed():
        selNum = (selNum // 10)
    elif buttons.buttonR.justPressed():
        selNum = (selNum * 10)
        
    printd(str(Num1) + 'x^2 \n\n\n\n' + str(selNum))
    
    if buttons.buttonU.justPressed():
            Num1 = Num1 + selNum
    elif buttons.buttonD.justPressed():
        Num1 = Num1 - selNum
        
    if buttons.buttonA.justPressed():
        numMode = 1
        
while menu == 'quadfun' and numMode == 1:
    
    if selNum < 1:
        selNum = 1000000000
    elif selNum > 1000000000:
        selNum = 1
        
    if buttons.buttonL.justPressed():
        selNum = (selNum // 10)
    elif buttons.buttonR.justPressed():
        selNum = (selNum * 10)
        
    if buttons.buttonU.justPressed():
            Num2 = Num2 + selNum
    elif buttons.buttonD.justPressed():
        Num2 = Num2 - selNum
        
    printd(str(Num1) + 'x^2' + ' + ' + str(Num2) + 'x' + '\n\n\n\n' + str(selNum))
        
    if buttons.buttonA.justPressed():
        numMode = 2
    
while menu == 'quadfun' and numMode == 2:
    
    if selNum < 1:
        selNum = 1000000000
    elif selNum > 1000000000:
        selNum = 1
        
    if buttons.buttonL.justPressed():
        selNum = (selNum // 10)
    elif buttons.buttonR.justPressed():
        selNum = (selNum * 10)
        
    if buttons.buttonU.justPressed():
            Num3 = Num3 + selNum
    elif buttons.buttonD.justPressed():
        Num3 = Num3 - selNum
        
    printd(str(Num1) + 'x^2' + ' + ' + str(Num2) + 'x + ' + str(Num3) + '\n\n\n' + str(selNum))
        
    if buttons.buttonA.justPressed():
        menu = 'equals'
        
while menu == 'vol' and numMode == 0:
    printd('What would you like to calculate?')
    display.drawText(measuringUnitTXT, 24, 32, 1)
    display.update()
    
    if buttons.buttonU.justPressed():
        measuringUnit = measuringUnit + 1
    elif buttons.buttonD.justPressed():
        measuringUnit = measuringUnit - 1
        
    if measuringUnit < 0:
        measuringUnit = 4
    elif measuringUnit > 4:
        measuringUnit = 0
        
    if measuringUnit == 0:
        measuringUnitTXT = 'mm'
    elif measuringUnit == 1:
        measuringUnitTXT = 'cm'
    elif measuringUnit == 2:
        measuringUnitTXT = 'm'
    elif measuringUnit == 3:
        measuringUnitTXT = 'in'
    elif measuringUnit == 4:
        measuringUnitTXT = 'ft'
        
    if buttons.buttonA.justPressed():
        numMode = 1

while menu == 'vol' and numMode == 1:
    printd('What would you like to calculate?')
    display.drawText(measuringUnitTXT + volOrSurf, 24, 32, 1)
    display.update()
    
    if buttons.buttonU.justPressed() or buttons.buttonD.justPressed():
        volOrSurf = '^3' if volOrSurf == '^2' else '^2'
        
    if buttons.buttonA.justPressed():
        numMode = 2

while menu == 'vol' and numMode == 2:
    printd(str(Num1) + '\n\n\n\n' + str(selNum))
    
    if buttons.buttonU.justPressed():
        Num1 = Num1 + selNum
    elif buttons.buttonD.justPressed():
        Num1 = Num1 - selNum
        
    if Num1 < 1:
        Num1 = 0
        Num1Deci = 1
        Num1DeciMode
    
    if buttons.buttonR.justPressed():
        selNum = selNum * 10
    elif buttons.buttonL.justPressed():
        selNum = selNum // 10
    
    if selNum < 1:
        selNum = 1000000
    elif selNum > 1000000:
        selNum = 1
        
    if buttons.buttonA.justPressed():
        numMode = 3
     
while menu == 'vol' and numMode == 3:
    printd(str(Num1) + ' x ' + str(Num2) + '\n\n\n\n' + str(selNum))
    
    print('menu = ' + menu + '\n' + volOrSurf)
    
    if buttons.buttonU.justPressed():
        Num2 = Num2 + selNum
    elif buttons.buttonD.justPressed():
        Num2 = Num2 - selNum
        
    if Num2 < 1:
        Num2 = 0
        Num2Deci = 1
        Num2DeciMode = 1
    
    if buttons.buttonR.justPressed():
        selNum = selNum * 10
    elif buttons.buttonL.justPressed():
        selNum = selNum // 10
    
    if selNum < 1:
        selNum = 1000000
    elif selNum > 1000000:
        selNum = 1

while menu == 'vol' and numMode == 4:
    printd(str(Num1) + ' x ' + str(Num2) + ' x ' + str(Num3) + '\n\n\n\n' + str(selNum))
    
    print('menu = ' + menu + '\n' + volOrSurf)
    
    if buttons.buttonU.justPressed():
        Num3 = Num3 + selNum
    elif buttons.buttonD.justPressed():
        Num3 = Num3 - selNum
        
    if Num3 < 1:
        Num3 = 0
        Num3Deci = 1
        Num3DeciMode = 1
    
    if buttons.buttonR.justPressed():
        selNum = selNum * 10
    elif buttons.buttonL.justPressed():
        selNum = selNum // 10
    
    if selNum < 1:
        selNum = 1000000
    elif selNum > 1000000:
        selNum = 1

while menu == 'equals':
    
    if selMode == 0:
        if operator == 0:
            printd(str((Num1 + (Num1Deci / 100)) + (Num2 + (Num2Deci / 100))) + '\n\n Press B to exit')
        elif operator == 1:
            printd(str((Num1 + (Num1Deci / 100)) - (Num2 + (Num2Deci / 100))) + '\n\n Press B to exit')
        elif operator == 2:
            printd(str((Num1 + (Num1Deci / 100)) * (Num2 + (Num2Deci / 100))) + '\n\n Press B to exit')
        elif operator == 3:
            printd(str((Num1 + (Num1Deci / 100)) / (Num2 + (Num2Deci / 100))) + '\n\n Press B to exit')
    elif selMode == 1:
        if operator == 4:
            printd(str((Num1 + (Num1Deci / 100)) ** (Num2)) + '\n\n Press B to exit')
        elif operator == 5:
            printd(math.sqrt(Num1 + (Num1Deci / 100)) + '\n\n Press B to exit')
        elif operator == 6:
            printd(str((Num1 + (Num1Deci)) ** (1/3)) + '\n\n Press B to exit')
    elif selMode == 2:
    	printd('NOT FINISHED')
    elif selMode == 3 and volMode == 'surface':
        printd(str(Num1 * Num2) + measuringUnitTXT + volOrSurf)
    elif selMode == 3 and volMode == 'volume':
        printd(str(Num1 * Num2 * Num3) + measuringUnitTXT + volOrSurf)
