# Imprime una tabla de verdad para la siguiente afirmación: "Una puerta tiene dos interruptores que controlan dos luces la puerta sólo debe abrirse cuando las dos luces están apagadas o las dos están encendidas, caso contrario la puerta no se abre, ¿qué operador lógico se puede utilizar?"

interruptor01 = True
interruptor02 = True
print ("Si interruptor 1:", interruptor01, "y el interruptor 2:", interruptor02, "entonces ¿la puerta esta abierta?", not((interruptor01 or interruptor02) and not(interruptor01 and interruptor02)))

interruptor01 = True
interruptor02 = False
print ("Si interruptor 1:", interruptor01, "y el interruptor 2:", interruptor02, "entonces ¿la puerta esta abierta?", not((interruptor01 or interruptor02) and not(interruptor01 and interruptor02)))

interruptor01 = False
interruptor02 = True
print ("Si interruptor 1:", interruptor01, "y el interruptor 2:", interruptor02, "entonces ¿la puerta esta abierta?", not((interruptor01 or interruptor02) and not(interruptor01 and interruptor02)))

interruptor01 = False
interruptor02 = False
print ("Si interruptor 1:", interruptor01, "y el interruptor 2:", interruptor02, "entonces ¿la puerta esta abierta?", not((interruptor01 or interruptor02) and not(interruptor01 and interruptor02)))