# Cookie Distribution — Input Validation Exercise

A small Python CLI exercise in defensive programming: divide a number of cookies evenly among a group, report the remainder, and handle invalid values without crashing.

## Behaviour

- Uses integer division and remainder to calculate an even distribution.
- Rejects zero or negative group sizes.
- Rejects negative cookie counts.
- Catches non-integer terminal input and lets the user try again.
- Keeps the calculation in `party_planner()`, separate from the prompt loop.

## Run

Requires Python 3.10 or newer.

~~~bash
python handling_errors.py
~~~

Example:

~~~text
How many cookies are you baking? 25
How many people are attending? 4
Let's party! 4 people get 6 cookies each, with 1 left over.
~~~

## Edge cases worth trying

| Cookies | People | Expected result |
|---:|---:|---|
| 25 | 4 | 6 each, 1 left over |
| 4 | 8 | 0 each, 4 left over |
| 10 | 0 | Clear validation message; no division error |
| -1 | 3 | Reject negative cookie count |
| `abc` | 3 | Prompt handles non-integer input |

This is a fundamentals exercise rather than a production application; the goal is clear input handling and predictable function behaviour.
