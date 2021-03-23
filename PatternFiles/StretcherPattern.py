#========================================================================#
#      _____               __                            
#      \_   \__ _ _ __     \ \  __ _ _ __ ___   ___  ___ 
#       / /\/ _` | '_ \     \ \/ _` | '_ ` _ \ / _ \/ __|
#    /\/ /_| (_| | | | | /\_/ / (_| | | | | | |  __/\__ \
#    \____/ \__,_|_| |_| \___/ \__,_|_| |_| |_|\___||___/
#
#
# Writes a stretcher bond pattern file to the dimensions specified 
# and the name given as follows:-
#       │       │       │       │
# ──┬───┴───┬───┴───┬───┴───┬───┴───┬───┴
#   │       │       │       │       │
#   │       │«--x--»│       │       │
#   │       │       │       │       │
# ──┴───┬───┴───┬───┴───┬───┴───┬───┴──
#       │       │    |  │       │       
#       │       │    y  │       │       
#       │       │    |  │       │       │    
# ──┬───┴───┬───┴───┬───┴───┬───┴───┬───┴
#   │       │       │       │       │
#
#  June 2020
#
#========================================================================#
x = 75.0
y = 150.0

patfile = ''

#Convert Numbers to String (Float) equivalents
#Must be floats so half of odd numbers returns .5
yminus = float(0-y).ToString()
xhalf = float(x/2).ToString()
x = float(x).ToString()
y = float(y).ToString()

patternName = 'Stretcher ' + x + '*' + y

patfile = patfile + ';%UNITS=MM\n'
patfile = patfile + '*' + patternName + '\n'
patfile = patfile + ';%TYPE=MODEL\n'
patfile = patfile + '0, 0, 0, 0, ' + y + '\n'
patfile = patfile + '90, 0, 0, 0, ' + x + ', ' + y + ', ' + yminus + '\n'
patfile = patfile + '90, ' + xhalf + ', ' + y + ', 0, ' + x + ', ' + y + ', ' + yminus

print patfile


