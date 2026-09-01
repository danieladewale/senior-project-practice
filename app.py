#!/usr/bin/env python3
"""
Senior Project Developer Profile
Displays personal information and goals for the senior project.
"""

# Replace these with your own information
NAME = "Daniel Adewale"
MAJOR = "Computer Science"
TECHNOLOGY_INTEREST = "Artificial Intelligence"
SKILL_GOAL = "Backend Developer "



def display_profile():
    """Display the Senior Project Developer Profile."""
    print("=" * 50)
    print("Senior Project Developer Profile")
    print("=" * 50)
    print(f"\nName: {NAME}")
    print(f"\nMajor: {MAJOR}")
    print(f"\nTechnology Interest: {TECHNOLOGY_INTEREST}")
    print(f"\nSkill Goal: {SKILL_GOAL}")
    print("\n" + "=" * 50)


if __name__ == "__main__":
    display_profile()
