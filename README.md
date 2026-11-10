# Pico Photocell Nightlight

Beginner MicroPython projects for a Raspberry Pi Pico (or Pico W) with a photocell (light sensor) and an LED.

## Programs

| File | What it does |
|---|---|
| `photocell.py` | Reads the photocell once a second and prints the number. Bright = big number, dark = small number. |
| `nightlight.py` | Same, and turns the LED on when it gets dark. |

## Parts

- 1 photocell (either way round)
- 1 10 kΩ resistor (brown-black-orange), for the photocell
- 1 LED
- 1 220 Ω resistor (red-red-brown), for the LED
- Jumper wires and a breadboard

## Wiring

| From | To |
|---|---|
| 3V3 (physical pin 36) | Red (+) rail |
| GND (physical pin 38) | Blue (-) rail |
| Red rail | Photocell leg A |
| Photocell leg B | 10 kΩ resistor (same row) |
| Other end of 10 kΩ resistor | Blue rail |
| Row where photocell and 10 kΩ meet | GP26 (physical pin 31) |
| GP15 (physical pin 20) | LED long leg (+) |
| LED short leg (-) | 220 Ω resistor (same row) |
| Other end of 220 Ω resistor | Blue rail |

Pin numbers are counted with the Pico **top side up** and the USB port at the top.

**Watch out:** many breadboards have a gap halfway along each rail. Keep the wires to the rails on the same half, or add a short jumper across the gap.

## How to run

1. Plug the Pico into the computer with a USB **data** cable.
2. Open the file in **Thonny**.
3. In the bottom-right corner, choose **MicroPython (Raspberry Pi Pico)**.
4. Click **Run**. Readings appear in the Shell panel.

## Tips

- If the LED stays on or never turns on, change `limit` in `nightlight.py`. Pick a number between the bright and dark readings.
