
# Chord Converter

This is an HTML & JavaScript-based Chord Converter. It will convert chord symbols to Roman numerals and vice versa.

## User Instructions

1. **Use the drop-down menu to select a key.**
2. **Check "Use Special Rules"** if you wish to reflect secondary and substitute dominant functions.
3. **Entering Note/Roman Numerals:**
    - For regular notes and Roman numerals, use capitalized letters.
    - For substitute dominants, enter `Sub/X` (e.g., `Sub/V` is the substitute dominant 7th of degree five).
    - For secondary dominants, enter `7/X`.
4. **Relative Seconds:** Although not completed, relative seconds can be reflected if you type `7/X`, but leave the chord quality as `-7` or `-7b5`. Diminished chords are not supported.
5. **Chord Quality Drop-down Menu:** Choose your chord quality here. **DO NOT** type the quality in the text box.
6. **Special Rules:** When "Use Special Rules" is checked and the chord quality is `7`, entering a non-diatonic `V` chord will be converted to a substitute or secondary `V`. (e.g., in the key of C major, `A7` will be converted to `7/II` if special rules are enabled, and will show as `VI7` if disabled).
7. **Tension Checkbox:** This feature is not complete; however, if you check the tension here, it will be reflected in the conversion.
8. **Note Spelling Matters:** The converter follows scale degrees strictly and currently has no enharmonic error tolerance. For example, in Eb major, `G#7` does not exist and will cause an error; use `Ab7` instead.
