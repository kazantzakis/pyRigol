import usbtmc

# Bus 001 Device 005: ID 1ab1:0588 Rigol Technologies DS1000 SERIES
instr =  usbtmc.Instrument(6833,1416)

instr.write(":KEY:LOCK ENAB")

print(instr.ask_raw("*IDN?"))

# read data
instr.write(":RUN")
#instr.write(":WAV:POIN:MODE RAW")
instr.write(":DISP:TYPE VECT") # {VECT|DOTS}
instr.write(":DISP:GRID FULL") # {FULL|HALF|NONE}
instr.write(":DISPlay:MNUStatus ON")
instr.write(":DISPlay:BRIGhtness 8")
instr.write(":CHANnel2:DISPlay OFF")
instr.write(":BEEP:ACTion")

# first ten bytes are header, so skip
#rawdata = instr.ask_raw(":WAV:DATA? CHAN1")[10:]
#data_size = len(rawdata)
 
# get metadata
sample_rate = float(instr.ask_raw(':ACQ:SAMP?'))
timescale = float(instr.ask_raw(":TIM:SCAL?"))
timeoffset = float(instr.ask_raw(":TIM:OFFS?"))
voltscale = float(instr.ask_raw(':CHAN1:SCAL?'))
voltoffset = float(instr.ask_raw(":CHAN1:OFFS?"))
display_type = instr.ask_raw(":DISP:TYPE?")
display_grid = instr.ask_raw(":DISP:GRID?")
display_menu_status = instr.ask_raw(":DISPlay:MNUStatus?") 
grid_brightness = instr.ask_raw(":DISPlay:BRIGhtness?") 
channel1_display = instr.ask_raw(":CHANnel1:DISPlay?")
channel2_display = instr.ask_raw(":CHANnel2:DISPlay?")
channel1_frequency = float(instr.ask_raw(":MEASure:FREQuency? CHANnel1"))
 
# show metadata
#print "Data size:      ", data_size
print "Sample rate:    ", sample_rate
print "Time scale:     ", timescale
print "Time offset:    ", timeoffset
print "Voltage offset: ", voltoffset
print "Voltage scale:  ", voltscale
print "Display Type:   ", display_type
print "Display Grid:   ", display_grid
print "Display Menu:   ", display_menu_status 
print "Grid Brightness:   ", grid_brightness 
print "Channel1 display:   ", channel1_display 
print "Channel2 display:   ", channel2_display 
print "Channel1 frequency: ", channel1_frequency 

#instr.write(":KEY:LOCK DIS")
instr.write(":KEY:FORCe")

