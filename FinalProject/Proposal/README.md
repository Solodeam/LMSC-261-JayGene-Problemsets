# Web-Based Chord Converter

## Project Overview
The Web-Based Chord Converter is designed to offer a simple interface that allows users to convert chords to degrees in music theory. The project will feature three user-accessible variables, with any two taken as input to calculate the remaining one. While many lead sheets use chord symbols, this tool is intended for users who prefer reading in degrees. For example:

- **Chord**: C9, Fmaj7, G7, C-
- **Degree**: Key = C Major, I9, IVmaj7, V7, I-

### Challenges
Though this concept may seem straightforward, it involves several complexities. The degree system, primarily used in music theory analysis, indicates the function of the chord. As a result, the same chord might have different degrees depending on the progression's context. For instance:

- **Chord**: C9, B-7, E7, A-
- **Degree**: Key = C Major, I9, II-7/V, V7/VI, VI-

In this case, B-7 and E7 do not represent VII-7 and III7 because they serve a II-V function in this context. Various other rules like this make the conversion process challenging.

## Implementation
To develop a functional program, I plan to reference rules from Berklee’s harmony class materials and convert them into algorithms. Berklee’s harmony rules are not optimal and can be redundant, so I will optimize them to create a program that approximates human analysis. While perfection is unattainable due to personal interpretation in some cases, the program aims to provide accurate results.

### Objective
This project is not intended to connect Berklee’s harmony course. The goal is to create a usable tool that assists students taking the harmony class at Berklee and people like me who prefer to read Degree lead sheet. Therefore, the project will be web-based.

## Expected Outcomes
- **Guaranteed**: With a given key and either a chord or degree, the program will provide the other. The output will comply with Berklee harmony course material, presented through a simple web-based interface.
  
- **Better**: Improved algorithm where the program can determine the key by analyzing either a chord or degree. This is significantly more challenging, especially when handling key changes.
  
- **Best**: A graphical user interface (e.g., piano layout) and MIDI input support. While MIDI-to-chord programs exist, integrating them into this project may be difficult.

## Next Steps
1. **Review Harmony Material**: Refreshing knowledge from Berklee’s harmony course.
2. **Algorithm Improvement**: Consider methods for reliable key detection based on chord or degree input.
3. **Explore MIDI Integration**: Investigate open-source MIDI interpretation programs and potential integration.

## Project Lead
- **Jay Gene**
