#### General / misc

| construct | description                       |
|-----------|-----------------------------------|
| .         | any sign                          |
| []        | anything inside the brackets      |
| ^         | start of a line                   |
| $         | end of a line                     |
| ()        | group                             |
| \1        | back reference to the first group |
| \|        | logical or                        |

#### Predefined character classes

| construct | description                                  |
|-----------|----------------------------------------------|
| \d        | [0-9] digit                                  |
| \D        | [^0-9] non-digit                             |
| \s        | [ \t \n \r \f \v ] whitespace character      |
| \S        | [^ \t \n \r \f \v ] non-whitespace character |
| \w        | [a-zA-Z0-9_] word character                  |
| \W        | [^a-zA-Z0-9_] non-word character             |
| \b        | empty string at start or end of a string     |
| \B        | empty string not at start or end of a string |
| \\        | backslash                                    |

#### Quantifiers

| construct | description                          |
|-----------|--------------------------------------|
| ?         | once or not at all                   |
| *         | zero or more                         |
| +         | one or more                          |
| {n}       | exactly n times                      |
| {n,m}     | at least n but not more than m times |

