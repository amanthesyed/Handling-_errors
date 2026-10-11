#!/usr/bin/env python3
"""Distribute cookies evenly and handle invalid input without crashing."""


def party_planner(cookies: int, people: int) -> tuple[int | None, int | None]:
    """Return (cookies per person, leftovers), or (None, None) for invalid input."""
    if people <= 0:
        print("Number of people must be greater than zero.")
        return None, None

    if cookies < 0:
        print("Number of cookies cannot be negative.")
        return None, None

    cookies_each, leftovers = divmod(cookies, people)
    return cookies_each, leftovers


def main() -> None:
    while True:
        try:
            cookies = int(input("How many cookies are you baking? "))
            people = int(input("How many people are attending? "))
        except ValueError:
            print("Please enter whole numbers for both questions.")
        else:
            cookies_each, leftovers = party_planner(cookies, people)
            if cookies_each is not None and leftovers is not None:
                print(
                    f"Let's party! {people} people get {cookies_each} cookies "
                    f"each, with {leftovers} left over."
                )

        again = input("Would you like to plan another party? (y/n) ").strip().lower()
        if again != "y":
            print("Goodbye.")
            break


if __name__ == "__main__":
    main()
