# Standardizing-Roman-Urdu
As Roman Urdu text have no rules and sets to write. Everyone write it of their own ways, so it is difficult for machine to understand and can work on it. So i have applied rule based transformation on Roman Urdu text so that it can become standardized. These rules have been formulated on similar patterns as are followed by phonetic alogorithm.

**Text should be preproccessed i.e Convert text to lowercase, Remove numbers, Remove punctuation and Remove whitespaces.**

### There are 21 step for transformation of roman urdu in standardize way. 

1. If the substring ends with "ain", replace it with "ein"

2. If the substring has "ar" in it except at the start, replace it with "r"

3. Replace "ai" with "ae"

4. If the substring has "iy" with mulitple "y", replace it with "I"

5. If the substring ends with "ay", replace it with "e"

6. If the substring has "ih" with mulitple "h", replace it with "eh"

7. If the substring ends with "ey", replace it with "e"

8. If the substring has multiple "s", replace it with "s"

9. If the substring ends with "ie", replace it with "y"

10. If the substring has "ry" at it except in the end, replace it with "ri"

11. If the substring starts with "es", replace it with "is"

12. If the substring has "sy" at it except in the end, replace it with "si"

13. If the substring has multiple "a", replace it with "a"

14. If the substring has "ty" at it except in the end, replace it with "ti"

15. If the substring has multiple "j", replace it with "j"

16. If the substring has multiple "o", replace it with "o"

17. If the substring has multiple "ee", replace it with "e"

18. If the substring ends with "i" when it is preceded by (bcdefghijklmnopqrtuvwxyz), replace it with "y

19. If the substring has multiple "d, replace it with "d"

20. Replace "u with "o"

21. If the substring has "h" and is proceded by (acefghijlmnoqrstuvwxyz), remove "h"
