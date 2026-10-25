English | [Türkçe](akilli-asansor.tr.md)

# Smart Elevator

A model elevator that can be called by voice, sign or button, aimed at people who have trouble using standard elevator panels.

## What it is

An Arduino-controlled elevator model. An MIT App Inventor app sends the floor command over Bluetooth (HC-06), and the Arduino UNO drives a DC motor through an L298N driver. Built by a middle school student under my supervision.

## How it works

- Commands `0`-`4` send the cabin to that floor and `5` stops it
- The motor speeds up and slows down with PWM instead of jumping to full speed
- A second version uses physical floor buttons and a 7-segment display
- Separate test sketches for Bluetooth, the motor and a voice recognition module
- The cabin was modelled in Tinkercad

## Stack

Arduino (C++), HC-06 Bluetooth, L298N, MIT App Inventor 2, Tinkercad

## My role

Advisor and developer: I wrote the firmware with the student and guided design and testing.

## Result

TÜBİTAK 2204-B · 3rd, İzmir regional, 2022.

---

The source code is private. Happy to show a demo or walk through the code.

[← Back to profile](../README.md)
