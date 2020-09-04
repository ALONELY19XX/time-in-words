# time-in-words
A Simple Python program to transform a time string of type/format "HH:MM" into a sentence.   

<ins>Examples:</ins>

<br>

**default:**
| Input | Output              |
|-------|---------------------|
| 00:00 | twelve o'clock      |
| 01:00 | one o'clock         |
| 12:01 | one past twelve     |
| 14:15 | quarter past two    |
| 15:30 | half past three     |
| 15:36 | twenty-four to four |
| 16:45 | quarter to five     |
| 16:50 | ten to five         |
| 16:59 | one to five         |

<br>
<br>

**use_minutes = True**
| Input | Output                      |
|-------|-----------------------------|
| 00:00 | twelve o'clock              |
| 01:00 | one o'clock                 |
| 12:01 | one **minute** past twelve      |
| 14:15 | quarter past two            |
| 15:30 | half past three             |
| 15:36 | twenty-four **minutes** to four |
| 16:45 | quarter to five             |
| 16:50 | ten **minutes** to five         |
| 16:59 | one **minute** to five          |