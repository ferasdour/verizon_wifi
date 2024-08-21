# verizon_wifi
Script to generate password possibilities for verizon 5g wifi routers

Example running on single system:
```
time python3 verizon-wifi.py --run | john --stdin --session=attack8 --stdout |aircrack-ng ./cap/Verizon_GC74.cap -e Verizon_GC74
M7 -w - -q
```

Example running on multiple systems, with same collision logic instead of complete wordlist logic:
```
ansible all -i hosts/ -a "time python3 verizon-wifi.py --run | john --stdin --session=attack8 --stdout |aircrack-ng /share/cap/Verizon_GC74.cap -e Verizon_GC74
M7 -w - -q" -u ansible -b --become-password-file /share/becomepass
```

To change the logic to add all plausibilities, change the random.randrange and make that a for each in range loop. 

Use of john's session tracking helps us return to our spot if it gets interrupted.

## To do list:
this entire project is a stop-gap because I couldn't figure out how to do this in hashcat, but there's gotta be a way to grab from two seperate wordlists in there, so... maybe I can trash this and simply create clustered hashcat thing.

